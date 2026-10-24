# scripts/build_chapter3_part1.py
# Questions 1 to 10 for Chapter 3

questions_1_to_10 = [
  {
    "id": 1,
    "question": "An operations analyst at an equipment leasing firm uses Claude daily to parse customer return damage logs. She adjusts her conversational prompts according to the complexity of each incident and manually flags high-cost claims for management. When she takes annual leave, unresolved claims accumulate because her colleagues cannot replicate her prompting style. According to workflow design principles, what core transition is required to convert this personal habit into a production workflow?",
    "options": {
      "A": "Authoring global custom instructions to standardize an equipment surveyor persona and voice across every session.",
      "B": "Storing shared prompt templates in a departmental repository for covering analysts to paste during daily triage.",
      "C": "Decomposing the procedure into discrete named steps with explicit input schemas, outputs, and fixed step owners.",
      "D": "Upgrading department workspace licensing to frontier reasoning models to diminish reliance on nuanced phrasing."
    },
    "correct": "C",
    "explanation": "Option C succeeds because the foundational thesis of workflow design states that the unit of value is the step, not the session. A personal habit lives in one individual's head, varies with operator temperament, and collapses during absence. A true workflow is an auditable, repeatable team process where each named step has a fixed owner, clear operational criteria, and consistent execution regardless of who sits at the keyboard.",
    "why_incorrect": {
      "A": "Assigning global personas modifies linguistic tone and styling across all chats, but fails to establish a structured procedural handoff with defined operational criteria.",
      "B": "Storing raw prompt templates merely shares fragmented personal habits; it does not establish standardized data contracts, step ownership, or operational continuity.",
      "D": "Upgrading model tiers provides higher parametric reasoning capacity, but cannot compensate for the lack of procedural decomposition, accountability gates, and step boundaries."
    },
    "full_justification": "Option C succeeds because workflow engineering establishes that the unit of value is the step, not the conversational session. Transforming personal habits into enterprise production requires auditable, named steps with fixed ownership criteria. Option A is incorrect because global personas only alter conversational voice. Option B is incorrect because pasting shared prompt snippets replicates unstructured individual habits. Option D is incorrect because advanced model tiers do not solve procedural workflow voids."
  },
  {
    "id": 2,
    "question": "A defence supplier's bidding team ingests a 70-page government tender into a dedicated Project workspace. The team uses an assistant to extract all mandatory contractual terms into a 4-column structured table. The proposal manager directs the associate to proceed immediately to drafting the technical proposal. Which operational review step was bypassed?",
    "options": {
      "A": "Interrogating extracted obligations for ambiguities, divergent team interpretations, and unstated assumptions.",
      "B": "Cross-referencing extracted clauses against competitor public tenders to determine optimal commercial margins.",
      "C": "Synthesizing an executive narrative summary of extraction outputs to verify model comprehension of the tender.",
      "D": "Executing sandbox scripts across the extracted tables to verify contractual section lengths and word densities."
    },
    "correct": "A",
    "explanation": "Option A succeeds because extracting requirements is only the first half of the design stage; the vital second half is attacking them. Extraction surfaces what is written plainly, but tenders are won or lost on ambiguities, unstated assumptions, and clauses two team members read differently. Catching these at the requirements stage costs a simple clarifying question, whereas catching them after proposal drafting costs the entire bid.",
    "why_incorrect": {
      "B": "Cross-referencing competitor public tenders introduces external strategic pricing analysis before the internal baseline compliance obligations of the tender are settled.",
      "C": "Synthesizing an executive narrative summary merely re-summarizes the text without stress-testing contractual ambiguities, conflicting requirements, or unstated dependencies.",
      "D": "Running sandbox scripts to verify section lengths and word counts checks cosmetic formatting rather than auditing binding legal liabilities and contractual risks."
    },
    "full_justification": "Option A succeeds because rigorous workflow design demands attacking extracted requirements for ambiguities, hidden assumptions, and divergent interpretations before drafting begins. Option B is incorrect because external market pricing analysis bypasses internal compliance verification. Option C is incorrect because executive summaries provide passive overviews rather than adversarial interrogation. Option D is incorrect because verifying section lengths focuses on cosmetic layout rather than contractual risks."
  },
  {
    "id": 3,
    "question": "A regional clinic director verbally tells an administrative coordinator: \"We need better management of our patient appointment no-shows.\" The coordinator opens an assistant and asks it to design a no-show remediation process. The assistant generates a full operational protocol with default assumptions. What delegation failure occurred at inception?",
    "options": {
      "A": "The coordinator omitted clinical consultation records necessary to verify historical patient attendance patterns.",
      "B": "The coordinator neglected to supply a few-shot demonstration illustrating an approved clinic scheduling roster.",
      "C": "The coordinator initiated the workflow in a standard conversational session rather than deploying an API connector.",
      "D": "The coordinator allowed the model to assume unstated operational dimensions instead of fixing a 5-part definition."
    },
    "correct": "D",
    "explanation": "Option D succeeds because vague instructions like \"better management\" lack operational definition. A proper task definition requires five settled answers: what is produced, for whom, how often, from what data, and in what format. When these slots are left blank, an AI assistant does not refuse; it silently populates them with likely-looking defaults that do not reflect the organization's real requirements.",
    "why_incorrect": {
      "A": "Attaching clinical consultation records violates patient data protection without resolving the fundamental absence of an operational task specification.",
      "B": "Providing few-shot scheduling exemplars guides formatting and visual syntax, but cannot resolve an undefined operational scope or missing stakeholder criteria.",
      "C": "Deploying API connectors provides external software integration, but integrating an undefined administrative goal simply accelerates operational misdirection."
    },
    "full_justification": "Option D succeeds because when operators provide uncalibrated, abstract goals, AI models silently hallucinate plausible operational defaults across the five foundational task dimensions. Option A is incorrect because feeding raw clinical records creates regulatory exposure without clarifying task boundaries. Option B is incorrect because few-shot examples improve formatting but do not define workflow objectives. Option C is incorrect because API connectors automate data movement, not process definition."
  },
  {
    "id": 4,
    "question": "An operations director at an airline logistics hub tasks an assistant with drafting next quarter’s ramp-agent shift allocation model using five years of flight telematics and cargo tonnage data. The assistant delivers an optimized staffing schedule recommending a 12% headcount reduction. The director rejects the plan as unworkable because the hub is entering mandatory union contract renegotiations next month. Why did this planning step fail the window test?",
    "options": {
      "A": "The historical flight telematics file contained uncleaned null values that distorted scheduling optimization.",
      "B": "The step required strategic and labor constraints that sat entirely outside the model's accessible context.",
      "C": "Shift allocation modeling requires deterministic spreadsheet macros rather than foundation model synthesis.",
      "D": "The model's context window suffered attention degradation from ingesting large multi-year cargo datasets."
    },
    "correct": "B",
    "explanation": "Option B succeeds because the window test asks: Could everything this step needs be put into the context window? Synthesis steps assemble provided facts, whereas judgment steps rely on inaccessible information—such as internal risk appetite, impending strikes, or confidential union negotiations held in private meetings. If an input cannot be supplied to the model, the step must remain human-retained.",
    "why_incorrect": {
      "A": "Historical data cleanliness was not the primary failure mode; the quantitative schedule was mathematically sound but blind to unsupplied labor constraints.",
      "C": "Foundation models excel at complex multi-factor synthesis; the failure was not computational tooling, but the omission of strategic labor relations context.",
      "D": "Context degradation manifests as dropped formatting or mid-session hallucination, whereas here the assistant produced a fully coherent plan that was strategically unworkable."
    },
    "full_justification": "Option B succeeds because the window test distinguishes delegable synthesis from human-retained judgment based on whether all necessary decision constraints can physically sit within the context window. Option A is incorrect because telemetry data quality was not the deciding factor. Option C is incorrect because LLMs can model shift allocations when properly bounded. Option D is incorrect because the model did not suffer technical token loss; it was blind to confidential labor negotiations."
  },
  {
    "id": 5,
    "question": "A commercial real estate consultancy prepares an investment prospectus for an industrial logistics park. The associate instructs the assistant: \"Provide the current commercial property tax rates for warehouse facilities across three target municipal districts.\" The assistant returns a well-formatted comparison table with specific millage rates and statutory assessment percentages. Which instruction should have governed this lookup to satisfy the research verification standard?",
    "options": {
      "A": "Restricting the assistant to its parametric memory index to avoid external retrieval latency across the report.",
      "B": "Directing the assistant to compile its findings as an interactive visual artifact with dynamic comparison charts.",
      "C": "Instructing the assistant to adopt the professional persona of an accredited commercial municipal tax assessor.",
      "D": "Requiring the assistant to provide openable primary source links for each rate rather than confident narrative text."
    },
    "correct": "D",
    "explanation": "Option D succeeds because of the foundational research rule: For anything current, priced, or dated, ask for an openable source and link, never a confident answer. Model parametric memory cuts off at a training date, and web retrieval requires auditability. Requiring links allows an analyst to verify the primary source rather than relying on plausible numbers.",
    "why_incorrect": {
      "A": "Restricting the query to parametric memory guarantees that the model cannot access current municipal tax rates enacted after its static training cutoff.",
      "B": "Visualizing ungrounded numbers in an interactive web artifact creates polished cosmetic presentation without auditing statutory accuracy.",
      "C": "Adopting an expert persona modifies narrative confidence and linguistic tone, which often increases the persuasive plausibility of hallucinated tax rates."
    },
    "full_justification": "Option D succeeds because the verification standard mandates requiring openable primary source links whenever retrieving dated, priced, or regulatory data. Option A is incorrect because parametric memory cannot capture recent statutory revisions. Option B is incorrect because visual artifacts present data cleanly but do not ground truth. Option C is incorrect because expert personas increase prose confidence without ensuring empirical accuracy."
  },
  {
    "id": 6,
    "question": "A shipping brokerage maps its customs demurrage reconciliation workflow. One critical step evaluates whether detention charges incurred at container terminals should be absorbed under operational overhead or billed back to the freight client. If misclassified, client disputes or unreclaimable transport losses occur. A team lead proposes classifying this step as AI-appropriate because Claude successfully categorised last week's sample invoices. Which operational criterion must overrule this proposal and keep the step human-retained?",
    "options": {
      "A": "Accountability, because this step is the commercial financial decision itself for which the broker answers.",
      "B": "Syntactic complexity, because carrier demurrage clauses exhibit substantial variation across global ports.",
      "C": "Throughput latency, because manual review of terminal invoices introduces customs documentation bottlenecks.",
      "D": "Reversibility, because billed invoices can be credited and corrected during subsequent reconciliation cycles."
    },
    "correct": "A",
    "explanation": "Option A succeeds because step ownership is governed strictly by three criteria: Reversibility, Stakes, and Accountability. Accountability cannot move onto the machine because software cannot answer for an outcome. A step that produces an input for someone else to evaluate can be delegated; a step that is the decision itself must stay human. Billing a client or absorbing a loss is the final commercial call.",
    "why_incorrect": {
      "B": "Syntactic contract variability is a technical parsing challenge, not an architectural criterion that determines operational step ownership.",
      "C": "Processing throughput and speed concerns represent business efficiency goals, but must never override non-transferable organizational accountability.",
      "D": "While billing credits can technically be issued, issuing erroneous charges damages client relationships and violates financial governance baselines."
    },
    "full_justification": "Option A succeeds because accountability is non-transferable; machine models can generate recommendations, but human brokers must own the final commercial decision. Option B is incorrect because contract variability affects prompt design, not governance ownership. Option C is incorrect because processing throughput must not override fiduciary controls. Option D is incorrect because commercial damage from erroneous billing makes post-hoc credits an unacceptable safeguard."
  },
  {
    "id": 7,
    "question": "A corporate procurement office reviews its automated contract evaluation workflow. The workflow features six distinct steps: Step 1: Extract supplier indemnification clauses (AI) Step 2: Flag departures from standard commercial playbook (AI) Step 3: Compute maximum financial exposure on penalty formulas (AI via Code Execution) Step 4: Approve or reject drafted liability clauses (Human Reviewer) Step 5: Draft supplier redline markups and rationales (Collaborative) Step 6: Execute and transmit binding contract addendum (Human Signer) A junior analyst argues that Step 3 carries high financial risk and must be moved to Human-retained. Why is Step 3 legitimately classified as AI-appropriate in this specific workflow?",
    "options": {
      "A": "Mathematical exposure formulas represent low-stakes calculation routines across enterprise procurement tasks.",
      "B": "Code execution sandboxes carry statutory liability exemptions under standardized corporate contracting laws.",
      "C": "The computed exposure figures land directly at Step 4, where an authorized human reviewer audits the decision.",
      "D": "Executing arithmetic in Python sandboxes guarantees complete immunity from calculation formula error states."
    },
    "correct": "C",
    "explanation": "Option C succeeds because calculating financial exposure is safe to delegate to AI here specifically because it lands directly before an explicit human approval gate. The calculation is reversible and provides an input that a qualified human reviewer evaluates before any action is taken. Take away Step 4, and Step 3 immediately stops being AI-appropriate.",
    "why_incorrect": {
      "A": "Mathematical formulas determining multi-million-pound contract liabilities are inherently high-stakes; they are delegable only when bounded by verification gates.",
      "B": "Computational sandboxes provide isolated software runtimes; they convey zero legal protections or statutory liability exemptions.",
      "D": "Running code in a sandbox eliminates mental arithmetic slips, but code can still reference the wrong data column or misapply a legal contractual formula."
    },
    "full_justification": "Option C succeeds because high-stakes analytical steps are safely delegable when positioned directly upstream of a mandatory, qualified human decision gate. Option A is incorrect because contract exposure calculations carry immense financial liability. Option B is incorrect because sandboxed execution environments carry no statutory legal immunity. Option D is incorrect because automated code can still execute incorrect formulas or query flawed inputs."
  },
  {
    "id": 8,
    "question": "A municipal transit authority implements an automated customer feedback workflow. An assistant extracts commuter complaints, matches them to bus routes, and drafts standard response letters. The drafts have been polite, grammatically accurate, and empathetic for three consecutive months. Encouraged by this performance, the team updates the workflow to let the assistant autonomously categorize complaint severity and dispatch compensation travel vouchers. Within two weeks, several fraudulent compensation claims are paid. What workflow mapping error caused this breakdown?",
    "options": {
      "A": "Mapping the tool instead of the work, by selecting an unapproved conversational plugin for ticket dispatch.",
      "B": "Halo delegation, by treating demonstrated drafting quality as evidence of autonomous adjudication reliability.",
      "C": "Expectation mismatch, because frontier language models are inherently incapable of parsing transit policies.",
      "D": "Unstaffed gate degradation, because human adjudicators were overwhelmed by daily commuter dispute volumes."
    },
    "correct": "B",
    "explanation": "Option B succeeds because halo delegation occurs when high competence in one step (drafting empathetic letters) is treated as evidence that the model is safe to own a completely different, higher-risk step (severity triage and issuing financial compensation). Drafting quality is evidence only about the draft, never about the decision.",
    "why_incorrect": {
      "A": "The failure was driven by misjudging step ownership and delegating financial payout authority without controls, not by using unapproved plugins.",
      "C": "Classifying passenger feedback against municipal policies is well within model capabilities; the error was bypassing human adjudication gates.",
      "D": "An unstaffed gate occurs when an existing reviewer rubber-stamps files under volume; here, the team intentionally redesigned the map to eliminate the gate."
    },
    "full_justification": "Option B succeeds because halo delegation conflates fluency in low-stakes drafting with reliable judgment in high-stakes financial payouts. Option A is incorrect because tool configuration was not the root cause. Option C is incorrect because language models can parse policy guidelines when supervised. Option D is incorrect because the agency actively removed the human gate rather than experiencing passive review fatigue."
  },
  {
    "id": 9,
    "question": "A retail bank deploys a collaborative workflow to draft customer loan restructuring proposals. Under the map design, an assistant extracts income statements and drafts the restructuring terms, after which a lending officer reviews and signs each proposal before dispatch. Over six months, weekly proposal volume increases from 15 cases to 85 cases per officer. An internal audit reveals that officers now spend an average of twelve seconds per file, clicking \"Approve\" without opening source attachments. What operational failure has occurred?",
    "options": {
      "A": "Prompt underspecification, because statutory loan affordability constraints were not updated each quarter.",
      "B": "Model performance drift, because the foundation model provider released an unannounced architectural update.",
      "C": "Context overload, because ingesting high-density income spreadsheets caused token saturation across turns.",
      "D": "Unstaffed gate degradation, because surging operational volume reduced the collaborative check to a glance."
    },
    "correct": "D",
    "explanation": "Option D succeeds because this is the classic anatomy of an unstaffed gate. The workflow map still says \"Collaborative\" and names a human reviewer, but because operational volume increased sixfold, the review decayed into a glance and a rubberstamp click. The step is now automated in reality, yet the map falsely records it as human-controlled.",
    "why_incorrect": {
      "A": "Prompt instructions remained unchanged and valid; the operational breakdown occurred in human review capacity at the verification gate.",
      "B": "The breakdown stems from human fatigue and volume saturation, not from an underlying foundational model regression or API update.",
      "C": "Context overload describes session token exhaustion in long chats, not the operational caseload distributed across human loan officers."
    },
    "full_justification": "Option D succeeds because an unstaffed gate occurs when excessive volume forces human reviewers to abandon substantive scrutiny, reducing formal verification to a perfunctory rubber-stamp. Option A is incorrect because prompt design did not trigger the audit failure. Option B is incorrect because platform model weights did not degrade. Option C is incorrect because the issue is human workload, not conversation token limits."
  },
  {
    "id": 10,
    "question": "A corporate facilities department restructures its office maintenance ticketing workflow. The supervisor discovers an impressive prompt-driven Skill that classifies incoming emails into a proprietary 9-category issue matrix. She redesigns the intake process to force all facility requests—ranging from minor stationery orders to emergency electrical failures—through this specific 9-category summary format. As a result, critical safety reports are delayed because contractors cannot parse the rigid layout. Which mapping failure does this redesign illustrate?",
    "options": {
      "A": "Mapping the tool instead of the work, by warping the operational process around an attractive software feature.",
      "B": "Unstaffed gate degradation, because maintenance engineers failed to inspect routine consumable orders in time.",
      "C": "Over-delegation, because mechanical dispatch routines were assigned to an unauthenticated external connector.",
      "D": "Halo delegation, because linguistic fluency in classification was conflated with emergency response routing.",
    },
    "correct": "A",
    "explanation": "Option A succeeds because mapping the tool instead of the work occurs when a team builds a workflow around an attractive feature or Skill they like, rather than around the actual operational needs of the organization. Bending emergency facility triage into a rigid 9-box template because the Skill produces that format compromises organizational safety.",
    "why_incorrect": {
      "B": "The breakdown was caused by structural process distortion at intake, not by engineers neglecting routine tickets under heavy volume.",
      "C": "Over-delegation involves assigning autonomous decisions without human gates, whereas here the failure is forcing diverse operational realities into a single tool template.",
      "D": "Halo delegation involves transferring authority across steps based on unrelated competence, rather than bending entire departmental pipelines to match a feature."
    },
    "full_justification": "Option A succeeds because mapping the tool instead of the work occurs when organizations distort their core operational procedures to accommodate an attractive software feature rather than business needs. Option B is incorrect because human review fatigue did not create the rigid intake format. Option C is incorrect because connector authentication was not the point of failure. Option D is incorrect because the error was architectural process warping, not halo delegation."
  }
]
