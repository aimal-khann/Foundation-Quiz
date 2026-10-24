# -*- coding: utf-8 -*-
"""
Chapter 6 Part 3: Questions 21 to 30
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 21,
        "question": "A senior maritime surveyor evaluates an AI-generated vessel hull inspection summary against three specific criteria: whether it captured every mandatory defect listed in the dry-dock notes, whether the quoted plate thickness measurements match the physical ultrasonic test sheets, and whether the proposed weld repair procedures satisfy international naval classification society standards. Which core discernment sub-competency does this systematic tripartite evaluation represent?",
        "options": {
            "A": "Creation diligence, by verifying software licensing boundaries prior to ingesting vessel records.",
            "B": "Performance discernment, by auditing third-party user satisfaction across dry-dock contractors.",
            "C": "Process discernment, by evaluating if prompt iterations are yielding compounding time savings.",
            "D": "Product discernment, by testing output against prompt requirements, source data, and standards."
        },
        "correct": "D",
        "explanation": "Product Discernment evaluates whether a deliverable is factually accurate, structurally complete, and technically sound. The 4D framework establishes a tripartite evaluation standard: checking the deliverable against what was requested (prompt requirements), primary grounding data (ultrasonic test sheets), and professional domain standards (naval classification rules).",
        "why_incorrect": {
            "A": "Creation Diligence governs tool vetting, data privacy boundaries, and organizational policies before work commences.",
            "B": "Performance Discernment evaluates how an independent autonomous agent interacts with end users over time across populations.",
            "C": "Process Discernment assesses the efficiency, friction, and steering economy of the human-AI collaborative session itself."
        },
        "full_justification": "Option D is correct because Product Discernment evaluates whether the deliverable itself is factually correct, complete, and credible. Evaluating an output requires checking it against three reference standards: what you asked for (prompt requirements), source material (inspection logs), and professional standards (naval classification rules). Option A is incorrect because Creation Diligence involves vetting licensing and privacy before work begins. Option B is incorrect because Performance Discernment evaluates agent behavior over time. Option C is incorrect because Process Discernment evaluates session efficiency."
    },
    {
        "id": 22,
        "question": "An investment director at an infrastructure private equity fund instructs an AI assistant to evaluate whether the firm should acquire a regional utility concessions asset or a competing commercial fibre network. To prevent the team from falling into automation bias when reviewing the final decision, which instruction should the director mandate in the prompt?",
        "options": {
            "A": "Direct the assistant to adopt the persona of a Wall Street infrastructure banker and employ confident investment terms.",
            "B": "Require the assistant to state its underlying assumptions, evidence, and scoring criteria before its recommendation.",
            "C": "Command the assistant to generate three independent responses simultaneously and compute their lexical similarities.",
            "D": "Mandate that the assistant restrict its final investment recommendation strictly to an interactive HTML presentation."
        },
        "correct": "B",
        "explanation": "When evaluating consequential AI recommendations, practitioners must inspect the underlying reasoning before reading the final conclusion. Forcing the assistant to articulate premises, evidence weighting, and decision criteria exposes flawed logic that would otherwise be concealed behind smooth, persuasive narrative prose.",
        "why_incorrect": {
            "A": "Assigning an executive persona enhances authoritative confidence and rhetorical polish, which intensifies automation bias.",
            "C": "Measuring lexical consensus across generated outputs measures superficial consistency rather than factual or analytical validity.",
            "D": "Formatting conclusions into visual presentation dashboards decorates the output without auditing its foundational logic."
        },
        "full_justification": "Option B is correct because the 4D framework dictates that when evaluating consequential decisions, users must inspect the justification before accepting a recommendation. Forcing the assistant to articulate assumptions, supporting evidence, criteria weightings, and key uncertainties exposes flawed reasoning that is otherwise concealed when only a smooth conclusion is provided. Option A is incorrect because personas enhance stylistic confidence and worsen automation bias. Option C is incorrect because consensus across hallucinations merely measures consistency. Option D is incorrect because visual dashboards decorate unverified claims."
    },
    {
        "id": 23,
        "question": "A municipal planning associate spends forty-five minutes crafting and refining six sequential corrective prompts to steer an AI assistant in drafting an 800-word zoning variance appeal. The resulting draft still requires thirty minutes of manual paragraph rewriting to make it legally defensible. A colleague notes that drafting the variance appeal by hand from scratch typically requires forty-five minutes. How should the associate evaluate this working session under process discernment standards?",
        "options": {
            "A": "As a successful operational pilot, because multi-turn conversational sessions contribute directly to model training weights.",
            "B": "As an infrastructure milestone, because six conversational turns indicate the immediate necessity of deploying web agents.",
            "C": "As an acceptable administrative cost, because prompt steering time should not be included when calculating labor expenses.",
            "D": "As an operational failure, because forty-five minutes of steering that saves fifteen minutes of writing is net negative."
        },
        "correct": "D",
        "explanation": "Process Discernment requires evaluating the 'steering economy' objectively. Spending 45 minutes of prompt steering plus 30 minutes of manual editing (75 minutes total) to produce a document that takes 45 minutes to draft from scratch represents net negative productivity—a loss disguised as technological progress.",
        "why_incorrect": {
            "A": "Standard commercial enterprise chat sessions do not dynamically retrain or update underlying foundation model parameters.",
            "B": "Conversational friction during a specialized drafting task reflects poor steering economy, not an immediate requirement for web agents.",
            "C": "Human labor expended on prompt formulation, inspection, and error correction is a direct operational cost that must be measured."
        },
        "full_justification": "Option D is correct because Process Discernment requires evaluating the steering economy honestly. Spending 45 minutes of steering to save 15 minutes of writing represents net negative productivity (a loss counted as a win simply because it felt technical). Option A is incorrect because commercial chats do not update model weights. Option B is incorrect because drafting difficulty does not signal a need for autonomous web agents. Option C is incorrect because human labor spent prompting is a direct operational expense."
    },
    {
        "id": 24,
        "question": "A financial crimes compliance officer uses an AI assistant to analyze complex commercial transaction logs for potential trade-based money laundering. After three conversational turns, the assistant continues to agree sycophantically with the officer's initial hypothesis, ignores specific invoice discrepancies highlighted twice in chat, and drifts into generic regulatory platitudes. According to the 4D framework, which sequence of escalating moves should the officer execute to resolve this breakdown?",
        "options": {
            "A": "Retype the initial prompt in capital letters, threaten to terminate the session, and lower model temperature parameters.",
            "B": "Deploy an unmonitored desktop automation script, remove all negative prompt constraints, and automate invoice clearances.",
            "C": "Modify the performance description, switch to an alternative tool or model tier, and reclaim the task manually if needed.",
            "D": "Saturate the context window with five years of historical transaction records, clear browser cache, and re-run the thread."
        },
        "correct": "C",
        "explanation": "When an AI collaboration stalls, the 4D framework prescribes three structured escalation steps: 1. Modify the performance description (instruct the model to stop agreeing and rigorously critique evidence). 2. Switch the tool or model tier (escalate to a deeper reasoning model). 3. Reclaim the task manually when steering overhead exceeds value.",
        "why_incorrect": {
            "A": "Typing in capital letters and issuing rhetorical threats fails to address context corruption, model capability boundaries, or task misalignment.",
            "B": "Deploying unmonitored desktop agents to clear financial compliance items removes essential human oversight on regulated investigations.",
            "D": "Flooding the context window with massive historical transaction logs exacerbates attention dilution and worsens instructional drift."
        },
        "full_justification": "Option C is correct because when a working session stalls, the framework establishes three disciplined escalation moves: first, change the performance description (e.g., reinstruct the model to stop agreeing and challenge assumptions); second, change the tool or model tier (e.g., escalate to a deeper reasoning model); third, reclaim the task manually. Taking the task back when AI fails is a core hallmark of fluency. Option A is incorrect because emotional prompting fails to fix model limits. Option B is incorrect because unmonitored automation on compliance violates regulations. Option D is incorrect because context bloat degrades performance."
    },
    {
        "id": 25,
        "question": "An operations supervisor reviews AI-generated incident reports across a pharmaceutical packaging facility. To eliminate the open-ended 'one more small change' loop that repeatedly consumes entire working afternoons, the supervisor requires reviewers to conclude every draft inspection by selecting one of three standardized operational verdicts. Which triad represents this disciplined review protocol?",
        "options": {
            "A": "Accept with reservations, flag for compliance audit, or route to software engineering for custom backend code refactoring.",
            "B": "Confirm model confidence score, verify system prompt parameters, or escalate compute tier to frontier reasoning engines.",
            "C": "Export as interactive artifact, convert into standing knowledge base file, or deploy as an account-level Skill package.",
            "D": "Ready to use, needs revision with structured feedback, or needs human override because the fix requires unsupplied context."
        },
        "correct": "D",
        "explanation": "Disciplined review cycles prevent endless iteration by enforcing three definitive terminal verdicts: 1. Ready to use (deliverable ships immediately). 2. Needs revision (returned to the assistant with structured Problem -> Why it matters -> Direction feedback). 3. Needs human override (reclaimed by the human because resolving the issue requires unsupplied context or expert domain judgment).",
        "why_incorrect": {
            "A": "Escalating routine textual drafting defects to software engineering for custom backend refactoring introduces unnecessary organizational friction.",
            "B": "Verifying technical model parameters and escalating compute tiers are diagnostic actions, not terminal document review verdicts.",
            "C": "Exporting files as artifacts or knowledge bases addresses asset storage and persistence, not the editorial triage of an active deliverable."
        },
        "full_justification": "Option D is correct because disciplined review cycles prevent endless iteration by enforcing three definitive endings: Ready to use (ships immediately), Needs revision (returned to AI with structured feedback), or Needs human override (reclaimed by the human because the fix requires unsupplied context or specialized professional judgment). Option A is incorrect because routing routine drafts to software engineers creates administrative friction. Option B is incorrect because parameter checks are diagnostic steps rather than review verdicts. Option C is incorrect because artifact storage addresses persistence rather than review classification."
    },
    {
        "id": 26,
        "question": "A vocational training institute deploys an automated AI tutoring agent to assist 500 remote apprentices with electrical wiring problem sets. When assessing the agent's performance, the instructional lead notices that while individual student chat transcripts show grammatically flawless explanations and 100% mathematical accuracy on textbook equations, apprentice exam scores drop significantly because the agent immediately provides completed schematics the moment a student hesitates. Which dimension of discernment did the instructional lead successfully apply?",
        "options": {
            "A": "Product discernment, by confirming that the individual equations generated in single chat windows were factually correct.",
            "B": "Task delegation, by deciding that electrical wiring schematics must be drafted exclusively using local Python scripts.",
            "C": "Performance discernment, by evaluating whether the agent's independent behavior produces good outcomes across the cohort.",
            "D": "Creation diligence, by confirming that the tutoring software was procured under an enterprise educational school license."
        },
        "correct": "C",
        "explanation": "Performance Discernment specifically evaluates an AI system's independent behavior across populations of end users when the designer is not present. While individual answers were accurate (passing product discernment), the agent's independent behavioral habit of supplying completed schematics too quickly destroyed pedagogical learning.",
        "why_incorrect": {
            "A": "Verifying individual mathematical equations represents Product Discernment; the instructional lead identified systemic behavioral failure across 500 students.",
            "B": "Task delegation governs upfront role allocation, not evaluating live behavioral outcomes across an apprentice population.",
            "D": "Confirming software procurement compliance and institutional licensing belongs to Creation Diligence."
        },
        "full_justification": "Option C is correct because Performance Discernment evaluates an AI system's independent behavior across populations of end users when the designer is not in the room. While individual answers were accurate (passing product discernment), the agent's independent behavioral habit of supplying answers too quickly destroyed pedagogical value, proving that independent system behavior must be judged separately from output accuracy. Option A is incorrect because equation accuracy is Product Discernment. Option B is incorrect because delegation governs upfront role splits. Option D is incorrect because institutional licensing belongs to Creation Diligence."
    },
    {
        "id": 27,
        "question": "An experienced corporate restructuring accountant and a newly hired junior marketing intern both test the same AI assistant on two separate tasks: Task 1 involves extracting complex debt covenant default penalties from a 60-page credit agreement; Task 2 involves summarizing quantum computing breakthroughs from an academic physics paper. Why does the accountant easily catch subtle errors in Task 1 while the intern uncritically accepts the physics summary in Task 2?",
        "options": {
            "A": "Foundation models deliberately insert subtle errors into financial legal contracts while generating pristine academic texts.",
            "B": "Discernment is effortless only when anchored by domain expertise; without an internal baseline, non-experts miss errors.",
            "C": "The marketing intern deployed a fast conversational tier, whereas the restructuring accountant utilized a dedicated sandbox.",
            "D": "The credit agreement exceeded the platform's active context window, whereas the physics paper sat completely in token memory."
        },
        "correct": "B",
        "explanation": "Discernment relies fundamentally on human domain expertise. An expert spots subtle errors, missing covenants, and flawed assumptions effortlessly because they possess an internal ground-truth baseline. Without domain knowledge, plausible, fluent, but completely inaccurate explanations pass through unnoticed because the user lacks an evaluative reference point.",
        "why_incorrect": {
            "A": "Foundation models do not selectively sabotage commercial legal agreements while generating pristine summaries of academic physics.",
            "C": "The variance in error detection stemmed entirely from the evaluators' respective domain expertise, not model tiers or execution sandboxes.",
            "D": "Both documents fit comfortably within modern large context windows; the difference was human evaluative capability."
        },
        "full_justification": "Option B is correct because discernment relies on human domain expertise. An expert catches subtle bugs, flawed assumptions, and missing clauses effortlessly because they possess an internal ground-truth baseline. A non-expert lacks this frame of reference, meaning plausible, well-written, but completely fabricated explanations land with zero friction because the user has nothing to check them against. Option A is incorrect because models do not selectively target specific domains with intentional errors. Option C is incorrect because evaluative capability resides in human expertise, not software sandboxes. Option D is incorrect because both texts fit within context windows."
    },
    {
        "id": 28,
        "question": "A risk management associate inspects an extended 25-page AI-generated feasibility study for a commercial biomass energy facility. On page 4, the narrative states that the regional feedstock supplier charges a fixed annual retainer of £150,000 regardless of delivered volume. On page 22, the financial model section computes operating cash outflows using a variable rate of £45 per tonne of delivered feedstock. What hallmark of hallucination and model degradation does this discrepancy illustrate?",
        "options": {
            "A": "Unexecuted action claims, where the assistant falsely asserts that it completed live external web verification queries.",
            "B": "Structural contradiction across extended text, where late-stage calculations drift away from premises set in early pages.",
            "C": "Fabricated numerical precision, where the assistant invents ungrounded decimal figures in the absence of source records.",
            "D": "Automation bias, where human reviewers uncritically accept polished outputs without verifying primary company ledgers."
        },
        "correct": "B",
        "explanation": "Long outputs frequently suffer from structural contradiction and premise drift. Large language models generate text sequentially; over extensive documents, attention weighting on early premises (a fixed retainer) degrades, leading later sections to adopt incompatible mechanisms (a variable per-tonne fee). Cross-checking late conclusions against early premises is a vital discernment discipline.",
        "why_incorrect": {
            "A": "The assistant did not claim to execute external web verification queries; it generated inconsistent narrative claims.",
            "C": "The defect is a conceptual and operational contradiction between two pricing models, not ungrounded decimal precision.",
            "D": "Automation bias describes human uncritical acceptance of outputs, whereas the scenario highlights an objective textual defect within the generated deliverable."
        },
        "full_justification": "Option B is correct because long outputs frequently exhibit structural drift and internal contradiction. Large language models predict text sequentially; over a 25-page document, early premise tokens (a flat retainer fee) can lose attention weighting, resulting in later sections adopting contradictory mechanisms (a variable per-tonne fee). Reading the ending against the beginning is an essential discernment habit. Option A is incorrect because the assistant did not assert external tool executions. Option C is incorrect because the issue is an operational contradiction rather than fabricated decimal precision. Option D is incorrect because automation bias describes human behavioral complacency rather than document defects."
    },
    {
        "id": 29,
        "question": "A hospital procurement manager reviews an AI-generated competitive tender evaluation comparing three commercial magnetic resonance imaging (MRI) scanners. The memorandum is written with authoritative clinical prose, cites detailed technical specifications, and concludes with an unambiguous recommendation to purchase System Alpha. Upon inspecting the underlying manufacturer bid documents, the manager discovers that System Alpha lacks the mandatory helium-free quenching system required by municipal hospital safety bylaws—a specification the assistant falsely declared was present. What root operational failure did the manager intercept?",
        "options": {
            "A": "Beginner Mistake 3, by catching the dangerous tendency to mistake surface linguistic fluency and confidence for factual accuracy.",
            "B": "Beginner Mistake 1, by launching into prompting without first establishing whether MRI scanners require specialized cooling units.",
            "C": "Beginner Mistake 4, by deploying an unvetted commercial assistant that violated national patient health data residency statutes.",
            "D": "Beginner Mistake 2, by failing to engage in iterative few-shot demonstration passes before generating procurement memoranda."
        },
        "correct": "A",
        "explanation": "Beginner Mistake 3 is 'Trusting a polished answer because it sounds professional.' The manager successfully avoided this trap by verifying the confident, fluent recommendation against primary bid documents, uncovering an invented safety feature that would have violated municipal bylaws.",
        "why_incorrect": {
            "B": "Beginner Mistake 1 involves prompting before defining the business problem, audience, and constraints.",
            "C": "Beginner Mistake 4 involves neglecting data privacy, confidentiality, and governance boundaries before deployment.",
            "D": "Beginner Mistake 2 involves treating the first draft as final rather than steering iteratively."
        },
        "full_justification": "Option A is correct because Beginner Mistake 3 is 'Trusting a polished answer because it sounds professional'. The manager successfully avoided this trap by verifying whether the confident, authoritative recommendation was factually supported by primary bid documentation, catching an invented safety feature that would have violated municipal bylaws. Option B is incorrect because Beginner Mistake 1 is prompting before scoping. Option C is incorrect because Beginner Mistake 4 is neglecting data governance. Option D is incorrect because Beginner Mistake 2 is treating the first draft as final."
    },
    {
        "id": 30,
        "question": "An engineering consultancy transitions from manual ad-hoc prompt engineering in personal chat windows to building a fleet of Digital FTEs that automate the extraction of structural load limits from civil engineering blueprints. How does the individual competency of Discernment scale into an engineering discipline within this automated factory architecture?",
        "options": {
            "A": "It converts personal supervisory judgment into systematic eval suites, automated telemetry monitoring, and release criteria.",
            "B": "It replaces enterprise project management software with unmonitored desktop automation scripts running on employee machines.",
            "C": "It eliminates the requirement for human domain specialists by transferring all final legal liability to model platform vendors.",
            "D": "It transforms probabilistic natural language models into deterministic relational SQL database engines with zero variance."
        },
        "correct": "A",
        "explanation": "The 4D framework illustrates how personal skills scale into Agent Factory infrastructure. Individual, manual product discernment ('Is this output accurate and complete?') scales into automated evaluation suites, statistical sampling gates, real-time performance telemetry, and formal release criteria.",
        "why_incorrect": {
            "B": "Building enterprise Digital FTEs requires centralized, auditable, and secure server infrastructure, not unmonitored local desktop scripts.",
            "C": "Professional and legal liability is non-transferable and remains entirely with the operating engineering consultancy.",
            "D": "Deploying Digital FTEs does not alter the underlying non-deterministic, probabilistic nature of foundation language models."
        },
        "full_justification": "Option A is correct because the 4D framework explicitly illustrates how manual chat skills scale into Agent Factory infrastructure. Manual, human product discernment ('Is this draft good enough?') scales into automated eval suites, continuous telemetry monitoring, statistical output sampling, and release review gates. One cannot automate a quality evaluation at system scale without first mastering manual discernment. Option B is incorrect because enterprise agents require centralized governed infrastructure rather than unmonitored desktop scripts. Option C is incorrect because legal liability cannot be shifted to model vendors. Option D is incorrect because models remain probabilistic."
    }
]
