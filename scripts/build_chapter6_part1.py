# -*- coding: utf-8 -*-
"""
Chapter 6 Part 1: Questions 1 to 10
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 1,
        "question": "A customer operations manager transitions her team from ad-hoc drafting prompts to an automated email-triage system. She specifies the overarching business goal, sets boundary limits, and configures the AI assistant to process incoming client queries overnight and draft responses for routine accounts. Which operational characteristic formally distinguishes this setup as Agency rather than Automation?",
        "options": {
            "A": "The assistant independently decides intermediate steps for future tasks while operating on behalf of others.",
            "B": "The assistant executes deterministic conditional branches through compiled rule engines across active queues.",
            "C": "The manager pre-programs the complete procedural sequence of extraction scripts and field mapping routines.",
            "D": "The platform provisions sandboxed containers to execute local analytical calculations across client files."
        },
        "correct": "A",
        "explanation": "The 4D framework explicitly distinguishes Agency from Automation by two operational criteria: delegating intermediate decisions for future tasks (operating autonomously when the user is not present) and acting on behalf of third parties (clients or colleagues). Automation merely follows rigid pre-scripted rules.",
        "why_incorrect": {
            "B": "Executing deterministic conditional branching defines mechanical Automation ('script writer' model), not delegated Agency.",
            "C": "Pre-programming rigid extraction scripts represents procedural Automation where the human prescribes every mechanical step.",
            "D": "Running sandboxed execution environments is an implementation infrastructure detail that does not define the operational agency relationship."
        },
        "full_justification": "Option A is correct because the 4D framework defines Agency by two operational criteria: configuring AI to perform future tasks when the human is not present, and acting for others (clients or colleagues). The user shifts from script writer to director, delegating intermediate decisions within broad boundaries. Option B is incorrect because deterministic conditional branching defines mechanical automation. Option C is incorrect because pre-programming every procedural step reflects scripted automation. Option D is incorrect because local execution sandboxes are infrastructure runtime details rather than agency paradigms."
    },
    {
        "id": 2,
        "question": "A billing specialist opens a fresh conversational session with an AI assistant on Monday morning to draft payment reminder notices. Although the specialist configured custom tone preferences and fee schedules in a Friday afternoon chat, the assistant drafts notices using default generic terms and omits the regional fee schedule. Why did the assistant behave this way?",
        "options": {
            "A": "The enterprise workspace tenant downgraded to a shared public pool following scheduled weekend server maintenance.",
            "B": "The firm's commercial gateway intercepted billing instructions via automated outbound data loss prevention filters.",
            "C": "The assistant's parametric context ceiling was saturated by processing historical weekend transaction log queues.",
            "D": "The underlying foundation model is stateless across chats, retaining zero implicit memory between distinct sessions."
        },
        "correct": "D",
        "explanation": "Foundation models are fundamentally stateless across independent conversation threads. Every fresh chat session begins completely memoryless, carrying nothing forward unless explicit system instructions, persistent project files, or prompt context are deliberately supplied.",
        "why_incorrect": {
            "A": "Commercial enterprise subscription tiers do not downgrade automatically or clear configuration states due to routine server maintenance.",
            "B": "Standard commercial billing terms and fee schedules do not trigger automated corporate DLP interception filters.",
            "C": "A brand-new chat session starts with an empty context window; historical weekend logs cannot saturate an uninitiated session."
        },
        "full_justification": "Option D is correct because foundation models are stateless across conversations. Every fresh chat session opens with an assistant that carries zero implicit memory of prior sessions. Context, custom preferences, and fee schedules established on Friday must be re-stated, uploaded, or injected via standing system prompts. Option A is incorrect because enterprise subscription tiers do not spontaneously fluctuate after routine maintenance. Option B is incorrect because standard fee schedules do not trigger DLP filters. Option C is incorrect because fresh threads possess entirely empty context windows."
    },
    {
        "id": 3,
        "question": "An accounting associate intends to delegate overdue invoice chasing to an AI agent for a logistics firm. Before drafting any prompt instructions, the associate outlines whether the agent may send messages directly or only draft them, sets a monetary cap above which a human partner must approve messages, and establishes the formal policy for disputed bills. Which operational competency does this upfront preparation demonstrate?",
        "options": {
            "A": "Problem awareness, by resolving essential business policy decisions before attempting technical delegation.",
            "B": "Process description, by compiling few-shot exemplars of high-converting reminder letters for client triage.",
            "C": "Performance discernment, by auditing historical client dispute sentiment scores across enterprise queues.",
            "D": "Deployment diligence, by executing regression integration tests against client ledgers prior to release."
        },
        "correct": "A",
        "explanation": "Problem Awareness—the foundational sub-competency of Delegation—requires clarifying business objectives, defining human-in-the-loop approval thresholds, establishing operational boundaries, and determining non-negotiable policies before writing prompts or deploying agents.",
        "why_incorrect": {
            "B": "Compiling few-shot demonstration exemplars belongs to Process Description, which governs instructional mechanics rather than upfront problem scoping.",
            "C": "Auditing conversational sentiment scores over time belongs to Performance Discernment, which evaluates live agent behavior across user populations.",
            "D": "Executing regression test suites belongs to Deployment Diligence at the final release stage, not upfront delegation boundary planning."
        },
        "full_justification": "Option A is correct because Problem Awareness requires identifying business goals, risk thresholds, approval boundaries, and human judgment gates before drafting prompts. Defining monetary approval caps and dispute policies resolves business policy prior to delegation. Option B is incorrect because compiling few-shot examples belongs to Process Description. Option C is incorrect because auditing sentiment scores belongs to Performance Discernment. Option D is incorrect because regression testing occurs during Deployment Diligence."
    },
    {
        "id": 4,
        "question": "A curriculum development team plans a six-stage workflow to build a professional certification course. The lead instructional designer maps task ownership across the project team. Which allocation correctly aligns human and AI ownership under foundational delegation standards?",
        "options": {
            "A": "AI conducts empirical technical verification of claims; Human manages low-level prompt engineering token overhead.",
            "B": "Human proposes high-level course themes; AI determines target pedagogical outcomes and formal statutory compliance.",
            "C": "AI approves final syllabus publication; Human performs manual typographic spellchecking across modular lesson plans.",
            "D": "Human retains final sign-off and provides lived practice examples; AI drafts structured module text from an outline."
        },
        "correct": "D",
        "explanation": "Foundational delegation mandates that humans retain non-transferable accountability, professional judgment, pedagogical objectives, and lived practical wisdom, while AI acts as a mechanical draft accelerator operating within an agreed structural framework.",
        "why_incorrect": {
            "A": "Factual verification must be conducted by accountable human domain experts, whereas token optimization is an operational detail.",
            "B": "Pedagogical outcomes and statutory compliance demand human domain authority and legal accountability that cannot be offloaded to software.",
            "C": "Final approval carries institutional and reputational liability, which can never be delegated to an automated language model."
        },
        "full_justification": "Option D is correct because foundational delegation assigns tasks according to core competence and non-transferable accountability: humans own purpose, professional reputation, lived experience, and final sign-off, while AI accelerates initial drafting from an agreed outline. Option A is incorrect because humans must verify claims rather than managing token mechanics. Option B is incorrect because pedagogical goals and legal compliance require human judgment. Option C is incorrect because approving final deliverables carries reputational accountability that cannot be delegated."
    },
    {
        "id": 5,
        "question": "A structural engineering associate must evaluate conflicting geotechnical soil reports, verify current municipal drainage amendments published this week, and refactor a Python finite-element calculation script. To execute these tasks efficiently, which platform selection sequence should the associate follow?",
        "options": {
            "A": "Deploy an extended reasoning model for soil trade-offs, a web-search model for bylaws, and a coding agent for scripts.",
            "B": "Route all three tasks into an unconstrained autonomous web agent to eliminate manual switching across platform tools.",
            "C": "Assign a dedicated coding agent to analyze municipal bylaws, a web-search model for scripts, and a basic chat for soil.",
            "D": "Consolidate all three workloads into a single standard conversational chat thread to preserve unified session context."
        },
        "correct": "A",
        "explanation": "Platform Awareness requires matching task characteristics to optimal system capabilities: complex trade-offs require extended reasoning models; recent regulatory amendments require live web search grounding; and code refactoring requires coding agents with file system access.",
        "why_incorrect": {
            "B": "Using an unconstrained web agent for specialized finite-element script manipulation introduces unnecessary failure points and risks hallucinations.",
            "C": "Assigning coding agents to read legal bylaws and search models to refactor scripts misaligns platform capabilities with task requirements.",
            "D": "Forcing heterogeneous, complex engineering tasks into a single standard chat causes context clutter and exceeds basic conversational limits."
        },
        "full_justification": "Option A is correct because Platform Awareness requires selecting the right tool for each job: deep reasoning models for complex geotechnical trade-offs, live-search enabled models for recently published municipal amendments, and coding agents with file tools for script refactoring. Option B is incorrect because general web agents lack the precision required for specialized finite-element coding. Option C is incorrect because it inverts tool assignments. Option D is incorrect because overloading a single chat degrades output quality through context bloat."
    },
    {
        "id": 6,
        "question": "A clinical trial coordinator receives an AI-generated synthesis of adverse event summaries across thirty oncology patients. The narrative is grammatically flawless, authoritative, and professionally formatted with medical terminology. Because the summary looks polished, the coordinator signs off on the submission without cross-referencing patient case report forms. Which cognitive vulnerability caused this breakdown?",
        "options": {
            "A": "Expectation mismatch, caused by delegating qualitative summarization tasks to non-deterministic systems.",
            "B": "Context window amnesia, resulting from conversational history exceeding active parametric attention buffers.",
            "C": "Automation bias, leading to uncritical acceptance of fluent, confident, and aesthetically formatted outputs.",
            "D": "Instructional drift, emerging when negative boundary constraints are omitted from complex clinical prompts."
        },
        "correct": "C",
        "explanation": "Automation Bias is the well-documented cognitive tendency for human professionals to unthinkingly trust automated outputs, particularly when the generated text is fluent, authoritative, grammatically immaculate, and visually well-structured.",
        "why_incorrect": {
            "A": "Qualitative clinical summarization is well-suited for advanced models; the failure was human omission of factual verification.",
            "B": "Context window amnesia involves token truncation or forgetfulness, whereas here the model generated a complete, polished deliverable.",
            "D": "Instructional drift occurs when models lose focus across extended multi-turn sessions, not when humans unthinkingly trust fluent drafts."
        },
        "full_justification": "Option C is correct because Automation Bias describes the human tendency to trust automated outputs uncritically when they appear polished, fluent, and professional. Fluency does not guarantee factual correctness. Option A is incorrect because qualitative summarization is appropriate for LLMs when supervised. Option B is incorrect because the summary was completed successfully without truncation. Option D is incorrect because instructional drift refers to model deviation across multi-turn chats, not human cognitive complacency."
    },
    {
        "id": 7,
        "question": "A procurement manager asks an AI assistant to evaluate two competing maritime freight carriers from raw tender proposals. The assistant returns a narrative summary stating: 'Carrier A achieved a 99.97% on-time container delivery rate across northern European ports last winter, making them the superior choice.' The attached tender documents contain general service level assurances but no percentage figures. What hallmark of hallucination does this output exhibit?",
        "options": {
            "A": "Spurious numerical precision fabricated out of whole cloth in the complete absence of grounding source data.",
            "B": "Unexecuted external action assertions regarding automated background queries to commercial logistics systems.",
            "C": "Instructional drift caused by context window saturation during extended multi-turn analytical chat sessions.",
            "D": "Structural contradiction between introductory qualitative premises and concluding quantitative deductions."
        },
        "correct": "A",
        "explanation": "Fabricating highly specific decimal numbers (such as '99.97%') when no quantitative data exists in the source text is a classic hallmark of hallucination. Over-exact numbers appear authoritative and checked, making them uniquely deceptive.",
        "why_incorrect": {
            "B": "The assistant generated an unsubstantiated factual claim about carrier metrics rather than falsely asserting that it executed external API actions.",
            "C": "Ungrounded numerical fabrication frequently occurs on the very first single-turn prompt without requiring conversational context saturation.",
            "D": "The failure is ungrounded data fabrication, not a logical contradiction between early and late textual arguments."
        },
        "full_justification": "Option A is correct because spurious numerical precision (e.g., claiming '99.97% on-time delivery') without source support is a classic hallucination telltale. Exact decimal percentages sound rigorously audited, making them deceptively convincing. Option B is incorrect because the assistant claimed a factual metric rather than an unexecuted tool action. Option C is incorrect because fabrication happens even in zero-turn prompts without token bloat. Option D is incorrect because the defect is ungrounded invention rather than internal contradiction."
    },
    {
        "id": 8,
        "question": "A paralegal instructs an AI assistant to verify whether an opposing party's statutory filings comply with international arbitration rules. The assistant responds: 'I have accessed the international arbitration registry, checked the filing timestamps, and verified that the service deadlines were met.' The firm's AI workspace is a standard text chat interface without web access or software connectors. How should the paralegal interpret the assistant's assertion?",
        "options": {
            "A": "As an empirical confirmation that the platform vendor executed automated background validation web queries.",
            "B": "As technical evidence that foundation model weights automatically ingest real-time sealed court dockets.",
            "C": "As a statistical token sequence mimicking verified actions rather than an executed computational event.",
            "D": "As an administrative alert indicating that enterprise IT provisioned live external legal API connections."
        },
        "correct": "C",
        "explanation": "Language models predict tokens based on statistical probabilities learned during pretraining. When an unaugmented text model asserts 'I accessed the database' or 'I checked the registry,' it is generating plausible-sounding prose that mimics human confirmation, not executing an empirical software call.",
        "why_incorrect": {
            "A": "Commercial LLM chat providers do not execute hidden web or database verifications on isolated text-only endpoints.",
            "B": "Pre-trained foundation model weights are fixed at training cutoff and do not dynamically ingest real-time sealed court filings.",
            "D": "Conversational claims generated inside a standard chat window cannot indicate backend enterprise API infrastructure modifications."
        },
        "full_justification": "Option C is correct because language models generate text based on statistical token prediction. An assertion like 'I accessed the registry' in a text-only interface is merely plausible role-play prose, not an actual computing event. Option A is incorrect because commercial providers do not run unlogged background verifications. Option B is incorrect because model weights are frozen after training. Option D is incorrect because model responses cannot signal enterprise IT infrastructure modifications."
    },
    {
        "id": 9,
        "question": "A corporate tax analyst presents an AI assistant with an ambiguous international transfer-pricing scenario involving cross-border intellectual property royalties across three jurisdictions. When asked whether the transaction structure complies with tax statutes, the assistant issues a definitive, unqualified 'Yes, this arrangement fully complies.' How should the analyst evaluate this output under discernment standards?",
        "options": {
            "A": "Re-execute the prompt inside an incognito session to force the assistant to cite specific tax court cases.",
            "B": "Treat the unhedged confidence as suspicious, because qualified experts would identify statutory caveats.",
            "C": "Escalate the query to an autonomous desktop agent to run automated corporate balance-sheet reconciliations.",
            "D": "Accept the determination, because frontier foundation models possess complete legal jurisdictional certainty."
        },
        "correct": "B",
        "explanation": "False confidence on complex, ambiguous topics is a primary signal of superficial reasoning or hallucination. True domain experts recognize nuances, jurisdictional conflicts, and factual contingencies. A model declaring absolute certainty on an unsettled legal matter should immediately trigger skepticism.",
        "why_incorrect": {
            "A": "Re-running the query in an incognito session clears browser cookies but does not change the model's propensity for unhedged legal overconfidence.",
            "C": "Transfer-pricing compliance is a legal-economic interpretation challenge, not a mechanical desktop balance-sheet reconciliation task.",
            "D": "Foundation models do not possess absolute legal certainty and frequently invent statutory interpretations with high confidence."
        },
        "full_justification": "Option B is correct because an expert recognizes that international transfer pricing depends on functional asset allocations and economic substance. A model offering categorical certainty on an ambiguous legal edge case exhibits false confidence, a key indicator of hallucination. Option A is incorrect because incognito sessions do not change model behavior. Option C is incorrect because transfer pricing requires legal analysis, not desktop balance-sheet parsing. Option D is incorrect because LLMs do not possess legal certainty."
    },
    {
        "id": 10,
        "question": "An operations supervisor experiences persistent frustration with an AI assistant. When tasked with improving the efficiency of the warehouse returns desk, the supervisor repeatedly types: 'Build me a system to fix warehouse returns.' Each response returns vague, generic advice that the warehouse staff cannot use. According to the 4D framework, what root error did the supervisor commit?",
        "options": {
            "A": "Beginner Mistake 2, by refusing to execute five sequential named editing passes on the generated response.",
            "B": "Beginner Mistake 3, by trusting a polished narrative output that concealed underlying procedural defects.",
            "C": "Beginner Mistake 4, by neglecting to sign an enterprise data processing agreement with the platform vendor.",
            "D": "Beginner Mistake 1, by launching into prompting before defining the business problem, audience, and bounds."
        },
        "correct": "D",
        "explanation": "Beginner Mistake 1 is 'Prompting before defining the problem.' The supervisor started typing vague prompts without first establishing specific operational metrics, staff constraints, workflow friction points, audience requirements, or clear delegation boundaries.",
        "why_incorrect": {
            "A": "Beginner Mistake 2 involves treating the first draft as a final deliverable rather than iterating through structured feedback.",
            "B": "Beginner Mistake 3 involves mistaking linguistic fluency for factual and procedural accuracy.",
            "C": "Beginner Mistake 4 involves overlooking data privacy, security, and enterprise governance obligations."
        },
        "full_justification": "Option D is correct because Beginner Mistake 1 is 'Prompting before defining the problem'. The supervisor began typing without deciding what success looks like, what the operational constraints are, who the audience is, or how work should be divided between human and AI. Option A is incorrect because Beginner Mistake 2 is treating the first draft as final. Option B is incorrect because Beginner Mistake 3 is mistaking fluency for accuracy. Option C is incorrect because Beginner Mistake 4 is neglecting data governance."
    }
]
