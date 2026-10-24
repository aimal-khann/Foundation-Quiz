# scripts/build_chapter7_perfect.py
import json
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

from scripts.build_chapter7_part1 import QUESTIONS as q_part1
from scripts.build_chapter7_part2 import QUESTIONS as q_part2
from scripts.build_chapter7_part3 import QUESTIONS as q_part3
from scripts.build_chapter7_part4 import QUESTIONS as q_part4

all_questions = q_part1 + q_part2 + q_part3 + q_part4

assert len(all_questions) == 40, f"Expected 40 questions, got {len(all_questions)}"

# Parity check
for q in all_questions:
    opts = q['options']
    lens = [len(v) for v in opts.values()]
    min_l, max_l = min(lens), max(lens)
    spread = (max_l - min_l) / min_l if min_l > 0 else 0
    assert spread <= 0.05, f"Question {q['id']} failed parity: min={min_l}, max={max_l}, spread={spread*100:.1f}%"

print("All 40 questions passed strict parity (<= 5.0% spread)!")

# Verify IDs
ids = [q['id'] for q in all_questions]
assert ids == list(range(1, 41)), f"IDs mismatch: {ids}"

chapter_data = {
    "chapterId": 7,
    "title": "Chapter 7: General Agents on the Web",
    "totalQuestions": 40,
    "questions": all_questions
}

# Generate JS
js_header = "// Chapter 7 Data - Normalized & Re-Balanced\nwindow.CHAPTER_DATA = window.CHAPTER_DATA || {};\nwindow.CHAPTER_DATA[7] = "
formatted_json = json.dumps(chapter_data, indent=2, ensure_ascii=False)
full_js = js_header + formatted_json + ";\n"

output_path = "data/chapter7.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"Successfully compiled and saved 40 questions to {output_path}!")
