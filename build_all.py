#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "site"
BOOKS_DIR = ROOT / "books"


def run_mkdocs(config_file: Path) -> None:
    """构建一个 MkDocs 项目。"""
    print(f"\n正在构建：{config_file}")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "mkdocs",
            "build",
            "--config-file",
            str(config_file),
        ],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    # 先统一清空最终输出目录
    if SITE_DIR.exists():
        print(f"删除旧网站：{SITE_DIR}")
        shutil.rmtree(SITE_DIR)

    # 1. 先构建主知识库
    main_config = ROOT / "mkdocs.yml"

    if not main_config.is_file():
        raise FileNotFoundError(f"找不到主配置：{main_config}")

    run_mkdocs(main_config)

    # 2. 再构建所有独立图书
    book_configs = sorted(BOOKS_DIR.glob("*/mkdocs.yml"))

    if not book_configs:
        print("\n没有发现独立图书配置。")
    else:
        for config_file in book_configs:
            run_mkdocs(config_file)

    print("\n全部构建完成。")
    print(f"输出目录：{SITE_DIR}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"\n构建失败，退出代码：{exc.returncode}")
        sys.exit(exc.returncode)
    except Exception as exc:
        print(f"\n运行失败：{exc}")
        sys.exit(1)