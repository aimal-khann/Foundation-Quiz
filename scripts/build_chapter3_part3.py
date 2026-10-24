# scripts/build_chapter3_part3.py
# Questions 21 to 30 for Chapter 3

questions_21_to_30 = [
  {
    "id": 21,
    "question": "An operations analyst uses an AI assistant to evaluate incoming customer warranty disputes. Over the last four weeks, the assistant generated well-grounded warranty assessments matching the company playbook. On Thursday afternoon, the analyst notices that outputs have suddenly become vague, omitting the statutory return windows. The analyst's first instinct is to switch the workspace to an advanced reasoning model. According to the diagnostic sequence, which question must the analyst investigate before changing any tools or settings?",
    "options": {
      "A": "When did the diagnostic symptom first emerge along the operational timeline of this workflow?",
      "B": "Did the cloud platform vendor modify the graphical layout of the chat interface configuration?",
      "C": "Does the dispute playbook mandate conversion into an interactive visual dashboard web artifact?",
      "D": "How many total input tokens did the customer support ticket ingest during Thursday's triage run?"
    },
    "correct": "A",
    "explanation": "Option A succeeds because the foundation of systematic workflow troubleshooting is: when did the symptom first appear? Timing is free diagnostic information that instantly narrows down root causes. Jumping directly to an advanced model or rewriting prompts bypasses the timeline analysis, leading to expensive and unnecessary adjustments.",
    "why_incorrect": {
      "B": "User interface visual changes affect client layouts, not underlying model reasoning or instruction retention within an active workflow.",
      "C": "Converting workflows into web artifacts is an implementation choice, not a diagnostic inquiry to isolate why text generation degraded.",
      "D": "Checking token counts on a single ticket is a secondary investigation; establishing the operational timeline must precede granular token audits."
    },
    "full_justification": "Option A succeeds because establishing the exact chronological emergence of a failure isolates the failure mode without costly trial-and-error changes. Option B is incorrect because interface layouts do not affect prompt processing. Option C is incorrect because artifact conversion is an implementation change rather than root-cause triage. Option D is incorrect because auditing single-ticket token consumption is premature before establishing the symptom timeline."
  },
  {
    "id": 22,
    "question": "A legal assistant asks an AI model to draft an executive summary of a commercial property lease. On the very first generation turn, the returned summary accurately extracts rent figures and renewal dates, but completely omits the break-clause penalty formulas and tenant repair obligations specified in the document. The prompt reads: \"Summarise the key terms in the attached commercial lease for our managing partner.\" What is the primary operational diagnosis?",
    "options": {
      "A": "Stale configuration, because the underlying lease analysis skill expired following platform maintenance.",
      "B": "Expectation mismatch, because modern language models lack the capacity to interpret commercial contracts.",
      "C": "Underspecification, because the prompt omitted explicit criteria defining which clauses qualify as key.",
      "D": "Context overload, because the attached 40-page commercial lease exceeded active token processing limits."
    },
    "correct": "C",
    "explanation": "Option C succeeds because the symptom appeared on the very first response. Underspecification occurs when the prompt fails to define essential operational parameters. Telling a model to extract \"key terms\" without defining the criteria for what qualifies as \"key\" forces the model to use default assumptions, omitting specific clauses like break penalties and repair duties.",
    "why_incorrect": {
      "A": "Stale configuration manifests as a gradual degradation over time after environmental drift, not as an omitted clause category on turn one of a fresh prompt.",
      "B": "Parsing commercial leases and extracting legal obligations is a core capability of modern frontier models, not an impossible expectation mismatch.",
      "D": "Context overload emerges gradually over extended multi-turn conversations as token limits are saturated, not on turn one of a single document."
    },
    "full_justification": "Option C succeeds because omitting the criteria that govern what constitutes a 'key term' forces the model to rely on statistical defaults, causing immediate turn-one omissions. Option A is incorrect because stale configuration requires a prior working baseline that later drifted. Option B is incorrect because legal document extraction is well within model capabilities. Option D is incorrect because single lease documents do not exceed modern context limits on turn one."
  },
  {
    "id": 23,
    "question": "A financial analyst conducts an extensive 45-minute working session to model debt service covenants across eight business scenarios. For the first six scenarios, the assistant formats tables with exact headers and rounds interest figures to two decimal places. By scenario seven, the assistant begins generating free-form prose paragraphs, drops decimals, and ignores the established table layout. What operational failure has occurred?",
    "options": {
      "A": "Underspecification, because the analyst omitted a system instruction declaring an investment persona.",
      "B": "Context overload, because the conversational history expanded beyond the effective context attention.",
      "C": "Wrong feature selection, because financial covenant modeling must execute in command-line terminals.",
      "D": "Expectation mismatch, because multi-scenario debt modeling exceeds modern foundation model capacity."
    },
    "correct": "B",
    "explanation": "Option B succeeds because the timeline matches context overload: the assistant executed reliably for several rounds, but degraded as the session expanded. As the conversation grows longer, early instructions (such as rounding rules and table layout constraints) are compressed, pushed out of effective attention, or diluted, causing formatting drift.",
    "why_incorrect": {
      "A": "Underspecification causes errors on turn one; here, the model followed the specifications accurately across six consecutive scenarios.",
      "C": "The assistant executed the formatting and rounding properly for the first six rounds; a feature failure would have produced errors from the beginning.",
      "D": "Debt covenant modeling across multiple scenarios is well within LLM capabilities, as evidenced by its successful completion of scenarios one through six."
    },
    "full_justification": "Option B succeeds because context overload specifically describes progressive instruction degradation occurring late in extended sessions as accumulated history dilutes model attention. Option A is incorrect because turn-one success disproves prompt underspecification. Option C is incorrect because conversational tools handled early rounds successfully. Option D is incorrect because the model proved its capability across the first six turns."
  },
  {
    "id": 24,
    "question": "A commercial shipping manager tests an AI assistant for two separate maritime logistics operations: Task 1: The model is asked to calculate daily bunker fuel consumption and port demurrage charges in prose; the figures arrive subtly incorrect by a few hundred dollars. Task 2: The model is assigned a complex multi-vessel routing optimization on a speed-optimised tier; the resulting itinerary overlooks cargo cooling constraints. Which diagnostic classification correctly identifies the root cause of these two failures?",
    "options": {
      "A": "Task 1 reflects stale configuration; Task 2 reflects a failure in designated human verification gates.",
      "B": "Task 1 reflects context overload; Task 2 reflects an out-of-date departmental project knowledge base.",
      "C": "Task 1 reflects an expectation mismatch; Task 2 reflects an underspecified prompt role instruction.",
      "D": "Task 1 reflects a wrong feature choice; Task 2 reflects an underpowered, inappropriate model tier."
    },
    "correct": "D",
    "explanation": "Option D succeeds because both failures illustrate wrong feature or model choices: 1. Wrong Feature: In Task 1, fuel and demurrage calculations performed in prose produce subtle arithmetic drift because generative text predicts tokens rather than evaluating deterministic math; this calculation belongs in code execution. 2. Wrong Model: In Task 2, complex routing optimization with interdependent constraints fails on a speed/lightweight tier; multi-step constraint satisfaction demands a frontier reasoning tier.",
    "why_incorrect": {
      "A": "Mathematical drift on turn one is an execution feature choice, and routing constraint oversights reflect model reasoning capacity, not human review gate staffing.",
      "B": "Neither problem stemmed from session length (overload) or deprecated reference files (stale configuration).",
      "C": "Fuel calculation is not an expectation mismatch (it is easily calculated via code execution), and routing failure is a model tier issue, not an absent persona."
    },
    "full_justification": "Option D succeeds because arithmetic performed in prose represents a wrong feature selection (requiring code execution), while multi-constraint logistics optimization represents a wrong model tier (requiring frontier reasoning). Option A is incorrect because neither failure stems from stale reference files or gate staffing. Option B is incorrect because conversation length and knowledge bases were not involved. Option C is incorrect because neither task represents an impossible expectation or missing persona."
  },
  {
    "id": 25,
    "question": "A pharmaceutical marketing team uses a dedicated Project workspace to generate product safety summaries. For four months, the outputs have been accurate, compliant, and formatted correctly. In the fifth month, a regulatory auditor notices that newly drafted summaries fail to incorporate the revised clinical contraindications issued by the health authority three weeks earlier, even though the system reports no errors. What diagnostic cause explains this breakdown?",
    "options": {
      "A": "Stale configuration, because the underlying Project knowledge repository contains outdated reference files.",
      "B": "Underspecification, because the operational prompt omitted explicit directives requesting an expert persona.",
      "C": "Expectation mismatch, because generative foundation models are fundamentally unable to parse clinical data.",
      "D": "Context overload, because the accumulated archive of historical marketing conversations saturated the system."
    },
    "correct": "A",
    "explanation": "Option A succeeds because this is the hallmark of stale configuration: it displays the \"it used to work\" timing pattern. The prompt, model, and workflow were set up correctly, but the underlying reference material in the Project knowledge base was not updated with the newly published clinical contraindications. Stale configurations degrade silently with zero error alerts.",
    "why_incorrect": {
      "B": "Underspecification produces failures from the first response, whereas this workflow functioned properly for four consecutive months.",
      "C": "Foundation models routinely parse pharmacology summaries; the failure was caused by obsolete reference documents, not an inability to read text.",
      "D": "Context overload affects long individual chat threads; it does not explain why a freshly initiated session in a project outputs outdated information."
    },
    "full_justification": "Option A succeeds because silent failure after months of successful operation indicates that static reference files in the Project knowledge base have drifted from live regulatory standards. Option B is incorrect because four months of successful outputs disprove prompt underspecification. Option C is incorrect because language models routinely extract clinical contraindications. Option D is incorrect because fresh sessions do not inherit context bloat from historical threads."
  },
  {
    "id": 26,
    "question": "A marketing director asks an AI assistant: \"Predict the exact unit sales figure for our new product line across the next four financial quarters based on our past three years of quarterly sales records.\" The assistant returns four precise quarterly numbers. At year-end, the actual sales diverge significantly from the prediction, and the director concludes that the AI tool is defective and should be decommissioned. How should a workflow designer evaluate this failure?",
    "options": {
      "A": "The breakdown was caused by a stale configuration in the assistant's underlying analytical workspace tool.",
      "B": "The failure resulted from underspecification because historical seasonal regression indexes were omitted.",
      "C": "The director encountered an expectation mismatch by requiring the model to execute an impossible task.",
      "D": "The model suffered from context overload because three full years of quarterly records flooded memory."
    },
    "correct": "C",
    "explanation": "Option C succeeds because the request represents an expectation mismatch. Asking an AI model to predict a single, exact future sales number demands predictive precognition that no prompt engineering, configuration update, or model tier can provide. The failure lies in the task itself; it must be restructured into an achievable design, such as modeling driver scenarios with adjustable assumptions.",
    "why_incorrect": {
      "A": "Stale configuration involves outdated saved instructions or reference files, whereas this failure is an inherently impossible task mandate.",
      "B": "Attaching seasonal indexes would still not make a single deterministic future point forecast possible or accurate.",
      "D": "Ingesting three years of quarterly sales records (12 data points) consumes negligible context window capacity."
    },
    "full_justification": "Option C succeeds because demanding a single point-forecast for future sales represents an expectation mismatch; generative models can model comparative scenarios but cannot predict unknowable future market reality. Option A is incorrect because reference documentation drift was not the root cause. Option B is incorrect because statistical indexes cannot grant predictive precognition. Option D is incorrect because twelve quarterly records cannot saturate a context window."
  },
  {
    "id": 27,
    "question": "An associate at a management consultancy receives a disappointing deliverable from an AI assistant. The summary missed key qualitative nuances, presented figures in text that should have been computed, and drifted in tone. A colleague advises: \"Switch immediately to the most expensive frontier reasoning model and re-write the task from scratch.\" According to the cheapest-first diagnostic sequence, which operational order should the associate follow before questioning whether the task is a fit?",
    "options": {
      "A": "Audit configuration files -> Execute in code sandbox -> Reset session memory -> Re-examine prompt slots.",
      "B": "Re-read the 5 prompt slots -> Check session length -> Check feature/tier -> Audit workspace configuration.",
      "C": "Clear conversational memory -> Re-read prompt slots -> Escalate to architect -> Alter foundation model tier.",
      "D": "Evaluate task suitability -> Change model reasoning tier -> Inspect session history -> Re-read the prompt."
    },
    "correct": "B",
    "explanation": "Option B succeeds because the diagnostic sequence mandates running checks from cheapest to most expensive: 1. Re-read the prompt (5 slots) 2. Check session length 3. Check feature and model tier 4. Check configuration 5. Question task fit. Re-reading a prompt costs seconds, while changing models, refactoring infrastructure, or abandoning tasks incurs significant operational cost.",
    "why_incorrect": {
      "A": "Auditing configurations and refactoring code execution sandboxes should only occur after ruling out prompt omissions and conversation bloat.",
      "C": "Escalating to systems architects without performing basic prompt and session triage wastes engineering capacity.",
      "D": "It reverses the diagnostic ladder, beginning with the most expensive move (questioning task fit) before checking basic prompt specifications."
    },
    "full_justification": "Option B succeeds because the diagnostic sequence enforces a disciplined, cost-effective progression from low-cost prompt inspection and session clearing to higher-cost tier changes and configuration audits. Option A is incorrect because infrastructure audits precede prompt checks. Option C is incorrect because premature architectural escalation bypasses basic triage. Option D is incorrect because starting with task abandonment inverts the troubleshooting ladder."
  },
  {
    "id": 28,
    "question": "A managing partner reviews an AI-generated client briefing on a tax law update and tells the associate: \"This is completely unhelpful—it's far too generic and misses the point.\" The associate must convert this subjective reaction into actionable configuration changes. Which two interventions correctly map the partner's reaction to the appropriate operational lever? (Select TWO.)",
    "options": {
      "A": "Address \"too generic\" by upgrading the tenant to an autonomous web agent equipped with unconstrained search.",
      "B": "Address \"too generic\" by adding an explicit instruction identifying the target reader and their commercial call.",
      "C": "Address \"missed the point\" by running an incognito session to purge stored conversational memory files cleanly.",
      "D": "Address \"missed the point\" by adding a constraint defining the primary legal issue that must be resolved first."
    },
    "correct": "B and D",
    "explanation": "Options B and D succeed because converting a reaction into an instruction requires asking: what would have to be present for this to be right, and which part of the setup controls that?: 1. Too generic: Addressed by defining the specific audience and the single decision or action they must take, anchoring the output in concrete operational stakes. 2. Missed the point: Controlled by the prompt; stating the primary legal or business question up front prevents the model from digressing into background trivia.",
    "why_incorrect": {
      "A": "Autonomous web agents expand search breadth, which worsens generic prose rather than focusing the analysis on the client's commercial problem.",
      "C": "Switching to an incognito session clears local chat history, but does nothing to provide the missing focus or purpose of the prompt."
    },
    "full_justification": "Options B and D succeed because operationalizing vague criticism requires defining the reader and decision for generic prose, and enforcing an explicit core question constraint for missed focus. Option A is incorrect because broader web scraping increases conversational sprawl. Option C is incorrect because private browsing sessions do not provide missing analytical direction."
  },
  {
    "id": 29,
    "question": "A supply chain coordinator audits a prompt that produced an inadequate vendor risk assessment on its first attempt: \"Review the attached supplier audit report and highlight the risks.\" When evaluating the prompt against the standard five-slot framework (Role, Context, Task, Constraints, Format), which two critical slots are completely unpopulated? (Select TWO.)",
    "options": {
      "A": "Context, because the prompt provides no operational background regarding business environment or risk profile.",
      "B": "Task, because the prompt completely lacks an operational directive instructing the assistant to take action.",
      "C": "Role, because language models cannot execute text analysis unless assigned a formal managerial job title.",
      "D": "Constraints, because the prompt sets no boundaries on severity categories, excluded risks, or length limits."
    },
    "correct": "A and D",
    "explanation": "Options A and D succeed because auditing a prompt against its five parts reveals what is missing: 1. Context: The prompt gives no background regarding the company's operating environment, supply chain tier, or industry risk thresholds. 2. Constraints: The prompt sets no boundaries on severity categories, report length, excluded operational risks, or scoring thresholds.",
    "why_incorrect": {
      "B": "The prompt contains a clear Task: \"Review the attached supplier audit report and highlight the risks\".",
      "C": "While assigning a persona is a component of Role, models do not strictly require job titles to execute text analysis."
    },
    "full_justification": "Options A and D succeed because the prompt completely lacks operational background (Context) and severity/boundary rules (Constraints), forcing the model to generate unguided generalizations. Option B is incorrect because 'Review and highlight' explicitly defines the Task. Option C is incorrect because formal job titles are optional styling aids rather than mandatory functional prerequisites."
  },
  {
    "id": 30,
    "question": "An analyst suspects that an assistant's sudden failure to adhere to output formatting rules halfway through a long session is caused by context overload rather than an under-specified prompt or a broken configuration. Which cheap, one-minute confirmation test should the analyst run to isolate this hypothesis?",
    "options": {
      "A": "Conduct a line-by-line audit across all reference policy documents stored in the Project knowledge archive.",
      "B": "Re-run the existing conversational thread from the start using a faster, speed-optimised foundation model.",
      "C": "Escalate the session to an enterprise software architect to inspect underlying platform API telemetry logs.",
      "D": "Paste the original formatting prompt into a clean session alongside input data to confirm if it holds."
    },
    "correct": "D",
    "explanation": "Option D succeeds because it is the one-minute confirmation test for context overload: restate the instruction in a fresh session to see if it holds. If the model formats the output correctly in a clean session, context overload is confirmed; if it fails in the fresh session, the prompt itself is under-specified.",
    "why_incorrect": {
      "A": "Auditing project knowledge bases tests for stale configuration, which is not the hypothesis when formatting degrades midway through an active session.",
      "B": "Re-running a failing prompt on a fast, speed-optimised tier reduces reasoning capacity and does not diagnose whether context bloat was the root cause.",
      "C": "Escalating to software architects to review backend infrastructure logs is costly and unnecessary for a routine session degradation diagnosis."
    },
    "full_justification": "Option D succeeds because running the exact prompt in a fresh session instantly isolates whether mid-session drift was caused by conversational token bloat or inherent prompt ambiguity. Option A is incorrect because reference documentation audits target stale configurations. Option B is incorrect because lightweight models degrade reasoning without isolating token exhaustion. Option C is incorrect because architectural telemetry logs are irrelevant for conversational context diagnosis."
  }
]
