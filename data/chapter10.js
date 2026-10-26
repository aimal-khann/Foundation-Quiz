// Chapter 10 Data - Normalized & Re-Balanced
window.CHAPTER_DATA = window.CHAPTER_DATA || {};
window.CHAPTER_DATA[10] = {
  "chapterId": 10,
  "title": "Chapter 10: Code You Never Write",
  "totalQuestions": 30,
  "questions": [
    {
      "id": 1,
      "question": "A procurement director receives a digital archive containing 120 supplier agreements. The director wants an AI assistant to identify which specific agreements omit a standard indemnity clause. The director considers pasting snippets conversationally to ask for a summary. According to workflow design principles, how should this specific operational task be classified and handled?",
      "options": {
        "A": "Treat it as an answer problem because evaluating legal text relies entirely on qualitative semantic judgment rather than arithmetic computation.",
        "B": "Treat it as a code problem because scanning numerous documents for specific structural deviations fires the volume and file processing signals.",
        "C": "Treat it as an answer problem because the provided contract dataset is small enough to fit within the active conversational context limits.",
        "D": "Treat it as a code problem because all contractual analyses mandate the deployment of deterministic script execution to ensure full compliance."
      },
      "correct": "B",
      "explanation": "Option B succeeds because the task triggers both the Volume and Files signals from the VPRF framework. While reading one single contract might be an answer problem, scanning 120 files for a specific structural deviation demands systematic processing that exceeds manual limits, categorizing it firmly as a code problem.",
      "why_incorrect": {
        "A": "volume fundamentally alters the nature of the task; human-led semantic judgment does not scale flawlessly across 120 documents without code assistance.",
        "C": "fitting within a token limit does not prevent a foundation model from skimming or superficially estimating data rather than systematically checking every single clause.",
        "D": "the task involves extracting text (omitted indemnity clauses), not executing arithmetic, yet it remains a code problem purely due to the VPRF signals (Volume/Files)."
      },
      "full_justification": "Option B succeeds because the task triggers both the Volume and Files signals from the VPRF framework. While reading one single contract might be an answer problem, scanning 120 files for a specific structural deviation demands systematic processing that exceeds manual limits, categorizing it firmly as a code problem. Option A is incorrect because volume fundamentally alters the nature of the task; human-led semantic judgment does not scale flawlessly across 120 documents without code assistance. Option C is incorrect because fitting within a token limit does not prevent a foundation model from skimming or superficially estimating data rather than systematically checking every single clause. Option D is incorrect because the task involves extracting text (omitted indemnity clauses), not executing arithmetic, yet it remains a code problem purely due to the VPRF signals (Volume/Files)."
    },
    {
      "id": 2,
      "question": "A regional sales director wants an AI agent to build a solution for branch managers. First, she requires a single downloadable spreadsheet merging last quarter's regional sales figures. Second, she requires an interactive, shareable web calculator that allows branch managers to estimate commission tiers. Which operational reality governs how the agent selects the programming languages for these tasks?",
      "options": {
        "A": "The director must explicitly dictate the programming language in the prompt to prevent the agent from defaulting to standard Python routines.",
        "B": "Requesting a downloadable spreadsheet requires Python, but interactive web calculators demand external software engineering interventions.",
        "C": "Requesting a downloadable spreadsheet automatically triggers Python execution, while requesting a shareable web calculator triggers JavaScript.",
        "D": "The foundation model relies on its static system prompt to determine the language, regardless of whether the output is a file or a web link."
      },
      "correct": "C",
      "explanation": "Option C succeeds because language choice is a technical judgment dictated entirely by the desired output format. When a user requests a data file, report, or cleaned spreadsheet, the AI naturally defaults to Python; when the user requests an interactive, clickable, or shareable web tool, it defaults to JavaScript/TypeScript.",
      "why_incorrect": {
        "A": "the curriculum strictly mandates never naming the programming language in the brief, as doing so usurps the model's technical judgment on the best tool for the job.",
        "B": "modern AI tools are highly capable of generating interactive JavaScript web artifacts within isolated side-panel sandboxes without requiring external engineering teams.",
        "D": "the model adapts its language choice dynamically based on the specific output requirements of the prompt, not a static system prompt limitation."
      },
      "full_justification": "Option C succeeds because language choice is a technical judgment dictated entirely by the desired output format. When a user requests a data file, report, or cleaned spreadsheet, the AI naturally defaults to Python; when the user requests an interactive, clickable, or shareable web tool, it defaults to JavaScript/TypeScript. Option A is incorrect because the curriculum strictly mandates never naming the programming language in the brief, as doing so usurps the model's technical judgment on the best tool for the job. Option B is incorrect because modern AI tools are highly capable of generating interactive JavaScript web artifacts within isolated side-panel sandboxes without requiring external engineering teams. Option D is incorrect because the model adapts its language choice dynamically based on the specific output requirements of the prompt, not a static system prompt limitation."
    },
    {
      "id": 3,
      "question": "A financial controller uploads an annual expense export into an AI assistant and prompts: \"Roughly how did my department's travel costs trend this year?\" The assistant immediately returns a fluent, highly confident summary outlining a slight upward trend in travel expenditure. Which TWO statements correctly describe the operational risk and the required remediation for this interaction? (Select TWO.)",
      "options": {
        "A": "The controller must use explicit phrasing like \"write and run code\" to force deterministic calculation over probabilistic estimation.",
        "B": "The controller must specify the exact mathematical libraries required to prevent the model from using outdated calculation methodologies.",
        "C": "The model likely provided an estimate based on a superficial scan, which appears identical in confidence to a calculated numerical total.",
        "D": "The model automatically defaults to code execution whenever the user uploads a spreadsheet containing more than fifty numerical data rows."
      },
      "correct": "A and C",
      "explanation": "Options A and C succeed because asking \"roughly how did my costs trend\" permits the model to glance at the data and probabilistically estimate the result. This estimate is delivered with high confidence, masking the lack of rigorous computation. To prevent this silent failure when precision matters, the user must mandate exact calculation by explicitly stating: \"write and run code\".",
      "why_incorrect": {
        "B": "specifying technical libraries violates the rule of briefing the problem rather than the program (over-managing the how).",
        "D": "foundation models do not automatically default to code execution based on file size alone; they decide based on the phrasing and apparent precision required by the user's prompt."
      },
      "full_justification": "Options A and C succeed because asking \"roughly how did my costs trend\" permits the model to glance at the data and probabilistically estimate the result. This estimate is delivered with high confidence, masking the lack of rigorous computation. To prevent this silent failure when precision matters, the user must mandate exact calculation by explicitly stating: \"write and run code\". Option B is incorrect because specifying technical libraries violates the rule of briefing the problem rather than the program (over-managing the how). Option D is incorrect because foundation models do not automatically default to code execution based on file size alone; they decide based on the phrasing and apparent precision required by the user's prompt."
    },
    {
      "id": 4,
      "question": "An HR associate uploads a messy, 5,000-row payroll spreadsheet into a conversational agent workspace. Before requesting any specific deductions or overtime calculations, the associate needs to verify that the agent has actually read and parsed the dataset, rather than generating a superficial statistical estimate. Which prompt establishes immediate, verifiable proof of file ingestion?",
      "options": {
        "A": "\"Execute the data analysis in an isolated sandbox environment and provide a downloadable log file detailing every computational step.\"",
        "B": "\"Run a preliminary statistical summary of the file and output the median, mean, and standard deviation for all numerical variables present.\"",
        "C": "\"Analyze the uploaded file using only deterministic Python code and confirm that no probabilistic text generation techniques were utilized.\"",
        "D": "\"Before analyzing anything, tell me the exact row count, the specific column names, and the complete date range of the uploaded data file.\""
      },
      "correct": "D",
      "explanation": "Option D succeeds because it deploys the \"cheapest lie detector\". By demanding the exact row count, column names, and date range before any analysis begins, the user forces the model to execute a read script on the file. If the model hallucinates or estimates from a glance, these specific metadata points will be immediately and obviously wrong.",
      "why_incorrect": {
        "A": "requesting exhaustive log files introduces unnecessary technical overhead without providing an immediate, readable proof of ingestion.",
        "B": "requesting statistical summaries does not prevent the model from estimating those summaries without actually executing code.",
        "C": "explicitly banning probabilistic text generation does not physically compel the model to parse the file; it merely alters the conversational tone."
      },
      "full_justification": "Option D succeeds because it deploys the \"cheapest lie detector\". By demanding the exact row count, column names, and date range before any analysis begins, the user forces the model to execute a read script on the file. If the model hallucinates or estimates from a glance, these specific metadata points will be immediately and obviously wrong. Option A is incorrect because requesting exhaustive log files introduces unnecessary technical overhead without providing an immediate, readable proof of ingestion. Option B is incorrect because requesting statistical summaries does not prevent the model from estimating those summaries without actually executing code. Option C is incorrect because explicitly banning probabilistic text generation does not physically compel the model to parse the file; it merely alters the conversational tone."
    },
    {
      "id": 5,
      "question": "A university administrator drafts a brief instructing an agent to reconcile student attendance logs against final examination eligibility. The brief clearly articulates the Goal, details the Input file formats, specifies the desired Output report, and outlines the institutional Rules defining valid absences. During execution, the script crashes repeatedly because several student records contain blank date fields, which the agent attempts to parse as string characters. Which section of the professional code brief was fatally omitted?",
      "options": {
        "A": "The Goal section, because it failed to explicitly articulate the overarching administrative objective behind the attendance reconciliation.",
        "B": "The Input section, because it neglected to specify the exact file format and structural schema of the uploaded student transcript datasets.",
        "C": "The Edge cases section, because it failed to establish advance decisions for handling imperfect, incomplete, or corrupted data rows entirely.",
        "D": "The Rules section, because it omitted the specific pedagogical constraints and professional parameters required for academic grading systems."
      },
      "correct": "C",
      "explanation": "Option C succeeds because the Edge cases section of a professional code brief is specifically designed to handle imperfect data, such as blank fields, duplicates, or corrupted strings, by deciding in advance what the code should do. By failing to decide how to handle blank dates, the administrator allowed the script to crash when it encountered unexpected data types.",
      "why_incorrect": {
        "A": "the Goal section clarifies the objective for the human and the AI, but it does not dictate low-level data-handling logic.",
        "B": "the Input section describes what is being handed over, not how to process structural flaws within it.",
        "D": "Rules cover assumed professional knowledge (e.g., specific grading policies), whereas Edge cases handle data corruption and formatting failures."
      },
      "full_justification": "Option C succeeds because the Edge cases section of a professional code brief is specifically designed to handle imperfect data, such as blank fields, duplicates, or corrupted strings, by deciding in advance what the code should do. By failing to decide how to handle blank dates, the administrator allowed the script to crash when it encountered unexpected data types. Option A is incorrect because the Goal section clarifies the objective for the human and the AI, but it does not dictate low-level data-handling logic. Option B is incorrect because the Input section describes what is being handed over, not how to process structural flaws within it. Option D is incorrect because Rules cover assumed professional knowledge (e.g., specific grading policies), whereas Edge cases handle data corruption and formatting failures."
    },
    {
      "id": 6,
      "question": "A procurement manager drafts a brief to process a monthly supplier invoice dataset. The manager must define both the unstated business knowledge required to parse the data and the contingency instructions for malformed entries. Which TWO statements correctly differentiate the required sections of this brief? (Select TWO.)",
      "options": {
        "A": "Rules encompass professional constraints that a stranger would not know, such as defining \"Pending\" as \"not yet submitted\" in the system.",
        "B": "Edge cases represent advance decisions about handling imperfect data, such as instructing the model to skip rows lacking transaction dates.",
        "C": "Rules dictate the specific error-handling routines the model must execute when encountering corrupted alphanumeric characters in a dataset.",
        "D": "Edge cases encompass overarching business logic, such as defining the fiscal calendar start date for an internal financial reconciliation."
      },
      "correct": "A and B",
      "explanation": "Options A and B succeed because they correctly define the two most critical components of a professional code brief. Rules contain the professional constraints that a stranger (or a machine) would not inherently know. Edge cases dictate exactly what the code should do when it encounters imperfect data, preventing silent errors or execution crashes.",
      "why_incorrect": {
        "C": "error-handling routines for corrupted data belong strictly in the Edge cases section, not the Rules section.",
        "D": "defining overarching business logic, such as a fiscal calendar start date, belongs in the Rules section, not Edge cases."
      },
      "full_justification": "Options A and B succeed because they correctly define the two most critical components of a professional code brief. Rules contain the professional constraints that a stranger (or a machine) would not inherently know. Edge cases dictate exactly what the code should do when it encounters imperfect data, preventing silent errors or execution crashes. Option C is incorrect because error-handling routines for corrupted data belong strictly in the Edge cases section, not the Rules section. Option D is incorrect because defining overarching business logic, such as a fiscal calendar start date, belongs in the Rules section, not Edge cases."
    },
    {
      "id": 7,
      "question": "A marketing analyst receives a raw CRM export spanning three years. The data was compiled by multiple regional offices, and the analyst suspects it contains severe formatting inconsistencies, mixed currency symbols, and duplicated entries. What is the most rigorous operational step the analyst should take before defining the Edge cases in the final code brief?",
      "options": {
        "A": "Instructing the agent to examine the files and report any unclear, inconsistent, or surprising elements before finalizing the code brief.",
        "B": "Restricting the dataset to a ten-row sample to minimize processing costs during the initial exploratory data analysis compilation phase.",
        "C": "Executing a cross-model check by uploading the same file to two separate foundation models to ensure consistent baseline parsing integrity.",
        "D": "Requesting a plain-English replay of the proposed computational logic to ensure the agent understands the underlying business objectives."
      },
      "correct": "A",
      "explanation": "Option A succeeds because when a user does not know what is hiding in their data, they must make discovery the first prompt. Instructing the AI to inspect the file for inconsistencies allows the analyst to write the Edge cases section using actual empirical knowledge rather than blind imagination.",
      "why_incorrect": {
        "B": "restricting the file to a small ten-row sample might completely miss the specific anomalies hiding deeper in the wider dataset.",
        "C": "cross-model checking is used to verify final, high-stakes outputs (Concept 6), not to perform initial exploratory data analysis to find data messiness.",
        "D": "a plain-English replay verifies the computational logic after the code has been written and executed, not before the brief is finalized."
      },
      "full_justification": "Option A succeeds because when a user does not know what is hiding in their data, they must make discovery the first prompt. Instructing the AI to inspect the file for inconsistencies allows the analyst to write the Edge cases section using actual empirical knowledge rather than blind imagination. Option B is incorrect because restricting the file to a small ten-row sample might completely miss the specific anomalies hiding deeper in the wider dataset. Option C is incorrect because cross-model checking is used to verify final, high-stakes outputs (Concept 6), not to perform initial exploratory data analysis to find data messiness. Option D is incorrect because a plain-English replay verifies the computational logic after the code has been written and executed, not before the brief is finalized."
    },
    {
      "id": 8,
      "question": "An auditor who has never studied programming receives a completed Python script designed to reconcile monthly corporate bank statements against internal ledgers. The script executes without errors and generates a final discrepancy figure. Which TWO verification moves correctly establish professional trust in the script's accuracy without requiring the auditor to read the underlying syntax? (Select TWO.)",
      "options": {
        "A": "Running the script on a historical month's data subset where the auditor independently knows the correct discrepancy calculation total.",
        "B": "Exporting the Python code into a local development environment and utilizing static analysis tools to verify underlying syntax integrity.",
        "C": "Instructing the foundation model to cross-reference its generated script against established open-source algorithmic data repositories.",
        "D": "Requesting a plain-English replay where the model explains its step-by-step processing logic to a non-technical organizational colleague."
      },
      "correct": "A and D",
      "explanation": "Options A and D succeed because they represent the primary methods for verifying code without reading syntax. The known-answer test (A) proves the script's mathematical accuracy by checking it against a previously verified sub-result. The plain-English replay (D) forces the model to explain its processing steps, allowing the domain expert to audit the logic for professional soundness without knowing Python.",
      "why_incorrect": {
        "B": "exporting and running static analysis tools requires the exact technical programming knowledge that the user explicitly does not possess.",
        "C": "cross-referencing against open-source repositories does not verify whether the script accurately applies the user's highly specific proprietary business rules."
      },
      "full_justification": "Options A and D succeed because they represent the primary methods for verifying code without reading syntax. The known-answer test (A) proves the script's mathematical accuracy by checking it against a previously verified sub-result. The plain-English replay (D) forces the model to explain its processing steps, allowing the domain expert to audit the logic for professional soundness without knowing Python. Option B is incorrect because exporting and running static analysis tools requires the exact technical programming knowledge that the user explicitly does not possess. Option C is incorrect because cross-referencing against open-source repositories does not verify whether the script accurately applies the user's highly specific proprietary business rules."
    },
    {
      "id": 9,
      "question": "A clinic manager commissions a script to analyze a year of patient appointment data to identify no-show trends by day and hour. The agent successfully writes and runs the Python code, but the result is returned as a dense, unformatted block of terminal text that cannot be easily shared with the clinical partners. Which principle of professional brief construction was violated?",
      "options": {
        "A": "The user neglected to request an HTML formatted page in the Output section to ensure a designed, shareable, and readable document format.",
        "B": "The user failed to specify the required Python data visualization libraries in the Input section of the five-part code execution brief.",
        "C": "The user omitted the markdown rendering tags within the Rules section, causing the model to default to raw text string output structures.",
        "D": "The user utilized an enterprise agent surface that inherently restricts the generation of graphical user interfaces for network security."
      },
      "correct": "A",
      "explanation": "Option A succeeds because the Output section of the brief strictly dictates the format of the deliverable. To ensure a result that a human will easily read and share, the user must explicitly ask for an HTML page or a structured report. If left unspecified, the script will simply output standard, unformatted terminal text.",
      "why_incorrect": {
        "B": "specifying technical libraries violates the core principle of briefing the problem rather than over-managing the program.",
        "C": "formatting requests belong directly in the Output section, not the Rules section.",
        "D": "enterprise agents are fully capable of rendering HTML and Markdown artifacts; the failure was entirely in the instruction, not the execution surface."
      },
      "full_justification": "Option A succeeds because the Output section of the brief strictly dictates the format of the deliverable. To ensure a result that a human will easily read and share, the user must explicitly ask for an HTML page or a structured report. If left unspecified, the script will simply output standard, unformatted terminal text. Option B is incorrect because specifying technical libraries violates the core principle of briefing the problem rather than over-managing the program. Option C is incorrect because formatting requests belong directly in the Output section, not the Rules section. Option D is incorrect because enterprise agents are fully capable of rendering HTML and Markdown artifacts; the failure was entirely in the instruction, not the execution surface."
    },
    {
      "id": 10,
      "question": "A team leader wants to automate the process of splitting Friday team lunch bills equally among attending staff members, automatically applying a standard 15% gratuity to the total before division. The leader attempts to write a custom code brief to construct a Python script for this task. According to workflow selection principles, why is commissioning custom code sub-optimal for this specific problem?",
      "options": {
        "A": "The task requires real-time network access to external financial institutions, which exceeds the scope of isolated sandbox execution tools.",
        "B": "The task demands advanced algorithmic reasoning capabilities that severely surpass the zero-shot baseline of modern foundation models.",
        "C": "The task involves sensitive financial information, triggering mandatory data compliance protocols that prohibit cloud-based scripting runs.",
        "D": "The task relies on standardized mathematical rules shared by everyone, making it perfectly suited for an existing off-the-shelf application."
      },
      "correct": "D",
      "explanation": "Option D succeeds because this task explicitly fails the \"off-the-shelf-app test\". Splitting a bill is a universal problem with standardized rules, meaning dedicated commercial applications (like Splitwise) already exist to handle it perfectly. Custom AI code briefs should be reserved for a \"market of one\"\u2014problems involving highly specific, proprietary business rules that no commercial app accommodates.",
      "why_incorrect": {
        "A": "splitting a bill conceptually does not inherently require live network integration with banking APIs.",
        "B": "calculating division and percentages is elementary arithmetic, not advanced algorithmic reasoning.",
        "C": "standard lunch bills do not typically invoke enterprise data compliance protocols or regulatory prohibitions. Please review"
      },
      "full_justification": "Option D succeeds because this task explicitly fails the \"off-the-shelf-app test\". Splitting a bill is a universal problem with standardized rules, meaning dedicated commercial applications (like Splitwise) already exist to handle it perfectly. Custom AI code briefs should be reserved for a \"market of one\"\u2014problems involving highly specific, proprietary business rules that no commercial app accommodates. Option A is incorrect because splitting a bill conceptually does not inherently require live network integration with banking APIs. Option B is incorrect because calculating division and percentages is elementary arithmetic, not advanced algorithmic reasoning. Option C is incorrect because standard lunch bills do not typically invoke enterprise data compliance protocols or regulatory prohibitions. Please review"
    },
    {
      "id": 11,
      "question": "An operations director at a regional healthcare cooperative reviews a delegation map for the patient intake scheduling workflow. The map was drafted six months ago and names the entire patient-access committee as the collective authority for workflow integrity. Although no clinical incidents have been reported, booking dispute backlogs have steadily increased. What governance failure caused this control framework to decay?",
      "options": {
        "A": "The clinic failed to deploy an autonomous scheduling agent equipped with real-time electronic health record connectors.",
        "B": "The delegation map omitted a named individual owner answerable for matching documented steps to live reality.",
        "C": "The foundation model provider updated its core system prompt, causing the underlying conversational weights to drift.",
        "D": "The patient-access committee failed to mandate that intake coordinators utilize incognito browser windows during shifts."
      },
      "correct": "B",
      "explanation": "Option B succeeds because a delegation map decays silently without alarms; review gates turn into glances, and documents diverge from reality. The foundational safeguard against this decay is naming a single, accountable map owner (one individual, not a broad committee) and setting a fixed scheduled read date. Assigning collective authority to a committee ensures that no specific individual is answerable for auditing the map against daily clinical practice.",
      "why_incorrect": {
        "A": "jumping to autonomous agent integrations is a premature technical leap that worsens governance risks when basic process ownership has not been established.",
        "C": "foundation model system prompt updates cause behavioral shifts, but do not explain the gradual internal procedural divergence of human booking teams.",
        "D": "incognito sessions manage data persistence and session history; they do not govern workflow map maintenance or step accountability."
      },
      "full_justification": "Option B succeeds because a delegation map decays silently without alarms; review gates turn into glances, and documents diverge from reality. The foundational safeguard against this decay is naming a single, accountable map owner (one individual, not a broad committee) and setting a fixed scheduled read date. Assigning collective authority to a committee ensures that no specific individual is answerable for auditing the map against daily clinical practice. Option A is incorrect because jumping to autonomous agent integrations is a premature technical leap that worsens governance risks when basic process ownership has not been established. Option C is incorrect because foundation model system prompt updates cause behavioral shifts, but do not explain the gradual internal procedural divergence of human booking teams. Option D is incorrect because incognito sessions manage data persistence and session history; they do not govern workflow map maintenance or step accountability."
    },
    {
      "id": 12,
      "question": "A compliance supervisor conducts a scheduled quarterly review of an insurance underwriting delegation map. The map classifies the risk-tier scoring step as collaborative, listing a senior underwriter as the reviewer. Which audit question provides the most reliable empirical evidence of whether this collaborative gate remains genuinely operational?",
      "options": {
        "A": "\"Does the underwriting policy manual still mandate senior review for risk-tier scores before policy issuance?\"",
        "B": "\"Who reviewed the flagged risk-tier scores last week, and how many minutes did they spend inspecting each file?\"",
        "C": "\"What did the prompt-engineering logs indicate regarding underwriter conversational satisfaction over the quarter?\"",
        "D": "\"Has the underwriting team attended the mandatory annual webinar on generative artificial intelligence ethics?\""
      },
      "correct": "B",
      "explanation": "Option B succeeds because the defining question of a scheduled map read is: For every collaborative step: who reviewed it last week, and how long did they spend? Asking about concrete historical reality (\"last week\") uncovers whether the gate is genuinely staffed or has degraded into an empty, rubber-stamped glance. If nobody can name the reviewer or the time spent, the step has become automated in practice regardless of what documentation claims.",
      "why_incorrect": {
        "A": "checking the policy manual only verifies what the organization designed or intended on paper, rather than what is actually occurring on the operational floor.",
        "C": "prompt engineering logs and conversational satisfaction metrics track user sentiment, not factual compliance verification at a risk gate.",
        "D": "training attendance records confirm educational compliance, but fail to provide empirical evidence of active gate execution."
      },
      "full_justification": "Option B succeeds because the defining question of a scheduled map read is: For every collaborative step: who reviewed it last week, and how long did they spend? Asking about concrete historical reality (\"last week\") uncovers whether the gate is genuinely staffed or has degraded into an empty, rubber-stamped glance. If nobody can name the reviewer or the time spent, the step has become automated in practice regardless of what documentation claims. Option A is incorrect because checking the policy manual only verifies what the organization designed or intended on paper, rather than what is actually occurring on the operational floor. Option C is incorrect because prompt engineering logs and conversational satisfaction metrics track user sentiment, not factual compliance verification at a risk gate. Option D is incorrect because training attendance records confirm educational compliance, but fail to provide empirical evidence of active gate execution."
    },
    {
      "id": 13,
      "question": "A business intelligence analyst builds an internal analytics tool using a prompt-and-iterate cycle (ideate, prototype, feedback, refine). She executes Cycle 1 in a temporary chat, Cycle 2 in a desktop text editor, and Cycle 3 in a different departmental chat workspace. Although individual responses look promising, the final prototype produces conflicting metrics that fail to integrate. What operational mistake corrupted the build loop?",
      "options": {
        "A": "Failing to write Python unit testing scripts before attempting to prompt the model for interactive chart components.",
        "B": "Selecting a commercial foundation model rather than building a custom fine-tuned open-source neural network.",
        "C": "Scattering iterative cycles across isolated environments instead of executing the loop inside a dedicated Project workspace.",
        "D": "Attempting to prototype interactive analytical dashboards without provisioning cloud-hosted database connectors."
      },
      "correct": "C",
      "explanation": "Option C succeeds because the build loop (ideate, prototype, feedback, refine) must run inside a stable workspace (such as a Project) so that background assumptions, constraints, and prior refinements remain grounded. Scattering rounds across ad-hoc chats, local text files, and separate workspaces forces each cycle to restart from a slightly different context, resulting in a fragmented pile of incompatible drafts rather than a coherent tool.",
      "why_incorrect": {
        "A": "the rapid build loop utilizes conversational prototyping and artifacts to explore requirements before committing to formal code unit tests.",
        "B": "standard commercial foundation models are fully capable of generating functional prototypes; fine-tuning a custom network is an expensive, unnecessary detour.",
        "D": "web artifacts are designed as lightweight, self-contained prototypes; requiring live database connections defeats their primary purpose as rapid, low-friction sandboxes."
      },
      "full_justification": "Option C succeeds because the build loop (ideate, prototype, feedback, refine) must run inside a stable workspace (such as a Project) so that background assumptions, constraints, and prior refinements remain grounded. Scattering rounds across ad-hoc chats, local text files, and separate workspaces forces each cycle to restart from a slightly different context, resulting in a fragmented pile of incompatible drafts rather than a coherent tool. Option A is incorrect because the rapid build loop utilizes conversational prototyping and artifacts to explore requirements before committing to formal code unit tests. Option B is incorrect because standard commercial foundation models are fully capable of generating functional prototypes; fine-tuning a custom network is an expensive, unnecessary detour. Option D is incorrect because web artifacts are designed as lightweight, self-contained prototypes; requiring live database connections defeats their primary purpose as rapid, low-friction sandboxes."
    },
    {
      "id": 14,
      "question": "A financial planning associate asks an assistant to draft a quarterly operating budget forecast. The prompt instructs: \"Analyse historical departmental travel expenses from the attached spreadsheet, calculate the compound quarterly growth rate, and recommend a department spending ceiling in your written report.\" The assistant returns an executive memorandum containing a recommended \u00a345,000 ceiling supported by detailed written narrative calculations. What structural flaw undermines this deliverable?",
      "options": {
        "A": "The associate omitted few-shot demonstration exemplars of approved financial budget narratives.",
        "B": "The prompt failed to specify whether the spending ceiling should be formatted in euros or British pounds.",
        "C": "Large language models lack the baseline cognitive capability to comprehend multi-department travel logs.",
        "D": "The compound growth figures were generated as prose text rather than calculated via code execution."
      },
      "correct": "D",
      "explanation": "Option D succeeds because of the foundational planning maxim: If a result matters, compute it. Never write it. Large language models can perform arithmetic, but a generated prose figure and a calculated figure look identical on the page. Whenever financial ceilings or critical metrics govern a plan, the calculation must be executed via code execution to ensure auditable, deterministic computation rather than statistical prose generation.",
      "why_incorrect": {
        "A": "adding few-shot exemplars improves narrative styling, but does not solve the underlying risk of prose-generated mathematical hallucinations.",
        "B": "currency formatting is a superficial presentation detail; the structural defect is writing a mathematical calculation in text rather than executing code.",
        "C": "lLMs routinely parse structured financial logs; the limitation lies in syntactic math generation versus deterministic computation."
      },
      "full_justification": "Option D succeeds because of the foundational planning maxim: If a result matters, compute it. Never write it. Large language models can perform arithmetic, but a generated prose figure and a calculated figure look identical on the page. Whenever financial ceilings or critical metrics govern a plan, the calculation must be executed via code execution to ensure auditable, deterministic computation rather than statistical prose generation. Option A is incorrect because adding few-shot exemplars improves narrative styling, but does not solve the underlying risk of prose-generated mathematical hallucinations. Option B is incorrect because currency formatting is a superficial presentation detail; the structural defect is writing a mathematical calculation in text rather than executing code. Option C is incorrect because lLMs routinely parse structured financial logs; the limitation lies in syntactic math generation versus deterministic computation."
    },
    {
      "id": 15,
      "question": "An operations team uses an assistant to build a web artifact that visualizes daily shipping container throughput across three port terminals. During Cycle 1, the assistant generates a clean dashboard with three interactive bar charts. During Cycle 2, the team requests a terminal comparison filter and a grand total volume summary. The deliverable arrives with elegant styling, functional interactive buttons, and correctly rendered figures; however, an audit reveals the grand total figure is understated by 15%. Why did this failure evade detection during preliminary testing?",
      "options": {
        "A": "The assistant suffered from complete context window amnesia due to ingesting excessive visual HTML styling tags.",
        "B": "The underlying web browser interface dropped mathematical floating-point precision during chart rendering.",
        "C": "Plausible, well-formatted prose numbers carry no visual signature of arithmetic fabrication on the page.",
        "D": "Interactive web artifacts automatically strip numerical calculation formulas from the chat interface."
      },
      "correct": "C",
      "explanation": "Option C succeeds because Cycle 2 represents the classic silent failure mode in a build loop. Unlike code syntax bugs that crash visibly with error messages, written-not-computed figures fail with zero noise. The output appeared polished, well-formatted, and completely plausible, allowing a material 15% arithmetic error to pass superficial inspection unnoticed.",
      "why_incorrect": {
        "A": "context window exhaustion causes amnesia, truncated code, or broken syntax, not a beautifully styled dashboard with subtle calculation drift.",
        "B": "modern web rendering engines do not arbitrarily lose floating-point precision on basic summation; the error was generated by the language model drafting text.",
        "D": "interactive artifacts execute client-side scripts; they do not automatically strip or alter underlying mathematical formulas."
      },
      "full_justification": "Option C succeeds because Cycle 2 represents the classic silent failure mode in a build loop. Unlike code syntax bugs that crash visibly with error messages, written-not-computed figures fail with zero noise. The output appeared polished, well-formatted, and completely plausible, allowing a material 15% arithmetic error to pass superficial inspection unnoticed. Option A is incorrect because context window exhaustion causes amnesia, truncated code, or broken syntax, not a beautifully styled dashboard with subtle calculation drift. Option B is incorrect because modern web rendering engines do not arbitrarily lose floating-point precision on basic summation; the error was generated by the language model drafting text. Option D is incorrect because interactive artifacts execute client-side scripts; they do not automatically strip or alter underlying mathematical formulas."
    },
    {
      "id": 16,
      "question": "An analyst builds a lightweight web artifact that tracks software licence renewal deadlines across twenty internal business units. Over eight months, four separate corporate departments begin opening the tool daily, and the chief information officer relies on its exported renewal calendar for executive vendor renegotiations. What operational milestone has this tool reached?",
      "options": {
        "A": "It has triggered the escalation signal, outgrowing prompt-and-iterate into engineered infrastructure.",
        "B": "It has reached an architectural ceiling that warrants immediate model fine-tuning and parameter retraining.",
        "C": "It has experienced halo delegation, requiring all tabular schedules to be converted into text prompts.",
        "D": "It has suffered from stale configuration, requiring the knowledge base to be scrubbed of expired contracts."
      },
      "correct": "A",
      "explanation": "Option A succeeds because dependency is the escalation signal. The moment multiple outside departments and executive leaders begin relying on an ad-hoc prompt artifact as production infrastructure, the tool has outgrown prompt-and-iterate. It now demands software engineering controls: guaranteed uptime, robust access permissions, formal change management, and dedicated maintenance support.",
      "why_incorrect": {
        "B": "an expectation mismatch occurs when a user asks a model to perform an impossible task (such as predicting exact future lottery numbers), not when a successful tool expands in usage.",
        "C": "halo delegation is an error in step assignment (giving AI approval authority because its drafting was good), not the operational scaling of an artifact.",
        "D": "stale configuration refers to out-of-date instructions or reference files, which is not the issue when an operational tool experiences widespread user adoption."
      },
      "full_justification": "Option A succeeds because dependency is the escalation signal. The moment multiple outside departments and executive leaders begin relying on an ad-hoc prompt artifact as production infrastructure, the tool has outgrown prompt-and-iterate. It now demands software engineering controls: guaranteed uptime, robust access permissions, formal change management, and dedicated maintenance support. Option B is incorrect because an expectation mismatch occurs when a user asks a model to perform an impossible task (such as predicting exact future lottery numbers), not when a successful tool expands in usage. Option C is incorrect because halo delegation is an error in step assignment (giving AI approval authority because its drafting was good), not the operational scaling of an artifact. Option D is incorrect because stale configuration refers to out-of-date instructions or reference files, which is not the issue when an operational tool experiences widespread user adoption."
    },
    {
      "id": 17,
      "question": "An automation lead identifies two distinct operational patterns within their organization. Workflow Alpha involves formatting weekly vendor compliance reports identically every Friday. Workflow Beta involves a lightweight data-visualization dashboard that the entire regional sales team has begun relying upon for daily pricing negotiations. How should these two workflows be operationally managed?",
      "options": {
        "A": "Workflow Alpha requires immediate escalation to full software engineering, while Workflow Beta should be retained as an unmanaged ad-hoc conversational prompt template.",
        "B": "Workflow Alpha should be standardized into a configured Skill or worker, while Workflow Beta has triggered the escalation signal requiring mission-critical infrastructure controls.",
        "C": "Both workflows should be recalled to human execution because multi-departmental dependency automatically invalidates lightweight prompt-based prototyping environments.",
        "D": "Workflow Alpha requires custom foundation model fine-tuning, while Workflow Beta should be migrated into an isolated local desktop editor to prevent organizational data leakage."
      },
      "correct": "B",
      "explanation": "Option B succeeds because the curriculum draws a strict boundary between two signals: I have solved this the same way three times (Workflow Alpha) means the workflow shape is stable and can be standardized into a configured worker/Skill. Other people now depend on this (Workflow Beta) means the tool has become infrastructure and must be escalated to professional software engineering.",
      "why_incorrect": {
        "A": "it reverses the escalation signal: solving a report repeatedly calls for configuration/Skills, whereas enterprise dependency demands formal engineering.",
        "C": "reclaiming Alpha wastes human time on a stable, delegable pattern, while turning Beta into an unmonitored prompt ignores the infrastructure risk of multi-team dependency.",
        "D": "lightweight artifacts are fully valid for rapid prototyping; they simply require escalation once they cross into mission-critical infrastructure."
      },
      "full_justification": "Option B succeeds because the curriculum draws a strict boundary between two signals: I have solved this the same way three times (Workflow Alpha) means the workflow shape is stable and can be standardized into a configured worker/Skill. Other people now depend on this (Workflow Beta) means the tool has become infrastructure and must be escalated to professional software engineering. Option A is incorrect because it reverses the escalation signal: solving a report repeatedly calls for configuration/Skills, whereas enterprise dependency demands formal engineering. Option C is incorrect because reclaiming Alpha wastes human time on a stable, delegable pattern, while turning Beta into an unmonitored prompt ignores the infrastructure risk of multi-team dependency. Option D is incorrect because lightweight artifacts are fully valid for rapid prototyping; they simply require escalation once they cross into mission-critical infrastructure."
    },
    {
      "id": 18,
      "question": "A risk modeling actuary delegates the estimation of storm damage liabilities to a Claude Code terminal agent equipped with a Python execution environment. The actuary reasons that because the agent calculates the liabilities deterministically in a sandbox rather than generating them as text, the workflow ownership has been successfully transferred to the AI. Which TWO statements correctly challenge this reasoning? (Select TWO.)",
      "options": {
        "A": "Sandboxed execution environments automatically strip semantic contextual parameters, rendering downstream actuarial risk outputs statistically ungrounded.",
        "B": "Implementation mechanics (such as deterministic code execution sandboxes) can never serve as valid criteria for transferring ultimate operational task ownership.",
        "C": "Terminal execution environments require secondary model API authentication before statistical scripts can access third-party meteorological telemetry tables.",
        "D": "The generated script might still reference the wrong data column or misapply institutional thresholds, requiring immediate downstream expert human review."
      },
      "correct": "B and D",
      "explanation": "Options B and D succeed because: Layer separation: The mapping layers must remain strictly sequential: Eligibility, Ownership, and Implementation. \"Carried by code execution\" is an implementation choice; it is never an ownership criterion and cannot justify transferring operational accountability to the AI. Downstream gates: Running arithmetic in a sandbox ensures calculation precision, but the code can still reference the wrong data column or misapply a threshold. Delegating a high-stakes calculation is safe only if an explicit human review gate immediately inspects the output.",
      "why_incorrect": {
        "A": "deterministic sandboxes calculate based exactly on what is programmed; they do not arbitrarily strip contextual risk variables.",
        "C": "terminal agents (like Claude Code) are designed specifically for local and networked execution, capable of processing diverse telemetry if configured."
      },
      "full_justification": "Options B and D succeed because: Layer separation: The mapping layers must remain strictly sequential: Eligibility, Ownership, and Implementation. \"Carried by code execution\" is an implementation choice; it is never an ownership criterion and cannot justify transferring operational accountability to the AI. Downstream gates: Running arithmetic in a sandbox ensures calculation precision, but the code can still reference the wrong data column or misapply a threshold. Delegating a high-stakes calculation is safe only if an explicit human review gate immediately inspects the output. Option A is incorrect because deterministic sandboxes calculate based exactly on what is programmed; they do not arbitrarily strip contextual risk variables. Option C is incorrect because terminal agents (like Claude Code) are designed specifically for local and networked execution, capable of processing diverse telemetry if configured."
    },
    {
      "id": 19,
      "question": "A regional banking manager configures a delegation map for processing small business loan applications. For the final risk assessment step, the manager documents the control as: \"A qualified credit assessment professional will look at the final recommendation whenever income discrepancies appear elevated.\" According to rigorous map governance standards, why is this control definition fundamentally defective?",
      "options": {
        "A": "It relies on subjective risk language (\"elevated\") without establishing deterministic, code-verified numerical variance thresholds to govern automated secondary review dispatch.",
        "B": "It omits mandatory cross-model arbitration protocols required to reconcile divergent credit scoring outcomes between competing proprietary foundation model vendor engines.",
        "C": "It introduces manual human supervision into an automated decision pipeline whose financial velocity requires end-to-end autonomous execution under statutory banking frameworks.",
        "D": "It assigns the review to an anonymous professional and relies on an unstaffed default condition (\"whenever... elevated\") rather than naming a specific person and a mandatory operational moment."
      },
      "correct": "D",
      "explanation": "Option D succeeds because a properly designed review gate cannot simply say \"a human looks at it\". To prevent the gate from decaying into an unstaffed pass-through, the delegation map must establish three explicit components: a named person (e.g., Sarah Jenkins, Senior Assessor), a named moment (before final recommendation), and a named thing being checked (tax figures match payslips). The manager's definition relies on a vague default condition (\"whenever elevated\") and an anonymous reviewer, virtually ensuring the gate will be bypassed.",
      "why_incorrect": {
        "A": "while threshold limits are useful, the fundamental defect is the lack of a named person and a mandatory operational moment.",
        "B": "assigning review to a competing model does not constitute a human review gate; collaborative steps require an accountable human, not another automated pass.",
        "C": "human intervention is non-negotiable for high-stakes operational workflows regardless of reasoning model sophistication."
      },
      "full_justification": "Option D succeeds because a properly designed review gate cannot simply say \"a human looks at it\". To prevent the gate from decaying into an unstaffed pass-through, the delegation map must establish three explicit components: a named person (e.g., Sarah Jenkins, Senior Assessor), a named moment (before final recommendation), and a named thing being checked (tax figures match payslips). The manager's definition relies on a vague default condition (\"whenever elevated\") and an anonymous reviewer, virtually ensuring the gate will be bypassed. Option A is incorrect because while threshold limits are useful, the fundamental defect is the lack of a named person and a mandatory operational moment. Option B is incorrect because assigning review to a competing model does not constitute a human review gate; collaborative steps require an accountable human, not another automated pass. Option C is incorrect because human intervention is non-negotiable for high-stakes operational workflows regardless of reasoning model sophistication."
    },
    {
      "id": 20,
      "question": "A fleet logistics director uses a foundation model to design a comprehensive five-year vehicle replacement schedule. The model analyzes historical maintenance telemetry, depreciation curves, and fuel efficiency metrics flawlessly. However, the generated replacement schedule recommends replacing the heavy haulage fleet next year, completely contradicting a private board decision made last month to freeze capital expenditure for three years. Why did the model generate a technically perfect but operationally useless plan?",
      "options": {
        "A": "The historical maintenance telemetry contained corrupted timestamp formatting, causing the model to miscalculate the depreciation curves.",
        "B": "Foundation models inherently lack the mathematical capability to compute multi-year vehicle amortisation schedules accurately.",
        "C": "The model operated within a cloud sandbox that lacked direct network access to the vehicles' onboard diagnostic systems.",
        "D": "The strategic capital expenditure freeze was an inaccessible judgment input that sat entirely outside the provided context window."
      },
      "correct": "D",
      "explanation": "Option D succeeds because of the window test: Could I put everything this step needs into the context window? If not, the step is mine. Strategic fleet decisions depend on inaccessible inputs: private board retreats, confidential capital expenditure freezes, and unrecorded risk appetites. Because these judgment inputs sat outside the window, the model did not refuse; it generated a plausible, optimized plan that was mathematically sound but entirely useless given organizational reality.",
      "why_incorrect": {
        "A": "the failure was not caused by corrupted vehicle telemetry; the historical data analysis was structurally sound, but blind to private corporate strategy.",
        "B": "modern foundation models (especially utilizing code execution) easily compute vehicle depreciation and amortisation schedules; the breakdown was strategic, not mathematical.",
        "C": "executing code sandboxes does not grant an assistant access to unrecorded board decisions made behind closed doors. Execution Halted. Please confirm if you would like to proceed with"
      },
      "full_justification": "Option D succeeds because of the window test: Could I put everything this step needs into the context window? If not, the step is mine. Strategic fleet decisions depend on inaccessible inputs: private board retreats, confidential capital expenditure freezes, and unrecorded risk appetites. Because these judgment inputs sat outside the window, the model did not refuse; it generated a plausible, optimized plan that was mathematically sound but entirely useless given organizational reality. Option A is incorrect because the failure was not caused by corrupted vehicle telemetry; the historical data analysis was structurally sound, but blind to private corporate strategy. Option B is incorrect because modern foundation models (especially utilizing code execution) easily compute vehicle depreciation and amortisation schedules; the breakdown was strategic, not mathematical. Option C is incorrect because executing code sandboxes does not grant an assistant access to unrecorded board decisions made behind closed doors. Execution Halted. Please confirm if you would like to proceed with"
    },
    {
      "id": 21,
      "question": "A data analyst explores a new dataset using a browser-based conversational agent. The analyst prompts the agent to write and run Python code to clean the data and generate a summary report. Which operational reality governs this specific execution surface?",
      "options": {
        "A": "The execution environment cannot modify or delete any files stored on the host computer.",
        "B": "The agent automatically synchronizes its output with the analyst's local hard drive folders.",
        "C": "The generated scripts remain permanently accessible across all future browser sessions.",
        "D": "The sandbox requires the analyst to install a local Python interpreter before running."
      },
      "correct": "A",
      "explanation": "Option A succeeds because the browser chat surface (e.g., Claude.ai) executes code within a temporary, isolated cloud sandbox. It poses zero risk to the user's local machine because it physically cannot touch, modify, or delete any files stored on the host computer.",
      "why_incorrect": {
        "B": "browser sandboxes are isolated; they do not automatically sync outputs to local hard drives.",
        "C": "the sandbox is temporary. Scripts effectively die with the chat unless explicitly downloaded and saved.",
        "D": "the Python interpreter runs entirely on the AI vendor's servers, requiring zero local installation."
      },
      "full_justification": "Option A succeeds because the browser chat surface (e.g., Claude.ai) executes code within a temporary, isolated cloud sandbox. It poses zero risk to the user's local machine because it physically cannot touch, modify, or delete any files stored on the host computer. Option B is incorrect because browser sandboxes are isolated; they do not automatically sync outputs to local hard drives. Option C is incorrect because the sandbox is temporary. Scripts effectively die with the chat unless explicitly downloaded and saved. Option D is incorrect because the Python interpreter runs entirely on the AI vendor's servers, requiring zero local installation."
    },
    {
      "id": 22,
      "question": "A network engineer needs to run a daily health report on multiple system log files located in a specific local workstation directory. The engineer decides to use a terminal-based agent (such as Claude Code or OpenCode) rather than a browser sandbox. What operational advantage does the terminal agent provide for this specific task?",
      "options": {
        "A": "It executes directly against the local directory without requiring manual file uploads.",
        "B": "It utilizes advanced cryptographic hashing to secure the local log files from ransomware.",
        "C": "It bypasses the foundation model's token limits by parsing binary machine code directly.",
        "D": "It automatically translates the local log files into HTML artifacts for web distribution."
      },
      "correct": "A",
      "explanation": "Option A succeeds because terminal agents (like Claude Code or OpenCode) operate directly inside a local folder environment. The agent can autonomously see, read, and execute scripts against the files already present in that directory without requiring the user to manually upload them to a chat window.",
      "why_incorrect": {
        "B": "terminal agents are automation tools, not cryptographic anti-ransomware security utilities.",
        "C": "terminal agents execute standard Python/shell scripts; they do not magically bypass token limits by parsing binary code.",
        "D": "generating HTML is an output formatting choice dictated by the brief, not an automatic baseline function of terminal agents."
      },
      "full_justification": "Option A succeeds because terminal agents (like Claude Code or OpenCode) operate directly inside a local folder environment. The agent can autonomously see, read, and execute scripts against the files already present in that directory without requiring the user to manually upload them to a chat window. Option B is incorrect because terminal agents are automation tools, not cryptographic anti-ransomware security utilities. Option C is incorrect because terminal agents execute standard Python/shell scripts; they do not magically bypass token limits by parsing binary code. Option D is incorrect because generating HTML is an output formatting choice dictated by the brief, not an automatic baseline function of terminal agents."
    },
    {
      "id": 23,
      "question": "A project manager uses a desktop AI application to reorganize a messy local directory containing 500 project assets. The application utilizes a \"plan-then-approve\" architectural model. How does this specific feature mitigate execution risk during the reorganization?",
      "options": {
        "A": "It cross-references the proposed file changes against a secondary open-source AI model.",
        "B": "It requires the manager to manually write the underlying Python scripts before execution.",
        "C": "It presents a plain-English list of proposed file modifications for authorization before acting.",
        "D": "It automatically backs up the entire host operating system to a secure cloud server first."
      },
      "correct": "C",
      "explanation": "Option C succeeds because desktop AI applications designed for knowledge workers (like Cowork or OpenWork) integrate \"plan-then-approve\" as a core safety feature. Before acting on real local files, the app writes a plain-English plan detailing exactly what it intends to do, allowing the human operator to catch wrong assumptions before any irreversible damage occurs.",
      "why_incorrect": {
        "A": "plan-then-approve relies on a human reading the plan, not an automated cross-model API check.",
        "B": "the entire premise of these applications is that the AI writes the code; the human only acts as the approving client.",
        "D": "these applications do not perform full-system operating system backups prior to task execution."
      },
      "full_justification": "Option C succeeds because desktop AI applications designed for knowledge workers (like Cowork or OpenWork) integrate \"plan-then-approve\" as a core safety feature. Before acting on real local files, the app writes a plain-English plan detailing exactly what it intends to do, allowing the human operator to catch wrong assumptions before any irreversible damage occurs. Option A is incorrect because plan-then-approve relies on a human reading the plan, not an automated cross-model API check. Option B is incorrect because the entire premise of these applications is that the AI writes the code; the human only acts as the approving client. Option D is incorrect because these applications do not perform full-system operating system backups prior to task execution."
    },
    {
      "id": 24,
      "question": "An accountant commissions a new script via an agent to automatically format and merge quarterly tax spreadsheets stored on a local drive. To strictly adhere to the first rule of blast radius containment, which operational instruction must the accountant append to the brief?",
      "options": {
        "A": "\"Require the model to execute a known-answer test on the first ten rows of the dataset.\"",
        "B": "\"Ensure the script is written in JavaScript rather than Python to prevent file overwrites.\"",
        "C": "\"Mandate that the agent explain its step-by-step processing logic in plain English first.\"",
        "D": "\"First copy the directory to a backup folder, then work only on the original target files.\""
      },
      "correct": "D",
      "explanation": "Option D succeeds because Rule 1 of blast radius containment mandates working on copies until a script has earned trust. Appending a single sentence commanding the agent to copy the folder to a backup before modifying the originals turns a potential bad run into a harmless error rather than a disaster.",
      "why_incorrect": {
        "A": "the known-answer test validates mathematical logic (Concept 6), whereas blast radius containment (Rule 1) specifically addresses preventing permanent file damage.",
        "B": "javaScript is equally capable of overwriting files if executed locally; the language choice does not mitigate blast radius.",
        "C": "explaining logic is a verification technique (plain-English replay), not a physical safeguard against file corruption."
      },
      "full_justification": "Option D succeeds because Rule 1 of blast radius containment mandates working on copies until a script has earned trust. Appending a single sentence commanding the agent to copy the folder to a backup before modifying the originals turns a potential bad run into a harmless error rather than a disaster. Option A is incorrect because the known-answer test validates mathematical logic (Concept 6), whereas blast radius containment (Rule 1) specifically addresses preventing permanent file damage. Option B is incorrect because javaScript is equally capable of overwriting files if executed locally; the language choice does not mitigate blast radius. Option C is incorrect because explaining logic is a verification technique (plain-English replay), not a physical safeguard against file corruption."
    },
    {
      "id": 25,
      "question": "A photographer instructs a local agent to rename 800 image files based on their internal metadata timestamps. To prevent irreversible data loss or organizational chaos, which constraint must be explicitly stated in the brief before the agent alters any files?",
      "options": {
        "A": "\"Upload the image files to a cloud sandbox to ensure the local originals remain untouched.\"",
        "B": "\"Show me the full list of operations, old name next to new name, and wait for my approval.\"",
        "C": "\"Cross-reference the new file names against a secondary AI model to verify timestamp accuracy.\"",
        "D": "\"Write the renaming script in Python and output the final results into a secure HTML document.\""
      },
      "correct": "B",
      "explanation": "Option B succeeds because Rule 2 of blast radius containment requires seeing changes before they happen via a \"dry run\". Before any rename, move, or delete operation, the user must demand a full list mapping the old names to the new names, and the agent must wait for explicit human approval before executing the changes.",
      "why_incorrect": {
        "A": "executing in a cloud sandbox prevents the renaming from occurring locally, defeating the purpose of the task entirely.",
        "C": "a secondary AI model cannot verify whether the newly generated names align with the user's specific organizational intent.",
        "D": "generating an HTML document does not prevent the underlying Python script from irreversibly scrambling the local files during execution."
      },
      "full_justification": "Option B succeeds because Rule 2 of blast radius containment requires seeing changes before they happen via a \"dry run\". Before any rename, move, or delete operation, the user must demand a full list mapping the old names to the new names, and the agent must wait for explicit human approval before executing the changes. Option A is incorrect because executing in a cloud sandbox prevents the renaming from occurring locally, defeating the purpose of the task entirely. Option C is incorrect because a secondary AI model cannot verify whether the newly generated names align with the user's specific organizational intent. Option D is incorrect because generating an HTML document does not prevent the underlying Python script from irreversibly scrambling the local files during execution."
    },
    {
      "id": 26,
      "question": "A researcher instructs a terminal agent to clean and standardize a batch of clinical trial CSV files stored on a local workstation. Which TWO operational rules minimize the risk of catastrophic file corruption during this automated process? (Select TWO.)",
      "options": {
        "A": "Instructing the agent to overwrite the original source files to prevent directory clutter.",
        "B": "Pointing the agent exclusively at the specific subfolder containing the trial CSV files.",
        "C": "Mandating that all standardized analytical data outputs be written into entirely new files.",
        "D": "Executing the agent from the operating system root directory to locate missing dependencies."
      },
      "correct": "B and C",
      "explanation": "Options B and C succeed because they represent Blast Radius Rules 3 and 4. Rule 3 dictates pointing the agent at the smallest possible folder containing the problem, preventing a confused script from damaging unrelated assets. Rule 4 dictates writing all outputs to new files, ensuring the original source data remains pristine and untouched.",
      "why_incorrect": {
        "A": "overwriting original files violates Rule 4, destroying the source data and making errors unrecoverable.",
        "D": "executing from the root directory violates Rule 3, exposing the entire hard drive to potential script errors."
      },
      "full_justification": "Options B and C succeed because they represent Blast Radius Rules 3 and 4. Rule 3 dictates pointing the agent at the smallest possible folder containing the problem, preventing a confused script from damaging unrelated assets. Rule 4 dictates writing all outputs to new files, ensuring the original source data remains pristine and untouched. Option A is incorrect because overwriting original files violates Rule 4, destroying the source data and making errors unrecoverable. Option D is incorrect because executing from the root directory violates Rule 3, exposing the entire hard drive to potential script errors."
    },
    {
      "id": 27,
      "question": "A marketing manager wants a script to automatically pull CRM data, draft personalized client emails, and dispatch them every Monday at 3:00 AM without any human supervision. Why does this specific workflow exceed the boundary of standard one-prompt code commissioning?",
      "options": {
        "A": "Unattended execution removes the human verification checks required to catch generated code errors.",
        "B": "The task requires JavaScript execution, which is strictly prohibited in scheduled terminal environments.",
        "C": "Foundation models fundamentally lack the programmatic capability to interface with external email APIs.",
        "D": "Processing CRM data mandates the deployment of a secondary foundation model for cross-checking loops."
      },
      "correct": "A",
      "explanation": "Option A succeeds because unattended automation (e.g., scheduled scripts running while the user sleeps) crosses the boundary of one-prompt code. The entire methodology relies on a human reviewing the results (Concept 6) before acting on them. Unattended execution removes this vital verification layer, requiring robust software engineering (Digital FTEs) to handle unexpected failures safely.",
      "why_incorrect": {
        "B": "javaScript can be scheduled locally; language restrictions do not define the boundary of unattended automation.",
        "C": "foundation models writing Python can easily interface with email APIs.",
        "D": "cross-checking loops are evaluation techniques, not mandatory architectural prerequisites for processing standard CRM data."
      },
      "full_justification": "Option A succeeds because unattended automation (e.g., scheduled scripts running while the user sleeps) crosses the boundary of one-prompt code. The entire methodology relies on a human reviewing the results (Concept 6) before acting on them. Unattended execution removes this vital verification layer, requiring robust software engineering (Digital FTEs) to handle unexpected failures safely. Option B is incorrect because javaScript can be scheduled locally; language restrictions do not define the boundary of unattended automation. Option C is incorrect because foundation models writing Python can easily interface with email APIs. Option D is incorrect because cross-checking loops are evaluation techniques, not mandatory architectural prerequisites for processing standard CRM data."
    },
    {
      "id": 28,
      "question": "A financial trader commissions a Python script to analyze market momentum indicators and automatically execute stock trades via an exchange API. According to safe operational boundaries for one-prompt code, how must this workflow design be modified?",
      "options": {
        "A": "The script must execute the trades in a browser sandbox rather than a local workstation terminal.",
        "B": "The script must utilize a cross-model verification check to audit the momentum indicators first.",
        "C": "The script must strictly prepare the trading orders, but a human operator must manually execute them.",
        "D": "The script must be rewritten in a statically typed programming language to prevent rounding errors."
      },
      "correct": "C",
      "explanation": "Option C succeeds because placing live trades is a \"high-stakes act with no undo,\" which explicitly lies across the edge of safe one-prompt code boundaries. The correct operational design is to let the code prepare the trades or analysis, while a human manually reviews and dispatches the irreversible action.",
      "why_incorrect": {
        "A": "executing an irreversible trade API call from a browser sandbox still results in real-world financial consequences.",
        "B": "a cross-model check validates logic but does not replace the mandatory human dispatch gate for high-stakes, irreversible actions.",
        "D": "statically typed languages do not eliminate the systemic risk of executing fully autonomous financial trades without human oversight."
      },
      "full_justification": "Option C succeeds because placing live trades is a \"high-stakes act with no undo,\" which explicitly lies across the edge of safe one-prompt code boundaries. The correct operational design is to let the code prepare the trades or analysis, while a human manually reviews and dispatches the irreversible action. Option A is incorrect because executing an irreversible trade API call from a browser sandbox still results in real-world financial consequences. Option B is incorrect because a cross-model check validates logic but does not replace the mandatory human dispatch gate for high-stakes, irreversible actions. Option D is incorrect because statically typed languages do not eliminate the systemic risk of executing fully autonomous financial trades without human oversight."
    },
    {
      "id": 29,
      "question": "An HR director asks an agent to calculate which mid-level employees deserve a promotion based on a spreadsheet of performance reviews, attendance records, and peer feedback scores. Why is this task an inappropriate application of automated script execution?",
      "options": {
        "A": "The dataset contains unstructured qualitative feedback that standard Python scripts cannot parse.",
        "B": "Employee performance records trigger regulatory compliance bans on cloud-based AI processing.",
        "C": "The criteria for promotion represent a strategic human judgment, not a mathematical computation.",
        "D": "The volume of the performance data exceeds the active context window of standard foundation models."
      },
      "correct": "C",
      "explanation": "Option C succeeds because deciding who gets a promotion based on qualitative and quantitative factors is a strategic judgment call, not an arithmetic computation. The curriculum explicitly defines \"judgment wearing a computation costume\" as a boundary; code computes the metrics, but the human must decide the criteria and final outcome.",
      "why_incorrect": {
        "A": "python scripts (especially those powered by LLMs) are highly capable of parsing unstructured qualitative feedback.",
        "B": "standard performance reviews do not trigger absolute regulatory bans on cloud processing (unlike specific PHI or strict compliance regimes).",
        "D": "typical departmental review spreadsheets easily fit within modern foundation model context windows."
      },
      "full_justification": "Option C succeeds because deciding who gets a promotion based on qualitative and quantitative factors is a strategic judgment call, not an arithmetic computation. The curriculum explicitly defines \"judgment wearing a computation costume\" as a boundary; code computes the metrics, but the human must decide the criteria and final outcome. Option A is incorrect because python scripts (especially those powered by LLMs) are highly capable of parsing unstructured qualitative feedback. Option B is incorrect because standard performance reviews do not trigger absolute regulatory bans on cloud processing (unlike specific PHI or strict compliance regimes). Option D is incorrect because typical departmental review spreadsheets easily fit within modern foundation model context windows."
    },
    {
      "id": 30,
      "question": "A logistics coordinator successfully uses a browser-based AI chat to generate a weekly shipping manifest report. Over time, the coordinator finds the process of manually dragging and dropping seven different database exports into the chat window every Friday increasingly inefficient. What operational migration does this friction signal justify?",
      "options": {
        "A": "Transitioning the workflow from a single foundation model to a multi-model cross-checking loop.",
        "B": "Transitioning the workflow from a browser sandbox to an agent operating inside a local folder.",
        "C": "Transitioning the workflow from a Python-based execution script to a JavaScript web calculator.",
        "D": "Transitioning the workflow from an automated code brief to a conversational estimation prompt."
      },
      "correct": "B",
      "explanation": "Option B succeeds because the precise graduation signal for moving from a browser sandbox (Claude.ai) to a local surface (Terminal or Desktop app) is when \"uploading becomes the annoying part of your week\". When a recurring task involves repeatedly dragging files into a chat, moving to an agent that operates directly inside the local folder eliminates that friction.",
      "why_incorrect": {
        "A": "multi-model loops address verification rigor, not file-uploading friction.",
        "C": "switching to JavaScript does not solve the necessity of manually transferring files into a browser environment.",
        "D": "estimation prompts reduce precision, whereas the goal is to maintain computational accuracy while reducing manual file handling. Gemini is AI and can make mistakes. Organizing the content from the chapter"
      },
      "full_justification": "Option B succeeds because the precise graduation signal for moving from a browser sandbox (Claude.ai) to a local surface (Terminal or Desktop app) is when \"uploading becomes the annoying part of your week\". When a recurring task involves repeatedly dragging files into a chat, moving to an agent that operates directly inside the local folder eliminates that friction. Option A is incorrect because multi-model loops address verification rigor, not file-uploading friction. Option C is incorrect because switching to JavaScript does not solve the necessity of manually transferring files into a browser environment. Option D is incorrect because estimation prompts reduce precision, whereas the goal is to maintain computational accuracy while reducing manual file handling. Gemini is AI and can make mistakes. Organizing the content from the chapter"
    }
  ]
};
