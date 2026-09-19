from __future__ import annotations

"""检查课程中的 Python 语法和 Markdown 相对链接。"""

import compileall
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_DIRS = [ROOT / "01_python_core", ROOT / "02_data_analysis"]


def check_markdown_links() -> list[str]:
    missing: list[str] = []
    pattern = re.compile(r"\[[^]]+]\(([^)]+)\)")
    for course_dir in COURSE_DIRS:
        for document in course_dir.rglob("*.md"):
            for target in pattern.findall(document.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                path = (document.parent / target.split("#", 1)[0]).resolve()
                if not path.exists():
                    missing.append(f"{document.relative_to(ROOT)} -> {target}")
    return missing


def main() -> None:
    syntax_ok = all(compileall.compile_dir(path, quiet=1) for path in COURSE_DIRS)
    missing_links = check_markdown_links()
    python_files = sum(1 for path in COURSE_DIRS for _ in path.rglob("*.py"))
    markdown_files = sum(1 for path in COURSE_DIRS for _ in path.rglob("*.md"))
    print(f"Python 文件：{python_files}")
    print(f"Markdown 文档：{markdown_files}")
    print(f"Python 语法：{'通过' if syntax_ok else '失败'}")
    print(f"Markdown 链接：{'通过' if not missing_links else '失败'}")
    for item in missing_links:
        print("缺失：", item)
    if not syntax_ok or missing_links:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
