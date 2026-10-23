import re
import json
import random

def rebalance_chapter_1(input_file="just-deligate-it.md", output_md="chapter1_rebalanced.md", output_js="data/chapter1.js"):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Clean pagination and header/footer noise
    clean_text = re.sub(r'\d{2}/\d{2}/\d{4},\s+\d{2}:\d{2}\s+here is the chapter\s*\nhttps://[^\n]+', '', content)

    # Locate the 3 batches of questions and answers
    q_sec_starts = [m.start() for m in re.finditer(r'Practice\s+Examination\s+Items:\s*Batch\s+\d', clean_text)]
    ans_sec_starts = [m.start() for m in re.finditer(r'Answer\s+Key\s+&\s+Deep\s+Analytical\s+Justifications', clean_text)]
    
    questions = {}
    for i in range(3):
        q_start = q_sec_starts[i]
        ans_start = ans_sec_starts[i]
        next_q_start = q_sec_starts[i+1] if i+1 < len(q_sec_starts) else len(clean_text)
        
        q_chunk = clean_text[q_start:ans_start]
        ans_chunk = clean_text[ans_start:next_q_start]
        
        # 1. Parse question stems and options
        q_matches = list(re.finditer(r'Question\s+(\d+)\s*\n', q_chunk))
        for j, qm in enumerate(q_matches):
            q_num = int(qm.group(1))
            start_pos = qm.end()
            end_pos = q_matches[j+1].start() if j+1 < len(q_matches) else len(q_chunk)
            q_body = q_chunk[start_pos:end_pos].strip()
            
            opt_matches = list(re.finditer(r'(?:^|\n)\s*([A-D])\.\s+', q_body))
            stem = q_body[:opt_matches[0].start()].strip() if opt_matches else q_body
            options = {}
            for k, om in enumerate(opt_matches):
                letter = om.group(1)
                o_start = om.end()
                o_end = opt_matches[k+1].start() if k+1 < len(opt_matches) else len(q_body)
                options[letter] = q_body[o_start:o_end].strip()
                
            questions[q_num] = {
                'id': q_num,
                'stem': stem,
                'options': options
            }
            
        # 2. Parse answer keys and analytical justifications
        a_matches = list(re.finditer(r'Question\s+(\d+)\s*\n', ans_chunk))
        for j, am in enumerate(a_matches):
            q_num = int(am.group(1))
            start_pos = am.end()
            end_pos = a_matches[j+1].start() if j+1 < len(a_matches) else len(ans_chunk)
            a_body = ans_chunk[start_pos:end_pos].strip()
            
            corr_m = re.search(r'Correct\s*Answers?:\s*([^\n]+)', a_body)
            correct = corr_m.group(1).strip() if corr_m else ''
            
            just_m = re.search(r'Analytical\s*Justification:\s*\n(.*)', a_body, re.DOTALL)
            just_raw = just_m.group(1).strip() if just_m else a_body
            
            # Clean any trailing prompt/next batch headers
            just_clean = re.split(r'\n(?:User\s+prompt|Response:|Pre-Batch|Practice\s+Examination)', just_raw)[0].strip()
            
            if q_num in questions:
                questions[q_num]['correct'] = correct
                questions[q_num]['justification'] = just_clean

    print(f"Loaded {len(questions)} questions from {input_file}.")

    # Identify single choice vs multi-choice questions
    single_choice_ids = []
    multi_choice_ids = []
    for q_id in range(1, 31):
        corr = questions[q_id]['correct']
        if 'and' in corr or ',' in corr:
            multi_choice_ids.append(q_id)
        else:
            single_choice_ids.append(q_id)

    print(f"Single-choice count: {len(single_choice_ids)} (IDs: {single_choice_ids})")
    print(f"Multi-choice count: {len(multi_choice_ids)} (IDs: {multi_choice_ids})")

    # Define balanced targets for single-choice:
    # 23 items -> 6 A, 6 B, 6 C, 5 D
    # Carefully randomized sequence with NO repetitive cyclic pattern (A, B, C, D...)
    # and no more than 2 consecutive identical answers
    single_targets = [
        'C', 'A', 'D', 'B', 'A', 
        'D', 'C', 'B', 'D', 'A', 
        'B', 'C', 'A', 'D', 'B', 
        'C', 'A', 'B', 'D', 'C', 
        'B', 'A', 'C'
    ]
    # Check distribution
    counts = {x: single_targets.count(x) for x in ['A', 'B', 'C', 'D']}
    print("Single choice target distribution:", counts)

    # For multi-choice items (7 items):
    # Diverse distinct pairs:
    multi_target_pairs = [
        ('C', 'D'),  # Q5
        ('B', 'D'),  # Q9
        ('B', 'C'),  # Q13
        ('A', 'D'),  # Q20
        ('A', 'B'),  # Q24
        ('B', 'D'),  # Q25
        ('A', 'C')   # Q29
    ]

    rebalanced_questions = []

    # Map each question to its new target answer and compute permutation
    single_idx = 0
    multi_idx = 0

    for q_id in range(1, 31):
        q = questions[q_id]
        orig_opts = q['options']
        orig_corr = q['correct']
        orig_just = q['justification']
        
        is_multi = q_id in multi_choice_ids

        if not is_multi:
            target_ans = single_targets[single_idx]
            single_idx += 1
            
            # We want orig_corr -> target_ans
            # The remaining 3 letters are mapped to the remaining 3 letters randomly
            orig_other = [x for x in ['A', 'B', 'C', 'D'] if x != orig_corr]
            target_other = [x for x in ['A', 'B', 'C', 'D'] if x != target_ans]
            
            # Deterministic pseudo-random shuffle based on q_id to keep reproducible
            rnd = random.Random(q_id * 42 + 7)
            rnd.shuffle(target_other)
            
            old_to_new = {orig_corr: target_ans}
            for o_old, o_new in zip(orig_other, target_other):
                old_to_new[o_old] = o_new
                
            new_corr_str = target_ans
        else:
            target_pair = sorted(multi_target_pairs[multi_idx])
            multi_idx += 1
            
            # Parse old letters from orig_corr e.g. 'A and B'
            old_pair = sorted(re.findall(r'[A-D]', orig_corr))
            orig_other = [x for x in ['A', 'B', 'C', 'D'] if x not in old_pair]
            target_other = [x for x in ['A', 'B', 'C', 'D'] if x not in target_pair]
            
            rnd = random.Random(q_id * 31 + 13)
            rnd.shuffle(target_other)
            
            # Map old pair to target pair
            if rnd.random() > 0.5:
                old_to_new = {old_pair[0]: target_pair[0], old_pair[1]: target_pair[1]}
            else:
                old_to_new = {old_pair[0]: target_pair[1], old_pair[1]: target_pair[0]}
                
            for o_old, o_new in zip(orig_other, target_other):
                old_to_new[o_old] = o_new
                
            new_corr_str = f"{target_pair[0]} and {target_pair[1]}"

        # Invert mapping: new letter -> old letter
        new_to_old = {v: k for k, v in old_to_new.items()}

        # Build new options
        new_options = {}
        for l in ['A', 'B', 'C', 'D']:
            new_options[l] = orig_opts[new_to_old[l]]

        # Synchronize Justification text
        # Step 1: Replace all mentions of Option(s) with unique placeholders
        updated_just = orig_just
        
        # Replace 'Options X and Y'
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                if o1 != o2:
                    p = re.compile(rf'\bOptions\s+{o1}\s+and\s+{o2}\b', re.IGNORECASE)
                    updated_just = p.sub(f'__OPTS_{o1}_{o2}__', updated_just)
                    
        # Replace 'Option X'
        for o in ['A', 'B', 'C', 'D']:
            p = re.compile(rf'\bOption\s+{o}\b', re.IGNORECASE)
            updated_just = p.sub(f'__OPT_{o}__', updated_just)
            
        # Step 2: Replace placeholders with target letters
        for o in ['A', 'B', 'C', 'D']:
            updated_just = updated_just.replace(f'__OPT_{o}__', f'Option {old_to_new[o]}')
            
        for o1 in ['A', 'B', 'C', 'D']:
            for o2 in ['A', 'B', 'C', 'D']:
                if o1 != o2:
                    sorted_pair = sorted([old_to_new[o1], old_to_new[o2]])
                    updated_just = updated_just.replace(f'__OPTS_{o1}_{o2}__', f'Options {sorted_pair[0]} and {sorted_pair[1]}')

        # Extract per-option breakdown for why_incorrect
        # In updated_just, find each "Option <L> is incorrect because..."
        why_incorrect_map = {}
        main_explanation = ""

        # Find paragraphs starting with Option or Options
        para_splits = list(re.finditer(r'(?:^|\n)\s*(Options?\s+[A-D](?:\s+and\s+[A-D])?\b[^\n:]*)[:\.]?\s*', updated_just, re.IGNORECASE))
        
        for k_idx, s in enumerate(para_splits):
            header = s.group(1).strip()
            end = para_splits[k_idx+1].start() if k_idx+1 < len(para_splits) else len(updated_just)
            full_text = updated_just[s.start():end].strip()
            
            # Check if this block describes the correct answer
            if ('succeed' in full_text.lower() or 'is correct' in full_text.lower()) and 'incorrect' not in full_text[:40].lower():
                main_explanation = full_text
            else:
                m = re.search(r'Option\s+([A-D])\b', header)
                if m:
                    letter = m.group(1)
                    # Strip 'Option X is incorrect because' prefix for concise clean distractor text
                    reason = re.sub(r'^Option\s+[A-D]\s+is\s+incorrect\s+because\s*', '', full_text, flags=re.IGNORECASE).strip()
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

    # Save to data/chapter1.js
    web_chapter_data = {
        'chapterId': 1,
        'title': "Chapter 1: Just Delegate It (A Crash Course)",
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
        f.write("// Chapter 1 Data - Fully Re-Balanced & Synchronized\n")
        f.write("window.CHAPTER_DATA = window.CHAPTER_DATA || {};\n")
        f.write(f"window.CHAPTER_DATA[1] = {json.dumps(web_chapter_data, indent=2, ensure_ascii=False)};\n")

    print(f"Generated {output_js} with {len(rebalanced_questions)} questions.")

    # Also generate a pristine, professionally formatted Markdown file
    md_lines = [
        "# Chapter 1: Just Delegate It — Re-Balanced Question Bank\n",
        "> **Note:** All 30 MCQs have been positionally balanced (~25% distribution across A, B, C, D) and analytical justifications synchronized.\n"
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
    rebalance_chapter_1()
