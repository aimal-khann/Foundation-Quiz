# -*- coding: utf-8 -*-
"""
Chapter 6 Part 2: Questions 11 to 20
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 11,
        "question": "A treasury associate asks an AI assistant to evaluate a corporate cash-flow projection. The first prompt states: 'Review this cash-flow projection.' The resulting output is generic, repetitive, and offers basic accounting definitions. The associate revises the instruction to define the executive audience, restrict the summary to one page, highlight month-over-month variances exceeding 10%, and exclude standard textbook formulas. Which foundational description principle does this revision demonstrate?",
        "options": {
            "A": "Model precision depends primarily on assigning a senior corporate officer persona in the opening system prompt.",
            "B": "Complex financial reviews require running dedicated local code sandboxes rather than refining conversational text.",
            "C": "Completeness across core deliverable parameters matters far more than rhetorical styling or clever vocabulary.",
            "D": "Analytical workflows demand invoking autonomous web-scraping agents to retrieve competitive market benchmark files."
        },
        "correct": "C",
        "explanation": "Product description governs 'What do I want back?' The 4D curriculum establishes that completeness across deliverable specifications (format, audience, length, focal metrics, negative constraints) matters far more than rhetorical phrasing or clever prompt tricks.",
        "why_incorrect": {
            "A": "Assigning an executive persona alters stylistic tone, but cannot substitute for explicit structural parameters, variance thresholds, and length boundaries.",
            "B": "Textual variance analysis does not require isolated code sandboxes; the improvement came from supplying missing task specifications.",
            "D": "Deploying autonomous web agents adds architectural complexity without resolving underspecified prompt constraints."
        },
        "full_justification": "Option C is correct because Product Description answers 'What do I want back?' by defining the deliverable type, target audience, format, length, focus areas, and explicit exclusions. Completeness of constraints drives output quality rather than clever wording. Option A is incorrect because persona assignment merely adjusts tone without providing structural bounds. Option B is incorrect because qualitative financial reviews do not require isolated sandboxes. Option D is incorrect because web agents cannot fix underspecified instructions."
    },
    {
        "id": 12,
        "question": "A hospital procurement committee evaluates three competitive commercial sterilizer tenders. The lead analyst pastes all three tender proposals into an assistant in a single turn and instructs: 'Extract pricing, compare warranty terms, score each vendor against our procurement rubric, and draft our award recommendation.' When reviewing the recommendation, the analyst discovers the scoring favoured Vendor B based on an erroneous maintenance fee calculation. According to process description standards, how should the analyst restructure this multi-stage workflow?",
        "options": {
            "A": "Re-run the identical single-pass prompt inside a fresh chat window to clear historical parametric token saturation.",
            "B": "Direct the assistant to generate three independent drafts simultaneously and compute their lexical consensus scores.",
            "C": "Structure the workflow into discrete stage-gates: extract raw facts first, verify cells, and then compare and score.",
            "D": "Escalate the single-turn prompt to an extended reasoning tier while increasing the sampling temperature parameter.",
        },
        "correct": "C",
        "explanation": "Process Description governs how multi-stage work is executed. When multiple sequential dependencies (extraction, comparison, scoring, drafting) are compressed into a single pass, errors in early extraction propagate silently into downstream scoring. Enforcing stage-gates allows human verification at each milestone.",
        "why_incorrect": {
            "A": "Clearing chat history does not eliminate the structural defect of bundling un-audited sequential steps into a single generation pass.",
            "B": "Averaging ungrounded drafts compounds statistical extraction errors rather than auditing calculations against source documentation.",
            "D": "Escalating reasoning tiers or increasing sampling temperature does not solve compounding pipeline errors caused by lack of intermediate verification gates."
        },
        "full_justification": "Option C is correct because Process Description governs multi-stage workflows. Bundling extraction, comparison, scoring, and recommendation into a single turn allows early extraction errors to compound silently. Breaking the job into stage-gates—extracting data into a table, verifying figures against primary bids, then scoring—ensures auditable accuracy. Option A is incorrect because clearing history does not fix un-staged prompts. Option B is incorrect because consensus scoring averages hallucinations. Option D is incorrect because model tiers cannot overcome structural workflow flaws."
    },
    {
        "id": 13,
        "question": "An equity research analyst wants to use an AI assistant to evaluate a controversial semiconductor merger thesis. To ensure the assistant acts as a rigorous thinking partner rather than a polite text generator, the analyst includes explicit behavioral instructions in the opening prompt. Which operational instruction correctly establishes this performance description?",
        "options": {
            "A": "Adopt the persona of an aggressive Wall Street banker and ensure all recommendations use executive finance terms.",
            "B": "Challenge my assumptions when weak, flag factual uncertainty, and do not agree with me merely to maintain rapport.",
            "C": "Ensure all analytical outputs are verified using Python execution sandboxes and display interactive chart widgets.",
            "D": "Search live market databases and output verified SEC regulatory filing hyperlinks for every single factual metric."
        },
        "correct": "B",
        "explanation": "Performance Description defines how the assistant interacts and behaves. Explicitly instructing the model to challenge weak premises, surface factual uncertainties, and resist sycophantic agreement transforms it from a flattering echo chamber into an objective thinking partner.",
        "why_incorrect": {
            "A": "Assigning an aggressive persona alters vocabulary and tone, but leaves the assistant prone to uncritical sycophancy and agreeable validation.",
            "C": "Executing Python sandboxes handles quantitative calculations, not dialectical premise testing or critical behavioral challenge.",
            "D": "Retrieving regulatory filings improves factual access (Platform Awareness), but does not alter the assistant's collaborative behavioral dynamic."
        },
        "full_justification": "Option B is correct because Performance Description defines how the assistant behaves. Instructing the model to challenge assumptions, flag uncertainty, and avoid polite agreement transforms it into a rigorous thinking partner. Option A is incorrect because personas adjust tone but leave models prone to sycophancy. Option C is incorrect because code sandboxes address arithmetic rather than critical debate. Option D is incorrect because filing retrieval addresses data access rather than behavioral interaction."
    },
    {
        "id": 14,
        "question": "A university instructional designer drafts behavioral constraints for an automated AI physics tutor that will interact independently with 1,200 undergraduate students. The designer specifies: 'Never provide the direct mathematical solution to a problem until the student has submitted at least one diagnostic attempt.' How does this instruction illustrate the transition from chat-scale to system-scale performance description?",
        "options": {
            "A": "It transforms non-deterministic language models into deterministic symbolic mathematics calculation algorithms.",
            "B": "It eliminates the requirement for human verification gates across downstream academic grading determinations.",
            "C": "It replaces the university's relational database infrastructure with client-side conversation memory caches.",
            "D": "It converts an ad-hoc conversational preference into a standing behavioral policy applied across all end users."
        },
        "correct": "D",
        "explanation": "Performance Description scales from individual chat interactions into system-scale agent design. In personal chat, behavioral instructions guide a single session; in an enterprise agent or Digital FTE, they become standing institutional policies enforced uniformly across thousands of third-party interactions.",
        "why_incorrect": {
            "A": "Behavioral prompting establishes pedagogical scaffolding; it does not change statistical language models into deterministic calculation engines.",
            "B": "Pedagogical prompt guardrails do not eliminate mandatory human oversight for consequential academic evaluations or formal grades.",
            "C": "Managing prompt instructions has no bearing on institutional relational database infrastructure or client caching mechanisms."
        },
        "full_justification": "Option D is correct because Performance Description operates at two scales: in personal chat, it guides a single conversation; at system scale (e.g., in an automated tutor or Digital FTE), it becomes a standing operational policy enforced across all end users. Option A is incorrect because prompting does not make probabilistic models deterministic. Option B is incorrect because educational guardrails do not remove human grading oversight. Option C is incorrect because prompt rules do not replace institutional databases."
    },
    {
        "id": 15,
        "question": "A fintech startup launches an automated AI customer-support assistant to resolve payment disputes. The engineering team crafts an intricate, five-paragraph prompt containing few-shot exemplars, advanced role definitions, and strict tone constraints. Despite this sophisticated prompt, the assistant repeatedly issues incorrect refund amounts and hallucinates non-existent chargeback rights. What operational reality explains this failure?",
        "options": {
            "A": "Prompt engineering cannot compensate for absent business rules, missing account data, or lacking tool connectors.",
            "B": "Customer dispute triage workflows are legally prohibited from utilizing commercial foundation language models.",
            "C": "Conversational assistants cannot parse numerical currency symbols unless hosted in local terminal environments.",
            "D": "The assistant's reasoning engine suffered from catastrophic forgetting caused by multi-shot exemplar structures."
        },
        "correct": "A",
        "explanation": "Description scales into Context Engineering. While prompt engineering focuses on phrasing and style, an agent cannot function without access to ground truth: transaction ledgers, dispute policies, customer history, and live tool integrations. Phrasing cannot substitute for missing operational data.",
        "why_incorrect": {
            "B": "Commercial language models are routinely and legally deployed for customer support triage when governed by appropriate tool boundaries.",
            "C": "Foundation models parse currency values and numerical figures natively; the failure was missing enterprise context and policy rules.",
            "D": "Multi-shot prompting formats examples to guide generation; it does not trigger model weight degradation or catastrophic forgetting."
        },
        "full_justification": "Option A is correct because Description scales into context engineering: providing the data, tools, documentation, business rules, and database records the assistant needs to succeed. Clever prompt phrasing cannot rescue an assistant operating with missing financial policies, absent dispute rules, or lack of tool integrations. Option B is incorrect because customer triage is a standard, legal use case. Option C is incorrect because LLMs parse currencies natively. Option D is incorrect because prompting does not cause catastrophic forgetting."
    },
    {
        "id": 16,
        "question": "A legal operations specialist instructs an AI assistant to analyze three vendor cloud hosting agreements to determine early-termination penalties. To eliminate hallucinated vendor policies and enforce strict source grounding, which TWO instructions must be included in the process description? (Select TWO.)",
        "options": {
            "A": "Explicitly authorize the assistant to state that the contract is silent if an agreement does not disclose penalty terms.",
            "B": "Mandate that the assistant formulate all findings as an interactive HTML presentation dashboard with visual fee graphs.",
            "C": "Require the assistant to search external public databases to estimate prevailing enterprise software termination fees.",
            "D": "Direct the assistant to quote the specific section heading and verbatim contract text for every single penalty figure."
        },
        "correct": "A and D",
        "explanation": "Rigorous source grounding requires two essential instructions: 1. Verbatim quote anchoring: Mandating exact section titles and quotes prevents speculative synthesis and makes factual audits fast. 2. Explicit permission to state absence: Giving permission to say 'the contract is silent' stops the model from inventing plausible terms to fill information gaps.",
        "why_incorrect": {
            "B": "Converting narrative claims into interactive HTML dashboards merely formats potential hallucinations without verifying contractual grounding.",
            "C": "Searching public databases introduces generalized external estimates that contaminate the precise legal review of these specific binding contracts."
        },
        "full_justification": "Options A and D are correct because they establish strict source grounding: (A) granting explicit permission to state that a document is silent prevents the model from confabulating terms to fill gaps, and (D) requiring verbatim citations and section titles ties every claim directly to primary evidence. Option B is incorrect because visual HTML dashboards decorate unverified claims without proving accuracy. Option C is incorrect because searching external databases introduces generic industry assumptions that distort the analysis of specific signed agreements."
    },
    {
        "id": 17,
        "question": "A senior communications manager reviews an extensive AI-drafted corporate restructuring announcement. Rather than attempting to correct structural flow, technical vocabulary, sentence length, and reader sensitivity simultaneously in a single sweeping revision prompt, the manager decides to execute named editing passes. Which sequence represents this disciplined editorial protocol?",
        "options": {
            "A": "Generate four parallel drafts, apply algorithmic sentiment scoring filters, and merge the two longest generated texts.",
            "B": "Execute an extraction pass on financial ledgers, launch an autonomous web crawler, and complete a code execution audit.",
            "C": "Execute a clarity pass for single-idea sentences, a tone pass for stakeholder empathy, and a formatting layout pass.",
            "D": "Perform an administrative security check, execute a browser session reset, and export the file as a markdown artifact."
        },
        "correct": "C",
        "explanation": "Disciplined iterative refinement uses named editing passes: addressing one specific editorial dimension at a time (e.g., clarity pass for sentence conciseness, tone pass for stakeholder empathy, formatting pass for layout). This prevents cognitive overload and yields precise prose control.",
        "why_incorrect": {
            "A": "Algorithmic sentiment scoring and merging unvetted drafts compounds inconsistent phrasing rather than refining document quality.",
            "B": "Financial extraction, web crawling, and code execution are technical data retrieval actions, not document editing disciplines.",
            "D": "Security audits, browser resets, and markdown exports are administrative technical tasks that do not edit or polish written prose."
        },
        "full_justification": "Option C is correct because disciplined iterative refinement relies on named editing passes rather than unstructured sweeps. Conducting a clarity pass (verifying each sentence delivers a single idea), a tone pass (ensuring stakeholder empathy), and a formatting pass (inspecting headers and flow) delivers systematic editorial control. Option A is incorrect because merging raw drafts compounds stylistic inconsistencies. Option B is incorrect because web crawling and code execution are retrieval actions. Option D is incorrect because session resets are administrative tasks."
    },
    {
        "id": 18,
        "question": "An IT director reviews an AI-generated cloud migration proposal. The section detailing database cutover strategies assumes the company operates an on-premises Oracle cluster, whereas the firm migrated fully to cloud-native PostgreSQL two years ago. Following the standard feedback pattern (Problem -> Why it matters -> Direction), which prompt intervention should the director issue?",
        "options": {
            "A": "Your database analysis is completely invalid. Re-read our company history documents and draft the cutover proposal again.",
            "B": "Switch to an extended reasoning model tier and generate an interactive architecture diagram illustrating our server clusters.",
            "C": "Adopt the persona of an enterprise cloud architect and ensure all cutover recommendations adhere to standard AWS blueprints.",
            "D": "The cutover assumes on-premises Oracle; we are on cloud PostgreSQL, so these steps fail. Rewrite the plan for PostgreSQL."
        },
        "correct": "D",
        "explanation": "The established feedback pattern consists of: Problem ('The cutover assumes an on-premises Oracle setup') -> Why it matters ('we are on cloud PostgreSQL, so these steps fail') -> Direction ('Rewrite the plan for PostgreSQL'). This structure enables targeted, single-turn corrections.",
        "why_incorrect": {
            "A": "Stating 'you are wrong, try again' provides vague feedback that forces the model to guess what needs correction and why.",
            "B": "Escalating compute tiers or requesting visual diagrams does not fix the underlying factual misconception regarding database infrastructure.",
            "C": "Assigning an architect persona changes stylistic tone, but fails to identify the specific error or provide technical remediation direction."
        },
        "full_justification": "Option D is correct because it precisely follows the feedback pattern: Problem ('assumes on-premises Oracle') -> Why it matters ('we are on cloud PostgreSQL, so these steps fail') -> Direction ('Rewrite the plan for PostgreSQL'). Structured feedback allows the assistant to rectify misalignments in a single turn. Option A is incorrect because telling a model it is wrong without specifics is unguided feedback. Option B is incorrect because higher tiers cannot guess unstated context. Option C is incorrect because personas do not correct factual inaccuracies."
    },
    {
        "id": 19,
        "question": "A technical operations lead receives an operational incident summary stating: 'Server rack ticket volume doubled this month, staffing remained fixed at four technicians, and mean ticket resolution time lengthened from four hours to nine hours.' The lead must present this data to two distinct audiences: the executive board and the front-line engineering team. Under dual-audience performance description principles, how should these outputs be structured? (Select TWO.)",
        "options": {
            "A": "Present the engineering team with reassuring narrative prose that conceals the lengthening of mean ticket resolution times.",
            "B": "Present the board with concise metrics, the root operational cause, and a clear staffing or service SLA decision to approve.",
            "C": "Present the engineering team with operational context, validation that volume drove delays, and prioritized triage actions.",
            "D": "Present the board with an unedited, raw 50-page dump of individual server error logs to ensure total technical auditability."
        },
        "correct": "B and C",
        "explanation": "Dual-audience product description tailors information to reader needs: 1. Executive Board: Demands high-level metrics, root causes, and explicit governance decisions (approving headcount or revising SLAs). 2. Front-line Team: Needs tactical reassurance that delays were driven by volume rather than incompetence, accompanied by clear triage priorities.",
        "why_incorrect": {
            "A": "Concealing critical resolution metrics from engineering staff destroys operational trust and obscures workload bottlenecks.",
            "D": "Dumping 50 pages of raw server logs overwhelms board members and fails to provide the executive synthesis required for governance decisions."
        },
        "full_justification": "Options B and C are correct because adapting outputs to divergent audiences is a key facet of Product Description: (B) the executive board requires synthesized business metrics, root causes, and clear governance decisions to authorize, while (C) the engineering team requires operational context, validation that volume drove delays, and tactical backlog priorities. Option A is incorrect because hiding metrics from front-line staff erodes trust. Option D is incorrect because raw server log dumps overwhelm board leadership without providing decision context."
    },
    {
        "id": 20,
        "question": "A marketing associate asks an AI assistant to outline a brand positioning strategy for a boutique sustainable footwear startup. The initial response provides five standard, generic marketing tactics that could apply to any retail brand. Frustrated by the bland deliverable, the associate concludes that the model is incapable of strategic thinking and abandons the tool. Which common operational failure did the associate commit?",
        "options": {
            "A": "Beginner Mistake 1, by launching into drafting prompts before defining the core business problem, audience, and bounds.",
            "B": "Beginner Mistake 2, by treating the initial draft as a final deliverable rather than iterating through guided steering.",
            "C": "Beginner Mistake 4, by deploying an unvetted third-party plugin that violated institutional data residency boundaries.",
            "D": "Beginner Mistake 3, by trusting a polished, confident narrative deliverable that concealed subtle factual discrepancies."
        },
        "correct": "B",
        "explanation": "Beginner Mistake 2 is 'Treating the first answer as the final answer.' First responses from AI are working drafts, not polished endpoints. Achieving high-value outputs requires the Description-Discernment loop: inspecting the initial draft, identifying gaps, and steering through iterative feedback.",
        "why_incorrect": {
            "A": "Beginner Mistake 1 involves prompting before defining the business problem, audience, and constraints.",
            "C": "Beginner Mistake 4 involves neglecting data privacy, security, and governance boundaries before deployment.",
            "D": "Beginner Mistake 3 involves falling into automation bias and unthinkingly trusting fluent but inaccurate deliverables."
        },
        "full_justification": "Option B is correct because Beginner Mistake 2 is treating the first answer as the final answer. Initial outputs are drafts, not finished deliverables. AI fluency requires engaging the Description-Discernment loop: inspecting initial drafts, identifying gaps, providing structured feedback, and steering the assistant iteratively. Option A is incorrect because Beginner Mistake 1 is prompting before scoping. Option C is incorrect because Beginner Mistake 4 is neglecting data governance. Option D is incorrect because Beginner Mistake 3 is mistaking fluency for accuracy."
    }
]
