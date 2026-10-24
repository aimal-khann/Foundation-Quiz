# scripts/build_chapter5_part3.py
# Questions 21 to 30 for Chapter 5

questions_21_to_30 = [
  {
    "id": 21,
    "question": "An operations analyst transitions from Claude to ChatGPT to assist a project management office. In Claude, she frequently utilized external system integrations called \"connectors\" to read team schedules. While configuring her new ChatGPT workspace, she searches the settings menu for the same feature. Which operational reality should guide her configuration?",
    "options": {
      "A": "ChatGPT renamed its external integration feature to \"apps,\" serving the identical system connection purpose.",
      "B": "ChatGPT requires all external system queries to execute via manual developer cURL terminal commands in chat.",
      "C": "ChatGPT restricts third-party tool integrations strictly to enterprise users on dedicated raw API licenses.",
      "D": "ChatGPT deprecated external workspace integrations completely in favor of sandboxed Python calculation code."
    },
    "correct": "A",
    "explanation": "Option A succeeds because the reference text directly documents the vendor terminology shift: Claude uses the term connector, whereas ChatGPT uses app for the exact same functional category (and previously called them connectors). Both terms describe permissioned integrations that allow the assistant to reach, search, read, and act in external systems.",
    "why_incorrect": {
      "B": "Integrations are managed through user-facing UI configurations and OAuth authorization flows, not manual cURL commands in chat.",
      "C": "App integrations are broadly available within ChatGPT's workspace features and are not restricted exclusively to raw API developer endpoints.",
      "D": "ChatGPT has not deprecated third-party integrations; it actively supports them through apps built on the Apps SDK and Model Context Protocol."
    },
    "full_justification": "Option A succeeds because Claude's 'connectors' and ChatGPT's 'apps' represent the same functional category of permissioned external integrations governed by common protocol standards. Option B is incorrect because integrations use UI-driven OAuth flows rather than terminal cURL strings. Option C is incorrect because app integrations are native to chat workspaces. Option D is incorrect because integrations remain active and central to both platforms."
  },
  {
    "id": 22,
    "question": "An enterprise IT director presents the Model Context Protocol (MCP) to an executive security committee, describing it as \"the universal USB-C standard for AI tooling.\" A security auditor asks how this architectural protocol impacts institutional data trust and risk governance. What is the correct operational explanation?",
    "options": {
      "A": "MCP permanently restricts connected tools to read-only queries, preventing external actions across systems.",
      "B": "MCP eliminates user authorization tokens by verifying employee identity via local biometric computer keys.",
      "C": "MCP standardizes the connection plug between systems, but granting access remains a distinct trust decision.",
      "D": "MCP encrypts all transmitted corporate payloads, transferring data breach liability to protocol maintainers."
    },
    "correct": "C",
    "explanation": "Option C succeeds because it captures the critical distinction established in Concept 8: MCP is the open integration standard (\"USB-C for AI tools\"), providing a common plug so tools built once work across multiple assistants. However, \"the shorthand hides one thing you should not lose. Plugging in a USB-C cable is not a decision about trust. Connecting an MCP tool is. The plug is standard; the access is not\". Standardized technical plumbing does not eliminate the security and authorization decision.",
    "why_incorrect": {
      "A": "MCP supports both read operations and write/action operations, depending on tool definitions and granted scopes.",
      "B": "MCP servers require explicit authentication, permissions, and credential scoping rather than relying on biometric hardware bypasses.",
      "D": "Open protocols provide technical communication specifications; they do not assume commercial data liability or indemnify organizations against breaches."
    },
    "full_justification": "Option C succeeds because while MCP provides a vendor-neutral physical transport standard ('the plug'), deciding to expose organizational databases remains an independent authorization and risk determination. Option A is incorrect because MCP fully supports write mutations. Option B is incorrect because authentication tokens remain required. Option D is incorrect because open-source standards convey zero corporate indemnification."
  },
  {
    "id": 23,
    "question": "A financial analyst wishes to link an AI assistant to the firm’s central cloud storage repository to synthesize customer debt reconciliation ledgers. Before authorizing the connection within the workspace, which four operational questions must the analyst resolve under safe-use governance standards?",
    "options": {
      "A": "Which neural weights are active; how fast the server runs; what monthly token fees cost; who authored APIs.",
      "B": "What the tool can read; whether it can execute actions; whether source is trusted; if connection is allowed.",
      "C": "Whether the model passed benchmarks; if the interface uses dark mode; what country hosts; how many users exist.",
      "D": "How many parameters the model contains; whether it writes Python; if the vendor provides live 24/7 chat support."
    },
    "correct": "B",
    "explanation": "Option B succeeds because it recites the four mandatory pre-connection security questions established in the governance framework: 1. What can it read? 2. Can it write, send, delete, buy, or take some other action in the outside world? 3. Do I trust the source? 4. Am I allowed to connect this account or system?",
    "why_incorrect": {
      "A": "Server latency and API author identity do not evaluate operational data reach, external action risks, or institutional authorization.",
      "C": "Public benchmark scores and dark-mode UI support are irrelevant to enterprise security and permissions vetting.",
      "D": "Parameter counts and live support availability do not evaluate whether a connection breaches organizational data boundaries."
    },
    "full_justification": "Option B succeeds because the safe-use framework mandates evaluating data visibility (read scope), operational impact (action scope), publisher provenance (trust), and policy compliance (authorization). Options A, C, and D focus on cosmetic UI settings or irrelevant architectural specs that provide zero security vetting."
  },
  {
    "id": 24,
    "question": "A marketing specialist connects an approved workspace app to the firm's email marketing platform. She prompts the assistant: \"Inspect our draft campaign, correct grammatical typos in the subject lines, and send the final newsletter to all 5,000 subscribers.\" The assistant successfully corrects the text but displays a notice stating it cannot dispatch the email. The specialist submits a ticket to IT requesting that they \"grant sending permissions\" to the app. What is the most probable technical explanation?",
    "options": {
      "A": "The app was built exclusively with read and draft actions, meaning permissions cannot add an unbuilt sending capability.",
      "B": "The model's active context window was exhausted by the volume of recipient addresses in the marketing subscriber list.",
      "C": "The marketing platform's security firewall blocked the assistant due to suspicious character length in subject lines.",
      "D": "The user attempted to execute an external dispatch action using a speed-optimized model tier instead of a flagship."
    },
    "correct": "A",
    "explanation": "Option A succeeds because the curriculum establishes a fundamental technical boundary: a connector or app can only do what it was built to do. \"Permissions choose among the actions a tool has. They do not add new ones\". If an app was engineered exclusively to inspect and draft content, no administrative permission setting can grant it the programmatic capability to transmit outbound marketing emails.",
    "why_incorrect": {
      "B": "Drafting text succeeded; the blocker was the absence of an implemented tool-action endpoint for sending, not subscriber token counts.",
      "C": "The failure was an architectural capability limitation of the app itself, not an incoming network firewall block.",
      "D": "Model tiering governs reasoning depth and token processing; it does not inject missing software actions into external apps."
    },
    "full_justification": "Option A succeeds because tool permissions only enable or restrict pre-existing programmatic actions; administrative toggles cannot activate actions that developers never coded into the app. Option B is incorrect because recipient list size did not cause the action omission. Option C is incorrect because network firewalls do not generate application-level action warnings. Option D is incorrect because model tiers do not alter API schemas."
  },
  {
    "id": 25,
    "question": "An operations director establishes a standard query routing policy for a manufacturing firm. The team frequently handles four distinct inquiry profiles: Profile 1: Checking the spot market price of copper on the London Metal Exchange this morning. Profile 2: Evaluating the mathematical trade-offs between three complex warehouse inventory depreciation formulas. Profile 3: Compiling an exhaustive, cited competitive intelligence report on emerging sodium-ion battery market entrants. Profile 4: Retrieving the firm's internal, proprietary travel reimbursement policy from connected corporate drives. Which operational route allocation correctly aligns these profiles to their optimal workspace mechanisms?",
    "options": {
      "A": "Profile 1 to Thinking Mode; Profile 2 to Web Search; Profile 3 to Workplace Search; Profile 4 to Research Mode.",
      "B": "Profile 1 to Workplace Search; Profile 2 to Research Mode; Profile 3 to Web Search; Profile 4 to Thinking Mode.",
      "C": "Profile 1 to Web Search; Profile 2 to Thinking Mode; Profile 3 to Research Mode; Profile 4 to Workplace Search.",
      "D": "Profile 1 to Web Search; Profile 2 to Research Mode; Profile 3 to Thinking Mode; Profile 4 to Workplace Search."
    },
    "correct": "C",
    "explanation": "Option C succeeds because it precisely mirrors the four-part retrieval routing architecture: Profile 1 (One current fact): Routes to Web Search for rapid retrieval in seconds. Profile 2 (Hard reasoning, no new info): Routes to Thinking Mode for multi-step logical planning. Profile 3 (Thorough, cited multi-source investigation): Routes to Research Mode for autonomous, multi-minute investigation. Profile 4 (Internal organization knowledge): Routes to Workplace Search (or connected apps) to query proprietary company systems.",
    "why_incorrect": {
      "A": "It misroutes quick external facts to thinking mode and assigns internal proprietary file queries to autonomous web research.",
      "B": "It misroutes live spot commodity prices to internal workplace search and directs mathematical trade-offs to web research.",
      "D": "It misroutes closed-system mathematical reasoning to web research while assigning external market reports to thinking mode."
    },
    "full_justification": "Option C succeeds because it correctly maps query archetypes to retrieval mechanisms: immediate facts to Web Search, complex math to Thinking Mode, multi-source deep investigations to Research Mode, and internal documents to Workplace Search. Options A, B, and D misallocate compute latency and search scope."
  },
  {
    "id": 26,
    "question": "A junior analyst tasked with writing a market overview of carbon capture technology toggles on Research Mode. Ten minutes later, the assistant returns a comprehensive, multi-page report containing dozens of citations. When explaining the mechanics of this tool to a colleague, which statement accurately distinguishes Research Mode from standard Web Search?",
    "options": {
      "A": "Research Mode broadcasts standard search queries simultaneously across four competing commercial foundation models.",
      "B": "Research Mode utilizes a dedicated hardware supercomputer cluster that guarantees 100% factual accuracy on claims.",
      "C": "Research Mode searches an internal offline knowledge base of academic textbooks without connecting to the live web.",
      "D": "Research Mode executes an autonomous investigation that plans searches, follows leads, and synthesizes sources."
    },
    "correct": "D",
    "explanation": "Option D succeeds because the text emphasizes that research mode is not \"better search\". While standard web search retrieves immediate facts in seconds with one or two sources, Research Mode operates autonomously over minutes—formulating an investigative plan, executing multiple queries, following leads, synthesizing cross-source evidence, and compiling a structured, cited report.",
    "why_incorrect": {
      "A": "Research Mode is an autonomous search and synthesis workflow within a single model architecture, not a parallel query aggregator across competing vendor platforms.",
      "B": "No model tier or search tool guarantees 100% factual accuracy; models remain probabilistic and can misinterpret sources.",
      "C": "Research Mode searches the live, external web dynamically rather than being restricted to an offline internal textbook repository."
    },
    "full_justification": "Option D succeeds because Research Mode operates as an autonomous multi-step research loop (planning, query expansion, link traversal, cross-synthesis) rather than an instantaneous single-query lookup. Option A is incorrect because it does not query multi-vendor models simultaneously. Option B is incorrect because probabilistic synthesis never provides absolute factual guarantees. Option C is incorrect because Research Mode queries the live web."
  },
  {
    "id": 27,
    "question": "An energy consultant receives an autonomous research report on European hydrogen pipeline infrastructure generated via Research Mode. The report includes sixteen inline web citations and concludes with a definitive recommendation to invest in a specific municipal distribution network. How should the consultant approach the validation of this deliverable before presenting it to investors? (Select TWO.)",
    "options": {
      "A": "Open and inspect cited source links to confirm that underlying reference documents substantiate the factual assertions.",
      "B": "Accept the investment recommendation without review, because Research Mode models hold professional fiduciary covers.",
      "C": "Re-run the prompt in a temporary chat session to verify whether the second run outputs identical citation hyperlinks.",
      "D": "Independently evaluate recommendations, recognizing that autonomous research tools extend reach rather than custody."
    },
    "correct": "A and D",
    "explanation": "Options A and D succeed because they operationalize professional Diligence when evaluating research outputs: 1. Citation auditing: Practitioners must open and inspect cited links to confirm that the underlying source text genuinely supports the factual claims made in the report. 2. Non-transferable accountability: \"Research extends your reach. It does not move your accountability\". The human consultant remains fully responsible for recommendations delivered to investors.",
    "why_incorrect": {
      "B": "Foundation model providers explicitly disclaim fiduciary, legal, and operational liabilities.",
      "C": "Verifying whether two probabilistic runs produce identical links does not prove that either set of citations is factually accurate or reliable."
    },
    "full_justification": "Options A and D succeed because diligent governance requires auditing primary sources for evidentiary substantiation and maintaining human accountability for strategic advice. Option B is incorrect because software providers carry no fiduciary liability for business recommendations. Option C is incorrect because checking link consistency across stochastic runs does not prove factual validity."
  },
  {
    "id": 28,
    "question": "A program manager wants to determine whether an AI assistant can reliably take over the quarterly analysis of regional vocational training outcomes. Instead of testing the system on incoming unverified figures, she retrieves the raw dataset and approved report from two quarters ago. What is the primary operational advantage of structuring an initial AI test around completed, trusted historical work?",
    "options": {
      "A": "It enables the assistant to index private server infrastructure without requiring administrative security tokens.",
      "B": "It provides a definitive, known ground truth against which output accuracy and reasoning can be objectively audited.",
      "C": "It ensures that the foundation model provider permanently waives ongoing enterprise API consumption billing costs.",
      "D": "It automatically fine-tunes base neural network weights to match the program manager's personal drafting voice."
    },
    "correct": "B",
    "explanation": "Option B succeeds because Concept 9 establishes the core testing rule: test the assistant on work you have already finished and already trust. Testing on historical work provides known ground truth. \"Without known truth you cannot tell whether the assistant reproduced the work or just sounded like it did\".",
    "why_incorrect": {
      "A": "Running an evaluation prompt does not bypass administrative security credentials or grant backend network indexing rights.",
      "C": "Testing on historical datasets does not alter commercial software licensing terms or waive consumption fees.",
      "D": "Running prompts in a chat workspace does not fine-tune the base neural weights of the foundation model."
    },
    "full_justification": "Option B succeeds because historical benchmark work provides verified ground truth, enabling objective auditing of model accuracy versus superficial fluency. Option A is incorrect because evaluation tests do not bypass authentication credentials. Option C is incorrect because testing does not alter enterprise API pricing contracts. Option D is incorrect because conversational prompts do not retrain model weights."
  },
  {
    "id": 29,
    "question": "A healthcare data analyst follows the five-step proving loop, asking an AI assistant to reproduce a complex statistical report on patient clinic wait times using last year's verified data. After three iterations, the assistant accurately calculates average wait times and formats the tables correctly, but repeatedly fails to identify anomalous scheduling patterns caused by unrecorded doctor shift swaps. How should the analyst interpret this proving outcome? (Select TWO.)",
    "options": {
      "A": "The assistant passed testing completely and should immediately be granted autonomous scheduling authority across clinics.",
      "B": "The test revealed an unsupplied data limitation, because shift swap records sat entirely outside the provided dataset.",
      "C": "The anomaly identification step relies on inaccessible institutional context and should remain a human-retained task.",
      "D": "The failure proves that foundation models are fundamentally incapable of processing numerical healthcare spreadsheets."
    },
    "correct": "B and C",
    "explanation": "Options B and C succeed because they illustrate the two vital diagnostic insights of the proving loop: 1. Unsupplied data limits: If an analysis requires data that does not exist in the files (unrecorded shift swaps), the proving loop exposes a data gap rather than an AI defect. 2. Human retention: \"If the assistant still cannot do part of the work reliably, that part stays human... Learning what not to delegate is worth the hour\". Detecting unrecorded operational anomalies remains a human-retained responsibility.",
    "why_incorrect": {
      "A": "Failing a critical analytical component prohibits granting autonomous authority.",
      "D": "The assistant successfully computed averages and formatted tables, disproving the claim that models cannot parse healthcare spreadsheets."
    },
    "full_justification": "Options B and C succeed because the proving loop exposes that unrecorded organizational context represents an external data limitation, mandating that the nuanced anomaly-detection step remains human-retained. Option A is incorrect because partial analytical failure prohibits autonomous deployment. Option D is incorrect because successful average calculations disprove spreadsheet incompatibility."
  },
  {
    "id": 30,
    "question": "An engineering consultancy completes a successful evaluation of an assistant's ability to extract structural load calculations from legacy architectural drawings, achieving a 98% match against historical engineering audits. Encouraged by the test results, the lead partner prepares to deploy the workflow on live infrastructure projects. Which governance principles must remain active following this successful proving run? (Select TWO.)",
    "options": {
      "A": "Passing the historical test earns confidence for similar future work, but does not prove zero future error rates.",
      "B": "The engineering lead must continue to verify new results, stand behind deliverables, and disclose AI assistance.",
      "C": "Achieving a successful test match legally transfers liability for structural calculation flaws to developers.",
      "D": "The engineering firm may decommission all downstream human engineering review gates on live structural projects."
    },
    "correct": "A and B",
    "explanation": "Options A and B succeed because they reinforce the professional accountability boundaries governing successful AI evaluations: 1. Earned confidence, not absolute proof: Passing an evaluation gives tested confidence for similar future work, but does not guarantee that every future case will be error-free. 2. Human responsibility: Passing an evaluation never transfers accountability. Professionals must continue to verify new results, stand behind deliverables, disclose AI assistance appropriately, and maintain human control over high-risk decisions.",
    "why_incorrect": {
      "C": "Commercial AI software terms explicitly disclaim legal liability for downstream engineering determinations.",
      "D": "Decommissioning review gates on live structural engineering projects breaches professional engineering standards and introduces catastrophic liability."
    },
    "full_justification": "Options A and B succeed because successful proving runs establish empirical confidence without guaranteeing future infallibility, and professional fiduciary accountability requires continued verification of live deliverables. Option C is incorrect because AI developers carry no downstream professional engineering liability. Option D is incorrect because eliminating verification gates on physical infrastructure violates engineering governance."
  }
]
