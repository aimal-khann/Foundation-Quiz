# scripts/build_chapter3_part2.py
# Questions 11 to 20 for Chapter 3

questions_11_to_20 = [
  {
    "id": 11,
    "question": "An operations director at a regional healthcare cooperative reviews a delegation map for the patient intake scheduling workflow. The map was drafted six months ago and names the entire patient-access committee as the collective authority for workflow integrity. Although no clinical incidents have been reported, booking dispute backlogs have steadily increased. What governance failure caused this control framework to decay?",
    "options": {
      "A": "The committee neglected to mandate that intake coordinators clear local browser cookies across daily shifts.",
      "B": "The delegation map lacked a single named individual owner answerable for matching documented steps to reality.",
      "C": "The clinic failed to deploy an autonomous scheduling agent equipped with real-time electronic health connectors.",
      "D": "The foundation model provider updated its core system prompt, causing the underlying model weights to drift."
    },
    "correct": "B",
    "explanation": "Option B succeeds because a delegation map decays silently without alarms; review gates turn into glances, and documents diverge from reality. The foundational safeguard against this decay is naming a single, accountable map owner (one individual, not a broad committee) and setting a fixed scheduled read date. Assigning collective authority to a committee ensures that no specific individual is answerable for auditing the map against daily clinical practice.",
    "why_incorrect": {
      "A": "Clearing browser cookies and cache manages temporary local session state, but provides zero organizational governance over process ownership or workflow step fidelity.",
      "C": "Deploying autonomous scheduling agents introduces technical complexity that magnifies governance risks when basic procedural accountability has not been established.",
      "D": "Platform system prompt updates can alter model behavior, but do not explain gradual operational divergence and growing administrative dispute backlogs among human coordinators."
    },
    "full_justification": "Option B succeeds because workflow governance requires a single accountable individual owner to conduct scheduled map reads and maintain alignment between documented controls and operational practice. Option A is incorrect because clearing browser cache manages client state rather than process governance. Option C is incorrect because deploying autonomous agents without process ownership accelerates operational decay. Option D is incorrect because vendor model updates do not drive team-level administrative divergence."
  },
  {
    "id": 12,
    "question": "A compliance supervisor conducts a scheduled quarterly review of an insurance underwriting delegation map. The map classifies the risk-tier scoring step as collaborative, listing a senior underwriter as the reviewer. Which audit question provides the most reliable empirical evidence of whether this collaborative gate remains genuinely operational?",
    "options": {
      "A": "\"Does the underwriting policy manual still mandate senior review for risk-tier scores prior to policy issuance?\"",
      "B": "\"Has the underwriting team completed the annual enterprise educational webinar covering artificial intelligence?\"",
      "C": "\"Who reviewed the flagged risk-tier scores last week, and how many minutes did they spend inspecting each file?\"",
      "D": "\"What did the prompt-engineering logs indicate regarding underwriter conversational satisfaction over the quarter?\""
    },
    "correct": "C",
    "explanation": "Option C succeeds because the defining question of a scheduled map read is: For every collaborative step: who reviewed it last week, and how long did they spend? Asking about concrete historical reality (\"last week\") uncovers whether the gate is genuinely staffed or has degraded into an empty, rubber-stamped glance. If nobody can name the reviewer or the time spent, the step has become automated in practice regardless of what documentation claims.",
    "why_incorrect": {
      "A": "Checking the policy manual only verifies what the organization designed or intended on paper, rather than what is actually occurring on the operational floor.",
      "B": "Training attendance records confirm educational compliance, but fail to provide empirical evidence of active gate execution.",
      "D": "Prompt engineering logs and conversational satisfaction metrics track user sentiment, not factual compliance verification at a risk gate."
    },
    "full_justification": "Option C succeeds because auditing collaborative gates requires examining empirical evidence from recent operational cycles to verify that designated human reviewers actively scrutinize outputs rather than rubber-stamping them. Option A is incorrect because policy manuals reflect intended standards rather than live operational adherence. Option B is incorrect because training completion does not prove gate enforcement. Option D is incorrect because user satisfaction does not establish gate diligence."
  },
  {
    "id": 13,
    "question": "A business intelligence analyst builds an internal analytics tool using a prompt-and-iterate cycle (ideate, prototype, feedback, refine). She executes Cycle 1 in a temporary chat, Cycle 2 in a desktop text editor, and Cycle 3 in a different departmental chat workspace. Although individual responses look promising, the final prototype produces conflicting metrics that fail to integrate. What operational mistake corrupted the build loop?",
    "options": {
      "A": "Scattering iterative cycles across isolated environments instead of running the loop in a unified workspace.",
      "B": "Neglecting to author Python unit testing scripts before prompting the model for interactive chart components.",
      "C": "Attempting to prototype visual dashboards without provisioning authenticated cloud-hosted database pipelines.",
      "D": "Selecting a commercial frontier model rather than pre-training a specialized domain-specific neural network."
    },
    "correct": "A",
    "explanation": "Option A succeeds because the build loop (ideate, prototype, feedback, refine) must run inside a stable workspace (such as a Project) so that background assumptions, constraints, and prior refinements remain grounded. Scattering rounds across ad-hoc chats, local text files, and separate workspaces forces each cycle to restart from a slightly different context, resulting in a fragmented pile of incompatible drafts rather than a coherent tool.",
    "why_incorrect": {
      "B": "The rapid build loop utilizes conversational prototyping and artifacts to explore requirements before committing to formal code unit tests.",
      "C": "Web artifacts are designed as lightweight, self-contained prototypes; requiring live database connections defeats their primary purpose as rapid, low-friction sandboxes.",
      "D": "Standard commercial foundation models are fully capable of generating functional prototypes; fine-tuning a custom network is an expensive, unnecessary detour."
    },
    "full_justification": "Option A succeeds because maintaining build loop integrity requires preserving contextual continuity across iterations within a dedicated Project workspace. Option B is incorrect because formal unit test authoring belongs in production engineering rather than preliminary prototyping. Option C is incorrect because rapid prototyping uses mock datasets rather than live production pipelines. Option D is incorrect because proprietary pre-training is completely unneeded for dashboard prototyping."
  },
  {
    "id": 14,
    "question": "A financial planning associate asks an assistant to draft a quarterly operating budget forecast. The prompt instructs: \"Analyse historical departmental travel expenses from the attached spreadsheet, calculate the compound quarterly growth rate, and recommend a department spending ceiling in your written report.\" The assistant returns an executive memorandum containing a recommended £45,000 ceiling supported by detailed written narrative calculations. What structural flaw undermines this deliverable?",
    "options": {
      "A": "The prompt failed to specify whether the spending threshold should be formatted in euros or British pounds.",
      "B": "The associate omitted few-shot demonstration exemplars illustrating approved financial budget narratives.",
      "C": "Large language models lack the baseline cognitive capability required to interpret corporate travel logs.",
      "D": "The compound growth figures were generated as prose text rather than calculated through code execution."
    },
    "correct": "D",
    "explanation": "Option D succeeds because of the foundational planning maxim: If a result matters, compute it. Never write it. Large language models can perform arithmetic, but a generated prose figure and a calculated figure look identical on the page. Whenever financial ceilings or critical metrics govern a plan, the calculation must be executed via code execution to ensure auditable, deterministic computation rather than statistical prose generation.",
    "why_incorrect": {
      "A": "Currency formatting is a superficial presentation detail; the structural defect is writing a mathematical calculation in text rather than executing code.",
      "B": "Adding few-shot exemplars improves narrative styling, but does not solve the underlying risk of prose-generated mathematical hallucinations.",
      "C": "LLMs routinely parse structured financial logs; the limitation lies in syntactic math generation versus deterministic computation."
    },
    "full_justification": "Option D succeeds because generating critical financial figures in prose produces unverified token predictions rather than deterministic computational calculations. Option A is incorrect because currency formatting does not address mathematical validity. Option B is incorrect because stylistic few-shot examples do not eliminate calculation hallucinations. Option C is incorrect because language models can structure spreadsheet data effectively."
  },
  {
    "id": 15,
    "question": "An operations team uses an assistant to build a web artifact that visualizes daily shipping container throughput across three port terminals. During Cycle 1, the assistant generates a clean dashboard with three interactive bar charts. During Cycle 2, the team requests a terminal comparison filter and a grand total volume summary. The deliverable arrives with elegant styling, functional interactive buttons, and correctly rendered figures; however, an audit reveals the grand total figure is understated by 15%. Why did this failure evade detection during preliminary testing?",
    "options": {
      "A": "The assistant suffered total context amnesia caused by processing excessive visual CSS styling directives.",
      "B": "Plausible, well-formatted prose numbers carry no visual signature of arithmetic fabrication on the page.",
      "C": "Interactive web artifacts automatically strip numerical calculation formulas from the chat interface view.",
      "D": "The underlying client browser engine dropped floating-point precision during front-end canvas rendering."
    },
    "correct": "B",
    "explanation": "Option B succeeds because Cycle 2 represents the classic silent failure mode in a build loop. Unlike code syntax bugs that crash visibly with error messages, written-not-computed figures fail with zero noise. The output appeared polished, well-formatted, and completely plausible, allowing a material 15% arithmetic error to pass superficial inspection unnoticed.",
    "why_incorrect": {
      "A": "Context window exhaustion causes amnesia, truncated code, or broken syntax, not a beautifully styled dashboard with subtle calculation drift.",
      "C": "Interactive artifacts execute client-side scripts; they do not automatically strip or alter underlying mathematical formulas.",
      "D": "Modern web rendering engines do not arbitrarily lose floating-point precision on basic summation; the error was generated by the language model drafting text."
    },
    "full_justification": "Option B succeeds because prose-generated mathematical errors produce visually flawless, plausible deliverables that exhibit zero apparent defects, easily evading casual inspection. Option A is incorrect because token exhaustion creates visible code breakage rather than refined visual dashboards. Option C is incorrect because artifacts execute JavaScript faithfully without formula stripping. Option D is incorrect because client browser rendering engines do not introduce double-digit arithmetic summation drift."
  },
  {
    "id": 16,
    "question": "An analyst builds a lightweight web artifact that tracks software licence renewal deadlines across twenty internal business units. Over eight months, four separate corporate departments begin opening the tool daily, and the chief information officer relies on its exported renewal calendar for executive vendor renegotiations. What operational milestone has this tool reached?",
    "options": {
      "A": "It has suffered from stale configuration, requiring project knowledge files to be scrubbed of expired terms.",
      "B": "It has encountered an expectation mismatch that warrants immediate parameter tuning across model endpoints.",
      "C": "It has triggered the escalation signal, outgrowing prompt-and-iterate into formal engineered infrastructure.",
      "D": "It has experienced halo delegation, requiring all tabular schedules to be converted back into text prompts."
    },
    "correct": "C",
    "explanation": "Option C succeeds because dependency is the escalation signal. The moment multiple outside departments and executive leaders begin relying on an ad-hoc prompt artifact as production infrastructure, the tool has outgrown prompt-and-iterate. It now demands software engineering controls: guaranteed uptime, robust access permissions, formal change management, and dedicated maintenance support.",
    "why_incorrect": {
      "A": "Stale configuration refers to out-of-date instructions or reference files, which is not the issue when an operational tool experiences widespread user adoption.",
      "B": "An expectation mismatch occurs when a user asks a model to perform an impossible task, not when a successful tool expands in usage.",
      "D": "Halo delegation is an error in step assignment (giving AI approval authority because its drafting was good), not the operational scaling of an artifact."
    },
    "full_justification": "Option C succeeds because multi-department operational dependency serves as the explicit milestone requiring an ad-hoc artifact to transition into engineered enterprise software. Option A is incorrect because organizational adoption does not signify knowledge base expiration. Option B is incorrect because widespread utility contradicts expectation mismatch. Option D is incorrect because halo delegation concerns improper step authority transfer."
  },
  {
    "id": 17,
    "question": "A systems architect evaluates two AI-assisted workflows within a pharmaceutical manufacturing plant to determine where software engineering resources must be allocated. Workflow Alpha: An internal research scientist has manually prompted an assistant four times using an identical data transformation sequence to format assay logs. Workflow Beta: Three clinical quality assurance teams now rely on an ad-hoc dashboard artifact as their daily operational clearinghouse for batch release milestones. How should the architect triage these systems under operational escalation standards?",
    "options": {
      "A": "Treat Alpha as stable worker manufacturing, and escalate Beta to enterprise engineering due to dependency.",
      "B": "Reclaim Alpha for manual human calculation, and convert Beta into an unmonitored desktop client task Skill.",
      "C": "Terminate both workflows immediately because custom artifacts violate pharmaceutical data integrity rules.",
      "D": "Escalate Alpha to enterprise engineering for custom code; leave Beta within the prompt-and-iterate loop."
    },
    "correct": "A",
    "explanation": "Option A succeeds because the curriculum draws a strict boundary between two signals: 1. I have solved this the same way three times (Workflow Alpha) means the workflow shape is stable and can be standardized into a configured worker/Skill. 2. Other people now depend on this (Workflow Beta) means the tool has become infrastructure and must be escalated to professional software engineering.",
    "why_incorrect": {
      "B": "Reclaiming Alpha wastes human time on a stable, delegable pattern, while turning Beta into an unmonitored Skill ignores the infrastructure risk of multi-team dependency.",
      "C": "Lightweight artifacts are fully valid for rapid prototyping; they simply require escalation once they cross into mission-critical infrastructure.",
      "D": "It reverses the escalation signal: solving an assay transformation repeatedly calls for configuration/Skills, whereas enterprise dependency demands formal engineering."
    },
    "full_justification": "Option A succeeds because repeatedly executing an established sequence calls for worker configuration, whereas external team dependency demands professional engineering hardening. Option B is incorrect because delegable tasks should be configured rather than manually reclaimed, and critical dashboards require governance. Option C is incorrect because rapid prototyping is legitimate prior to hardening. Option D is incorrect because it completely inverts escalation criteria."
  },
  {
    "id": 18,
    "question": "A legal operations manager constructs a delegation map for reviewing non-disclosure agreements. She comes to the step: \"Calculate liquidated damages exposure under the multi-tier breach penalty clause.\" A paralegal recommends: \"Because this requires exact mathematics, it should be carried by code execution, which makes it safe to assign this step as AI-appropriate without human review.\" Which two foundational workflow principles did the paralegal violate? (Select TWO.)",
    "options": {
      "A": "Ignoring that damages calculations are statutory legal duties that cannot be executed in code sandboxes.",
      "B": "Overlooking that sandboxed code execution environments are restricted exclusively to software developers.",
      "C": "Conflating the implementation layer with the governance criteria of Reversibility, Stakes, and Account.",
      "D": "Assuming that running arithmetic via code execution eliminates the requirement for human verification gates."
    },
    "correct": "C and D",
    "explanation": "Options C and D succeed because: 1. Layer separation: The three mapping layers must remain strictly sequential: Eligibility, Ownership, and Implementation. \"Carried by code execution\" is an implementation choice; it is never an ownership criterion and cannot justify making a step AI-appropriate. 2. Downstream gates: Running arithmetic in a sandbox ensures calculation precision, but the code can still reference the wrong data column or misapply a legal threshold. Delegating a high-stakes liability calculation to AI is safe only if an explicit human review gate immediately inspects the output.",
    "why_incorrect": {
      "A": "Arithmetic modeling and damages estimation are routine computational support tasks that software tools and sandboxes legitimately execute.",
      "B": "Code execution features are broadly available across modern commercial analyst tiers, not restricted exclusively to software development engineers."
    },
    "full_justification": "Options C and D succeed because technical implementation tools (code execution) must not be confused with governance ownership criteria, and automated calculation precision never eliminates human verification gates for contractual liabilities. Option A is incorrect because computational assistance in contract analysis is routine and permissible. Option B is incorrect because code execution tools are accessible across standard enterprise roles."
  },
  {
    "id": 19,
    "question": "A mortgage brokerage firm drafts a delegation map for processing residential loan applications. The compliance officer reviews four proposed descriptions for the step: \"Verify borrower declared bonus income against employer tax filings.\" Which description correctly formulates a robust, auditable review gate?",
    "options": {
      "A": "\"Step 4: Checked thoroughly by a senior underwriting officer whenever income discrepancies appear elevated.\"",
      "B": "\"Step 4: Managed collaboratively using an advanced reasoning model to verify borrower credit affordability.\"",
      "C": "\"Step 4: Inspected by the credit assessment team with appropriate professional diligence prior to loan offer.\"",
      "D": "\"Step 4: Reviewed by Sarah Jenkins (Senior Underwriter), before loan sanction, checking tax figures match W2.\""
    },
    "correct": "D",
    "explanation": "Option D succeeds because a properly designed review gate cannot simply say \"a human looks at it\". To prevent the gate from decaying into an unstaffed pass-through, the delegation map must establish three explicit components: a named person (Sarah Jenkins), a named moment (before loan sanction), and a named thing being checked (tax figures match W2).",
    "why_incorrect": {
      "A": "\"Whenever income discrepancies appear elevated\" creates an unstaffed default condition where ordinary or subtle errors pass through completely unreviewed.",
      "B": "Using an advanced model does not constitute a human review gate; collaborative steps require an accountable human reviewer, not another automated pass.",
      "C": "Assigning review to an anonymous \"credit assessment team\" under vague \"professional diligence\" lacks individual accountability and specific inspection criteria."
    },
    "full_justification": "Option D succeeds because a verifiable control gate must specify a named individual owner, a fixed chronological checkpoint, and explicit evidentiary criteria. Option A is incorrect because conditional triggers allow non-obvious discrepancies to bypass review. Option B is incorrect because automated models cannot serve as human accountability gates. Option C is incorrect because collective committee assignments diffuse personal accountability."
  },
  {
    "id": 20,
    "question": "A fleet management company tasks an assistant with drafting an annual vehicle replacement schedule. The assistant is supplied with five years of telemetry data, depreciation schedules, maintenance logs, and fuel expense reports. The assistant produces an optimized replacement roster recommending that forty diesel vans be replaced with electric utility vans in November. The fleet director rejects the output because the board had decided during a private executive retreat to freeze all capital expenditure until Q2 of next year. Why did this strategic planning step fail?",
    "options": {
      "A": "The prompt failed to run within an isolated code sandbox to calculate precise commercial vehicle depreciation.",
      "B": "The assistant faced a judgment step governed by strategic constraints that sat outside the context window.",
      "C": "The historical telemetry dataset was corrupted by uncleaned maintenance records from regional depot shops.",
      "D": "The model lacked parametric reasoning capability required to balance commercial amortisation curves properly."
    },
    "correct": "B",
    "explanation": "Option B succeeds because of the window test: Could I put everything this step needs into the context window? If not, the step is mine. Strategic fleet decisions depend on inaccessible inputs: private board retreats, confidential capital expenditure freezes, and unrecorded risk appetites. Because these judgment inputs sat outside the window, the model did not refuse; it generated a plausible, optimized plan that was entirely useless.",
    "why_incorrect": {
      "A": "Executing code sandboxes ensures mathematical accuracy, but cannot grant an assistant access to unrecorded board decisions made behind closed doors.",
      "C": "The failure was not caused by corrupted vehicle telemetry; the historical data analysis was structurally sound, but blind to private corporate strategy.",
      "D": "Modern foundation models easily compute vehicle depreciation and amortisation schedules; the breakdown was strategic, not mathematical."
    },
    "full_justification": "Option B succeeds because strategic planning tasks fail the context window test when critical decision constraints—such as confidential board deliberations and unrecorded capital freezes—cannot be placed in context. Option A is incorrect because sandbox calculation does not resolve missing strategic constraints. Option C is incorrect because the quantitative telemetry analysis was accurate. Option D is incorrect because foundation models handle vehicle amortisation logic proficiently."
  }
]
