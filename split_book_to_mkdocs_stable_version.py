#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将大型 Markdown 图书按章拆分，并直接生成一个独立的 MkDocs Material 图书项目。

直接运行（交互输入路径）：
    python split_book_to_mkdocs_project.py

也支持命令行参数：
    python split_book_to_mkdocs_project.py \
        --markdown "D:/books/source/book.md" \
        --images-dir "D:/books/source/images" \
        --project-dir "D:/knowledge-base/books/wind-energy" \
        --site-name "风能技术" \
        --site-dir "../../site/books/wind-energy" \
        --homepage "/" \
        --clean

生成结构：
    books/wind-energy/
    ├─ mkdocs.yml
    └─ docs/
       ├─ index.md
       ├─ split-report.txt
       ├─ 00-front-matter/
       │  ├─ index.md
       │  └─ images/
       ├─ assets/
       │  └─ javascripts/
       │     └─ mathjax.js
       └─ chapters/
          ├─ 01-introduction/
          │  ├─ index.md
          │  └─ images/
          └─ ...

主要功能：
1. 按二级标题识别主章节，兼容编号章节和无编号论文式章节。
2. 支持“## 1. 引言”“## 第1章 引言”“## **引言**”等格式。
3. 将章标题提升为一级标题，并根据 2.1、2.1.1 等编号自动规范小节层级。
4. 将每章引用的图片复制到该章自己的 images 文件夹，并重写链接。
5. 直接在图书项目根目录生成 mkdocs.yml，不再只生成 nav 片段。
6. 左侧只显示图书首页和各章，右侧显示当前章节的二、三级目录。
7. 生成图书首页 docs/index.md、MathJax 配置和拆分报告。
8. 自动区分前置内容、正文章节和参考文献等后置内容。
9. 不删除源 Markdown 和源图片；--clean 只清空目标项目的 docs 文件夹。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import unquote


CHAPTER_HEADING_RE = re.compile(r"^\s*##\s+(.+?)\s*$")
SECTION_1_RE = re.compile(
    r"^\s*#{3,6}\s+(\d{1,3})\.1(?:[.．、:：]?(?:\s+|$))"
)
ANY_HEADING_RE = re.compile(r"^(#{1,6})(\s+.*)$")

CHAPTER_TITLE_PATTERNS = [
    re.compile(
        r"^第\s*(?P<number>\d{1,3})\s*章\s*"
        r"(?:[.．、:：\-—]\s*)?(?P<title>.+?)$"
    ),
    re.compile(
        r"^(?:chapter|chap\.)\s*(?P<number>\d{1,3})\s*"
        r"(?:[.．、:：\-—]\s*)?(?P<title>.+?)$",
        flags=re.IGNORECASE,
    ),
    re.compile(
        r"^(?P<number>\d{1,3})\s*[.．、:：\-—]\s*"
        r"(?P<title>.+?)$"
    ),
    re.compile(
        r"^(?P<number>\d{1,3})\s+(?P<title>.+?)$"
    ),
]

NUMBERED_SUBHEADING_RE = re.compile(
    r"^(?P<number>\d+(?:\.\d+)+)\s*[.．、:：]?\s*(?P<title>.+?)$"
)


FRONT_MATTER_TITLES = {
    "摘要",
    "abstract",
    "亮点",
    "highlights",
    "章节",
    "目录",
    "contents",
    "文章信息",
    "article info",
    "article information",
    "图文摘要",
    "graphical abstract",
    "关键词",
    "keywords",
}

BODY_START_TITLES = {
    "引言",
    "绪论",
    "前言",
    "概述",
    "introduction",
    "background",
    "overview",
}

BACK_MATTER_TITLES = {
    "参考文献",
    "references",
    "bibliography",
    "作者贡献声明",
    "作者贡献",
    "author contributions",
    "credit authorship contribution statement",
    "利益冲突声明",
    "利益冲突",
    "competing interests",
    "conflict of interest",
    "conflicts of interest",
    "致谢",
    "acknowledgements",
    "acknowledgments",
    "数据可用性说明",
    "数据可用性",
    "data availability",
    "additional information",
    "附加信息",
    "写作过程中关于生成式 ai 和 ai 辅助技术的声明",
}

