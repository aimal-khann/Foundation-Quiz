import re
import json
import random
import sys

def rebalance_chapter_4(
    input_file="skill-conncetors.md", 
    output_md="chapter4_rebalanced.md", 
    output_js="data/chapter4.js"
):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Clean pagination headers & URL footers
    clean_text = re.sub(r'\d{2}/\d{2}/\d{4},\s+\d{2}:\d{2}\s+[^\n]+\s*\nhttps://[^\n]+', '', content)
    # Normalize stray arrow characters for safety
    clean_text = clean_text.replace('\u2192', '->')

    # Locate Answer Key section markers (4 batches)
    ans_sec_starts = [m.start() for m in re.finditer(r'Answer\s+Key\s+&\s+Deep\s+Analytical\s+Justifications', clean_text)]
    
    # Locate Question start markers for batches 2, 3, 4
    m11 = re.search(r'(?:^|\n)\s*Practice\s+Examination\s+Items:\s*Batch\s+2', clean_text)
    m21 = re.search(r'(?:^|\n)\s*Practice\s+Examination\s+Items:\s*Batch\s+3', clean_text)
    m31 = re.search(r'(?:^|\n)\s*Practice\s+Examination\s+Items:\s*Batch\s+4', clean_text)
    q_starts = [0, m11.start(), m21.start(), m31.start()]

    questions = {}

    for b_idx in range(4):
        q_start = q_starts[b_idx]
        ans_start = ans_sec_starts[b_idx]
        next_q_start = q_starts[b_idx + 1] if b_idx + 1 < 4 else len(clean_text)
        
        q_chunk = clean_text[q_start:ans_start]
        ans_chunk = clean_text[ans_start:next_q_start]
        
        # 1. Parse questions and options
        q_matches = list(re.finditer(r'(?:^|\n)\s*(?:###\s*)?Question\s+(\d+)\s*\n', q_chunk))
        for j, qm in enumerate(q_matches):
            q_num = int(qm.group(1))
            start_pos = qm.end()
            end_pos = q_matches[j+1].start() if j+1 < len(q_matches) else len(q_chunk)
            q_body = q_chunk[start_pos:end_pos].strip()
            
            # Use regex for options A. B. C. D.
            opt_matches = list(re.finditer(r'\b([A-D])\.\s+', q_body))
            if opt_matches:
                stem = q_body[:opt_matches[0].start()].strip()
                options = {}
                for k, om in enumerate(opt_matches):
                    letter = om.group(1)
                    o_start = om.end()
                    o_end = opt_matches[k+1].start() if k+1 < len(opt_matches) else len(q_body)
                    options[letter] = q_body[o_start:o_end].strip()
            else:
                stem = q_body
                options = {}
                
            questions[q_num] = {
                'id': q_num,
                'stem': stem,
                'options': options
            }
            
        # 2. Parse answer keys and justifications
        a_matches = list(re.finditer(r'(?:^|\n)\s*(?:###\s*)?Question\s+(\d+)\s*\n', ans_chunk))
        for j, am in enumerate(a_matches):
            q_num = int(am.group(1))
            start_pos = am.end()
            end_pos = a_matches[j+1].start() if j+1 < len(a_matches) else len(ans_chunk)
            a_body = ans_chunk[start_pos:end_pos].strip()
            
            corr_m = re.search(r'Correct\s*Answers?:\s*([^\n]+)', a_body)
            correct = corr_m.group(1).strip() if corr_m else ''
            
            just_m = re.search(r'Analytical\s*Justification:\s*\n(.*)', a_body, re.DOTALL)
            just_raw = just_m.group(1).strip() if just_m else a_body
            just_clean = re.split(r'\n(?:User\s+prompt|Response:|Pre-Batch|Practice\s+Examination|Batch\s+\d)', just_raw)[0].strip()
            
            if q_num in questions:
                questions[q_num]['correct'] = correct
                questions[q_num]['justification'] = just_clean

    print(f"Loaded {len(questions)} questions from {input_file}.")

    # Identify single-choice vs multi-choice items
    single_choice_ids = []
    multi_choice_ids = []
    for q_id in range(1, 41):
        corr = questions[q_id]['correct']
        if 'and' in corr or ',' in corr:
            multi_choice_ids.append(q_id)
        else:
            single_choice_ids.append(q_id)

    print(f"Single-choice count: {len(single_choice_ids)} (IDs: {single_choice_ids})")
    print(f"Multi-choice count: {len(multi_choice_ids)} (IDs: {multi_choice_ids})")

    # High-entropy pseudo-random balanced target distribution for 35 single choice items:
    # 9 A's, 9 B's, 9 C's, 8 D's (Total: 35)
    # Verified: No letter repeated > 2 times, no cyclic 4-grams (ABCD/DCBA), well distributed across quarters.
    single_targets = [
        'C', 'A', 'C', 'B', 'B', 'D', 'A', 'A', 'D', 'D', 
        'B', 'A', 'C', 'B', 'D', 'A', 'B', 'B', 'C', 'A', 
        'A', 'C', 'C', 'A', 'B', 'D', 'D', 'C', 'A', 'D', 
        'B', 'C', 'D', 'C', 'B'
    ]

    counts = {x: single_targets.count(x) for x in ['A', 'B', 'C', 'D']}
    print("Single choice target distribution:", counts)

    # For 5 multi-choice items (Q2, Q11, Q27, Q36, Q40), 5 distinct diverse pairs:
    multi_target_pairs = [
        ('A', 'D'),  # Q2
        ('B', 'C'),  # Q11
        ('B', 'D'),  # Q27
        ('A', 'C'),  # Q36
        ('C', 'D')   # Q40
    ]

    rebalanced_questions = []
    single_idx = 0
    multi_idx = 0

    for q_id in range(1, 41):
        q = questions[q_id]
        orig_opts = q['options']
        orig_corr = q['correct']
        orig_just = q['justification']
        
        is_multi = q_id in multi_choice_ids

        if not is_multi:
            target_ans = single_targets[single_idx]
            single_idx += 1
            
            orig_other = [x for x in ['A', 'B', 'C', 'D'] if x != orig_corr]
            target_other = [x for x in ['A', 'B', 'C', 'D'] if x != target_ans]
            
            rnd = random.Random(q_id * 71 + 37)
            rnd.shuffle(target_other)
            
            old_to_new = {orig_corr: target_ans}
            for o_old, o_new in zip(orig_other, target_other):
                old_to_new[o_old] = o_new
                
            new_corr_str = target_ans
        else:
            target_pair = sorted(multi_target_pairs[multi_idx])
            multi_idx += 1
            
            old_pair = sorted(re.findall(r'[A-D]', orig_corr))
            orig_other = [x for x in ['A', 'B', 'C', 'D'] if x not in old_pair]
            target_other = [x for x in ['A', 'B', 'C', 'D'] if x not in target_pair]
            
            rnd = random.Random(q_id * 53 + 41)
            rnd.shuffle(target_other)
            
            if rnd.random() > 0.5:
                old_to_new = {old_pair[0]: target_pair[0], old_pair[1]: target_pair[1]}
            else:
                old_to_new = {old_pair[0]: target_pair[1], old_pair[1]: target_pair[0]}
                
            for o_old, o_new in zip(orig_other, target_other):
                old_to_new[o_old] = o_new
                
            new_corr_str = f"{target_pair[0]} and {target_pair[1]}"

        # Invert mapping: new letter -> old letter
        new_to_old = {v: k for k, v in old_to_new.items()}

        # Build re-balanced options dict
        new_options = {}
        for l in ['A', 'B', 'C', 'D']:
            new_options[l] = orig_opts[new_to_old[l]]

        # Synchronize Justification text with multi-pass placeholder substitution
        updated_just = orig_just
        
        # 1. Replace 3-option groupings: e.g. "Options A, C, and D"
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                for o3 in ['A', 'B', 'C', 'D']:
                    if len({o1, o2, o3}) == 3:
                        p = re.compile(rf'\bOptions\s+{o1},\s*{o2},?\s+and\s+{o3}\b', re.IGNORECASE)
                        updated_just = p.sub(f'__OPTS_3_{o1}_{o2}_{o3}__', updated_just)
                        
        # 2. Replace 2-option groupings: e.g. "Options A and B"
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                if o1 != o2:
                    p = re.compile(rf'\bOptions\s+{o1}\s+and\s+{o2}\b', re.IGNORECASE)
                    updated_just = p.sub(f'__OPTS_2_{o1}_{o2}__', updated_just)
                    
        # 3. Replace single options: e.g. "Option A"
        for o in ['A', 'B', 'C', 'D']:
            p = re.compile(rf'\bOption\s+{o}\b', re.IGNORECASE)
            updated_just = p.sub(f'__OPT_{o}__', updated_just)
            
        # Replace placeholders with final mapped new letters
        for o in ['A', 'B', 'C', 'D']:
            updated_just = updated_just.replace(f'__OPT_{o}__', f'Option {old_to_new[o]}')
            
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                if o1 != o2:
                    sorted_pair = sorted([old_to_new[o1], old_to_new[o2]])
                    updated_just = updated_just.replace(f'__OPTS_2_{o1}_{o2}__', f'Options {sorted_pair[0]} and {sorted_pair[1]}')
                    
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                for o3 in ['A', 'B', 'C', 'D']:
                    if len({o1, o2, o3}) == 3:
                        sorted_triplet = sorted([old_to_new[o1], old_to_new[o2], old_to_new[o3]])
                        updated_just = updated_just.replace(
                            f'__OPTS_3_{o1}_{o2}_{o3}__', 
                            f'Options {sorted_triplet[0]}, {sorted_triplet[1]}, and {sorted_triplet[2]}'
                        )

        # Extract per-option breakdown for why_incorrect
        why_incorrect_map = {}
        main_explanation = ""

        para_splits = list(re.finditer(r'(?:^|\n)\s*(Options?\s+[A-D](?:,\s*[A-D])*(?:\s+and\s+[A-D])?\b[^\n:]*)[:\.]?\s*', updated_just, re.IGNORECASE))
        
        for k_idx, s in enumerate(para_splits):
            header = s.group(1).strip()
            end = para_splits[k_idx+1].start() if k_idx+1 < len(para_splits) else len(updated_just)
            full_text = updated_just[s.start():end].strip()
            
            if ('succeed' in full_text.lower() or 'is correct' in full_text.lower()) and 'incorrect' not in full_text[:40].lower():
                main_explanation = full_text
            else:
                letters_in_header = re.findall(r'\b([A-D])\b', header)
                reason = re.sub(r'^Options?\s+[A-D, and]+\s+(?:is|are)\s+incorrect\s+because\s*', '', full_text, flags=re.IGNORECASE).strip()
                for letter in letters_in_header:
                    why_incorrect_map[letter] = reason

        if not main_explanation and para_splits:
            main_explanation = updated_just[:para_splits[1].start()].strip() if len(para_splits) > 1 else updated_just

        rebalanced_questions.append({
            'id': q_id,
            'question': q['stem'],
            'options': new_options,
            'correct': new_corr_str,
            'explanation': main_explanation,
            'why_incorrect': why_incorrect_map,
            'full_justification': updated_just,
            'old_correct': orig_corr,
            'mapping': old_to_new
        })

    # Save to data/chapter4.js
    web_chapter_data = {
        'chapterId': 4,
        'title': "Chapter 4: Skills & Connectors: Architecture & Safe-Use",
        'totalQuestions': len(rebalanced_questions),
        'questions': [
            {
                'id': item['id'],
                'question': item['question'],
                'options': item['options'],
                'correct': item['correct'],
                'explanation': item['explanation'],
                'why_incorrect': item['why_incorrect'],
                'full_justification': item['full_justification']
            }
            for item in rebalanced_questions
        ]
    }

    with open(output_js, 'w', encoding='utf-8') as f:
        f.write("// Chapter 4 Data - Fully Re-Balanced & Synchronized\n")
        f.write("window.CHAPTER_DATA = window.CHAPTER_DATA || {};\n")
        f.write(f"window.CHAPTER_DATA[4] = {json.dumps(web_chapter_data, indent=2, ensure_ascii=False)};\n")

    print(f"Generated {output_js} with {len(rebalanced_questions)} questions.")

    # Also generate markdown file chapter4_rebalanced.md
    md_lines = [
        "# Chapter 4: Skills & Connectors: Architecture & Safe-Use — Re-Balanced Question Bank\n",
        "> **Note:** All 40 MCQs have been positionally balanced (~25% distribution across A, B, C, D) and analytical justifications synchronized.\n"
    ]

    for item in rebalanced_questions:
        md_lines.append(f"### Question {item['id']}")
        md_lines.append(item['question'])
        md_lines.append("")
        for l in ['A', 'B', 'C', 'D']:
            md_lines.append(f"{l}. {item['options'][l]}")
        md_lines.append("")
        md_lines.append(f"**Correct Answer:** {item['correct']}")
        md_lines.append("")
        md_lines.append("**Analytical Justification:**")
        md_lines.append(item['full_justification'])
        md_lines.append("\n---\n")

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"Generated {output_md} successfully.")
    return rebalanced_questions

if __name__ == '__main__':
    rebalance_chapter_4()
