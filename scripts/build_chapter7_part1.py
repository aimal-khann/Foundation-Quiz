# -*- coding: utf-8 -*-
"""
Chapter 7 Part 1: Questions 1 to 10
Refactored for strict psychometric rigor, non-guessable distractors,
and strict character length parity (spread <= 0.05).
"""

QUESTIONS = [
    {
        "id": 1,
        "question": "An operations director at a regional transport authority evaluates two AI deployment patterns for staff handling driver roster dispute emails. Setup Alpha runs in the standard conversational interface where an officer pastes each dispute email and reviews suggested replies. Setup Beta runs on an agent surface where a task is assigned to monitor incoming driver disputes, verify telematics records, and draft formal determinations. What foundational operational test distinguishes Setup Beta from Setup Alpha?",
        "options": {
            "A": "Setup Beta executes queries exclusively on fine-tuned open-source models hosted within private cloud clusters.",
            "B": "Setup Beta eliminates the non-transferable organizational liability of human supervisors over disputed claims.",
            "C": "If the human operator stops typing, the operational work continues progressing autonomously toward completion.",
            "D": "If the client browser viewport closes, all active computational processing threads are permanently terminated."
        },
        "correct": "C",
        "explanation": "The defining operational test separating conversational chat from an agent surface is: 'If I stop typing, does the work stop?' Synchronous chat interfaces pause and await manual user input at every turn. An agent surface operates under delegated authority; once commissioned, it plans, invokes tools, navigates sequential dependencies, and progresses toward the assigned outcome even if the user closes the window or ceases typing.",
        "why_incorrect": {
            "A": "Agent surfaces can run on proprietary closed models (such as Claude 3.5 Sonnet or GPT-4o) or open-weights models; model licensing does not define the agentic loop.",
            "B": "Accountability is legally non-transferable; deploying an agent surface automates execution but does not relieve human supervisors of organizational liability.",
            "D": "In a cloud agent surface, closing the local browser viewport merely disconnects the display; the remote agent container continues running on server infrastructure."
        },
        "full_justification": "Option C is correct because the defining operational test separating ordinary conversational chat from an agent surface is: 'If I stop typing, does the work stop?' Synchronous chat boxes wait for the user's next manual input at every turn. An agent surface operates under delegated authority; once commissioned, the system plans, invokes tools, works through sequential steps, and continues progressing toward the assigned outcome even if the user closes the window or ceases typing. Option A is incorrect because agent surfaces can be powered by proprietary closed foundation models or open-weights models. Option B is incorrect because accountability is legally non-transferable. Option D is incorrect because in a cloud agent surface, closing the local browser tab merely closes the viewport while execution continues."
    },
    {
        "id": 2,
        "question": "A freight forwarder's compliance associate initiates a cloud Cowork task at 17:00 to reconcile port demurrage receipts against carrier invoices. The task uses a cloud connector to read carrier billing files from Google Drive and uses a desktop bridge to inspect container delivery slips stored in a folder on her office laptop. At 17:15, she closes her laptop and leaves the office. What is the operational state of the running workflow at 17:30?",
        "options": {
            "A": "The workflow crashes with an unrecoverable kernel panic triggered by broken TCP socket keepalive connections.",
            "B": "The cloud session continues its Drive work, but the local delivery slip folder tool becomes unavailable.",
            "C": "The entire Cowork session pauses instantly because closing the laptop terminates the remote cloud agent loop.",
            "D": "The agent loop and all attached workstation file tools migrate automatically to the mobile companion runtime."
        },
        "correct": "B",
        "explanation": "Agent systems operate under a two-axis runtime model: agent-loop location versus tool-execution location. The agent loop runs on cloud server infrastructure, so closing the laptop does not terminate the remote session. However, tools executing locally—such as folders mounted via the desktop bridge—depend on that host machine remaining online. When the laptop sleeps, cloud connectors remain operational, but bridged workstation tools disconnect.",
        "why_incorrect": {
            "A": "Losing an attached bridge is a standard runtime tool-disconnection event that the harness handles by marking the tool unavailable, not with an unrecoverable kernel crash.",
            "C": "The agent loop resides in the cloud, not on the laptop; closing the device lid does not terminate remote container execution.",
            "D": "Local workstation filesystem paths cannot magically migrate to a separate mobile operating system sandbox."
        },
        "full_justification": "Option B is correct because it correctly applies the two-axis runtime model: agent-loop location versus tool-execution location. The agent loop runs on cloud servers, so closing the laptop does not stop the session; the cloud run continues. However, tools that execute locally—such as folders mounted via the desktop bridge—depend on that host computer remaining online. When the laptop sleeps, cloud-reachable tools (Google Drive connector) remain functional, but bridged local tools vanish from the session. Option A is incorrect because tool disconnects are gracefully handled. Option C is incorrect because the agent loop resides in the cloud. Option D is incorrect because local filesystems cannot migrate to mobile devices."
    },
    {
        "id": 3,
        "question": "A paralegal at an international commercial law firm uses a cloud Cowork task to draft a comparison memo across sixty confidential client leases. To maintain strict data residency compliance, the firm's internal data policy strictly forbids transmitting confidential client files to third-party vendor cloud infrastructure. The paralegal mounts the lease folder from his workstation using the Claude Desktop bridge, believing that keeping the files on his hard drive satisfies the residency policy. Why does this deployment breach the firm's data policy?",
        "options": {
            "A": "Reading a local file through the desktop bridge transmits document contents to vendor cloud servers for processing.",
            "B": "Mounting a workstation folder automatically transfers legal intellectual property ownership to the platform vendor.",
            "C": "The desktop bridge requires disabling operating system firewall rules, exposing internal subnets to outside access.",
            "D": "Workstation filesystem caches automatically mirror mounted document text to unauthenticated public web endpoints."
        },
        "correct": "A",
        "explanation": "A bridge is an operational convenience, not a custody loophole. While the tool execution endpoint resides on the local hard drive, any file read by a cloud session is transmitted over the network and processed inside vendor cloud infrastructure. 'The file originated on my laptop' does not mean 'the file remained on my laptop.' Ingesting confidential leases into a cloud agent loop transmits data off-premises.",
        "why_incorrect": {
            "B": "Processing data through commercial enterprise AI services does not transfer legal copyright or ownership of source documents to the software vendor.",
            "C": "Desktop agent bridges communicate over encrypted outbound TLS tunnels without requiring local firewall deactivation.",
            "D": "Local desktop bridges establish authenticated client-server connections; they do not publish workstation files to public web endpoints."
        },
        "full_justification": "Option A is correct because of the core operational rule: 'A bridge is a convenience, not a custody loophole'. While the tool execution endpoint sits on the local hard drive, any file read by a cloud session is transmitted over the network and processed inside vendor cloud infrastructure. 'The file came from my laptop' does not mean 'the file stayed on my laptop'. Ingesting confidential leases into a cloud agent loop violates strict data residency bans. Option B is incorrect because processing data does not transfer intellectual property rights. Option C is incorrect because bridges use secure outbound tunnels without disabling firewalls. Option D is incorrect because bridges do not publish data publicly."
    },
    {
        "id": 4,
        "question": "An enterprise systems architect evaluates a newly released autonomous productivity tool. The product's marketing documentation highlights five key features: automated webhook triggers, deep integration with enterprise databases, autonomous multi-step problem resolution, persistent team memory, and fine-grained action approvals. When mapping these features to the universal six-part agent harness, which component is entirely omitted from the product's marketing description?",
        "options": {
            "A": "The State spine, which manages operational persistence across multi-day enterprise workflows.",
            "B": "The Reach layer, which dictates which external corporate systems and databases are accessed.",
            "C": "The Body, which defines where the agent loop and tool execution environments physically run.",
            "D": "The Human gate, which defines the operational boundary where execution pauses for sign-off."
        },
        "correct": "C",
        "explanation": "The marketing documentation covers five of the six universal harness components: automated webhook triggers = Heartbeat; database integrations = Reach; multi-step problem resolution = Run-until-done loop; persistent team memory = State spine; action approvals = Human gate. It completely omits the Body—the runtime environment specifying where the agent loop physically executes (cloud container, local machine, or hybrid) and where tools run.",
        "why_incorrect": {
            "A": "Persistent team memory explicitly satisfies the State spine component.",
            "B": "External enterprise database integration represents the Reach component.",
            "D": "Fine-grained action approvals represent the Human gate component."
        },
        "full_justification": "Option C is correct because the marketing claims explicitly map to five of the six universal harness parts: automated webhook triggers = Heartbeat; database integrations = Reach; multi-step problem resolution = Run-until-done loop; persistent team memory = State spine; and action approvals = Human gate. The description completely omits the Body—the runtime environment specifying where the agent loop actually executes (cloud sandbox, local workstation, or hybrid bridge) and where each tool runs. Option A is incorrect because persistent memory represents the State spine. Option B is incorrect because database connectors represent Reach. Option D is incorrect because approvals represent the Human gate."
    },
    {
        "id": 5,
        "question": "A wealth management advisory configures an assistant workspace to support analysts writing portfolio reviews across four institutional client accounts. The team lead must establish three persistent constraints: Constraint 1: A client-specific rule mandating that Client Alpha's portfolio reports must never recommend unhedged derivative instruments. Constraint 2: A team-wide stylistic rule requiring all deliverables to format financial figures in thousands (e.g., £'000) using British English spelling. Constraint 3: An evolving personal shorthand that an individual analyst uses when summarizing daily equity market feeds. Following the persistent context stack, how should these constraints be partitioned?",
        "options": {
            "A": "Constraint 1 in Semantic Memory; Constraint 2 in Standing Instructions; Constraint 3 in a Project workspace.",
            "B": "Constraint 1 in a Project workspace; Constraint 2 in Standing Instructions; Constraint 3 in Semantic Memory.",
            "C": "Constraint 1 in Semantic Memory; Constraint 2 in a Project workspace; Constraint 3 in Standing Instructions.",
            "D": "Constraint 1 in Standing Instructions; Constraint 2 in a Project workspace; Constraint 3 in Semantic Memory."
        },
        "correct": "B",
        "explanation": "The persistent context stack partitions knowledge by scope: 1. Constraint 1 (Client Alpha rule): Belongs in a Project workspace dedicated to Client Alpha, ensuring client boundaries do not leak into other accounts. 2. Constraint 2 (Team formatting rule): Belongs in Standing Instructions (workspace instructions) as an immutable rule applying across all team outputs. 3. Constraint 3 (Personal shorthand): Belongs in Semantic Memory, where individual user habits and evolving preferences persist dynamically.",
        "why_incorrect": {
            "A": "Placing a single client's investment restrictions into general Semantic Memory risks cross-client data contamination across unrelated accounts.",
            "C": "Scrambles the persistence layers, placing global formatting rules into a single project workspace while placing client rules in user memory.",
            "D": "Global Standing Instructions should never contain account-specific portfolio restrictions that apply to only one institutional client."
        },
        "full_justification": "Option B is correct because it correctly partitions knowledge across the persistent context stack: 1. Constraint 1 (Client Alpha restriction): Belongs in a Project workspace dedicated to Client Alpha, ensuring client-specific boundaries do not leak into other accounts. 2. Constraint 2 (Team formatting rule): Belongs in Standing Instructions because it is a stable rule that applies across all workstreams. 3. Constraint 3 (Personal shorthand): Belongs in Semantic Memory, where individual user preferences and evolving personal working habits are maintained dynamically across sessions. Option A is incorrect because client restrictions in Semantic Memory leak across accounts. Option C is incorrect because it scrambles workspace and global scopes. Option D is incorrect because client-specific rules do not belong in global instructions."
    },
    {
        "id": 6,
        "question": "An equity research analyst maintains a dedicated Project workspace named 'Biotech Mergers' on Claude Cowork. She also conducts ad-hoc industry research in regular Claude chat sessions and occasionally runs a local Cowork session on her desktop. With the introduction of cross-surface semantic memory, how do memory updates propagate across these working environments? (Select TWO.)",
        "options": {
            "A": "Facts learned in general Claude chat sessions are accessible to cloud Cowork tasks where memory is activated.",
            "B": "Preferences recorded during cloud Cowork tasks are automatically applied to local desktop Cowork sessions.",
            "C": "Modifying global memory topics in Claude chat permanently purges historical files stored in cloud Projects.",
            "D": "Memory accumulated inside the 'Biotech Mergers' Project workspace remains strictly quarantined to that Project."
        },
        "correct": "A and D",
        "explanation": "Cross-surface semantic memory operates under two foundational architectural rules: 1. Shared Cloud Memory: Cloud Cowork tasks share the same semantic memory layer used by standard Claude chat sessions, allowing verified user preferences and factual context to transfer seamlessly between chat and cloud tasks. 2. Project Boundary Quarantine: Memory created inside a Project workspace stays quarantined within that specific Project to prevent confidential context leakage across disparate engagements.",
        "why_incorrect": {
            "B": "Local desktop Cowork sessions operate on an isolated local runtime architecture and do not inherit or synchronize with cloud semantic memory.",
            "C": "Modifying or clearing a semantic memory topic does not delete underlying reference documents uploaded into Project knowledge repositories."
        },
        "full_justification": "Options A and D are correct because they reflect cross-surface memory architecture: (A) cloud Cowork tasks share semantic memory with standard Claude chat, allowing learned facts and preferences to inform cloud tasks; and (D) memory accumulated inside a specific Project workspace remains quarantined within that Project to prevent confidential data leakage across engagements. Option B is incorrect because local desktop Cowork sessions maintain an isolated local architecture and do not synchronize cloud semantic memory. Option C is incorrect because updating memory topics does not delete underlying files stored in Project knowledge repositories."
    },
    {
        "id": 7,
        "question": "A clinical research coordinator uses an autonomous web agent to perform a multi-variable statistical extraction across 400 patient trial records. During the four-hour unattended run, the agent writes intermediate data frames, temporary CSV calculations, and preliminary demographic distributions to its temporary task filesystem (Tier 1). The agent completes the calculations and posts a final summary paragraph in the session thread, but does not export the underlying CSV files. What is the operational status of the intermediate calculation files?",
        "options": {
            "A": "They remain permanently accessible to desktop applications via the encrypted operating system browser cache.",
            "B": "They are automatically converted into immutable markdown artifacts that persist across all future chat runs.",
            "C": "They are archived permanently in the organization's enterprise cloud storage bucket under the user's account.",
            "D": "They are temporary scratch assets that will be wiped upon task termination, leaving the data irrecoverable."
        },
        "correct": "D",
        "explanation": "Tier 1 (the task filesystem) is an ephemeral, isolated container provisioned on vendor servers solely for the duration of an active run. By definition, Tier 1 is scratch space; it is completely wiped when the task finishes. Intermediate data frames and CSVs that are not explicitly exported to Tier 2 (platform storage) or Tier 3 (the exit) are permanently destroyed.",
        "why_incorrect": {
            "A": "Remote cloud container filesystems do not persist into local client desktop caches or operating system storage.",
            "B": "Intermediate calculation files and scratchpad data do not convert into persistent user-facing artifacts unless explicitly commanded in the brief.",
            "C": "Temporary task filesystems are not automatically preserved or archived in enterprise account storage buckets."
        },
        "full_justification": "Option D is correct because Tier 1 (the task filesystem) is strictly a temporary, isolated working environment provisioned on vendor servers solely for the duration of the run. By definition, Tier 1 is scratch space; it is cleaned up and wiped when the task finishes. Intermediate files that are not deliberately exported to Tier 2 (platform storage) or Tier 3 (the exit) are permanently lost. Option A is incorrect because remote container files do not mirror to local caches. Option B is incorrect because scratch files do not convert into persistent artifacts automatically. Option C is incorrect because task filesystems are not archived to enterprise buckets."
    },
    {
        "id": 8,
        "question": "A corporate restructuring advisor uses a managed agent surface to synthesize confidential creditor claims into an interactive visual dashboard. Upon completion, the advisor emails the vendor-hosted platform sharing link directly to the client's board of directors, without downloading the underlying dataset or exporting the dashboard. Which two operational liabilities does this practice introduce? (Select TWO.)",
        "options": {
            "A": "The foundation model provider assumes legal professional indemnity liability for financial discrepancies displayed in the link.",
            "B": "The firm's official matter repository contains a records gap because the deliverable remains exclusively in Tier 2 platform storage.",
            "C": "Client access and document retention are governed by the third-party vendor's platform rules rather than internal firm policies.",
            "D": "Distributing an interactive platform sharing link automatically converts the advisor's private workspace into a public web server."
        },
        "correct": "B and C",
        "explanation": "Distributing vendor platform links rather than institutional exports violates core data custody principles: 1. System-of-Record Gap: Deliverables retained only in Tier 2 (platform storage) exist on vendor infrastructure; the advisory firm's official document repository lacks an auditable record because the asset was never exited into institutional custody. 2. Governance Loss: Shared links depend on vendor retention lifecycles, authentication regimes, and platform policies, preventing the firm from enforcing its own legal hold, access revocation, or retention rules.",
        "why_incorrect": {
            "A": "Commercial AI platform vendors explicitly disclaim all professional advisory and indemnity liabilities in their terms of service.",
            "D": "Generating a platform sharing URL creates an authenticated platform access link; it does not convert the private workspace into an open web server."
        },
        "full_justification": "Options B and C are correct because sharing platform links violates fundamental data custody discipline: (B) deliverables left in Tier 2 (platform storage) leave a records gap in the firm's official system of record because the asset was never exited into institutional custody; and (C) access and retention are governed by third-party vendor platform rules rather than internal organizational compliance policies. Option A is incorrect because platform providers explicitly disclaim professional liability. Option D is incorrect because authenticated platform links do not convert workspaces into open public web servers."
    },
    {
        "id": 9,
        "question": "An operations manager at a renewable energy supplier configures an autonomous agent to execute weekly supplier invoice reconciliation. The prompt instructs the agent to parse utility meter feeds, match kilowatt charges against contractual wholesale tariffs, and flag billing discrepancies. To enforce rigorous file custody discipline, which terminal instruction must be appended to the work brief?",
        "options": {
            "A": "Format all identified tariff discrepancies as an interactive HTML canvas and email the active session URL to the corporate finance desk.",
            "B": "Ensure that the agent loop and all financial data calculation scripts execute exclusively within temporary task container memory buffers.",
            "C": "List every file created and ensure finished reconciliation deliverables exit to our enterprise Drive folder rather than staying on platform.",
            "D": "Store all intermediate calculation scratchpads in cloud platform storage to enable cross-session context retrieval during next month's run."
        },
        "correct": "C",
        "explanation": "The course establishes a strict file custody mandate: 'Finished work exits the platform. Everything else may stay.' Mandating that the agent list every file created and explicitly save finished reconciliation deliverables to an enterprise Google Drive folder moves the asset into Tier 3 (the exit), ensuring it resides within corporate custody where retention, compliance, and auditing apply.",
        "why_incorrect": {
            "A": "Emailing a platform URL leaves the deliverable in Tier 2 platform storage under vendor custody rather than exiting into institutional systems.",
            "B": "While calculations run in container memory, leaving deliverables trapped in temporary container memory causes them to be wiped upon task termination.",
            "D": "Intermediate calculations are scratch assets that belong in Tier 1; saving scratchpads to Tier 2 platform storage clutters project context unnecessarily."
        },
        "full_justification": "Option C is correct because it operationalizes the core custody mandate: 'Finished work exits the platform. Everything else may stay'. Mandating that the agent list every file created and explicitly save finished reconciliation files to enterprise Google Drive moves the asset into Tier 3 (the exit), placing it inside the firm's system of record where corporate retention, access, and auditing apply. Option A is incorrect because keeping deliverables on platform URLs leaves them under vendor custody. Option B is incorrect because deliverables trapped in container memory are destroyed upon task completion. Option D is incorrect because storing intermediate scratchpads clutters project storage."
    },
    {
        "id": 10,
        "question": "An IT consultancy establishes an automation standard for client engagements across competing foundation model platforms. The engagement lead insists that operational guidelines, formatting standards, and verification rules must be documented in a portable, user-owned context file (such as CLAUDE.md or a root markdown file) rather than relying exclusively on vendor-managed platform memory and project instruction fields. What primary risk does this engineering practice mitigate?",
        "options": {
            "A": "High switching costs and deep operational dependencies resulting from vendor platform lock-in.",
            "B": "Security vulnerabilities emerging from the execution of untrusted third-party Python scripts.",
            "C": "Context window saturation caused by ingesting structured markdown tables during session start.",
            "D": "Compliance violations resulting from the omission of business associate agreements under HIPAA."
        },
        "correct": "A",
        "explanation": "Relying exclusively on proprietary platform memory, closed project instruction consoles, and vendor session stores creates severe switching costs and vendor lock-in. Documenting operational constraints, behavioral rules, and formatting standards in portable, user-owned markdown context files (e.g., CLAUDE.md) allows workflows to be re-platformed across tools without losing institutional knowledge.",
        "why_incorrect": {
            "B": "User-owned context files contain declarative text instructions; they do not execute untrusted binary scripts or patch runtime vulnerabilities.",
            "C": "Structured markdown files consume negligible context tokens and do not saturate modern large context windows.",
            "D": "HIPAA compliance is governed by institutional legal agreements (BAAs) and security architecture, not by file storage formats."
        },
        "full_justification": "Option A is correct because relying exclusively on vendor-managed persistence stacks (proprietary session histories, cloud memory topics, and project instruction consoles) creates severe switching cost and platform lock-in. If an organization maintains its core procedural methods, behavioral rules, and business constraints in portable, user-owned context files (like CLAUDE.md or plain markdown files), moving workflows across competing tools becomes a straightforward re-platforming exercise. Option B is incorrect because text files do not execute untrusted scripts. Option C is incorrect because lightweight markdown files consume minimal tokens. Option D is incorrect because HIPAA compliance requires legal BAAs."
    }
]