MARKDOWN_IMAGE_RE = re.compile(
    r"!\[([^\]]*)\]\(\s*(<[^>]+>|[^\s)]+)"
    r"(?P<title>\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)

HTML_IMAGE_RE = re.compile(
    r'(<img\b[^>]*?\bsrc\s*=\s*)(["\'])([^"\']+)(\2)',
    flags=re.IGNORECASE,
)

DEFAULT_MATHJAX = r'''window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise();
});
'''


@dataclass(frozen=True)
class ChapterStart:
    line_index: int
    number: int
    title: str
    original_heading: str


@dataclass
class ChapterResult:
    number: int
    title: str
    directory_name: str
    markdown_path: Path
    image_count: int
    missing_images: list[str]



@dataclass(frozen=True)
class DocumentStructure:
    chapters: list[ChapterStart]
    back_matter_line: int | None


def clean_heading_text(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[*_`]+$", "", value).strip()
    value = re.sub(r"^[*_`]+", "", value).strip()
    value = re.sub(r"\s+", " ", value)
    return value



def normalize_heading_key(value: str) -> str:
    value = clean_heading_text(value)
    value = re.sub(r"\([^)]*\)$", "", value).strip()
    value = re.sub(r"\s+", " ", value)
    return value.casefold()


def parse_chapter_title(value: str) -> tuple[int, str] | None:
    """识别常见章标题：1 标题、1. 标题、第1章 标题、Chapter 1 标题。"""
    cleaned = clean_heading_text(value)

    for pattern in CHAPTER_TITLE_PATTERNS:
        match = pattern.match(cleaned)
        if not match:
            continue

        number = int(match.group("number"))
        title = clean_heading_text(match.group("title"))

        if 1 <= number <= 999 and title:
            return number, title

    return None


def parse_numbered_subheading(value: str) -> tuple[list[int], str] | None:
    """识别 2.1、2.1.1 等编号标题，并忽略编号后的句点。"""
    cleaned = clean_heading_text(value)
    match = NUMBERED_SUBHEADING_RE.match(cleaned)
    if not match:
        return None

    parts = [int(part) for part in match.group("number").split(".")]
    title = clean_heading_text(match.group("title"))
    if len(parts) < 2 or not title:
        return None

    return parts, title


def slugify(value: str) -> str:
    value = clean_heading_text(value)
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "chapter"


def infer_unnumbered_chapter(
    lines: list[str],
    heading_index: int,
    used_numbers: set[int],
) -> tuple[int, str] | None:
    raw_match = CHAPTER_HEADING_RE.match(lines[heading_index].rstrip("\r\n"))
    if not raw_match:
        return None

    title = clean_heading_text(raw_match.group(1))

    for next_index in range(heading_index + 1, len(lines)):
        candidate = lines[next_index].rstrip("\r\n")

        if CHAPTER_HEADING_RE.match(candidate):
            break

        section_match = SECTION_1_RE.match(candidate)
        if section_match:
            number = int(section_match.group(1))
            if number not in used_numbers:
                return number, title
            break

    return None


def find_chapter_starts(lines: list[str]) -> DocumentStructure:
    """
    识别正文主章节。

    优先级：
    1. 优先识别带章号的二级标题；
    2. 若全文没有带章号章节，则按论文式无编号二级标题识别；
    3. 摘要、目录等保留为前置内容；
    4. 参考文献、作者贡献、利益冲突等保留为后置内容。
    """
    h2_items: list[tuple[int, str, str]] = []

    for index, line in enumerate(lines):
        match = CHAPTER_HEADING_RE.match(line.rstrip("\r\n"))
        if not match:
            continue

        original = match.group(1).strip()
        title = clean_heading_text(original)
        h2_items.append((index, original, title))

    if not h2_items:
        raise ValueError("没有识别到任何二级标题（## 标题）。")

    starts: list[ChapterStart] = []
    used_numbers: set[int] = set()

    # 第一阶段：识别显式编号章节。
    for index, original, _ in h2_items:
        numbered = parse_chapter_title(original)

        if numbered:
            number, title = numbered
            if number not in used_numbers:
                starts.append(
                    ChapterStart(
                        line_index=index,
                        number=number,
                        title=title,
                        original_heading=original,
                    )
                )
                used_numbers.add(number)
            continue

        inferred = infer_unnumbered_chapter(lines, index, used_numbers)
        if inferred:
            number, title = inferred
            starts.append(
                ChapterStart(
                    line_index=index,
                    number=number,
                    title=title,
                    original_heading=original,
                )
            )
            used_numbers.add(number)

    starts.sort(key=lambda item: item.line_index)

    if starts:
        # 带编号文档：在最后一个章节之后查找后置内容起点。
        last_chapter_line = starts[-1].line_index
        back_matter_line: int | None = None

        for index, _, title in h2_items:
            if index <= last_chapter_line:
                continue
            if normalize_heading_key(title) in BACK_MATTER_TITLES:
                back_matter_line = index
                break

        numbers = [item.number for item in starts]
        duplicates = sorted({n for n in numbers if numbers.count(n) > 1})
        if duplicates:
            raise ValueError(f"检测到重复章号：{duplicates}")

        return DocumentStructure(
            chapters=starts,
            back_matter_line=back_matter_line,
        )

    # 第二阶段：论文式无编号章节。
    body_start_pos: int | None = None

    for pos, (_, _, title) in enumerate(h2_items):
        if normalize_heading_key(title) in BODY_START_TITLES:
            body_start_pos = pos
            break

    if body_start_pos is None:
        for pos, (_, _, title) in enumerate(h2_items):
            key = normalize_heading_key(title)
            if key not in FRONT_MATTER_TITLES and key not in BACK_MATTER_TITLES:
                body_start_pos = pos
                break

    if body_start_pos is None:
        raise ValueError("未找到正文起始章节。请确认文档中存在“## 引言”或其他正文二级标题。")

    back_matter_pos: int | None = None
    for pos in range(body_start_pos + 1, len(h2_items)):
        key = normalize_heading_key(h2_items[pos][2])
        if key in BACK_MATTER_TITLES:
            back_matter_pos = pos
            break

    body_items = (
        h2_items[body_start_pos:back_matter_pos]
        if back_matter_pos is not None
        else h2_items[body_start_pos:]
    )

    if not body_items:
        raise ValueError("没有识别到可拆分的正文章节。")

    for number, (index, original, title) in enumerate(body_items, start=1):
        starts.append(
            ChapterStart(
                line_index=index,
                number=number,
                title=title,
                original_heading=original,
            )
        )

    back_matter_line = (
        h2_items[back_matter_pos][0]
        if back_matter_pos is not None
        else None
    )

    return DocumentStructure(
        chapters=starts,
        back_matter_line=back_matter_line,
    )


def promote_chapter_headings(
    lines: list[str],
    number: int,
    title: str,
) -> list[str]:
    """把每章整理成适合独立 MkDocs 页面使用的标题层级。"""
    if not lines:
        return [f"# {number} {title}\n"]

    output: list[str] = [f"# {number} {title}\n"]

    for line in lines[1:]:
        stripped = line.rstrip("\r\n")
        ending = line[len(stripped):]
        match = ANY_HEADING_RE.match(stripped)

        if not match:
            output.append(line)
            continue

        hashes = match.group(1)
        remainder = match.group(2)
        heading_text = remainder.strip()
        numbered_heading = parse_numbered_subheading(heading_text)

        if numbered_heading:
            number_parts, _ = numbered_heading

            # 编号层级决定输出层级：2.1 -> H2，2.1.1 -> H3。
            # 这样即使源文档误写成 ##### 2.1.2，也能自动纠正。
            if number_parts[0] == number:
                target_level = min(max(len(number_parts), 2), 6)
                output.append(
                    f"{'#' * target_level} {heading_text}{ending}"
                )
                continue

        if len(hashes) >= 3:
            hashes = hashes[:-1]

        output.append(f"{hashes}{remainder}{ending}")

    return output


def is_external_path(path: str) -> bool:
    lowered = path.lower()
    return (
        lowered.startswith(("http://", "https://", "data:", "mailto:", "#"))
        or path.startswith("//")
    )


def strip_query_and_fragment(path: str) -> str:
    return re.split(r"[?#]", path, maxsplit=1)[0]


def build_image_index(images_dir: Path | None) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}

    if images_dir is None or not images_dir.exists():
        return index

    for item in images_dir.rglob("*"):
        if item.is_file():
            index.setdefault(item.name, []).append(item)

    return index


def resolve_image_source(
    raw_path: str,
    markdown_file: Path,
    images_dir: Path | None,
    image_index: dict[str, list[Path]],
) -> Path | None:
    path_text = raw_path.strip()

    if path_text.startswith("<") and path_text.endswith(">"):
        path_text = path_text[1:-1]

    if is_external_path(path_text):
        return None

    decoded = unquote(strip_query_and_fragment(path_text)).replace("\\", "/")
    relative_path = PurePosixPath(decoded)
    basename = relative_path.name

    candidates: list[Path] = [
        markdown_file.parent.joinpath(*relative_path.parts),
    ]

    if images_dir is not None:
        candidates.extend(
            [
                images_dir.joinpath(*relative_path.parts),
                images_dir / basename,
            ]
        )

    for candidate in candidates:
        try:
            if candidate.is_file():
                return candidate.resolve()
        except OSError:
            continue

    indexed = image_index.get(basename, [])
    if len(indexed) == 1:
        return indexed[0].resolve()

    return None


def short_hash(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()[:8]


def choose_destination_name(
    source: Path,
    destination_dir: Path,
    source_to_name: dict[Path, str],
) -> str:
    source = source.resolve()

    if source in source_to_name:
        return source_to_name[source]

    preferred = source.name
    destination = destination_dir / preferred

    if not destination.exists():
        source_to_name[source] = preferred
        return preferred

    try:
        if source.read_bytes() == destination.read_bytes():
            source_to_name[source] = preferred
            return preferred
    except OSError:
        pass

    candidate = f"{source.stem}-{short_hash(source)}{source.suffix.lower()}"
    source_to_name[source] = candidate
    return candidate


def copy_and_rewrite_images(
    content: str,
    markdown_file: Path,
    images_dir: Path | None,
    chapter_images_dir: Path,
    image_index: dict[str, list[Path]],
) -> tuple[str, int, list[str]]:
    chapter_images_dir.mkdir(parents=True, exist_ok=True)

    copied_sources: set[Path] = set()
    missing: list[str] = []
    source_to_name: dict[Path, str] = {}

    def process_path(raw_path: str) -> str:
        if is_external_path(raw_path.strip("<>")):
            return raw_path

        source = resolve_image_source(
            raw_path=raw_path,
            markdown_file=markdown_file,
            images_dir=images_dir,
            image_index=image_index,
        )

        decoded = unquote(strip_query_and_fragment(raw_path.strip("<>")))
        basename = PurePosixPath(decoded.replace("\\", "/")).name

        if source is None:
            missing.append(raw_path)
            return f"images/{basename}" if basename else raw_path

        destination_name = choose_destination_name(
            source=source,
            destination_dir=chapter_images_dir,
            source_to_name=source_to_name,
        )
        destination = chapter_images_dir / destination_name

        if source not in copied_sources:
            shutil.copy2(source, destination)
            copied_sources.add(source)

        return f"images/{destination_name}"

    def markdown_replacer(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        raw_path = match.group(2)
        title = match.group("title") or ""
        rewritten = process_path(raw_path)
        return f"![{alt_text}]({rewritten}{title})"

    def html_replacer(match: re.Match[str]) -> str:
        prefix = match.group(1)
        quote = match.group(2)
        raw_path = match.group(3)
        rewritten = process_path(raw_path)
        return f"{prefix}{quote}{rewritten}{quote}"

    content = MARKDOWN_IMAGE_RE.sub(markdown_replacer, content)
    content = HTML_IMAGE_RE.sub(html_replacer, content)

    return content, len(copied_sources), list(dict.fromkeys(missing))


def detect_images_directory(
    markdown_file: Path,
    explicit_images_dir: str | None,
) -> Path | None:
    if explicit_images_dir:
        path = Path(explicit_images_dir).expanduser().resolve()
        if not path.is_dir():
            raise FileNotFoundError(f"图片目录不存在：{path}")
        return path

    for folder_name in ("images", "image", "draw", "figures", "figure", "media"):
        candidate = markdown_file.parent / folder_name
        if candidate.is_dir():
            return candidate.resolve()

    return None


def extract_book_title(lines: Iterable[str], fallback: str) -> str:
    for line in lines:
        match = re.match(r"^\s*#\s+(.+?)\s*$", line.rstrip("\r\n"))
        if match:
            return clean_heading_text(match.group(1))
    return fallback


def yaml_scalar(value: str) -> str:
    """JSON 字符串也是合法 YAML，可安全处理中文、冒号和 Windows 反斜杠。"""
    return json.dumps(value, ensure_ascii=False)


def write_home_page(
    docs_dir: Path,
    book_title: str,
    results: list[ChapterResult],
    has_front_matter: bool,
    has_back_matter: bool,
) -> None:
    lines = [
        f"# {book_title}\n",
        "\n",
        "## 目录\n",
        "\n",
    ]

    if has_front_matter:
        lines.append("- [前置内容](00-front-matter/index.md)\n")

    for item in results:
        relative = item.markdown_path.relative_to(docs_dir).as_posix()
        lines.append(
            f"- [第{item.number}章 {item.title}]({relative})\n"
        )

    if has_back_matter:
        lines.append("- [参考文献与附加信息](99-back-matter/index.md)\n")

    (docs_dir / "index.md").write_text("".join(lines), encoding="utf-8")


def build_nav_lines(
    docs_dir: Path,
    results: list[ChapterResult],
    include_front_matter_in_nav: bool,
    has_back_matter: bool,
) -> list[str]:
    lines = [
        "nav:\n",
        "  - 图书首页: index.md\n",
    ]

    if include_front_matter_in_nav:
        lines.append("  - 前置内容: 00-front-matter/index.md\n")

    for item in results:
        relative = item.markdown_path.relative_to(docs_dir).as_posix()
        label = f"第{item.number}章 {item.title}"
        lines.append(f"  - {yaml_scalar(label)}: {relative}\n")

    if has_back_matter:
        lines.append("  - 参考文献与附加信息: 99-back-matter/index.md\n")

    return lines


def write_mkdocs_yml(
    project_dir: Path,
    docs_dir: Path,
    site_name: str,
    site_dir_value: str,
    homepage: str,
    icon: str,
    results: list[ChapterResult],
    include_front_matter_in_nav: bool,
    has_back_matter: bool,
) -> Path:
    """
    生成最简单的 Material 导航：

    - 左侧：图书首页和各章；
    - 右侧：当前页面的二、三级标题；
    - 不启用 toc.integrate；
    - 不生成额外导航 CSS。
    """
    features = [
        "toc.follow",
        "navigation.top",
        "navigation.footer",
        "navigation.path",
        "content.code.copy",
    ]

    lines = [
        f"site_name: {yaml_scalar(site_name)}\n",
        "\n",
        "docs_dir: docs\n",
        f"site_dir: {yaml_scalar(site_dir_value)}\n",
        "\n",
        "theme:\n",
        "  name: material\n",
        "  language: zh\n",
        "\n",
        "  icon:\n",
        f"    logo: {icon}\n",
        "\n",
        "  features:\n",
    ]

    for feature in features:
        lines.append(f"    - {feature}\n")

    lines.extend(["\n", *build_nav_lines(
        docs_dir=docs_dir,
        results=results,
        include_front_matter_in_nav=include_front_matter_in_nav,
        has_back_matter=has_back_matter,
    )])

    lines.extend(
        [
            "\n",
            "markdown_extensions:\n",
            "  - tables\n",
            "  - attr_list\n",
            "  - md_in_html\n",
            "  - pymdownx.arithmatex:\n",
            "      generic: true\n",
            "  - toc:\n",
            "      permalink: true\n",
            '      toc_depth: "2-3"\n',
            "\n",
            "extra_javascript:\n",
            "  - assets/javascripts/mathjax.js\n",
            "  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js\n",
            "\n",
            "extra:\n",
            f"  homepage: {yaml_scalar(homepage)}\n",
        ]
    )

    config_path = project_dir / "mkdocs.yml"
    config_path.write_text("".join(lines), encoding="utf-8")
    return config_path


def write_mathjax_file(
    docs_dir: Path,
    mathjax_source: str | None,
) -> Path:
    destination = docs_dir / "assets" / "javascripts" / "mathjax.js"
    destination.parent.mkdir(parents=True, exist_ok=True)

    if mathjax_source:
        source = Path(mathjax_source).expanduser().resolve()
        if not source.is_file():
            raise FileNotFoundError(f"MathJax 配置文件不存在：{source}")

        if source != destination.resolve():
            shutil.copy2(source, destination)
    else:
        destination.write_text(DEFAULT_MATHJAX, encoding="utf-8")

    return destination


def write_report(
    docs_dir: Path,
    project_dir: Path,
    markdown_file: Path,
    images_dir: Path | None,
    config_path: Path,
    results: list[ChapterResult],
    front_image_count: int,
    front_missing: list[str],
    back_image_count: int,
    back_missing: list[str],
) -> Path:
    lines = [
        "Markdown 图书拆分报告\n",
        "=" * 60 + "\n",
        f"图书项目目录：{project_dir}\n",
        f"MkDocs 配置：{config_path}\n",
        f"源文件：{markdown_file}\n",
        f"图片目录：{images_dir if images_dir else '未检测到'}\n",
        f"章节数量：{len(results)}\n",
        "\n",
        f"前置内容：复制图片 {front_image_count} 张，缺失 {len(front_missing)} 张\n",
        f"后置内容：复制图片 {back_image_count} 张，缺失 {len(back_missing)} 张\n",
    ]

    for item in results:
        lines.append(
            f"第 {item.number} 章 {item.title}："
            f"复制图片 {item.image_count} 张，"
            f"缺失 {len(item.missing_images)} 张\n"
        )

    all_missing: list[tuple[str, str]] = []

    for path in front_missing:
        all_missing.append(("前置内容", path))

    for item in results:
        for path in item.missing_images:
            all_missing.append((f"第 {item.number} 章", path))

    for path in back_missing:
        all_missing.append(("后置内容", path))

    if all_missing:
        lines.extend(["\n", "未找到的图片\n", "-" * 60 + "\n"])
        for location, path in all_missing:
            lines.append(f"[{location}] {path}\n")

    report_path = docs_dir / "split-report.txt"
    report_path.write_text("".join(lines), encoding="utf-8")
    return report_path


def is_inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def split_book_to_project(
    markdown_path: str,
    project_path: str,
    site_name: str | None,
    site_dir_value: str,
    images_path: str | None = None,
    homepage: str = "/",
    icon: str = "material/wind-turbine",
    mathjax_source: str | None = None,
    clean_docs: bool = False,
    include_front_matter_in_nav: bool = False,
) -> list[ChapterResult]:
    markdown_file = Path(markdown_path).expanduser().resolve()
    project_dir = Path(project_path).expanduser().resolve()
    docs_dir = project_dir / "docs"

    if not markdown_file.is_file():
        raise FileNotFoundError(f"Markdown 文件不存在：{markdown_file}")

    if markdown_file.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError(f"输入文件不是 Markdown：{markdown_file}")

    images_dir = detect_images_directory(
        markdown_file=markdown_file,
        explicit_images_dir=images_path,
    )

    if clean_docs and docs_dir.exists():
        if is_inside(markdown_file, docs_dir):
            raise ValueError("源 Markdown 位于目标 docs 内，不能使用清空模式。")
        if images_dir is not None and is_inside(images_dir, docs_dir):
            raise ValueError("源图片目录位于目标 docs 内，不能使用清空模式。")
        shutil.rmtree(docs_dir)

    project_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    text = markdown_file.read_text(encoding="utf-8-sig", errors="replace")
    lines = text.splitlines(keepends=True)
    structure = find_chapter_starts(lines)
    chapter_starts = structure.chapters
    back_matter_line = structure.back_matter_line

    detected_title = extract_book_title(lines, fallback=markdown_file.stem)
    final_site_name = (site_name or detected_title).strip()

    image_index = build_image_index(images_dir)

    first_chapter_line = chapter_starts[0].line_index
    front_lines = lines[:first_chapter_line]
    has_front_matter = bool("".join(front_lines).strip())

    front_image_count = 0
    front_missing: list[str] = []

    if has_front_matter:
        front_dir = docs_dir / "00-front-matter"
        front_dir.mkdir(parents=True, exist_ok=True)

        front_content = "".join(front_lines)
        front_content, front_image_count, front_missing = copy_and_rewrite_images(
            content=front_content,
            markdown_file=markdown_file,
            images_dir=images_dir,
            chapter_images_dir=front_dir / "images",
            image_index=image_index,
        )

        (front_dir / "index.md").write_text(front_content, encoding="utf-8")

    chapters_root = docs_dir / "chapters"
    chapters_root.mkdir(parents=True, exist_ok=True)

    results: list[ChapterResult] = []

    for position, start in enumerate(chapter_starts):
        end_line = (
            chapter_starts[position + 1].line_index
            if position + 1 < len(chapter_starts)
            else (back_matter_line if back_matter_line is not None else len(lines))
        )

        segment_lines = lines[start.line_index:end_line]
        segment_lines = promote_chapter_headings(
            lines=segment_lines,
            number=start.number,
            title=start.title,
        )

        directory_name = f"{start.number:02d}-{slugify(start.title)}"
        chapter_dir = chapters_root / directory_name
        chapter_dir.mkdir(parents=True, exist_ok=True)

        chapter_content = "".join(segment_lines)
        chapter_content, image_count, missing_images = copy_and_rewrite_images(
            content=chapter_content,
            markdown_file=markdown_file,
            images_dir=images_dir,
            chapter_images_dir=chapter_dir / "images",
            image_index=image_index,
        )

        chapter_markdown = chapter_dir / "index.md"
        chapter_markdown.write_text(chapter_content, encoding="utf-8")

        results.append(
            ChapterResult(
                number=start.number,
                title=start.title,
                directory_name=directory_name,
                markdown_path=chapter_markdown,
                image_count=image_count,
                missing_images=missing_images,
            )
        )

    back_image_count = 0
    back_missing: list[str] = []
    has_back_matter = back_matter_line is not None

    if has_back_matter:
        back_dir = docs_dir / "99-back-matter"
        back_dir.mkdir(parents=True, exist_ok=True)

        back_content = "".join(lines[back_matter_line:])
        back_content, back_image_count, back_missing = copy_and_rewrite_images(
            content=back_content,
            markdown_file=markdown_file,
            images_dir=images_dir,
            chapter_images_dir=back_dir / "images",
            image_index=image_index,
        )

        (back_dir / "index.md").write_text(back_content, encoding="utf-8")

    write_home_page(
        docs_dir=docs_dir,
        book_title=final_site_name,
        results=results,
        has_front_matter=has_front_matter,
        has_back_matter=has_back_matter,
    )

    mathjax_path = write_mathjax_file(
        docs_dir=docs_dir,
        mathjax_source=mathjax_source,
    )

    config_path = write_mkdocs_yml(
        project_dir=project_dir,
        docs_dir=docs_dir,
        site_name=final_site_name,
        site_dir_value=site_dir_value,
        homepage=homepage,
        icon=icon,
        results=results,
        include_front_matter_in_nav=(
            include_front_matter_in_nav and has_front_matter
        ),
        has_back_matter=has_back_matter,
    )

    report_path = write_report(
        docs_dir=docs_dir,
        project_dir=project_dir,
        markdown_file=markdown_file,
        images_dir=images_dir,
        config_path=config_path,
        results=results,
        front_image_count=front_image_count,
        front_missing=front_missing,
        back_image_count=back_image_count,
        back_missing=back_missing,
    )

    print("\n拆分完成")
    print(f"图书项目：{project_dir}")
    print(f"MkDocs 配置：{config_path}")
    print(f"图书首页：{docs_dir / 'index.md'}")
    print(f"MathJax：{mathjax_path}")
    print(f"拆分报告：{report_path}")
    print(f"识别章节：{len(results)} 章")

    total_missing = len(front_missing) + len(back_missing) + sum(
        len(item.missing_images) for item in results
    )
    if total_missing:
        print(f"警告：有 {total_missing} 个图片引用未找到，请查看拆分报告。")

    print("\n预览命令：")
    print(f'  mkdocs serve -f "{config_path}"')

    return results


def prompt_text(label: str, default: str | None = None, required: bool = True) -> str:
    while True:
        suffix = f" [{default}]" if default not in (None, "") else ""
        value = input(f"{label}{suffix}：").strip().strip('"')

        if value:
            return value
        if default is not None:
            return default
        if not required:
            return ""

        print("该项不能为空，请重新输入。")


def prompt_yes_no(label: str, default: bool = True) -> bool:
    hint = "Y/n" if default else "y/N"
    while True:
        value = input(f"{label} [{hint}]：").strip().lower()
        if not value:
            return default
        if value in {"y", "yes", "1", "是"}:
            return True
        if value in {"n", "no", "0", "否"}:
            return False
        print("请输入 y 或 n。")


def interactive_options(args: argparse.Namespace) -> argparse.Namespace:
    print("=" * 62)
    print("Markdown 图书 → 独立 MkDocs 图书项目")
    print("直接输入路径即可；路径两侧有引号也能识别。")
    print("=" * 62)

    if not args.markdown:
        args.markdown = prompt_text("源 Markdown 文件路径")

    markdown_file = Path(args.markdown).expanduser()

    if args.images_dir is None:
        auto_images = ""
        for name in ("images", "image", "draw", "figures", "figure", "media"):
            candidate = markdown_file.parent / name
            if candidate.is_dir():
                auto_images = str(candidate)
                break
        args.images_dir = prompt_text(
            "原始图片文件夹路径（没有可留空）",
            default=auto_images,
            required=False,
        ) or None

    if not args.project_dir:
        args.project_dir = prompt_text(
            "图书项目目录，例如 knowledge-base/books/wind-energy"
        )

    project_name = Path(args.project_dir).name or "book"

    if not args.site_name:
        args.site_name = prompt_text("图书名称", default=markdown_file.stem)

    if not args.site_dir:
        args.site_dir = prompt_text(
            "构建输出 site_dir",
            default=f"../../site/books/{project_name}",
        )

    if args.homepage is None:
        args.homepage = prompt_text("主知识库首页地址", default="/")

    if not args.icon:
        args.icon = prompt_text(
            "Material 图标",
            default="material/wind-turbine",
        )

    if args.mathjax_source is None:
        args.mathjax_source = prompt_text(
            "已有 mathjax.js 路径（留空则自动生成）",
            default="",
            required=False,
        ) or None

    if args.clean is None:
        args.clean = prompt_yes_no("是否先清空目标项目中的 docs 文件夹", True)


    if args.front_matter_nav is None:
        args.front_matter_nav = prompt_yes_no(
            "是否在左侧目录显示前置内容",
            False,
        )

    return args


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="按章拆分 Markdown，并直接生成独立 MkDocs Material 图书项目。"
    )

    parser.add_argument("--markdown", help="源 Markdown 文件路径")
    parser.add_argument("--images-dir", help="原始图片目录")
    parser.add_argument("--project-dir", help="图书项目根目录，内部会创建 docs 和 mkdocs.yml")
    parser.add_argument("--site-name", help="MkDocs 的 site_name")
    parser.add_argument("--site-dir", help="写入 mkdocs.yml 的 site_dir")
    parser.add_argument("--homepage", help="图书 Logo 返回的主知识库地址")
    parser.add_argument("--icon", help="Material 图标，例如 material/wind-turbine")
    parser.add_argument("--mathjax-source", help="已有 mathjax.js；不传则自动生成")

    parser.add_argument(
        "--clean",
        dest="clean",
        action="store_true",
        help="先清空目标项目的 docs 文件夹",
    )
    parser.add_argument(
        "--no-clean",
        dest="clean",
        action="store_false",
        help="不清空目标项目的 docs 文件夹",
    )
    parser.set_defaults(clean=None)


    parser.add_argument(
        "--front-matter-nav",
        dest="front_matter_nav",
        action="store_true",
        help="在左侧导航中显示前置内容",
    )
    parser.add_argument(
        "--no-front-matter-nav",
        dest="front_matter_nav",
        action="store_false",
        help="不在左侧导航中显示前置内容",
    )
    parser.set_defaults(front_matter_nav=None)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    required_missing = not args.markdown or not args.project_dir
    if required_missing or len(sys.argv) == 1:
        if not sys.stdin.isatty():
            parser.error("缺少必要参数：--markdown 和 --project-dir")
        args = interactive_options(args)
    else:
        if args.site_name is None:
            args.site_name = Path(args.markdown).stem
        if args.site_dir is None:
            project_name = Path(args.project_dir).name or "book"
            args.site_dir = f"../../site/books/{project_name}"
        if args.homepage is None:
            args.homepage = "/"
        if args.icon is None:
            args.icon = "material/wind-turbine"
        if args.clean is None:
            args.clean = False
        if args.front_matter_nav is None:
            args.front_matter_nav = False

    try:
        split_book_to_project(
            markdown_path=args.markdown,
            images_path=args.images_dir,
            project_path=args.project_dir,
            site_name=args.site_name,
            site_dir_value=args.site_dir,
            homepage=args.homepage,
            icon=args.icon,
            mathjax_source=args.mathjax_source,
            clean_docs=args.clean,
            include_front_matter_in_nav=args.front_matter_nav,
        )
    except Exception as exc:
        print(f"\n运行失败：{exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
