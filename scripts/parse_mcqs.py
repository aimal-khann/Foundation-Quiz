"""
mcq_parser.py
Utility to automatically parse Markdown files containing MCQs into structured JSON/JS data.
Accepts flexible markdown formats for MCQs, including:
- Question title / number
- Options (A, B, C, D or 1, 2, 3, 4)
- Correct answer indicator
- Main explanation
- Specific breakdowns explaining why each other option is incorrect
"""

import sys
import os
import re
import json

def parse_markdown_mcqs(md_text, chapter_num=1, chapter_title=None):
    lines = md_text.splitlines()
    questions = []
    
    current_q = None
    collecting_explanation = False
    collecting_option_breakdowns = False
    
    # Regular expressions for matching
    q_start_re = re.compile(r'^(?:###?\s*|)(?:Question\s*|Q\s*|)(\d+)[\.:\s]+(.*)', re.IGNORECASE)
    option_re = re.compile(r'^\s*[-*]?\s*(?:[A-Da-d][\.\)]|\([A-Da-d]\))\s*(.*)')
    correct_re = re.compile(r'^\s*[-*]?\s*(?:\*\*)?(?:Correct\s*(?:Answer|Option)?|Answer)(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*\(?([A-Da-d])\)?', re.IGNORECASE)
    explanation_re = re.compile(r'^\s*[-*]?\s*(?:\*\*)?(?:Detailed\s+Explanation|Explanation)(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*(.*)', re.IGNORECASE)
    why_distractor_re = re.compile(r'^\s*[-*]?\s*(?:\*\*)?(?:Why\s+([A-Da-d])\s+is\s+(?:not\s+correct|incorrect)|Option\s+([A-Da-d]))(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*(.*)', re.IGNORECASE)

    def finalize_question(q):
        if not q or not q.get('question'):
            return None
        # Clean options dict
        options = q.get('options', {})
        # Ensure at least A, B, C, D
        correct = q.get('correct', 'A').upper()
        # Clean explanations
        explanation = q.get('explanation', '').strip()
        why_incorrect = q.get('why_incorrect', {})
        
        return {
            'id': q.get('id', len(questions) + 1),
            'question': q['question'].strip(),
            'options': options,
            'correct': correct,
            'explanation': explanation,
            'why_incorrect': why_incorrect
        }

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Check for new question
        q_match = q_start_re.match(stripped)
        if q_match and ('?' in stripped or len(stripped.split()) > 3 or 'Question' in stripped or 'Q.' in stripped):
            if current_q:
                finalized = finalize_question(current_q)
                if finalized:
                    questions.append(finalized)
            q_num = int(q_match.group(1))
            q_text = q_match.group(2).strip()
            if not q_text and len(lines) > lines.index(line) + 1:
                q_text = lines[lines.index(line) + 1].strip()
            current_q = {
                'id': q_num,
                'question': q_text,
                'options': {},
                'correct': 'A',
                'explanation': '',
                'why_incorrect': {}
            }
            collecting_explanation = False
            collecting_option_breakdowns = False
            continue

        if not current_q:
            continue

        # Check for Correct Answer
        corr_match = correct_re.search(stripped)
        if corr_match:
            current_q['correct'] = corr_match.group(1).upper()
            collecting_explanation = False
            collecting_option_breakdowns = False
            continue

        # Check for Why incorrect breakdown
        distr_match = why_distractor_re.search(stripped)
        if distr_match:
            opt_key = (distr_match.group(1) or distr_match.group(2)).upper()
            detail = distr_match.group(3).strip()
            current_q['why_incorrect'][opt_key] = detail
            collecting_option_breakdowns = opt_key
            collecting_explanation = False
            continue

        # Check for Explanation
        exp_match = explanation_re.search(stripped)
        if exp_match:
            exp_text = exp_match.group(1).strip()
            current_q['explanation'] = exp_text
            collecting_explanation = True
            collecting_option_breakdowns = False
            continue

        # Check for Option (A, B, C, D)
        opt_match = option_re.match(stripped)
        if opt_match and not collecting_explanation and not collecting_option_breakdowns:
            # find which letter
            letter_m = re.match(r'^\s*[-*]?\s*(?:([A-Da-d])[\.\)]|\(([A-Da-d])\))', stripped)
            if letter_m:
                letter = (letter_m.group(1) or letter_m.group(2)).upper()
                opt_content = re.sub(r'^\s*[-*]?\s*(?:[A-Da-d][\.\)]|\([A-Da-d]\))\s*', '', stripped).strip()
                current_q['options'][letter] = opt_content
                continue

        # Continuation of explanation
        if collecting_explanation:
            if current_q['explanation']:
                current_q['explanation'] += ' ' + stripped
            else:
                current_q['explanation'] = stripped
            continue

        # Continuation of why_incorrect
        if collecting_option_breakdowns:
            opt_key = collecting_option_breakdowns
            current_q['why_incorrect'][opt_key] = (current_q['why_incorrect'].get(opt_key, '') + ' ' + stripped).strip()
            continue

        # If question text spans multiple lines before options start
        if not current_q['options'] and not collecting_explanation:
            current_q['question'] += ' ' + stripped

    if current_q:
        finalized = finalize_question(current_q)
        if finalized:
            questions.append(finalized)

    if not chapter_title:
        chapter_title = f"Chapter {chapter_num}"

    return {
        'chapterId': chapter_num,
        'title': chapter_title,
        'totalQuestions': len(questions),
        'questions': questions
    }

def convert_file(input_md_path, output_js_path, output_json_path=None, chapter_num=1, chapter_title=None):
    with open(input_md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    data = parse_markdown_mcqs(md_text, chapter_num=chapter_num, chapter_title=chapter_title)
    
    # Save as JS for local browser file:// compatibility
    js_content = f"// Chapter {chapter_num} Data\nwindow.CHAPTER_DATA = window.CHAPTER_DATA || {{}};\nwindow.CHAPTER_DATA[{chapter_num}] = {json.dumps(data, indent=2, ensure_ascii=False)};\n"
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    if output_json_path:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    print(f"Successfully converted '{input_md_path}' -> {len(data['questions'])} questions generated into '{output_js_path}'")
    return data

if __name__ == '__main__':
    if len(sys.argv) > 1:
        md_file = sys.argv[1]
        chap_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        out_js = f"data/chapter{chap_num}.js"
        convert_file(md_file, out_js, chapter_num=chap_num)
    else:
        print("Usage: python parse_mcqs.py <path_to_markdown.md> [chapter_number]")
