#!/usr/bin/env python
"""Convert the bundled Zhou Zhihua EPUB into a chapter-based MkDocs book."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BOOK_ROOT = ROOT / "books" / "zhou-machine-learning"
DOCS = BOOK_ROOT / "docs"
DOWNLOADS = DOCS / "downloads"
EPUB = next(DOWNLOADS.glob("*.epub"))
BVID = "BV1gG411f7zX"


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    slug: str
    video_parts: tuple[tuple[int, int, str], ...] = ()


CHAPTERS = (
    Chapter(1, "绪论", "introduction", (
        (3, 1235315584, "机器学习"),
        (4, 1235317100, "典型的机器学习过程"),
        (5, 1235318919, "机器学习理论"),
        (6, 1235323747, "基本术语"),
        (7, 1235331120, "归纳偏好"),
        (8, 1235332912, "NFL 定理"),
    )),
    Chapter(2, "模型评估与选择", "model-evaluation-and-selection", (
        (9, 1235726895, "泛化能力"),
        (10, 1235727628, "过拟合和欠拟合"),
        (11, 1235729889, "三大问题"),
        (12, 1235730688, "评估方法"),
        (13, 1235735468, "调参与验证集"),
        (14, 1235737518, "性能度量"),
        (15, 1235738483, "比较检验"),
    )),
    Chapter(3, "线性模型", "linear-models", (
        (16, 1235925424, "线性回归"),
        (17, 1235928267, "最小二乘解"),
        (18, 1235930504, "多元线性回归"),
        (19, 1235933167, "广义线性模型"),
        (20, 1235934127, "对率回归"),
        (21, 1235936428, "对率回归求解"),
        (22, 1236961257, "线性判别分析"),
        (23, 1462516099, "LDA 的多类推广"),
        (24, 1462516494, "多分类学习基本思路"),
        (25, 1235948080, "类别不平衡"),
    )),
    Chapter(4, "决策树", "decision-trees", (
        (26, 1236964212, "决策树基本流程"),
        (27, 1236965536, "信息增益划分"),
        (28, 1236966712, "其他属性划分准则"),
        (29, 1236968418, "决策树剪枝"),
        (30, 1236969063, "缺失值的处理"),
    )),
    Chapter(5, "神经网络", "neural-networks", (
        (37, 29655696620, "神经网络模型"),
        (38, 29655696902, "万有逼近能力"),
        (39, 29655696933, "缓解过拟合"),
        (40, 29655892942, "神经网络简史"),
        (41, 29655894518, "深度神经网络的发展"),
    )),
    Chapter(6, "支持向量机", "support-vector-machines", (
        (31, 29655697209, "支持向量机基本型"),
        (32, 29655697132, "对偶问题与解的特性"),
        (33, 29655697337, "求解方法"),
        (34, 29655697360, "特征空间映射"),
        (35, 29655697511, "核函数"),
        (36, 29655697421, "SVM 简史"),
    )),
    Chapter(7, "贝叶斯分类器", "bayesian-classifiers", (
        (42, 29655895389, "贝叶斯决策论"),
        (43, 29655895319, "生成式和判别模型"),
        (44, 29655895505, "贝叶斯定理"),
        (45, 29655895550, "极大似然估计"),
        (46, 29655895759, "朴素贝叶斯分类器"),
        (47, 29656089533, "拉普拉斯修正"),
    )),
    Chapter(8, "集成学习", "ensemble-learning", (
        (48, 29655957698, "集成学习"),
        (49, 29655957713, "好而不同"),
        (50, 29655957770, "两类常用集成学习方法"),
        (51, 29655957798, "Boosting"),
        (52, 29655957881, "Bagging"),
    )),
    Chapter(9, "聚类", "clustering", (
        (53, 29655958072, "聚类"),
        (54, 29655957925, "聚类性能度量"),
        (55, 29655958180, "距离计算"),
        (56, 29655957955, "聚类方法概述"),
    )),
    Chapter(10, "降维与度量学习", "dimensionality-reduction-and-metric-learning"),
    Chapter(11, "特征选择与稀疏学习", "feature-selection-and-sparse-learning"),
    Chapter(12, "计算学习理论", "computational-learning-theory"),
    Chapter(13, "半监督学习", "semi-supervised-learning"),
    Chapter(14, "概率图模型", "probabilistic-graphical-models"),
    Chapter(15, "规则学习", "rule-learning"),
    Chapter(16, "强化学习", "reinforcement-learning"),
)


def video_block(chapter: Chapter) -> str:
    if not chapter.video_parts:
        return (
            '\n<div class="chapter-video chapter-video--unavailable">\n'
            '<strong>本章配套视频</strong>\n'
            '<p>当前这套 56P《机器学习初步》只覆盖教材第 1–9 章，'
            '没有本章的对应分 P。此处不强行错配，请以本章原书正文为准。</p>\n'
            f'<a href="https://www.bilibili.com/video/{BVID}/" target="_blank" '
            'rel="noopener">查看完整视频选集 ↗</a>\n'
            '</div>\n\n'
        )

    first_p, first_cid, _ = chapter.video_parts[0]
    last_p = chapter.video_parts[-1][0]
    label = f"P{first_p}" if first_p == last_p else f"P{first_p}–P{last_p}"
    links = "\n".join(
        f'<a class="video-part" href="https://www.bilibili.com/video/{BVID}/?p={part}" '
        f'target="_blank" rel="noopener">P{part} · {title}</a>'
        for part, _, title in chapter.video_parts
    )
    return f'''\n<div class="chapter-video">
<div class="chapter-video__heading"><strong>本章配套视频 · {label}</strong><span>播放器从 P{first_p} 开始</span></div>
<div class="video-embed">
  <iframe
    src="https://player.bilibili.com/player.html?isOutside=true&amp;bvid={BVID}&amp;cid={first_cid}&amp;p={first_p}&amp;high_quality=1&amp;danmaku=0&amp;autoplay=0"
    title="第 {chapter.number} 章 {chapter.title}配套视频，从 P{first_p} 开始"
    loading="lazy"
    scrolling="no"
    frameborder="0"
    allow="fullscreen; picture-in-picture"
    allowfullscreen>
  </iframe>
</div>
<details class="video-parts">
<summary>展开本章全部分 P（{label}）</summary>
<div class="video-parts__links">
{links}
</div>
</details>
</div>

'''


def normalize_markdown(text: str) -> str:
    # Pandoc emits absolute Windows paths when --extract-media receives an
    # absolute directory. Keep only the EPUB image filename in final pages.
    text = re.sub(
        r'[A-Za-z]:\\[^"\'\)>\n]*?\\media[\\/]images[\\/]([A-Za-z0-9_.-]+)',
        r'images/\1',
        text,
    )
    text = re.sub(
        r'[A-Za-z]:\\[^"\'\)>\n]*?\\media[\\/]cover\.jpeg',
        r'images/cover.jpeg',
        text,
    )
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip() + "\n"


def referenced_images(text: str) -> set[str]:
    return set(re.findall(r'images/([A-Za-z0-9_.-]+)', text))


def copy_images(text: str, source_images: Path, target_dir: Path) -> int:
    names = referenced_images(text)
    if not names:
        return 0
    target_dir.mkdir(parents=True, exist_ok=True)
    for name in sorted(names):
        source = source_images / name
        if not source.is_file():
            raise FileNotFoundError(f"Missing extracted EPUB image: {source}")
        shutil.copy2(source, target_dir / name)
    return len(names)


def write_front_matter(source: str, media_root: Path) -> int:
    start = source.index("# 序言")
    end = source.index("# 第1章")
    body = source[start:end]
    body = re.sub(r'^# ', '## ', body, flags=re.MULTILINE)
    body = normalize_markdown("# 前置内容\n\n" + body)
    target = DOCS / "00-front-matter"
    target.mkdir(parents=True, exist_ok=True)
    (target / "index.md").write_text(body, encoding="utf-8")
    count = copy_images(body, media_root / "images", target / "images")
    shutil.copy2(media_root / "cover.jpeg", target / "images" / "cover.jpeg")
    return count + 1


def write_back_matter(source: str, media_root: Path) -> int:
    start = source.index("# 附录")
    body = source[start:]
    body = re.sub(r'^# ', '## ', body, flags=re.MULTILINE)
    body = normalize_markdown("# 附录与后记\n\n" + body)
    target = DOCS / "99-back-matter"
    target.mkdir(parents=True, exist_ok=True)
    (target / "index.md").write_text(body, encoding="utf-8")
    return copy_images(body, media_root / "images", target / "images")


def write_chapters(source: str, media_root: Path) -> tuple[int, int]:
    matches = list(re.finditer(r'^# 第(\d+)章\s+(.+?)\s*$', source, flags=re.MULTILINE))
    if len(matches) != len(CHAPTERS):
        raise RuntimeError(f"Expected 16 chapter headings, found {len(matches)}")
    appendix = source.index("# 附录", matches[-1].start())
    total_images = 0
    for index, (chapter, match) in enumerate(zip(CHAPTERS, matches, strict=True)):
        found_number = int(match.group(1))
        found_title = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if (found_number, found_title) != (chapter.number, chapter.title):
            raise RuntimeError(
                f"Chapter mismatch: expected {chapter.number} {chapter.title!r}, "
                f"found {found_number} {found_title!r}"
            )
        end = matches[index + 1].start() if index + 1 < len(matches) else appendix
        body = source[match.start():end]
        first_newline = body.index("\n") + 1
        body = body[:first_newline] + video_block(chapter) + body[first_newline:]
        body = normalize_markdown(body)
        target = DOCS / "chapters" / f"{chapter.number:02d}-{chapter.slug}"
        target.mkdir(parents=True, exist_ok=True)
        (target / "index.md").write_text(body, encoding="utf-8")
        total_images += copy_images(body, media_root / "images", target / "images")
    return len(CHAPTERS), total_images


def write_homepage() -> None:
    chapter_links = "\n".join(
        f'- [第 {chapter.number} 章　{chapter.title}]'
        f'(chapters/{chapter.number:02d}-{chapter.slug}/index.md)'
        for chapter in CHAPTERS
    )
    text = f'''---
hide:
  - toc
---

<div class="study-hero study-hero--ml" markdown>

<span class="study-hero__eyebrow">FULL TEXT · 16 CHAPTERS · 1100+ FIGURES</span>

# 周志华《机器学习》

“西瓜书”完整 EPUB 正文已转换为 16 个按章组织的 Markdown 页面，公式、表格和插图随章保存。第 1–9 章开头嵌入周志华《机器学习初步》对应分 P，第 10–16 章保留原书主线并明确标出视频覆盖边界。

[开始阅读第 1 章](chapters/01-introduction/index.md){{ .md-button .md-button--primary }}
[阅读前置内容](00-front-matter/index.md){{ .md-button }}
[下载原 EPUB](downloads/周志华-机器学习.epub){{ .md-button download }}

</div>

<div class="book-intro-grid">
  <img class="book-cover" src="00-front-matter/images/cover.jpeg" alt="周志华《机器学习》封面">
  <div markdown>

## 在线阅读说明

- 左侧目录按原书 16 章组织，站内搜索可直接检索正文。
- 每章图片位于该章自己的 `images` 目录，页面不依赖外部图床。
- 视频选集共 56P，对应教材第 1–9 章；第 5、6 章已按书本主题校正顺序。
- 原 EPUB 与 PDF 下载仍保留，在线正文以本次 EPUB 转换结果为准。

  </div>
</div>

## 章节目录

{chapter_links}

## 其他内容

- [序言、前言、使用说明与主要符号表](00-front-matter/index.md)
- [附录与后记](99-back-matter/index.md)
'''
    (DOCS / "index.md").write_text(text, encoding="utf-8")


def write_mkdocs_config() -> None:
    nav = [
        "  - 图书首页: index.md",
        "  - 前置内容: 00-front-matter/index.md",
    ]
    nav.extend(
        f"  - 第{chapter.number}章 {chapter.title}: "
        f"chapters/{chapter.number:02d}-{chapter.slug}/index.md"
        for chapter in CHAPTERS
    )
    nav.append("  - 附录与后记: 99-back-matter/index.md")
    text = '''site_name: 周志华《机器学习》· 在线图书
site_description: 周志华《机器学习》16 章完整在线正文与分 P 配套视频
docs_dir: docs
site_dir: ../../site/book-sites/zhou-machine-learning
theme:
  name: material
  language: zh
  icon: {logo: material/book-education}
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: orange
      toggle: {icon: material/brightness-7, name: 切换深色模式}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: orange
      toggle: {icon: material/brightness-4, name: 切换浅色模式}
  features: [navigation.sections, navigation.top, navigation.footer, navigation.path, content.code.copy]
nav:
''' + "\n".join(nav) + '''
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - footnotes
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tasklist:
      custom_checkbox: true
  - toc:
      permalink: true
      toc_depth: 2-3
extra_css: [assets/stylesheets/study-site.css, assets/stylesheets/back-to-main.css]
extra_javascript: [assets/javascripts/study-progress.js, assets/javascripts/back-to-main.js]
extra:
  homepage: /programming/
copyright: '返回 <a href="/programming/">编程与人工智能学习中心</a>'
'''
    (BOOK_ROOT / "mkdocs.yml").write_text(text, encoding="utf-8")


def main() -> None:
    if not EPUB.is_file():
        raise FileNotFoundError(EPUB)

    with tempfile.TemporaryDirectory(prefix="zhou-epub-") as temp_name:
        temp = Path(temp_name)
        media = temp / "media"
        media.mkdir()
        markdown = temp / "book.md"
        subprocess.run(
            [
                "pandoc",
                str(EPUB),
                "-f", "epub",
                "-t", "gfm",
                "--wrap=none",
                f"--extract-media={media}",
                "-o", str(markdown),
            ],
            cwd=ROOT,
            check=True,
        )
        source = markdown.read_text(encoding="utf-8")

        chapter_count, chapter_images = write_chapters(source, media)
        front_images = write_front_matter(source, media)
        back_images = write_back_matter(source, media)

    write_homepage()
    write_mkdocs_config()
    print(
        f"Converted {chapter_count} chapters; copied "
        f"{chapter_images + front_images + back_images} chapter-local image files."
    )


if __name__ == "__main__":
    main()
