# 🎓 AI Certification Interactive MCQ Exam Portal (10 Chapters)

An enterprise-grade, high-performance web application designed for comprehensive preparation and testing across all **10 core AI certification chapters**. 

Engineered with instant choice evaluation, detailed rationale, in-depth distractor analysis (*why other options are incorrect*), rapid question jump palette, keyboard accessibility, and one-click PDF revision sheet generation.

---

## 🚀 Live Demo & Deployment

Deployable instantly to **Vercel**, **GitHub Pages**, or any static hosting service.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

---

## 📋 Table of Contents

- [Curated Chapters](#-curated-chapters)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Deploy to GitHub](#-deploy-to-github-step-by-step)
- [Deploy to Vercel](#-deploy-to-vercel-step-by-step)
- [Local Development](#-local-development)
- [Adding / Updating Questions](#-adding--updating-questions)
- [License](#-license)

---

## 📚 Curated Chapters

| Chapter | Title | Focus & Core Concepts |
|:---:|:---|:---|
| **Ch. 1** | **Just Delegate It (A Crash Course)** | Delegation psychology, task specification, cognitive handoff, autonomy boundaries |
| **Ch. 2** | **Governance, Risk & Responsible Use** | Compliance frameworks, bias mitigation, security policies, AI audit trails |
| **Ch. 3** | **Workflow Design & Diagnosis** | Bottleneck detection, agent chaining, pipeline optimization, failure modes |
| **Ch. 4** | **Skills & Connectors: Architecture & Safe-Use** | Tool invocation, API wrappers, authentication security, connector sandboxing |
| **Ch. 5** | **ChatGPT & Claude: Architectures & Tooling** | Model tradeoffs, context window utilization, system prompts, artifacts |
| **Ch. 6** | **AI Fluency: The 4D Framework** | Discover, Design, Delegate, Diagnose operational framework |
| **Ch. 7** | **General Agents on the Web** | Browser automation, DOM perception, multi-step web reasoning, safety |
| **Ch. 8** | **AI Prompting in 2026 (A Crash Course)** | Power-user briefing, Loud/Quiet/Secret framework, operational limits, context hygiene |
| **Ch. 9** | **What AI Actually Is (A Crash Course)** | Probabilistic token prediction, frozen weights vs active context, sampling temperature |
| **Ch. 10** | **Code You Never Write** | VPRF framework, deterministic execution vs estimation, code problems, artifact sandboxes |

---

## ✨ Key Features

- **🎯 Interactive Option Selection & Instant Evaluation**:
  - Click any option (A, B, C, D) or use keyboard shortcuts `[A-D]`.
  - Click **"Confirm Answer"** (`[Enter]`) to lock in answers and reveal evaluation.
  - **Correct Answer** highlighted in emerald green with checkmark.
  - **Selected Distractor** highlighted in crimson with error mark.
- **💡 In-Depth Explanations & Distractor Analysis**:
  - Clear rationale explaining the underlying concept.
  - **Why Other Options Are Incorrect**: Dedicated section dissecting each distractor to eliminate misconceptions.
- **⚡ Rapid Question Navigation**:
  - **Previous MCQ** (`<` / `[←]`) and **Next MCQ** (`>` / `[→]`).
  - **Question Palette**: Grid of numbers (1, 2, 3...) clickable to jump directly to any question. Color-coded (Green = Correct, Red = Incorrect, Blue = Current).
- **📄 One-Click PDF Export**:
  - Clean, print-ready study revision sheets formatted for offline study and high-resolution printing.
- **🎨 Executive Dark / Light UI**:
  - Minimalist enterprise aesthetic (obsidian slate `#090d16`, high-contrast typography, no distracting neon glows).
  - Fluid text wrapping with zero awkward line breaks or ragged edges.
- **⚡ Client-Side Markdown Importer**:
  - Ingests questions formatted in Markdown directly from the browser modal without modifying HTML files.

---

## 📂 Project Architecture

```
├── index.html                 # Main dashboard listing all 7 chapters
├── quiz.html                  # Interactive quiz runner & evaluation engine
├── css/
│   └── style.css              # Executive dark/light design system & print styles
├── js/
│   └── app.js                 # Quiz controller, text normalizer, storage & PDF exporter
├── data/
│   ├── chapters_meta.js       # Chapter metadata, titles, descriptions & icons
│   ├── chapter1.js            # Chapter 1 questions (rebalanced & normalized)
│   ├── chapter2.js            # Chapter 2 questions
│   ├── chapter3.js            # Chapter 3 questions
│   ├── chapter4.js            # Chapter 4 questions
│   ├── chapter5.js            # Chapter 5 questions
│   ├── chapter6.js            # Chapter 6 questions
│   ├── chapter7.js            # Chapter 7 questions
│   ├── chapter8.js            # Chapter 8 questions
│   ├── chapter9.js            # Chapter 9 questions
│   └── chapter10.js           # Chapter 10 questions
├── scripts/
│   └── parse_mcqs.py          # Fast Python parser for Markdown question ingestion
├── vercel.json                # Vercel deployment & security headers config
├── package.json               # Project manifest
└── .gitignore                 # Standard repository ignores
```

---

## 🚀 Deploy to GitHub (Step-by-Step)

Follow these steps in your terminal (PowerShell or Git Bash) inside this folder:

### 1. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: Executive 7-Chapter AI Certification Exam Portal"
git branch -M main
```

### 2. Create a New Repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Enter a repository name (e.g., `ai-certification-exam-portal`).
3. Leave it Public (or Private), and do **not** initialize with a README, .gitignore, or license (they are already created here).
4. Click **Create repository**.

### 3. Connect & Push to GitHub
Copy the commands shown on GitHub (replacing `<YOUR_USERNAME>` with your GitHub username):
```bash
git remote add origin https://github.com/<YOUR_USERNAME>/ai-certification-exam-portal.git
git push -u origin main
```

---

## ⚡ Deploy to Vercel (Step-by-Step)

### Option A: Via Vercel Web Dashboard (Recommended)
1. Log in to [vercel.com](https://vercel.com).
2. Click **"Add New..."** → **"Project"**.
3. Select your GitHub repository (`ai-certification-exam-portal`) and click **"Import"**.
4. In the Project Configuration:
   - **Framework Preset**: *Other*
   - **Root Directory**: `./` (leave default)
   - **Build Command**: *Empty* (no build step required)
   - **Output Directory**: *Empty* (static site)
5. Click **"Deploy"**.
6. Within 10 seconds, Vercel will provide your live URL (e.g., `https://ai-certification-exam-portal.vercel.app`).

### Option B: Via Vercel CLI
If you have Node.js and Vercel CLI installed:
```bash
npm i -g vercel
vercel
```
Follow the interactive prompts (accept defaults). For production deployment:
```bash
vercel --prod
```

---

## 💻 Local Development

No compilation or build step required! Run locally using any static web server:

### Using Python:
```bash
python -m http.server 8080
```
Then open [http://localhost:8080](http://localhost:8080) in your browser.

### Using Node.js:
```bash
npx serve .
```

---

## 📝 Adding / Updating Questions

Whenever you have new questions in Markdown:

```bash
python scripts/parse_mcqs.py "path_to_markdown.md" <chapter_number>
```

Or open the web app, click **"Import MCQs"** in the top navigation, paste the Markdown text, and save.

---

## 📄 License
MIT License. Free for educational and certification training use.
