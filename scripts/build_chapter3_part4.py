# scripts/build_chapter3_part4.py
# Questions 31 to 40 for Chapter 3

questions_31_to_40 = [
  {
    "id": 31,
    "question": "An operations analyst at an asset management firm identifies three recurring corrections required in their team's monthly portfolio reporting workflow: Correction 1: Always highlight emerging market equity holdings exceeding a 5% allocation threshold in bold red font. Correction 2: Incorporate the firm’s statutory regulatory disclosure appendix and approved terminology glossary. Correction 3: Execute the five-stage monthly data rebalancing sequence in exact chronological order. How should these three operational improvements be allocated to ensure they persist across the entire team?",
    "options": {
      "A": "Correction 1 in Standing Instructions; Correction 2 in the Knowledge Base; Correction 3 in a Skill.",
      "B": "Correction 1 in a Skill; Correction 2 in Standing Instructions; Correction 3 in the Knowledge Base.",
      "C": "Correction 1 in Standing Instructions; Correction 2 in a Skill; Correction 3 in the Knowledge Base.",
      "D": "Correction 1 in the Knowledge Base; Correction 2 in a Skill; Correction 3 in Standing Instructions."
    },
    "correct": "A",
    "explanation": "Option A succeeds because it precisely applies the rule, reference, or procedure test to assign fixes to their appropriate configuration homes: 1. Rules go to Standing Instructions: Highlighting emerging market equities exceeding 5% in bold red is an immutable behavioral constraint that must govern every run in the workspace. 2. References go to the Knowledge Base: Regulatory appendices and glossaries represent static source text that the model must read and consult. 3. Procedures go to Skills: The five-stage data rebalancing sequence represents an ordered, step-by-step operational workflow that must execute identically every time.",
    "why_incorrect": {
      "B": "It misfiles an immutable formatting rule into a procedural Skill and places an executable multi-step sequence into a static reference folder.",
      "C": "It treats static reference glossaries as an executable Skill while burying ordered procedural sequences in static reference documentation.",
      "D": "It buries behavioral formatting constraints inside reference documents where they fail to govern generation, and confuses procedures with standing rules."
    },
    "full_justification": "Option A succeeds because the persistence triad assigns behavioral constraints to Standing Instructions, static source text to the Knowledge Base, and ordered execution sequences to Skills. Option B is incorrect because rules belong in instructions and procedures belong in skills. Option C is incorrect because glossaries are references, not skills. Option D is incorrect because knowledge bases do not enforce formatting rules."
  },
  {
    "id": 32,
    "question": "A paralegal discovers that the assistant consistently omits mandatory dispute escalation steps when summarizing vendor supplier claims. To ensure this fix lasts, she types: \"Follow our four-tier vendor dispute escalation sequence\" into the Project's standing instructions. Two weeks later, colleagues observe that while the assistant acknowledges the existence of the dispute sequence, it routinely skips step two and reorders steps three and four. What configuration error caused this breakdown?",
    "options": {
      "A": "The standing instruction directly conflicted with the platform's core content safety filters.",
      "B": "Static reference text was injected into standing instructions, causing prompt attention loss.",
      "C": "A multi-step procedure was misfiled as an abstract one-line rule, losing its execution steps.",
      "D": "The paralegal neglected to provision code sandboxes to process the complex dispute hierarchy."
    },
    "correct": "C",
    "explanation": "Option C succeeds because a procedure is an ordered sequence of steps. When a multi-step procedure is compressed into a one-line standing instruction (\"Follow our four-tier sequence\"), the model receives an abstract rule without the underlying procedural scaffold, causing it to skip or reorder steps. Procedures belong in Skills, where the step-by-step sequence is permanently structured and executed consistently.",
    "why_incorrect": {
      "A": "Commercial dispute escalation protocols do not violate foundation model safety filters.",
      "B": "The paralegal did not upload a bloated reference document into the instructions; she typed a terse, underspecified directive.",
      "D": "Text-based dispute classification and procedural routing do not require mathematical sandbox execution."
    },
    "full_justification": "Option C succeeds because procedural workflows require step-by-step execution scaffolding (Skills); compressing an ordered sequence into a one-line rule causes the model to hallucinate or scramble steps. Option A is incorrect because dispute protocols do not trigger content safety filters. Option B is incorrect because the issue was procedural brevity, not document bloat. Option D is incorrect because qualitative classification does not require sandbox code execution."
  },
  {
    "id": 33,
    "question": "A corporate advisory group operates six dedicated Project workspaces representing distinct industrial client sectors. The compliance director approves an updated statutory ESG reporting framework containing a rigorous five-step extraction sequence that every sector team must follow identically. How should the enterprise architect deploy this procedure to ensure single-point maintenance across all six workspaces?",
    "options": {
      "A": "Upload the statutory framework text into each workspace local Project knowledge base folder.",
      "B": "Deploy the extraction procedure as an account-level Skill available across enterprise sites.",
      "C": "Paste the complete procedure into standing instructions across all six Project workspaces.",
      "D": "Direct individual analysts to enable personal conversational memory toggles on desktop apps."
    },
    "correct": "B",
    "explanation": "Option B succeeds because of the architectural scope of configuration homes: Knowledge bases and Standing Instructions reside at the Project level, whereas Skills sit at the account level. When a repeatable, multi-step procedure must run identically across multiple independent Project workspaces, deploying it as an account-level Skill enables centralized management; a single update propagates across all six workspaces immediately.",
    "why_incorrect": {
      "A": "Uploading a procedure into Project Knowledge stores it as reference text rather than an executable sequence, and duplicates storage across six folders.",
      "C": "Duplicating standing instructions across six workspaces creates configuration divergence, requiring six separate manual edits whenever the ESG framework changes.",
      "D": "Personal memory is client-specific and unshared, preventing standardized team-wide compliance."
    },
    "full_justification": "Option B succeeds because account-level Skills provide a shared, centralized procedural home that executes consistently across multiple independent Project workspaces without duplicate configuration maintenance. Option A is incorrect because knowledge bases store reference reading material rather than executable sequences. Option C is incorrect because manual duplication causes configuration drift. Option D is incorrect because conversational memory is isolated per user."
  },
  {
    "id": 34,
    "question": "A senior financial analyst notices that Claude regularly remembers his preference for displaying currency values in thousands (e.g., £'000) and applying British accounting spelling across chats. Relying on this automated adaptation, he assumes the department's financial reporting workflow is stabilized. When he takes medical leave, his replacement generates reports containing unformatted numbers and Americanized terminology, triggering client complaints. Why is native conversational memory an inadequate substitute for formal configuration? (Select TWO.)",
    "options": {
      "A": "Conversational memory is technically barred from storing formatting rules or conventions.",
      "B": "Conversational memory is strictly user-specific and cannot transfer preferences to peers.",
      "C": "Conversational memory functions opportunistically and cannot be inspected or audit-proven.",
      "D": "Enabling conversational memory automatically invalidates standing reference project files."
    },
    "correct": "B and C",
    "explanation": "Options B and C succeed because conversational memory cannot substitute for auditable configuration: 1. Per-user isolation: Memory is tied to an individual user's account profile. Whatever an assistant learns about one analyst's preferences remains locked to that user; a colleague covering their desk starts from scratch. 2. Best-effort unreliability: Conversational memory is opportunistic and opaque. It cannot be formally inspected, version-controlled, verified, or handed to an auditor as a binding operational standard. Shared configuration (Projects, Instructions, Skills) provides a stable, transparent home accessible to the entire team.",
    "why_incorrect": {
      "A": "Memory features can store formatting preferences; the failure is that they are stored informally, unreliably, and privately.",
      "D": "Enabling conversational memory does not delete or disable Project Knowledge assets."
    },
    "full_justification": "Options B and C succeed because conversational memory is private to an individual user profile (preventing handover to colleagues) and operates on an opaque, unversioned, best-effort basis unsuitable for compliance auditing. Option A is incorrect because conversational memory frequently records user styling habits. Option D is incorrect because enabling memory does not affect project reference files."
  },
  {
    "id": 35,
    "question": "A customer support director audits a team of twelve service agents who use an AI assistant to triage and respond to enterprise service tickets. The audit reveals three distinct operational patterns: Pattern 1: Every agent manually copies and pastes the same four-paragraph corporate refund policy into their chat window every morning. Pattern 2: Every agent manually deletes an apologetic opening disclaimer that the model generates on every drafted response. Pattern 3: Different agents processing identical billing complaints produce radically different response structures and tone. Which sequence of friction signals corresponds precisely to Patterns 1, 2, and 3?",
    "options": {
      "A": "Pattern 1 represents Correction; Pattern 2 represents Repetition; Pattern 3 represents Variance.",
      "B": "Pattern 1 represents Repetition; Pattern 2 represents Variance; Pattern 3 represents Correction.",
      "C": "Pattern 1 represents Variance; Pattern 2 represents Repetition; Pattern 3 represents Correction.",
      "D": "Pattern 1 represents Repetition; Pattern 2 represents Correction; Pattern 3 represents Variance."
    },
    "correct": "D",
    "explanation": "Option D succeeds because it correctly maps the three friction signals to their operational definitions: 1. Repetition: Typing or pasting the same background policy into every session indicates missing context that belongs in Project Knowledge or Standing Instructions. 2. Correction: Manually removing the same unwanted output flaw (the apologetic disclaimer) from every response indicates an unpromoted rule that belongs in Standing Instructions. 3. Variance: Inconsistent outputs across different operators running the same task indicate missing standardization that belongs in a shared Skill or Knowledge Base.",
    "why_incorrect": {
      "A": "It reverses Pattern 1 (repetition of pasted policies) and Pattern 2 (manual deletion of unwanted disclaimers).",
      "B": "It misclassifies Pattern 2 as variance, whereas stripping unwanted output text is an explicit correction.",
      "C": "It treats pasting corporate policies as output variance and misclassifies inconsistent structures as correction."
    },
    "full_justification": "Option D succeeds because repeatedly pasting context is Repetition, editing out recurring flaws is Correction, and divergent outputs across operators is Variance. Option A is incorrect because manual stripping is correction, not repetition. Option B is incorrect because deleting boilerplate is correction, not variance. Option C is incorrect because pasting shared text is repetition, not variance."
  },
  {
    "id": 36,
    "question": "An operations team redesigns an expense reconciliation workflow that currently requires an analyst to run four sequential conversational prompts: Prompt 1 extracts line items; Prompt 2 classifies expense categories using internal policy; Prompt 3 checks meal allowances; Prompt 4 drafts the reimbursement voucher. An enthusiastic associate recommends immediately converting all four prompts into four separate account-level Skills. What workflow sequencing rule did the associate violate?",
    "options": {
      "A": "Consolidation should precede promotion, avoiding engineering configuration for mergeable prompts.",
      "B": "Prompts involving corporate finance are strictly prohibited from being automated via custom Skills.",
      "C": "Parallel runs must be conducted for twelve months before authoring any permanent task configuration.",
      "D": "Procedural prompts must always be promoted to standing instructions rather than custom agent Skills."
    },
    "correct": "A",
    "explanation": "Option A succeeds because the standard optimization rule mandates: consolidate, then promote. Consolidation reduces the number of steps by merging sequential prompts that share context, while promotion moves the remaining steps into permanent configuration. Promoting four fragmented prompts into four separate Skills before consolidating them wastes engineering effort configuring manual handoffs that should have been eliminated.",
    "why_incorrect": {
      "B": "Financial expense workflows are frequently supported by Skills, provided proper human verification gates govern the output.",
      "C": "While parallel runs are vital before full production cutover, they are conducted after designing the new process, not for an arbitrary twelve-month delay.",
      "D": "Procedural sequences belong in Skills, whereas standing instructions are designed for global rules and constraints."
    },
    "full_justification": "Option A succeeds because workflow optimization mandates consolidating contiguous prompts into unified steps before promoting them into permanent configuration artifacts (Skills). Option B is incorrect because financial workflows routinely leverage Skills with human gates. Option C is incorrect because twelve-month validation delays are ungrounded. Option D is incorrect because multi-step sequences belong in Skills, not standing instructions."
  },
  {
    "id": 37,
    "question": "A commercial logistics company plans to automate the drafting of international customs declarations using an AI assistant. The operations director insists on conducting a three-week parallel run alongside the legacy manual workflow. Which operational benefits justify the duplicated cost and effort of this parallel run? (Select TWO.)",
    "options": {
      "A": "It provides a verified operational fallback path if the new AI workflow encounters failures.",
      "B": "It guarantees that the foundation model vendor assumes legal liability for misclassifications.",
      "C": "It generates empirical comparative data proving whether the new system beats baseline metrics.",
      "D": "It allows the engineering team to eliminate all downstream human verification review gates."
    },
    "correct": "A and C",
    "explanation": "Options A and C succeed because a parallel run (operating legacy and redesigned workflows concurrently for 2–3 cycles) provides two critical operational safeguards: 1. Empirical proof: It compares live performance against baseline metrics (time, error rates, revision rounds), turning subjective assumptions into verifiable evidence. 2. Operational resilience: It preserves an active, proven fallback process that the team can revert to immediately if the AI-enabled workflow encounters unforeseen failures.",
    "why_incorrect": {
      "B": "Foundation model providers explicitly disclaim legal liability for downstream operational errors in commercial filings.",
      "D": "Parallel runs validate workflow redesign; they do not eliminate mandatory human sign-off gates on high-stakes external filings."
    },
    "full_justification": "Options A and C succeed because parallel runs provide empirical validation against baseline metrics and maintain an active operational fallback during transition. Option B is incorrect because software providers disclaim legal liability for business filings. Option D is incorrect because parallel testing does not eliminate mandatory human verification gates."
  },
  {
    "id": 38,
    "question": "A financial services firm designs an AI workflow to triage customer hardship payment deferral requests. During design time, the workflow architect establishes the first-hour incident response protocol in case a malformed prompt or stale configuration grants unauthorized debt write-offs. Which two decisions must be made and documented at design time before the workflow enters production? (Select TWO.)",
    "options": {
      "A": "The scope discovery method, establishing how to determine how many outputs were affected and where.",
      "B": "The emergency halting mechanism, specifying who can stop the workflow without seeking permission.",
      "C": "The complete rewrite of the enterprise acceptable-use policy, executed prior to inspecting logs.",
      "D": "The customer compensation script, drafted after the public relations impact has been evaluated."
    },
    "correct": "A and B",
    "explanation": "Options A and B succeed because the four-step incident protocol (Stop, Scope, Tell, Map Change) relies on two decisions that must be made at design time: 1. How it gets stopped: The exact mechanism to halt the workflow immediately, naming the individual authorized to pull the plug without seeking permission. 2. What is already out (Scope): The predetermined audit method to determine the blast radius—identifying exactly how many bad outputs were generated, when the failure began, and where they went.",
    "why_incorrect": {
      "C": "Rewriting corporate-wide acceptable-use policies is an enterprise governance activity, not an operational workflow incident decision.",
      "D": "Stakeholder notification messages are executed during the incident response; the designer specifies who is told and by when, not a post-hoc PR script."
    },
    "full_justification": "Options A and B succeed because design-time incident readiness requires establishing an unencumbered emergency halting authority and a predetermined scope-auditing procedure to determine blast radius. Option C is incorrect because acceptable-use policies are broad governance documents rather than immediate operational stop controls. Option D is incorrect because customer PR scripts are reactive communications rather than design-time control decisions."
  },
  {
    "id": 39,
    "question": "A healthcare logistics manager presents an AI-assisted organ transport scheduling workflow to three distinct stakeholder groups. When briefing the hospital risk and clinical governance committee, which description properly balances operational utility with defensible governance standards?",
    "options": {
      "A": "\"The scheduling system operates fully autonomously, eliminating all human dispatch communication latency.\"",
      "B": "\"The assistant completely handles transport routing, matching ambulance crew capacity across all regions.\"",
      "C": "\"The tool drafts candidate transit routes; an on-duty medical controller reviews and authorizes dispatches.\"",
      "D": "\"The model performs basically as well as a human dispatcher at coordinating complex multi-hospital routes.\""
    },
    "correct": "C",
    "explanation": "Option C succeeds because defensible workflow communication follows the rule: state what the tool does, then name the human checkpoint. Describing the assistant as a drafting mechanism while explicitly naming the qualified human controller who inspects and authorizes dispatch provides an accurate, trustworthy account that satisfies risk and clinical governance scrutiny.",
    "why_incorrect": {
      "A": "\"Fully automated\" is an overstatement that misrepresents operational reality and breaks stakeholder trust upon the first visible error.",
      "B": "Using \"handles\" drops the human gate from the description, leading stakeholders to believe that critical medical logistics execute without oversight.",
      "D": "Claiming the model is \"basically as good as a person\" sets an unrealistic benchmark that the tool will eventually fail."
    },
    "full_justification": "Option C succeeds because defensible governance communication pairs what the tool computes (drafting candidate routes) with the named human verification gate (authorized medical controller review). Option A is incorrect because claiming full automation misrepresents the control framework. Option B is incorrect because 'handles' obscures mandatory human review. Option D is incorrect because personification benchmarks establish ungrounded expectations."
  },
  {
    "id": 40,
    "question": "A procurement associate drafts a briefing note for the company intranet describing a new AI-enabled tool that flags compliance departures in supplier non-disclosure agreements. The draft reads: \"Our new AI system fully handles supplier NDA reviews, ensuring our commercial contracts are basically as good as a person could make them.\" When revising this statement to adhere to communication and governance standards, what changes must be made? (Select TWO.)",
    "options": {
      "A": "State that the contract review workflow operates completely autonomously without any human intervention.",
      "B": "Assert that the AI assistant holds professional indemnity insurance covering contractual drafting errors.",
      "C": "Explicitly name the human review gate, confirming a legal specialist approves departures before signing.",
      "D": "Remove the phrases \"handles\" and \"as good as a person\" to eliminate ungrounded claims of tool autonomy."
    },
    "correct": "C and D",
    "explanation": "Options C and D succeed because accurate stakeholder communication requires eliminating overstatements and establishing human oversight: 1. Eliminating overstatement: Phrases like \"handles\" and \"as good as a person\" misrepresent tool autonomy and set dangerous expectations. 2. Naming the gate: Explaining what the tool does (extracts clauses, flags playbook departures) must always be followed by naming the human checkpoint (a legal specialist reviews and approves each departure).",
    "why_incorrect": {
      "A": "Falsely claiming a legal contract review operates without human oversight increases liability and violates governance standards.",
      "B": "Software assistants do not carry professional indemnity insurance; enterprise liability remains entirely with the operating organization."
    },
    "full_justification": "Options C and D succeed because responsible governance communication eliminates misleading autonomous phrasing ('handles', 'as good as a person') and transparently names the qualified human verification gate. Option A is incorrect because claiming complete autonomy creates severe compliance liability. Option B is incorrect because software models do not hold professional indemnity insurance."
  }
]
