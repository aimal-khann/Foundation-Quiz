# scripts/build_chapter5_perfect.py
import json
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

from scripts.build_chapter5_part1 import questions_1_to_10
from scripts.build_chapter5_part2 import questions_11_to_20
from scripts.build_chapter5_part3 import questions_21_to_30

all_questions = questions_1_to_10 + questions_11_to_20 + questions_21_to_30

assert len(all_questions) == 30, f"Expected 30 questions, got {len(all_questions)}"

# Parity check
for q in all_questions:
    opts = q['options']
    lens = [len(v) for v in opts.values()]
    min_l, max_l = min(lens), max(lens)
    spread = (max_l - min_l) / min_l if min_l > 0 else 0
    assert spread <= 0.05, f"Question {q['id']} failed parity: min={min_l}, max={max_l}, spread={spread*100:.1f}%"

print("All 30 questions passed strict parity (<= 5.0% spread)!")

# Verify IDs
ids = [q['id'] for q in all_questions]
assert ids == list(range(1, 31)), f"IDs mismatch: {ids}"

chapter_data = {
    "chapterId": 5,
    "title": "Chapter 5: ChatGPT & Claude: Architectures, Workspaces & Tooling",
    "totalQuestions": 30,
    "questions": all_questions
}

# Generate JS
js_header = "// Chapter 5 Data - Normalized & Re-Balanced\nwindow.CHAPTER_DATA = window.CHAPTER_DATA || {};\nwindow.CHAPTER_DATA[5] = "
formatted_json = json.dumps(chapter_data, indent=2, ensure_ascii=False)
full_js = js_header + formatted_json + ";\n"

output_path = "data/chapter5.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"Successfully compiled and saved 30 questions to {output_path}!")
