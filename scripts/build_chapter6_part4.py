# -*- coding: utf-8 -*-
"""
Chapter 6 Part 4: Questions 31 to 40
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 31,
        "question": "A university lecturer drafts personalized mid-term academic performance evaluations for ninety engineering undergraduates. To expedite drafting, the lecturer pastes student matriculation numbers, raw exam scores, and confidential attendance dispute records into a free consumer chatbot service via a personal browser profile. The university provides an approved enterprise AI workspace governed by an institutional data processing agreement. Under creation diligence standards, why is this workflow unacceptable?",
        "options": {
            "A": "Free consumer chatbot tiers operate with lower token generation speeds that degrade complex narrative clarity.",
            "B": "Foundation models cannot parse raw student examination score matrices unless hosted on internal school servers.",
            "C": "Ingesting confidential student records into an unapproved consumer tool violates institutional data boundaries.",
            "D": "Educational feedback drafting is legally classified as an impossible reasoning task for commercial assistants."
        },
        "correct": "C",
        "explanation": "Creation Diligence requires making responsible, compliant choices regarding tools, data sensitivity, and organizational authorization before and during work. Ingesting identifiable, confidential student records and dispute notes into an unapproved consumer service breaches data privacy policies, institutional agreements, and confidentiality standards.",
        "why_incorrect": {
            "A": "Token generation speed is a computational performance metric, not an ethical compliance or governance failure.",
            "B": "Foundation models parse tabular score matrices natively; the violation is data exposure and unapproved tool usage.",
            "D": "Drafting educational feedback from structured criteria is a well-established LLM use case when conducted inside approved tools."
        },
        "full_justification": "Option C is correct because Creation Diligence requires making responsible choices regarding tools, data sensitivity, and organizational authorization before and during the work. Pasting confidential student disciplinary notes, exam marks, and matriculation identifiers into an unapproved consumer tool breaches data protection policies and exposes institutional data. Option A is incorrect because generation speed is an infrastructure metric rather than a governance violation. Option B is incorrect because models handle tables natively. Option D is incorrect because educational feedback drafting is standard when done in compliant workspaces."
    },
    {
        "id": 32,
        "question": "A clinical data coordinator prepares a clinical study dataset for an AI assistant to extract seasonal asthma exacerbation patterns. The coordinator scrubs patient full names and national identity numbers. However, the uploaded dataset retains the hospital clinic branch code, the exact date and minute of admission, and the patient's rare congenital heart diagnosis. In that specific clinic branch, only one patient has that diagnosis. Why did this data preparation fail the redaction test?",
        "options": {
            "A": "The coordinator retained combination quasi-identifiers that permit deterministic re-identification of the patient.",
            "B": "Foundation models refuse to process clinical datasets that contain any direct references to respiratory diseases.",
            "C": "The coordinator omitted the patient's primary residential postal address from the statistical extraction table.",
            "D": "Redaction protocols mandate converting all medical research datasets into executable HTML canvas code sandboxes."
        },
        "correct": "A",
        "explanation": "The test of redaction is whether someone reading only what was uploaded could identify the subject. Removing direct identifiers (names, ID numbers) is insufficient if unique combinations of indirect attributes—quasi-identifiers such as exact timestamps, specific clinic locations, and exceptionally rare diagnoses—enable deterministic re-identification.",
        "why_incorrect": {
            "B": "Language models do not reject datasets containing respiratory terminology; medical text analysis is standard practice.",
            "C": "Omitting residential postal addresses is proper data minimization; the failure was retaining unique clinical and temporal quasi-identifiers.",
            "D": "Data sanitization protocols govern information suppression, not rendering datasets inside HTML canvas code sandboxes."
        },
        "full_justification": "Option A is correct because redaction fails when it leaves a combination of indirect attributes (quasi-identifiers) that uniquely identify an individual. Retaining the exact admission timestamp, specific clinic branch, and an exceptionally rare heart condition allows anyone with basic local knowledge to identify the patient. Option B is incorrect because models do not refuse respiratory clinical terms. Option C is incorrect because omitting addresses was correct minimization. Option D is incorrect because HTML canvas sandboxes are irrelevant to data privacy."
    },
    {
        "id": 33,
        "question": "A human resources consultancy utilizes an AI system to rank 400 candidate résumés for a senior engineering leadership position at a regional utility. The system's algorithmic scores will be used directly to eliminate the bottom 300 applicants without human resume inspection. Under transparency diligence standards, which operational principle governs this evaluation?",
        "options": {
            "A": "Algorithmic transparency is strictly optional whenever an evaluation suite achieves test accuracy above 95%.",
            "B": "Commercial recruitment workflows are exempt from disclosure rules if executed within incognito browser sessions.",
            "C": "Disclosure obligations are fully satisfied by maintaining internal server logs without informing candidates.",
            "D": "The more an AI-assisted result materially affects external people, the stronger the imperative for disclosure."
        },
        "correct": "D",
        "explanation": "Transparency Diligence establishes a core governance imperative: The more an AI-assisted outcome materially impacts external individuals—particularly for consequential life decisions such as employment, credit, or healthcare—the stronger the ethical and professional requirement for full disclosure.",
        "why_incorrect": {
            "A": "High internal model benchmark accuracy does not eliminate ethical, professional, or statutory transparency obligations.",
            "B": "Incognito browser sessions manage client-side caching; they provide zero exemption from legal and professional disclosure duties.",
            "C": "Retaining private internal server logs satisfies internal logging requirements, but completely fails the test of transparency toward impacted applicants."
        },
        "full_justification": "Option D is correct because Transparency Diligence dictates: The more an AI-assisted result affects other people, the stronger the case for transparency. When an automated system makes consequential, life-affecting decisions—such as eliminating job applicants without human review—the obligation to disclose the role of AI is paramount. Option A is incorrect because high algorithmic accuracy does not waive disclosure duties. Option B is incorrect because incognito sessions provide no legal exemptions. Option C is incorrect because internal audit logs do not satisfy candidate-facing transparency."
    },
    {
        "id": 34,
        "question": "An operations coordinator configures an AI assistant connected to the company's enterprise resource planning platform. The coordinator drafts an automated workflow that executes three sequential tasks: Task 1: Synthesize quarterly inventory turnover trends from warehouse spreadsheets. Task 2: Draft restocking recommendations for regional distribution hubs. Task 3: Transmit binding purchase orders and execute electronic bank payments to suppliers. Under deployment diligence standards, which task requires a mandatory, non-negotiable human verification gate before execution?",
        "options": {
            "A": "Task 2, because drafting logistics recommendations demands frontier reasoning models with extended thinking.",
            "B": "Task 3, because executing electronic supplier payments is an irreversible real-world financial transaction.",
            "C": "Tasks 1, 2, and 3 equally, because language models cannot interact safely with enterprise spreadsheets.",
            "D": "Task 1, because summarizing inventory turnover spreadsheets requires running local Python unit test suites."
        },
        "correct": "B",
        "explanation": "Deployment Diligence dictates: The wider the reach and the harder an action is to undo, the deeper the human verification gate required. While analytical summaries and internal drafts are reversible, executing financial payments and binding purchase orders creates immediate, irreversible external commitments requiring non-negotiable human sign-off.",
        "why_incorrect": {
            "A": "Drafting restocking recommendations is an internal, reversible analytical step that does not commit corporate capital to third parties.",
            "C": "Language models process structured tabular and spreadsheet data routinely; gating is mandated by financial irreversibility, not technical impossibility.",
            "D": "Summarizing quarterly turnover trends is an internal exploratory task with minimal external operational risk."
        },
        "full_justification": "Option B is correct because Deployment Diligence establishes a strict rule: The more people the result reaches, and the harder a step is to undo, the deeper the check it requires. Reversible analytical summaries or internal drafts can be inspected post-generation, but an irreversible real-world act—such as executing bank payments or dispatching binding supplier contracts—must be checked before the act occurs. Option A is incorrect because drafting recommendations is reversible. Option C is incorrect because models process spreadsheets effectively. Option D is incorrect because trend analysis is low-risk."
    },
    {
        "id": 35,
        "question": "A corporate financial analyst asks an AI assistant to summarize an eighty-page quarterly financial report. The assistant returns an executive memorandum highlighting a successful quarter, citing an operating profit of £14.2 million based on a 22% gross margin on £64.5 million in revenue. When the analyst checks the primary balance sheet, revenue was actually £58.0 million and operating profit was £11.1 million. The assistant's text was fluent, grammatical, and authoritative. What core computational rule did the analyst violate?",
        "options": {
            "A": "Narrative financial summaries must be exported into markdown tables before cross-referencing corporate ledgers.",
            "B": "Analysts must avoid asking models to extract textual figures from financial reports exceeding twenty-five pages.",
            "C": "Consequential financial numbers must be computed via deterministic code, never generated in free-flowing prose.",
            "D": "Financial analysis prompts must always direct the assistant to adopt the persona of an expert forensic auditor."
        },
        "correct": "C",
        "explanation": "The Numbers Rule dictates: Any number a business decision relies upon must be deterministically computed (via code, formulas, or spreadsheets) and never generated through probabilistic language model token prediction. Statistical language models predict plausible text tokens; they do not balance ledgers.",
        "why_incorrect": {
            "A": "Exporting unverified numbers into markdown tables merely reformats hallucinations without auditing mathematical truth.",
            "B": "Modern context windows easily accommodate eighty-page reports; the root failure was relying on generative arithmetic rather than deterministic code.",
            "D": "Assigning a forensic auditor persona adjusts writing style and tone, but does not prevent statistical token generation errors in numerical calculations."
        },
        "full_justification": "Option C is correct because of The Numbers Rule: Any number a decision rests on, such as a total or a percentage, must be computed and never generated. Language models predict plausible-looking text tokens statistically; they do not calculate sums or margins like a spreadsheet engine. Consequential metrics must be calculated via deterministic code (Python/spreadsheets). Option A is incorrect because markdown tables do not validate math. Option B is incorrect because context windows handle eighty pages easily. Option D is incorrect because personas do not prevent generative arithmetic errors."
    },
    {
        "id": 36,
        "question": "A regional mortgage lender uses an automated AI tool to rank commercial loan applicants. An underwriter notices that the tool consistently assigns lower creditworthiness tiers to small businesses located in specific postcodes, even when their audited cash flows satisfy approval criteria. The underwriter cannot determine whether the tool is detecting legitimate commercial credit risks or applying historical geographic bias. When facing this ambiguous situation, which TWO questions must the underwriter answer before proceeding? (Select TWO.)",
        "options": {
            "A": "How many model tokens did the loan underwriting prompt consume during the automated batch scoring run?",
            "B": "What specific harms could occur for those affected, and would rejected loan applicants be able to tell?",
            "C": "Which local server operating system was provisioned to host the commercial banking transaction database?",
            "D": "Who is materially affected by this ranking, including applicants who will never inspect the final score?"
        },
        "correct": "B and D",
        "explanation": "When facing ambiguous algorithmic bias or ethical dilemmas, the 4D framework mandates asking four specific evaluative questions: 1. Who is affected, including people who will never see the result? 2. What could go wrong for them, and would they be able to tell? 3. What would a fair outcome look like? 4. What should be disclosed, and to whom?",
        "why_incorrect": {
            "A": "Token consumption metrics track computational billing cost, not algorithmic fairness, geographic discrimination, or social harm.",
            "C": "The host server operating system is an infrastructure implementation detail that has zero bearing on credit underwriting bias or applicant harm."
        },
        "full_justification": "Options B and D are correct because when an AI-assisted outcome is unclear rather than plainly wrong, the framework mandates asking four specific ethical questions before acting: 1. Who is affected, including people who will never see the result? 2. What could go wrong for them, and would they be able to tell? 3. What would a fair outcome look like? 4. What should be disclosed, and to whom? Questions B and D directly address impact and harm. Option A is incorrect because token consumption measures computational cost. Option C is incorrect because server operating systems are irrelevant to ethical dilemmas."
    },
    {
        "id": 37,
        "question": "A civil engineering firm deploys an autonomous coding assistant to refactor Python stress-strain calculations for a municipal suspension bridge project. The assistant introduces an error into the shear modulus equation that underestimates structural reinforcement requirements by 30%. The firm's lead structural engineer reviews the script, misses the error, and submits the calculation package to the municipal transport authority. If a structural failure occurs, where does operational and professional accountability reside?",
        "options": {
            "A": "Accountability splits equally between the software platform provider and the municipal transport authority.",
            "B": "Accountability remains 100% with the lead structural engineer and the operating engineering consultancy.",
            "C": "Accountability transfers entirely to the commercial foundation model vendor that authored the code generator.",
            "D": "Accountability is legally voided because the software error was generated by a non-deterministic algorithm."
        },
        "correct": "B",
        "explanation": "AI automates cognitive and mechanical effort; it can never assume professional, legal, or ethical accountability. Accountability is non-transferable. The licensed professional engineer who reviewed and stamped the submission, along with the operating engineering consultancy, remains 100% liable for structural calculations.",
        "why_incorrect": {
            "A": "Municipal regulatory authorities review compliance submissions as overseers; they do not absorb primary design liability from licensed engineers of record.",
            "C": "Commercial foundation model vendors explicitly disclaim all operational, engineering, and consequential liability in their standard enterprise contracts.",
            "D": "The probabilistic nature of software does not legally void professional negligence doctrines or engineering standards of care."
        },
        "full_justification": "Option B is correct because AI can automate work; it cannot automate accountability. Software cannot assume professional liability. If an engineering assistant introduces a catastrophic mathematical error into a structural model, the licensed professional engineer who stamped the package and the operating firm remain 100% accountable. Option A is incorrect because regulatory authorities do not absorb design liability. Option C is incorrect because model vendors legally disclaim liability. Option D is incorrect because non-deterministic generation does not void professional negligence."
    },
    {
        "id": 38,
        "question": "A forward-deployed engineer helps an accounting practice design a bookkeeping Digital FTE to automate monthly bank reconciliations. The engineer maps the project across the four competencies: Step 1: Establish that the agent matches transactions and drafts reports, while partners approve adjustments and write-offs. Step 2: Provide the chart of accounts, transaction matching rules, and past reconciliation report exemplars. Step 3: Test the agent against historical reconciliation files to audit false matches and escalation rates. Step 4: Ensure financial data stays within approved infrastructure, log all agent actions, and mandate partner sign-off. Which sequence correctly maps Steps 1, 2, 3, and 4 to the 4D framework?",
        "options": {
            "A": "Description of matching rules, Delegation of partner roles, Diligence of system logging, Discernment of evals.",
            "B": "Delegation of task boundaries, Description of matching context, Discernment of accuracy, Diligence of governance.",
            "C": "Delegation of partner authority, Discernment of matching rules, Description of test suites, Diligence of logging.",
            "D": "Diligence of security controls, Delegation of transactional rules, Description of eval tests, Discernment audits."
        },
        "correct": "B",
        "explanation": "The four implementation steps map directly to the 4D operational loop: Step 1 is Delegation (scoping task boundaries between human and AI). Step 2 is Description (providing context, rules, and few-shot exemplars). Step 3 is Discernment (evaluating accuracy against historical files). Step 4 is Diligence (enforcing security, logging, and human sign-off).",
        "why_incorrect": {
            "A": "Scrambles the operational sequence: Description occurs in Step 2, Delegation in Step 1, Diligence in Step 4, and Discernment in Step 3.",
            "C": "Inverts Description and Discernment, misclassifying test evaluation as Description and matching rules as Discernment.",
            "D": "Scrambles the framework sequence by misidentifying initial role scoping as Diligence rather than Delegation."
        },
        "full_justification": "Option B is correct because it correctly maps the four chronological implementation steps to the 4D framework: Step 1 is Delegation (scoping boundaries of the Digital FTE, deciding what the agent does and what humans keep); Step 2 is Description (supplying the chart of accounts, rules, and exemplars via context engineering); Step 3 is Discernment (testing the agent against historical files to audit false matches); Step 4 is Diligence (enforcing data residency, logging, and partner sign-off). Options A, C, and D are incorrect because they scramble the established sequence."
    },
    {
        "id": 39,
        "question": "An enterprise operations director teaches junior associates how the 4D AI Fluency Framework aligns with the book's 10-80-10 operational execution rule (10% setting direction, 80% orchestrating execution, 10% judging the truth). Which TWO statements correctly describe the structural integration of the 4Ds across this operational timeline? (Select TWO.)",
        "options": {
            "A": "In the final 10%, Discernment becomes critical to verify deliverables before anything consequential ships.",
            "B": "In the middle 80%, Diligence executes in total isolation while Description and Discernment are deactivated.",
            "C": "In the first 10%, Delegation and Description dominate by establishing the work split, bounds, and goals.",
            "D": "In the final 10%, Diligence is confined strictly to an optional administrative checklist after delivery."
        },
        "correct": "A and C",
        "explanation": "Under the 10-80-10 execution rule: 1. The First 10% (Setting Direction): Delegation and Description dominate by defining problem scope, boundaries, task division, and deliverable specifications. 2. The Final 10% (Judging the Truth): Discernment dominates by rigorously verifying outputs, auditing claims, and evaluating facts before release.",
        "why_incorrect": {
            "B": "The middle 80% is an active orchestration loop where Description and Discernment iterate constantly as intermediate outputs are steered.",
            "D": "Diligence is not a post-hoc optional checklist; it operates continuously across Creation Diligence, Transparency, and Deployment Diligence."
        },
        "full_justification": "Options A and C are correct because they accurately integrate the 4Ds into the 10-80-10 operational model: (A) in the final 10% (Judging the Truth), Discernment is paramount to verify factual correctness and domain validity before release; (C) in the first 10% (Setting Direction), Delegation and Description dominate by establishing the work split, constraints, and deliverable targets. Option B is incorrect because the middle 80% requires continuous Description and Discernment iteration. Option D is incorrect because Diligence is an active, end-to-end discipline rather than a post-hoc checklist."
    },
    {
        "id": 40,
        "question": "A clinical research associate completes a rush data extraction project for a medical conference presentation. To meet the printing deadline, the associate pastes fifty unredacted clinical case summaries into a free online chatbot, exports the generated tables, and submits the poster to the conference committee. Three weeks later, a compliance audit flags the unauthorized disclosure of protected health records. The associate argues: 'The extraction was 100% accurate, so the tool was used correctly.' What fundamental error did the associate commit?",
        "options": {
            "A": "Beginner Mistake 4, by treating privacy, data rules, and accountability as an afterthought rather than practicing Diligence.",
            "B": "Beginner Mistake 1, by failing to define the target audience and clinical scope before prompting the model for extraction.",
            "C": "Beginner Mistake 2, by accepting the initial table extraction without executing three named editorial refinement passes.",
            "D": "Beginner Mistake 3, by falling into automation bias and trusting an authoritative but inaccurate medical claim in chat."
        },
        "correct": "A",
        "explanation": "Beginner Mistake 4 is 'Thinking about privacy or accountability only after something goes wrong.' The associate focused entirely on output speed and accuracy while completely bypassing Creation Diligence (using an unvetted consumer tool and failing to redact protected health records). High task accuracy never excuses reckless data handling.",
        "why_incorrect": {
            "B": "Beginner Mistake 1 involves prompting before defining the business problem, audience, and constraints.",
            "C": "Beginner Mistake 2 involves treating the first draft as final rather than iterating through structured steering.",
            "D": "Beginner Mistake 3 involves mistaking linguistic fluency for factual accuracy; here the extraction was accurate but non-compliant."
        },
        "full_justification": "Option A is correct because Beginner Mistake 4 is 'Thinking about privacy or accountability only after something goes wrong'. The associate focused entirely on output speed and task completion, completely bypassing Creation Diligence (using an unapproved consumer tool and failing to redact protected clinical records). High extraction accuracy does not excuse irresponsible data handling. Option B is incorrect because Beginner Mistake 1 is prompting before scoping. Option C is incorrect because Beginner Mistake 2 is treating the first draft as final. Option D is incorrect because Beginner Mistake 3 is mistaking fluency for accuracy."
    }
]
