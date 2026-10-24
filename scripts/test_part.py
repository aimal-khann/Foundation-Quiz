import sys
import os
import importlib

sys.path.insert(0, os.path.abspath('.'))

mod_name = sys.argv[1]
mod = importlib.import_module(mod_name)

failed = 0
for q in mod.QUESTIONS:
    lens = [len(v) for v in q['options'].values()]
    min_l, max_l = min(lens), max(lens)
    spread = (max_l - min_l) / min_l if min_l > 0 else 0
    ok = spread <= 0.05
    status = "OK" if ok else "FAIL"
    if not ok:
        failed += 1
    print(f"Q{q['id']:<2}: lens={lens} min={min_l} max={max_l} spread={spread:5.1%} [{status}] Key: {q['correct']}")

print(f"\nResult: {'ALL PASSED' if failed == 0 else f'{failed} FAILED'}")
