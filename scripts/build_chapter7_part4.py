# -*- coding: utf-8 -*-
"""
Chapter 7 Part 4: Questions 31 to 40
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 31,
        "question": "An enterprise solutions architect establishes operational routing rules for a multi-disciplinary analytics team. An associate asks which criteria should decide whether a new workflow belongs in conversational chat, a cloud agent surface, a local desktop session, or a developer terminal. Under the course's three-question routing framework, which combination of questions must the architect evaluate?",
        "options": {
            "A": "How many subagents are declared in the plugin, what is the monthly subscription tier, and does the user possess coding skills?",
            "B": "Which foundation model has highest benchmark scores, how many tokens does the brief use, and is the prompt written in English?",
            "C": "What does the work touch, must it run while the device is off, and who is legally and contractually allowed to hold the data?",
            "D": "Is the workstation connected via optical fibre, does the user utilize an incognito window, and has the vendor signed an NDA?"
        },
        "correct": "C",
        "explanation": "The three load-bearing routing questions that govern workflow placement are: 1) What does the work touch? (files, connectors, browser pages, databases, local terminals), 2) Must it run while my device is off? (determining whether continuous cloud execution is required vs. local workstation tools), and 3) Who is allowed to hold and process the data? (governing legal data custody, residency, compliance, and enterprise contracts).",
        "why_incorrect": {
            "A": "Subagent counts and individual subscription tiers do not dictate architectural data governance or execution boundaries.",
            "B": "Benchmark scores, prompt token counts, and language selection are tactical prompt details that do not resolve architectural routing or custody.",
            "D": "Physical network cable media and browser caching states are superficial mechanisms that do not govern institutional workflow placement."
        },
        "full_justification": "Option C is correct because the curriculum establishes three load-bearing routing questions to guide operational deployment: 1) What does the work touch? (files, connectors, browser pages, terminals), 2) Must it run while my device is off? (determining whether pure cloud continuity is required vs. local workstation tools), and 3) Who is allowed to hold and process the data? (governing data residency, compliance, and enterprise custody). Option A is incorrect because subagent counts do not govern compliance boundaries. Option B is incorrect because benchmark scores are irrelevant to architectural data residency. Option D is incorrect because cable media and incognito modes are superficial."
    },
    {
        "id": 32,
        "question": "A hospital network's health informatics lead explores using autonomous web agents to extract billing discrepancy trends from patient oncology treatment files. The hospital operates under an enterprise agreement with Anthropic that includes a Business Associate Agreement (BAA) for covered clinical services. The lead proposes running these medical records through Claude Cowork's cloud session interface. What regulatory compliance barrier invalidates this proposal?",
        "options": {
            "A": "As of current certification standards, Anthropic states that Claude Cowork is not covered under its BAA for HIPAA use.",
            "B": "Cloud sandboxes are technically incapable of ingesting tabular clinical data files containing patient diagnosis codes.",
            "C": "Federal healthcare regulations mandate that all oncology records must be processed via on-premises legacy mainframes.",
            "D": "Enterprise BAAs automatically expire whenever an automated agent task executes more than ten sequential tool actions."
        },
        "correct": "A",
        "explanation": "Product availability is not compliance permission. While foundation model providers maintain HIPAA-ready Enterprise plans for specific core API or chat endpoints, vendor documentation explicitly clarifies that autonomous agent workspaces (such as Claude Cowork or event-triggered ChatGPT Work tasks) are not covered under active BAAs for HIPAA use. Ingesting protected health information (PHI) into non-BAA covered agent surfaces violates federal healthcare privacy statutes.",
        "why_incorrect": {
            "B": "Cloud containers ingest structured spreadsheets and clinical diagnosis codes routinely; the barrier is legal and contractual, not computational.",
            "C": "HIPAA does not require on-premises legacy mainframes; cloud processing of PHI is lawful provided the specific software service is formally covered under a BAA.",
            "D": "Business Associate Agreements are binding legal contracts, not technical quotas that expire after an arbitrary count of agent tool executions."
        },
        "full_justification": "Option A is correct because product availability is not compliance permission. While Anthropic provides HIPAA-ready Enterprise plans for certain services, its documentation and the course fact check explicitly state that Claude Cowork is not covered under its BAA for HIPAA use. (OpenAI maintains an identical boundary: event-triggered Work tasks in ChatGPT for Healthcare are not BAA-covered and must not process PHI). Ingesting patient oncology records into Cowork breaches HIPAA compliance. Option B is incorrect because containers handle clinical tables easily. Option C is incorrect because mainframes are not mandated by law. Option D is incorrect because BAAs do not expire based on tool action counts."
    },
    {
        "id": 33,
        "question": "A private clinic's operations coordinator wants to analyze appointment cancellation trends across surgical specialties to optimize theatre utilization. The source booking file contains patient names, residential postcodes, surgical procedures, and match dates. The clinic's commercial agent workspace is not approved to process protected health information (PHI). How can the coordinator legitimately proceed with this analysis without breaching healthcare data privacy regulations?",
        "options": {
            "A": "Apply the discriminator test: remove patient names and quasi-identifiers, retaining only surgical specialty and cancellation patterns.",
            "B": "Route the booking file through a desktop bridge to ensure the patient records remain physically housed on the clinic laptop hard drive.",
            "C": "Convert the patient spreadsheet into an interactive HTML canvas artifact to bypass cloud network inspection and privacy filters safely.",
            "D": "Upload the raw spreadsheet into an incognito Cowork session and append a prompt instructing the model to forget all patient names."
        },
        "correct": "A",
        "explanation": "The coordinator must apply the discriminator strategy: 'Does the task need the identifiers, or only the pattern?' Analyzing clinic cancellation trends across surgical specialties requires aggregate categorical patterns (specialty, procedure type, cancellation flag), not individual patient identities. Removing direct identifiers (names) and unique quasi-identifiers (specific postcodes, exact admission timestamps) de-identifies the dataset, allowing the analytical work to proceed lawfully without ingesting PHI.",
        "why_incorrect": {
            "B": "Reading local files through a desktop bridge still transmits file contents over the network to vendor cloud servers for processing, violating health data restrictions.",
            "C": "Rendering data inside an HTML canvas artifact does not prevent unredacted patient data from being transmitted to and processed by third-party cloud servers.",
            "D": "Instructing a model to 'forget names' inside an incognito chat session is conversational prompting, not a legally recognized de-identification standard under HIPAA."
        },
        "full_justification": "Option A is correct because it applies the discriminator strategy: 'Does the task need the identifiers, or only the pattern?' Determining clinic theatre utilization and cancellation trends across specialties depends entirely on aggregate categorical patterns (specialty, procedure category, cancellation rate), not patient identities. Removing direct names and unique quasi-identifiers (such as specific residential postcodes and exact match dates) removes PHI from the dataset entirely, allowing the analysis to proceed legally. 'Removing what the task does not need is a route, not an evasion'. Option B is incorrect because desktop bridges still transmit data to cloud servers. Option C is incorrect because canvas artifacts do not prevent cloud transmission. Option D is incorrect because conversational prompts do not meet statutory de-identification standards."
    },
    {
        "id": 34,
        "question": "A compliance officer at a wealth management firm audits an analyst who used a cloud Cowork session to parse an unannounced corporate merger term sheet. The analyst insists he complied with the firm's strict local-custody policy because the file was stored on his laptop hard drive and accessed through the Claude Desktop connected folder bridge. Why is the analyst's defense technically and operationally flawed?",
        "options": {
            "A": "Connecting a local folder automatically mirrors the hard drive's entire contents to a public GitHub repository endpoint.",
            "B": "Using Claude Desktop forces the host workstation operating system to permanently disable local disk encryption protocols.",
            "C": "A desktop bridge is a convenience, not a custody loophole; file contents were transmitted to and processed in the cloud.",
            "D": "The platform vendor automatically acquires statutory co-ownership of any corporate merger document opened via a bridge."
        },
        "correct": "C",
        "explanation": "A bridge is an operational convenience, not a custody loophole. When a cloud Cowork session inspects a local folder via the Claude Desktop bridge, the agent loop executes in the vendor's cloud; the contents of the local file are transmitted over the network and processed on vendor cloud servers. 'The file originated on my laptop' does not mean 'the file remained on my laptop.'",
        "why_incorrect": {
            "A": "Authenticated desktop bridges establish encrypted client-server sessions; they do not mirror or publish local drives to public repositories.",
            "B": "Application-level desktop bridges interact with the filesystem via standard operating system APIs without modifying BitLocker or FileVault disk encryption.",
            "D": "Processing documents via enterprise AI software does not transfer copyright or legal ownership of corporate assets to the software vendor."
        },
        "full_justification": "Option C is correct because the curriculum establishes: 'A bridge is a convenience, not a custody loophole'. When a cloud Cowork session inspects a local folder through the Claude Desktop bridge, the agent loop executes in Anthropic's cloud; the contents of the local file are transmitted over the network and processed on vendor cloud servers. 'The file came from my laptop' does not mean 'the file stayed on my laptop'. Option A is incorrect because desktop bridges do not publish files to public repositories. Option B is incorrect because bridges do not disable disk encryption. Option D is incorrect because commercial processing does not transfer asset ownership."
    },
    {
        "id": 35,
        "question": "An international humanitarian NGO requires an automated weekly workflow to compile field security incident reports. The NGO's internal data governance policy strictly prohibits hosting vulnerable aid-worker transit logs on commercial cloud infrastructure. However, the operations desk has no dedicated software engineers. If the NGO deploys the open path (such as self-hosted OpenWork) to satisfy its data sovereignty mandate, what operational trade-off must leadership accept?",
        "options": {
            "A": "The NGO eliminates all software licensing fees and avoids needing any ongoing system operator or maintenance engineering support.",
            "B": "The open path legally obligates the organization to make all internal field security data publicly accessible under open licenses.",
            "C": "The NGO gains local data custody and model choice, but must build, operate, and maintain the state spine and scheduler itself.",
            "D": "The NGO must completely abandon automated agents and return entirely to manual, paper-based incident reporting spreadsheets."
        },
        "correct": "C",
        "explanation": "The core operational trade-off of the open path is: 'The companies sell you a spine. The open path makes you build one.' Managed vendor platforms provide the state spine (saved sessions, synchronizations, schedulers, phone notification gates) in their cloud custody on day one. Self-hosted agent platforms grant total local data custody and model autonomy, but require the organization to deploy, configure, update, and maintain the runtime infrastructure and schedulers themselves: custody is paid for in operational overhead.",
        "why_incorrect": {
            "A": "Operating self-hosted software eliminates vendor subscriptions but creates an ongoing internal engineering and operational maintenance burden.",
            "B": "Deploying open-source software to process proprietary records does not require an organization to publish or license its private operational data.",
            "D": "Open-source agent frameworks (e.g., OpenWork, OpenCode) exist specifically to automate workflows securely on private infrastructure without manual paper methods."
        },
        "full_justification": "Option C is correct because it articulates the core operational trade-off of the open path: 'The companies sell you a spine. The open path makes you build one'. On vendor platforms, the state spine (saved sessions, sync, scheduler, phone gate) is managed for you on day one in their custody. Self-hosted stacks (like OpenWork or OpenCode) grant total data custody and model choice, but demand that the organization deploy, configure, update, and operate the infrastructure and schedulers themselves. 'Custody is paid for in operations'. Option A is incorrect because self-hosted systems require internal maintenance. Option B is incorrect because open-source tools do not require publishing private data. Option D is incorrect because open-source agents automate workflows locally."
    },
    {
        "id": 36,
        "question": "A corporate strategy lead conducts a 'portability drill' to assess her firm's lock-in exposure if their primary commercial AI vendor were to terminate services unexpectedly. When auditing an automated weekly market intelligence workflow, which assets can be successfully migrated to a competing platform, and which assets remain permanently locked to the incumbent vendor? (Select TWO.)",
        "options": {
            "A": "Proprietary project memory, native account state spines, and browser login states remain trapped on the original platform.",
            "B": "The 8-part task brief, primary source URLs, output schema, and definition of done migrate cleanly across alternative tools.",
            "C": "Platform-specific approval toggle labels and vendor-hosted dashboard URLs travel without operational modification rules.",
            "D": "Historical session conversation logs, proprietary cloud memory topics, and vendor plugin hooks migrate completely cleanly."
        },
        "correct": "A and B",
        "explanation": "The portability drill distinguishes between owned portable assets and vendor-locked platform assets: 1. Portable Assets: Objective definitions, 8-part task briefs, source URL registries, JSON output schemas, validation rules, and definition-of-done criteria are user-owned intellectual assets that can be re-hosted on any competing platform immediately. 2. Vendor-Locked Assets: Native semantic memory topics, proprietary conversation histories, closed project instruction consoles, platform approval toggles, and browser credential states reside in vendor platform storage (Tier 2) and cannot be natively transferred.",
        "why_incorrect": {
            "C": "Approval toggle labels and vendor-hosted links (such as ChatGPT Sites or Cowork share links) are proprietary platform artifacts that become dead links if the vendor relationship terminates.",
            "D": "Proprietary conversation histories, semantic memory topics, and vendor-specific plugin hooks are formatted in closed vendor schemas and cannot be exported into competing engines."
        },
        "full_justification": "Options A and B are correct because they reflect the findings of the portability drill: (A) proprietary project memory, native account state spines, and browser login states remain locked within vendor platform storage (Tier 2); while (B) 8-part task briefs, primary source locations, output schemas, and empirical definitions of done are portable, user-owned assets that transfer cleanly to competing systems. Option C is incorrect because platform-specific labels and hosted URLs become dead links if the platform changes. Option D is incorrect because proprietary session logs and memory topics cannot be natively ingested by competing vendor memory engines."
    },
    {
        "id": 37,
        "question": "An enterprise systems engineer compares Claude Cowork's managed plugin architecture with a repository-based agentic coding harness running in continuous integration (CI). While modern Cowork plugins can package skills, connectors, sub-agents, and lifecycle hooks, what critical governance distinction separates the managed web surface from the owned coding harness?",
        "options": {
            "A": "Managed web surfaces forbid all forms of automation, whereas repository coding harnesses allow unattended script execution workflows.",
            "B": "Managed web plugins run exclusively on local workstation hardware, whereas CI pipelines run exclusively in public consumer cloud nodes.",
            "C": "Managed web surfaces execute tasks using probabilistic models, whereas repository coding harnesses utilize deterministic symbolic code.",
            "D": "On managed web surfaces, you rent vendor-enforced safety policies; in an owned harness, you own and can reproduce the enforcement code."
        },
        "correct": "D",
        "explanation": "The fundamental boundary separating a rented harness from an owned harness is governance reproducibility: on a managed web surface (Claude Cowork, ChatGPT Work), organizations configure settings within a vendor-owned runtime and safety layer (platform sandboxes, product safety classifiers, proprietary hook lifecycles). In an owned coding harness (such as repository-backed workflows in CI), the organization authors, versions, inspects, and executes the actual enforcement code, guardrail policies, sandboxes, and verification test suites.",
        "why_incorrect": {
            "A": "Managed web surfaces support extensive unattended automation, including recurring schedulers and background execution loops.",
            "B": "Managed Cowork plugins run within vendor cloud infrastructure, while enterprise CI pipelines typically execute on private corporate runners or dedicated virtual machines.",
            "C": "Both web agents and coding harnesses utilize probabilistic foundation models for cognitive reasoning; the difference lies in the governance and execution harness around the model."
        },
        "full_justification": "Option D is correct because it defines the fundamental boundary between a rented harness and an owned harness. On a managed web surface (Claude Cowork, ChatGPT Work), you configure settings within a vendor-owned runtime and safety layer (platform sandboxes, product safety classifiers, proprietary hook lifecycles). In an owned coding harness (such as repository-backed workflows in CI), your team authors, versions, inspects, and executes the actual enforcement code, guardrail policies, sandboxes, and verification test suites. Option A is incorrect because managed surfaces support unattended scheduling. Option B is incorrect because managed plugins run in cloud sandboxes. Option C is incorrect because both utilize probabilistic foundation models."
    },
    {
        "id": 38,
        "question": "A digital transformation consultant evaluates an autonomous web agent that drafts weekly supplier performance scorecards. The agent's first run completed smoothly, extracting data from twelve portals without an error. A junior analyst recommends immediately scheduling the agent for unattended production runs. Following the evaluation disciplines taught in Trusting the Checker, how should the consultant respond? (Select TWO.)",
        "options": {
            "A": "Approve the recommendation, because autonomous agents exhibit deterministic execution consistency once a workflow succeeds once.",
            "B": "Reject the recommendation, because a single successful execution is an isolated demo rather than proof of a reliable distribution.",
            "C": "Decommission the human review gate immediately, because successful browser extraction proves that the model judge is fully calibrated.",
            "D": "Insist on evaluating multiple trials across diverse edge cases, prioritizing the severity of individual failure modes over volume."
        },
        "correct": "B and D",
        "explanation": "The evaluation maxims from 'Trusting the Checker' dictate: 1. Grade the rate, not the run: A single flawless execution is merely an isolated demonstration, not empirical evidence of system reliability ('Demos are the weakest evidence'). 2. Severity over volume: When evaluating agentic performance distributions, uncovering a single catastrophic failure mode (such as publishing invalid credit terms or hallucinating bank details) outweighs ninety-nine routine successful extractions.",
        "why_incorrect": {
            "A": "Foundation models coupled with web scrapers represent non-deterministic distributions that encounter changing DOM structures, dynamic timeouts, and varying interpretations across runs.",
            "C": "Extracting data from web pages does not calibrate internal model judgment or justify removing human review gates on consequential scorecards."
        },
        "full_justification": "Options B and D are correct because they embody the professional evaluation maxims established in Trusting the Checker: (B) grade the rate, not the run—a single successful execution is merely an isolated demonstration, not empirical evidence of system reliability; and (D) severity over volume—insist on evaluating multiple trials across diverse edge cases, recognizing that a single catastrophic failure outweighs many routine successes. Option A is incorrect because language models and web scrapers are non-deterministic. Option C is incorrect because successful initial extraction does not eliminate the need for human review gates on consequential scorecards."
    },
    {
        "id": 39,
        "question": "An operations director maps the firm's automation portfolio across the runtime custody spectrum, transitioning tasks from casual exploratory use to mission-critical enterprise systems. Which progression correctly orders these runtime patterns from lowest operational ownership to highest operational control?",
        "options": {
            "A": "Hybrid cloud loop with desktop bridge -> Interactive cloud session -> Cloud scheduled task -> Managed runtime in corporate CI.",
            "B": "Interactive cloud session -> Cloud scheduled task -> Hybrid cloud loop with desktop bridge -> Owned self-hosted infrastructure.",
            "C": "Owned self-hosted infrastructure -> Managed runtime in corporate CI -> Cloud scheduled task -> Interactive cloud session run.",
            "D": "Cloud scheduled task -> Owned self-hosted infrastructure -> Interactive cloud session -> Hybrid cloud loop with desktop bridge."
        },
        "correct": "B",
        "explanation": "The runtime custody spectrum progresses from pure vendor platform management to total organizational infrastructure ownership: 1. Interactive cloud session (vendor operates the loop and tools in its cloud; user interacts via browser viewport). 2. Cloud scheduled task (vendor initiates and executes the loop automatically on cloud infrastructure). 3. Hybrid cloud loop with desktop bridge (vendor runs the remote loop while accessing specific local workstation tools). 4. Owned self-hosted infrastructure (organization operates the physical servers, orchestration harness, runtime environment, and data storage).",
        "why_incorrect": {
            "A": "Scrambles the progression, placing hybrid desktop bridges ahead of purely managed cloud sessions.",
            "C": "Inverts the entire spectrum, placing fully owned infrastructure first and interactive cloud sessions last.",
            "D": "Scrambles the progression, misplacing cloud scheduled tasks ahead of owned infrastructure."
        },
        "full_justification": "Option B is correct because it accurately traces the runtime custody progression from pure vendor management to total organizational control: 1. Interactive cloud session: Vendor runs the loop and tools on its infrastructure; user interacts via viewport. 2. Cloud scheduled task: Vendor initiates and executes the loop automatically on cloud infrastructure. 3. Hybrid cloud loop with desktop bridge: Vendor runs the remote loop while borrowing specific local workstation tools. 4. Owned self-hosted infrastructure: The enterprise operates the physical/virtual servers, runtime environment, orchestration harness, and storage. Options A, C, and D are incorrect because they scramble the progression."
    },
    {
        "id": 40,
        "question": "A logistics executive reflects on the operational upgrades introduced across modern web agent surfaces in mid-2026, including shared cloud memory, integrated browsers, autonomous plugin sub-agents, and automated schedulers. What enduring operational limit governs these advanced capabilities?",
        "options": {
            "A": "Modern safety classifiers have eliminated prompt injection risks, making untrusted third-party web content fully authoritative.",
            "B": "Expanded harness capabilities accelerate task execution, but cannot transform a fundamentally flawed brief into sound results.",
            "C": "Autonomous agent surfaces have eliminated the architectural necessity for Tier 3 data exits into corporate systems of record.",
            "D": "Foundation models have achieved full statutory certification, legally eliminating human operational liability in supply chains."
        },
        "correct": "B",
        "explanation": "The foundational operational limit is: 'The surface makes weak work faster, not better.' Providing an agent with persistent memory, autonomous browsing, plugin sub-agents, and recurring schedulers does not fix an ambiguous brief, flawed logic, or missing evidence. If the underlying operational brief is defective, an autonomous agent simply repeats and scales that defect into the future more rapidly. Human judgment, rigorous briefs, plan reviews, and verified Tier 3 exits remain non-negotiable.",
        "why_incorrect": {
            "A": "Automated safety classifiers screen proposed actions but cannot eliminate prompt injection; untrusted outside content remains untrusted evidence, never an authoritative instruction.",
            "C": "Tier 3 exits (saving deliverables into enterprise systems of record) remain essential to prevent critical corporate assets from being trapped in Tier 2 platform storage.",
            "D": "Commercial AI software terms explicitly disclaim all operational, legal, and regulatory liability; human professionals retain 100% non-transferable accountability."
        },
        "full_justification": "Option B is correct because of the foundational curriculum principle: 'The surface makes weak work faster, not better'. Providing an agent with persistent memory, autonomous browsing, and recurring schedulers does not fix an ambiguous brief, unsound reasoning, or missing evidence. If the underlying operational logic is defective, an autonomous agent simply repeats and scales that error into the future more rapidly. Human judgment, clear briefs, plan reviews, and verified Tier 3 exits remain the primary controls. Option A is incorrect because prompt injection remains an active risk. Option C is incorrect because Tier 3 exits remain essential. Option D is incorrect because human accountability is non-transferable."
    }
]
