# -*- coding: utf-8 -*-
"""
Chapter 7 Part 3: Questions 21 to 30
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 21,
        "question": "An operations director at a marine salvage brokerage spends two hours every Friday manually checking three separate shipping casualty feeds, reconciling vessel IDs against insured registries, and updating an underwriting dashboard. She wants to delegate this task to Claude Cowork, but struggles to formalize the messy edge cases and procedural rules in a prompt. According to expert agent workflow design, what is the most effective initial prompt to establish this workflow?",
        "options": {
            "A": "Upgrade to an enterprise developer workspace to build and configure headless command-line web scraping routines.",
            "B": "Paste all sixty pages of historical vessel salvage logs into a fresh chat and demand an autonomous triage pipeline.",
            "C": "Command the assistant to generate twenty speculative procedural flows and pick the one with the lowest token count.",
            "D": "Instruct the agent to interview her until the objective, key sources, immutable rules, and done criteria are fixed."
        },
        "correct": "D",
        "explanation": "When an operator understands an operational problem but cannot articulate the procedural sequence cleanly, the established technique is workflow discovery via interview. Instructing the agent to interview the user ('Interview me until you understand what I am trying to accomplish, what sources matter, what must never change, and what done looks like') lets the system extract requirements interactively.",
        "why_incorrect": {
            "A": "Jumping to developer command-line scrapers adds technical complexity before underlying business rules are established.",
            "B": "Dumping raw historical logs without constraints forces the model to guess procedures, producing brittle and hallucinated workflows.",
            "C": "Generating speculative procedural flows without business context wastes tokens and optimizes the wrong criteria."
        },
        "full_justification": "Option D is correct because when a practitioner understands their operational pain point but cannot cleanly articulate the end-to-end procedural steps, the established best practice is workflow discovery via interview. Prompting the agent to interview the user ('Interview me until you understand what I am trying to accomplish, what sources matter, what I never want changed, and what a good finished brief looks like') lets the system structure the automation design interactively. Option A is incorrect because developer scrapers add premature overhead. Option B is incorrect because dumping raw logs without rules forces models to hallucinate. Option C is incorrect because generating random flows does not uncover real constraints."
    },
    {
        "id": 22,
        "question": "A logistics analyst constructs an operational brief for an unattended cloud agent tasked with compiling weekly port congestion surcharges. The brief outlines the target audience, allowable data sources, calculation methods, escalation triggers, the Tier 3 enterprise Google Drive destination, and empirical definitions of done. However, the analyst omits the Boundaries parameter. Which operational failure mode does this omission invite during unattended execution?",
        "options": {
            "A": "The agent assumes unbounded authority to email shipping lines, adjust tariffs, or publish unvetted findings.",
            "B": "The underlying foundation model automatically reverts to its base pretraining weights during the active run.",
            "C": "The cloud session immediately terminates because task containers require negative constraints to initialize.",
            "D": "The agent fails to compute numerical currency figures and defaults to descriptive qualitative draft reports."
        },
        "correct": "A",
        "explanation": "In the 8-part unattended brief architecture, Boundaries establish the negative risk fence—explicitly dictating what the agent must not read, change, send, purchase, delete, or publish. If an agent possesses tool reach (such as email or ERP connectors) and boundaries are omitted, it operates without constraints on its blast radius and may execute irreversible external actions autonomously.",
        "why_incorrect": {
            "B": "Prompt omissions affect instructional context; they do not alter or reset underlying foundation model pretraining weights.",
            "C": "Cloud containers initialize based on runtime configs; omitting prompt boundaries does not cause container startup crashes.",
            "D": "Mathematical computation depends on code execution tools and instructions, not on negative boundary definitions."
        },
        "full_justification": "Option A is correct because in the 8-part unattended brief architecture, Boundaries establish the negative risk fence—explicitly dictating what the agent must not read, change, send, purchase, delete, or publish. If an agent possesses tool reach (such as email or ERP connectors) and boundaries are omitted, the agent operates without constraints on its blast radius and may autonomously execute irreversible, real-world state changes. Option B is incorrect because model weights do not reset due to prompt omissions. Option C is incorrect because containers initialize normally. Option D is incorrect because arithmetic relies on code tools rather than boundaries."
    },
    {
        "id": 23,
        "question": "A clinical audit associate delegates an unattended overnight agent run to extract adverse medication interaction reports from patient clinic discharge summaries. The associate appends the critical instruction: 'If the necessary evidence is missing, state what is missing and stop rather than inventing it.' Why is this specific guardrail significantly more vital in unattended agent runs than in interactive chat turns?",
        "options": {
            "A": "In conversational chat, automated safety classifiers screen and block all ungrounded medical generations.",
            "B": "An ungrounded assumption in an unattended run cascades undetected through downstream analytical reports.",
            "C": "Interactive chat sessions automatically query external medical registries when encountering missing data.",
            "D": "Unattended cloud tasks lack access to secure Python code execution sandboxes to verify clinical dosages."
        },
        "correct": "B",
        "explanation": "In an unattended run, no human operator is watching the screen to intercept an ungrounded inference mid-stride. If an agent encounters missing evidence and hallucinates a plausible fact to fill the gap, that false premise compounds through downstream analysis, calculations, and recommendations before a human ever inspects the output. Mandating that the model 'state what is missing and stop' serves as an essential circuit-breaker.",
        "why_incorrect": {
            "A": "Safety classifiers screen for abuse and policy violations; they do not verify empirical factual grounding in patient files.",
            "C": "Conversational chat sessions cannot independently query outside registries unless configured with live connectors.",
            "D": "Cloud agent containers routinely have code execution sandboxes; the risk is probabilistic confabulation, not missing tooling."
        },
        "full_justification": "Option B is correct because in an unattended run, there is no human operator sitting at the screen to catch an ungrounded inference mid-stride. If an agent encounters missing data and hallucinates a plausible fact to bridge the gap, that false premise compounds through subsequent analysis, calculations, and final reports before a human ever inspects the output. Mandating that the model 'state what is missing and stop' serves as an essential circuit-breaker. Option A is incorrect because safety classifiers do not check factual accuracy. Option C is incorrect because chat models cannot search without connectors. Option D is incorrect because sandboxes are available in cloud tasks."
    },
    {
        "id": 24,
        "question": "A commercial property manager commissions an automated agent to audit tenant utility arrears across fifty retail units. Following the delegation loop, the manager commands the agent to output its plan first. The returned plan contains four sequential milestones: 1. Connect to the property management database and download tenant payment ledgers. 2. Calculate cumulative water surcharge arrears for each tenant. 3. Automatically email formal default notices to tenants with arrears exceeding £1,000. 4. Export the consolidated arrears schedule to the corporate OneDrive folder. When auditing this plan, which critical flaw must prompt the manager to redirect the agent?",
        "options": {
            "A": "The plan sequences data extraction from the property management database prior to computing debt totals.",
            "B": "The plan saves the final consolidated arrears report into an institutional Tier 3 cloud records system.",
            "C": "The plan proposes calculating numerical arrears using deterministic mathematical Python script routines.",
            "D": "The plan proposes irreversible external communication before tenant arrears have undergone human review."
        },
        "correct": "D",
        "explanation": "Reviewing the plan before execution intercepts flawed scope, order, reach, and assumptions. The proposed plan violates safe operational sequencing and reach by placing an irreversible, high-consequence external action (emailing default notices to commercial tenants) before arrears figures have been reviewed or archived in institutional records. Step 3 must be paused or converted into a draft-only queue requiring human sign-off.",
        "why_incorrect": {
            "A": "Retrieving primary ledger records before calculating arrears is the correct, logical procedural sequence.",
            "B": "Exporting final deliverables to an enterprise cloud repository correctly satisfies Tier 3 data exit requirements.",
            "C": "Computing arrears using deterministic code execution is best practice computational hygiene."
        },
        "full_justification": "Option D is correct because reviewing the plan before execution is designed to intercept flawed scope, order, reach, and assumptions. The proposed plan violates safe operational order and reach by placing an irreversible, high-consequence external action (dispatching default notices to commercial tenants) before the figures have been reviewed or exited into institutional records. Step 3 must be halted or converted into a draft-only queue requiring human sign-off. Option A is incorrect because downloading ledgers first is correct. Option B is incorrect because saving to OneDrive is correct. Option C is incorrect because mathematical scripts are desirable."
    },
    {
        "id": 25,
        "question": "An IT systems lead configures four automated tasks across ChatGPT Work and Claude Cowork. She maps each task to one of the four universal heartbeat patterns: Task 1: A one-time reminder task set to compile an equipment inventory tomorrow at 09:00, then terminate. Task 2: A recurring compliance summary that executes every Monday morning at 06:00. Task 3: A triage workflow that initiates immediately when a new pull request or customer ticket is created. Task 4: An inspection routine that checks an exchange rate feed hourly and alerts the desk only if volatility exceeds 5%. Which sequence correctly classifies the heartbeats of Tasks 1, 2, 3, and 4?",
        "options": {
            "A": "Once for Task 1; While monitoring for Task 2; On a supported event for Task 3; On a schedule for Task 4.",
            "B": "While monitoring for Task 1; On a schedule for Task 2; Once for Task 3; On a supported event for Task 4.",
            "C": "Once for Task 1; On a schedule for Task 2; On a supported event for Task 3; While monitoring for Task 4.",
            "D": "On a schedule for Task 1; Once for Task 2; While monitoring for Task 3; On a supported event for Task 4."
        },
        "correct": "C",
        "explanation": "The four universal heartbeat mechanisms are: 1. Task 1 (One-time future timestamp): Maps to Once (executes on a scheduled timestamp and terminates). 2. Task 2 (Clock-based recurrence): Maps to On a schedule (fires on a recurring calendar/cron schedule). 3. Task 3 (Event-driven trigger): Maps to On a supported event (fires reactively upon a designated webhook, ticket, or commit). 4. Task 4 (Continuous threshold watching): Maps to While monitoring (repeatedly inspects a condition and alerts only upon threshold breach).",
        "why_incorrect": {
            "A": "Misclassifies Task 2 as While monitoring and Task 4 as On a schedule.",
            "B": "Scrambles the definitions, misidentifying one-time reminders and continuous monitoring.",
            "D": "Scrambles the sequence, placing scheduled recurrence on Task 1 and one-time execution on Task 2."
        },
        "full_justification": "Option C is correct because it correctly identifies the four universal heartbeat mechanisms established in the curriculum: 1. Task 1 (One-time future execution): Maps to Once (runs a single time on a future timestamp and terminates). 2. Task 2 (Clock-based recurrence): Maps to On a schedule (fires on a recurring calendar/clock trigger). 3. Task 3 (Event-driven trigger): Maps to On a supported event (fires reactively upon a designated webhook, email, or repository event). 4. Task 4 (Continuous threshold watching): Maps to While monitoring (repeatedly inspects a condition and alerts only upon threshold breach). Options A, B, and D are incorrect because they scramble the definitions and operational behaviors of these four distinct heartbeat types."
    },
    {
        "id": 26,
        "question": "A treasury associate designs a recurring Monday morning task in Claude Cowork to aggregate foreign exchange exposure. The workflow reads cloud-hosted market feeds via an API connector, writes a summary report to Google Drive, and references a currency risk policy file stored on the associate's laptop via a Claude Desktop connected folder. If the associate closes her laptop over the weekend, what happens on Monday morning?",
        "options": {
            "A": "The scheduled task fires and runs to completion by retrieving the laptop file from Anthropic's server cache.",
            "B": "The entire Cowork task executes normally on the cloud sandbox without attempting to read the risk file.",
            "C": "The task fails to initialize at all because cloud schedulers require active client pings to trigger runs.",
            "D": "The cloud session starts, but fails or delivers incomplete output because the bridged local file is offline."
        },
        "correct": "D",
        "explanation": "A scheduled task is truly device-independent only if every required tool and data source is reachable without the user's host device. The cloud session starts because its heartbeat and agent loop reside on vendor cloud infrastructure; however, when it attempts to read the currency risk policy file from the sleeping laptop via the desktop bridge, that tool is offline. The workflow pauses, fails, or delivers an incomplete report.",
        "why_incorrect": {
            "A": "Vendor cloud servers do not mirror or cache local files that reside across an offline desktop bridge.",
            "B": "The agent executes its briefed instructions; discovering a missing required file tool halts or impairs the run rather than gracefully ignoring it.",
            "C": "Cloud scheduled tasks trigger from server clocks without requiring active client pings or open browser tabs."
        },
        "full_justification": "Option D is correct because of the foundational scheduling rule: 'A schedule is truly device-independent only if every required tool is also reachable without your device'. The cloud session starts because its heartbeat and agent loop reside on Anthropic's cloud servers; however, when the task attempts to read the currency risk file from the sleeping laptop via the desktop bridge, that tool is offline. The workflow either pauses, crashes, or delivers an incomplete report missing critical risk constraints. Option A is incorrect because vendor clouds do not cache offline bridge files. Option B is incorrect because missing files impair execution rather than being bypassed. Option C is incorrect because cloud schedulers trigger independently of client machines."
    },
    {
        "id": 27,
        "question": "An operations supervisor inspects the status dashboard of an automated overnight invoice matching agent. The platform scheduler displays a green status badge reading: 'Task completed successfully at 03:14 (Duration: 18m).' When the finance director inspects the accounts payable shared drive at 09:00, no reconciled invoice register is present. What core operational principle explains this discrepancy?",
        "options": {
            "A": "Automated tasks configured in cloud sandboxes automatically self-delete if outputs are not opened in 2 hours.",
            "B": "Platform schedulers track runtime execution events, which does not prove the deliverable succeeded or exited.",
            "C": "The foundation model platform suffered an unlogged network failure that erased the task container filesystem.",
            "D": "The green scheduler indicator confirms that all reconciliation records were automatically vetted and approved."
        },
        "correct": "B",
        "explanation": "A green scheduler badge proves runtime evidence, not outcome evidence: 'Ran is not the same as worked.' The badge confirms only that the scheduler triggered, the container initialized, and the loop terminated without an unhandled system crash. It provides zero proof that the business logic succeeded, calculations were correct, or files exited into Tier 3 institutional storage.",
        "why_incorrect": {
            "A": "While Tier 1 scratch space is cleaned up after task termination, finished deliverables intended for external drives do not 'self-delete' after viewing delays.",
            "C": "The scheduler reported normal completion; an unlogged network failure would show a container timeout or task crash.",
            "D": "Runtime completion is entirely distinct from human financial authorization; software cannot self-certify audit compliance."
        },
        "full_justification": "Option B is correct because it embodies the operational maxim: 'Ran is not the same as worked'. A green scheduler badge or execution log proves only runtime evidence—that the scheduler triggered, the container initialized, and the loop terminated without a fatal unhandled system exception. It provides zero outcome evidence confirming whether the business logic was sound, the reconciliation succeeded, or the deliverable exited to Tier 3 storage. Option A is incorrect because deliverables do not self-delete due to delays. Option C is incorrect because normal completion excludes network crashes. Option D is incorrect because runtime completion is not compliance sign-off."
    },
    {
        "id": 28,
        "question": "A marketing manager establishes a recurring scheduled task to summarize competitor blog updates every Wednesday. For three consecutive weeks, the task generated a formatted summary in Tier 2 platform storage. On the fourth Wednesday, no notification arrives, and no output is produced. Following standard troubleshooting protocols, what initial diagnostic checks should the manager conduct? (Select TWO.)",
        "options": {
            "A": "Verify whether the external competitor websites altered their page structures or blocked web agent scrapers.",
            "B": "Delete the active workspace project and re-import all historical files into a personal consumer chat window.",
            "C": "Inspect whether the scheduled task encountered an unapproved gate pause or exceeded metered usage limits.",
            "D": "Re-write the entire core prompt brief from scratch using highly aggressive negative framing constraints."
        },
        "correct": "A and C",
        "explanation": "When an unattended workflow produces silence, disciplined troubleshooting isolates failure points before altering prompts: 1. Platform & Gate Status: Check whether the run stalled at an unobserved human gate (waiting for approval on an unwatched surface) or exhausted its compute allowance. 2. Reach & Source Availability: External websites frequently change DOM structure, deploy CAPTCHAs, or block automated crawlers, causing silent extraction failures.",
        "why_incorrect": {
            "B": "Destroying project workspaces and pasting data into personal chats abandons enterprise persistence and security controls.",
            "D": "Rewriting the brief before diagnosing whether the task fired, stalled at a gate, or lost web access is unscientific troubleshooting."
        },
        "full_justification": "Options A and C are correct because when an unattended scheduled workflow produces silence, disciplined troubleshooting isolates failure points before altering prompts: (A) external web targets frequently update DOM elements, introduce CAPTCHA challenges, or block autonomous web scrapers, causing silent extraction failures; and (C) the operator must verify whether the run was halted at an unobserved human gate or exhausted its metered compute allowance. Option B is incorrect because deleting workspaces destroys governance. Option D is incorrect because rewriting prompts before diagnosing execution status is premature."
    },
    {
        "id": 29,
        "question": "A junior supply chain coordinator wants to deploy an automated cloud scheduled agent to manage factory inventory shortages. The coordinator proposes granting the agent authority to evaluate parts deficits overnight, generate purchase orders, and transmit binding supply contracts directly to vendors via DocuSign. Under recommended operational progression standards, why must this proposal be rejected?",
        "options": {
            "A": "Cloud scheduled agents lack the technical capability to interact with live external enterprise vendor APIs.",
            "B": "Foundation models cannot interpret multi-variable inventory spreadsheets without manual user interventions.",
            "C": "Statutory procurement rules strictly forbid using generative artificial intelligence for commercial supply.",
            "D": "Beginners must restrict recurring schedules to reporting workflows before graduating to autonomous actions."
        },
        "correct": "D",
        "explanation": "The curriculum establishes an operational progression ceiling for beginners: 'Schedules that REPORT, not schedules that ACT.' Recurring unattended agents should initially be restricted to reading data, analyzing trends, and compiling reports. Granting autonomous write, purchasing, or contract execution authority while operators sleep introduces an unacceptable blast radius before reliability has been proven.",
        "why_incorrect": {
            "A": "Agent surfaces equipped with MCP connectors possess the technical capability to invoke vendor APIs.",
            "B": "Foundation models coupled with code sandboxes easily parse and evaluate multi-variable inventory spreadsheets.",
            "C": "Statutory regulations do not categorically outlaw AI assistance; the restriction is an operational governance standard."
        },
        "full_justification": "Option D is correct because the curriculum establishes a clear teaching ceiling for beginners: schedules that REPORT, not schedules that ACT. Recurring unattended agents should initially be restricted to reading data, analyzing trends, and compiling reports. Granting autonomous write, purchasing, or contract execution authority while operators sleep introduces an unacceptable blast radius before a workflow has established repeated, audited reliability. Option A is incorrect because agents can interact with APIs. Option B is incorrect because models handle spreadsheets effectively. Option C is incorrect because regulations do not ban AI in procurement."
    },
    {
        "id": 30,
        "question": "A financial controller prepares to schedule a recurring daily agent task to flag anomalous corporate credit card transactions. Before enabling the automated clock trigger, the controller enforces the operational discipline: 'Walk it before you schedule it.' Which two verification checks must the controller complete during these preliminary manual runs? (Select TWO.)",
        "options": {
            "A": "Direct the agent to run financial audit calculations using generative probabilistic prose rather than code scripts.",
            "B": "Upgrade the active agent workspace to an unmonitored command-line terminal environment with full root permissions.",
            "C": "Confirm that when no suspicious transactions exist, the agent outputs a valid empty case rather than confabulating.",
            "D": "Run the workflow manually at least twice to verify source data access, plan logic, and Tier 3 delivery endpoints."
        },
        "correct": "C and D",
        "explanation": "The operational rule 'Walk it before you schedule it' mandates two checks: 1. Empirical Verification: Executing the workflow manually at least twice proves that source paths, connectors, analytical logic, and Tier 3 file exits function under real conditions. 2. The Empty Case: Schedulers repeat tasks blindly into the future; verifying the empty case (confirming that the agent cleanly outputs 'no new items found' when zero anomalies exist, rather than inventing discrepancies to satisfy the prompt) prevents hallucinated work.",
        "why_incorrect": {
            "A": "Financial audit calculations must be computed deterministically via code execution rather than generated via probabilistic text prediction.",
            "B": "Provisioning root terminal access to an unmonitored agent violates least privilege and introduces severe security risks."
        },
        "full_justification": "Options C and D are correct because of the core operational rule: 'Walk it before you schedule it': (C) verifying the empty case (confirming that the agent cleanly reports 'no new items' when zero discrepancies exist, rather than inventing anomalies to satisfy the prompt) prevents hallucinated work; and (D) executing the task manually at least twice proves that source paths, permissions, analytical plan logic, and Tier 3 file exits work under real conditions. Option A is incorrect because financial calculations must be deterministic. Option B is incorrect because root terminal access violates least privilege."
    }
]
