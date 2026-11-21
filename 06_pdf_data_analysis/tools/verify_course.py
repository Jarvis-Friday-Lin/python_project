"""从任何目录运行：批量验证课程结构、打印分隔符、示例与参考答案。"""
import ast
import contextlib
import io
import os
from pathlib import Path
import runpy
import sys
import traceback
import warnings

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "outputs" / "mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / "outputs" / "cache"))
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # 批量检查时不打开窗口；学生正常运行教学文件仍会显示图像。
    plt.show = lambda *args, **kwargs: None
    folders = sorted({p.parent for p in ROOT.glob("[0-9][0-9]_*/*/01_examples.py")})
    failures = []
    expected = {"01_基础准备": 3, "02_numpy": 19, "03_pandas": 15, "04_matplotlib": 13, "05_综合案例": 3}
    for section, count in expected.items():
        actual = sum(folder.parent.name == section for folder in folders)
        if actual != count:
            failures.append(f"{section}目录数量：预期{count}，实际{actual}")
    warning_messages = set()
    executed = 0
    output = ROOT / "outputs"
    output.mkdir(exist_ok=True)
    for folder in folders:
        for filename in ["01_examples.py", "02_exercises.py", "03_answers.py"]:
            path = folder / filename
            if not path.exists():
                failures.append(f"缺少文件：{path.relative_to(ROOT)}")
                continue
            source = path.read_text(encoding="utf-8")
            try:
                tree = ast.parse(source, filename=str(path))
                compile(tree, str(path), "exec")
                if filename == "02_exercises.py":
                    assert "# |" in source, "练习缺少案例数据表"
                    assert "业务任务与本题要求" in source, "练习缺少独立要求"
                    continue
                assert any(isinstance(n, ast.Assert) for n in ast.walk(tree)), "缺少结果检查"
                lines = source.splitlines()
                for node in ast.walk(tree):
                    if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call):
                        continue
                    call = node.value
                    is_print = isinstance(call.func, ast.Name) and call.func.id == "print"
                    is_info = isinstance(call.func, ast.Attribute) and call.func.attr == "info"
                    if not (is_print or is_info):
                        continue
                    if is_print and call.args and isinstance(call.args[0], ast.Constant) and str(call.args[0].value).startswith("\n====="):
                        continue
                    assert node.lineno > 1 and "=====" in lines[node.lineno - 2], "数据输出前缺少分隔符"
                with warnings.catch_warnings(record=True) as records:
                    warnings.simplefilter("always")
                    with contextlib.redirect_stdout(io.StringIO()):
                        runpy.run_path(str(path), run_name="__main__")
                    warning_messages.update(str(w.message) for w in records)
                executed += 1
            except Exception:
                failures.append(str(path.relative_to(ROOT)) + "\n" + traceback.format_exc())
            finally:
                plt.close("all")
    report = [f"知识点/案例目录：{len(folders)}", f"运行成功：{executed}", f"失败：{len(failures)}",
              f"Python：{sys.version.split()[0]}", f"NumPy：{np.__version__}",
              f"Pandas：{pd.__version__}", f"Matplotlib：{matplotlib.__version__}"]
    report.extend(failures)
    if warning_messages:
        report += ["运行警告："] + sorted(warning_messages)
    text = "\n".join(report) + "\n"
    (output / "verification.txt").write_text(text, encoding="utf-8")
    print(text)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
