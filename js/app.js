/**
 * Master Application Script for 7-Chapter MCQ Exam Portal
 */

// Text Normalization Helpers (Sanitize & collapse accidental hard line breaks)
function normalizeText(text) {
  if (text === null || text === undefined) return '';
  return String(text)
    .split(/\r?\n\s*\r?\n/)
    .map(paragraph => paragraph.replace(/\r?\n|\r|\t/g, ' ').replace(/\s+/g, ' ').trim())
    .filter(Boolean)
    .join('\n\n');
}

function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function formatNormalizedHtml(text) {
  if (text === null || text === undefined) return '';
  const normalized = normalizeText(text);
  const paragraphs = normalized.split('\n\n');
  if (paragraphs.length <= 1) {
    return escapeHtml(paragraphs[0] || '');
  }
  return paragraphs.map(p => `<p class="q-para">${escapeHtml(p)}</p>`).join('');
}

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  const themeBtn = document.getElementById('theme-toggle-btn');
  if (themeBtn) {
    themeBtn.innerHTML = savedTheme === 'light' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
  }
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const newTheme = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  const themeBtn = document.getElementById('theme-toggle-btn');
  if (themeBtn) {
    themeBtn.innerHTML = newTheme === 'light' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
  }
}

// Global Answer Correctness Evaluator (Supports single and multi-choice)
function isAnswerCorrect(q, userAnswer) {
  if (!userAnswer || !q || !q.correct) return false;
  const extractLetters = (str) => {
    if (Array.isArray(str)) return str.slice().map(s => String(s).trim().toUpperCase()).sort();
    return String(str)
      .replace(/and|,/gi, ' ')
      .split(/\s+/)
      .map(s => s.trim().toUpperCase())
      .filter(s => ['A', 'B', 'C', 'D'].includes(s))
      .sort();
  };
  const u = extractLetters(userAnswer).join('');
  const c = extractLetters(q.correct).join('');
  return u.length > 0 && u === c;
}

// Global Storage Helpers
const Storage = {
  getProgress(chapterId) {
    try {
      const data = localStorage.getItem(`quiz_prog_ch_${chapterId}`);
      return data ? JSON.parse(data) : { answers: {}, confirmed: {} };
    } catch (e) {
      return { answers: {}, confirmed: {} };
    }
  },
  saveProgress(chapterId, progress) {
    try {
      localStorage.setItem(`quiz_prog_ch_${chapterId}`, JSON.stringify(progress));
    } catch (e) {}
  },
  getCustomChapter(chapterId) {
    try {
      const custom = localStorage.getItem(`custom_chapter_${chapterId}`);
      return custom ? JSON.parse(custom) : null;
    } catch (e) {
      return null;
    }
  },
  saveCustomChapter(chapterId, chapterData) {
    try {
      localStorage.setItem(`custom_chapter_${chapterId}`, JSON.stringify(chapterData));
    } catch (e) {}
  }
};

// ============================================================
// INDEX PAGE CONTROLLER
// ============================================================
function initIndexPage() {
  const container = document.getElementById('chapters-grid');
  if (!container) return;

  const metadata = window.QUIZ_METADATA || [];
  let totalAllQuestions = 0;
  let totalAllAnswered = 0;
  let totalAllCorrect = 0;

  function renderCards(filterText = '') {
    container.innerHTML = '';
    
    metadata.forEach(ch => {
      // Get question count from CHAPTER_DATA or custom
      const custom = Storage.getCustomChapter(ch.id);
      const chData = custom || (window.CHAPTER_DATA && window.CHAPTER_DATA[ch.id]) || { questions: [] };
      const qCount = chData.questions ? chData.questions.length : 0;
      totalAllQuestions += qCount;

      const progress = Storage.getProgress(ch.id);
      const answeredCount = Object.keys(progress.confirmed || {}).length;
      totalAllAnswered += answeredCount;

      // Count correct
      let correctCount = 0;
      if (chData.questions) {
        chData.questions.forEach(q => {
          if (progress.confirmed && progress.confirmed[q.id] && isAnswerCorrect(q, progress.answers && progress.answers[q.id])) {
            correctCount++;
          }
        });
      }
      totalAllCorrect += correctCount;

      const pct = qCount > 0 ? Math.round((answeredCount / qCount) * 100) : 0;

      // Search match
      const searchMatch = !filterText || 
        ch.title.toLowerCase().includes(filterText.toLowerCase()) || 
        ch.subtitle.toLowerCase().includes(filterText.toLowerCase()) ||
        ch.category.toLowerCase().includes(filterText.toLowerCase());

      if (!searchMatch) return;

      const card = document.createElement('div');
      card.className = 'chapter-card glass';
      card.style.setProperty('--card-accent', ch.color || 'var(--accent-primary)');

      card.innerHTML = `
        <div>
          <div class="chapter-card-top">
            <div class="chapter-card-icon">
              <i class="fa-solid ${ch.icon || 'fa-book-open'}"></i>
            </div>
            <span class="chapter-num-badge">Ch. ${ch.id}</span>
          </div>
          <h3 class="chapter-title">${ch.title}</h3>
          <p class="chapter-desc">${ch.subtitle}</p>
          <div class="chapter-meta-row">
            <span class="chapter-meta-item"><i class="fa-regular fa-circle-question"></i> ${qCount} MCQs</span>
            <span class="chapter-meta-item"><i class="fa-solid fa-check-double"></i> ${answeredCount}/${qCount} Done</span>
            <span class="chapter-meta-item"><i class="fa-solid fa-chart-pie"></i> ${pct}%</span>
          </div>
          <div class="chapter-progress-bar">
            <div class="chapter-progress-fill" style="width: ${pct}%;"></div>
          </div>
        </div>
        <div class="chapter-card-actions">
          <a href="quiz.html?chapter=${ch.id}" class="btn btn-primary">
            <i class="fa-solid fa-play"></i> Start Quiz
          </a>
          <button onclick="downloadChapterPdfDirectly(${ch.id})" class="btn btn-secondary" title="Download PDF of this Chapter">
            <i class="fa-solid fa-file-pdf"></i> PDF
          </button>
        </div>
      `;
      container.appendChild(card);
    });

    // Update global stat ribbon if present
    const statTotalCh = document.getElementById('stat-total-chapters');
    if (statTotalCh) statTotalCh.innerText = metadata.length;
    const statQ = document.getElementById('stat-total-questions');
    if (statQ) statQ.innerText = totalAllQuestions;
    const statA = document.getElementById('stat-total-answered');
    if (statA) statA.innerText = totalAllAnswered;
    const statAcc = document.getElementById('stat-accuracy');
    if (statAcc) {
      const acc = totalAllAnswered > 0 ? Math.round((totalAllCorrect / totalAllAnswered) * 100) : 0;
      statAcc.innerText = `${acc}%`;
    }
  }

  renderCards();

  const searchInput = document.getElementById('chapter-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      renderCards(e.target.value.trim());
    });
  }
}

// ============================================================
// QUIZ ENGINE CONTROLLER
// ============================================================
class QuizEngine {
  constructor() {
    const params = new URLSearchParams(window.location.search);
    this.chapterId = parseInt(params.get('chapter')) || 1;
    this.currentIndex = 0;
    this.selectedOption = null;
    this.chapterData = null;
    this.progress = Storage.getProgress(this.chapterId);
  }

  init() {
    this.loadChapterData();
    this.bindEvents();
    this.renderHeader();
    this.renderPalette();
    this.renderQuestion();
  }

  loadChapterData() {
    // Check localStorage custom data first, then window.CHAPTER_DATA
    const custom = Storage.getCustomChapter(this.chapterId);
    if (custom && custom.questions && custom.questions.length > 0) {
      this.chapterData = custom;
    } else if (window.CHAPTER_DATA && window.CHAPTER_DATA[this.chapterId]) {
      this.chapterData = window.CHAPTER_DATA[this.chapterId];
    } else {
      this.chapterData = {
        chapterId: this.chapterId,
        title: `Chapter ${this.chapterId}`,
        totalQuestions: 0,
        questions: []
      };
    }
  }

  bindEvents() {
    const prevBtn = document.getElementById('btn-prev');
    const nextBtn = document.getElementById('btn-next');
    const confirmBtn = document.getElementById('btn-confirm');
    const resetBtn = document.getElementById('btn-reset-quiz');
    const pdfBtn = document.getElementById('btn-download-pdf');

    if (prevBtn) prevBtn.addEventListener('click', () => this.prevQuestion());
    if (nextBtn) nextBtn.addEventListener('click', () => this.nextQuestion());
    if (confirmBtn) confirmBtn.addEventListener('click', () => this.confirmAnswer());
    if (resetBtn) resetBtn.addEventListener('click', () => this.resetQuiz());
    if (pdfBtn) pdfBtn.addEventListener('click', () => this.openPdfModal());

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowLeft') this.prevQuestion();
      if (e.key === 'ArrowRight') this.nextQuestion();
      if (['a', 'b', 'c', 'd'].includes(e.key.toLowerCase())) {
        this.selectOption(e.key.toUpperCase());
      }
      if (e.key === 'Enter') {
        const confirmBtn = document.getElementById('btn-confirm');
        if (confirmBtn && !confirmBtn.disabled) this.confirmAnswer();
      }
    });
  }

  renderHeader() {
    const titleEl = document.getElementById('quiz-title');
    const badgeEl = document.getElementById('quiz-badge');
    if (titleEl) titleEl.innerText = this.chapterData.title || `Chapter ${this.chapterId}`;
    if (badgeEl) badgeEl.innerText = `Chapter ${this.chapterId}`;
    this.updateStats();
  }

  updateStats() {
    const total = this.chapterData.questions.length;
    let correctCount = 0;
    let wrongCount = 0;

    this.chapterData.questions.forEach(q => {
      if (this.progress.confirmed[q.id]) {
        if (isAnswerCorrect(q, this.progress.answers[q.id])) {
          correctCount++;
        } else {
          wrongCount++;
        }
      }
    });

    const statCorrect = document.getElementById('stat-correct');
    const statWrong = document.getElementById('stat-wrong');
    const progressThumb = document.getElementById('quiz-progress-bar');
    const answeredCount = correctCount + wrongCount;

    if (statCorrect) statCorrect.innerText = correctCount;
    if (statWrong) statWrong.innerText = wrongCount;
    if (progressThumb) {
      const pct = total > 0 ? (answeredCount / total) * 100 : 0;
      progressThumb.style.width = `${pct}%`;
    }
  }

  renderPalette() {
    const grid = document.getElementById('palette-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const questions = this.chapterData.questions;
    questions.forEach((q, idx) => {
      const item = document.createElement('div');
      item.className = 'palette-item';
      item.innerText = idx + 1;
      item.id = `palette-item-${idx}`;

      if (idx === this.currentIndex) {
        item.classList.add('active');
      }

      // Check status
      if (this.progress.confirmed[q.id]) {
        if (isAnswerCorrect(q, this.progress.answers[q.id])) {
          item.classList.add('status-correct');
        } else {
          item.classList.add('status-wrong');
        }
      }

      item.addEventListener('click', () => {
        this.goToQuestion(idx);
      });

      grid.appendChild(item);
    });
  }

  renderQuestion() {
    const questions = this.chapterData.questions;
    const qCount = questions.length;
    
    if (qCount === 0) {
      document.getElementById('question-area').innerHTML = `
        <div style="text-align: center; padding: 40px;">
          <i class="fa-solid fa-folder-open" style="font-size: 3rem; color: var(--text-muted); margin-bottom: 16px;"></i>
          <h3>No Questions in Chapter ${this.chapterId} yet</h3>
          <p style="color: var(--text-secondary); margin: 12px 0 24px;">Paste or import questions in Markdown format to populate this chapter.</p>
          <button onclick="openImportModal(${this.chapterId})" class="btn btn-primary">
            <i class="fa-solid fa-file-import"></i> Import Questions (Markdown)
          </button>
        </div>
      `;
      return;
    }

    const currentQ = questions[this.currentIndex];
    const isConfirmed = !!this.progress.confirmed[currentQ.id];
    const savedAnswer = this.progress.answers[currentQ.id];
    this.selectedOption = savedAnswer || null;

    const isMulti = String(currentQ.correct).includes('and') || currentQ.question.toLowerCase().includes('select two');
    const extractLetters = (val) => {
      if (Array.isArray(val)) return val.slice().map(s => String(s).trim().toUpperCase());
      return String(val || '')
        .replace(/and|,/gi, ' ')
        .split(/\s+/)
        .map(s => s.trim().toUpperCase())
        .filter(s => ['A', 'B', 'C', 'D'].includes(s));
    };

    const correctLetters = extractLetters(currentQ.correct);
    const chosenLetters = extractLetters(savedAnswer);

    // Update Question Badges
    const seqBadge = document.getElementById('q-seq-badge');
    const multiTag = isMulti ? ' <span style="background:rgba(236,72,153,0.2); color:#f472b6; padding:2px 8px; border-radius:12px; margin-left:6px; font-size:0.75rem;">Select TWO</span>' : '';
    if (seqBadge) seqBadge.innerHTML = `<i class="fa-regular fa-circle-question"></i> Question ${this.currentIndex + 1} of ${qCount}${multiTag}`;

    // Update Question Text (Sanitized and collapsed hard line breaks)
    const textEl = document.getElementById('q-text');
    if (textEl) {
      textEl.innerHTML = formatNormalizedHtml(currentQ.question);
    }

    // Render Options
    const optionsList = document.getElementById('options-list');
    optionsList.innerHTML = '';

    const optionKeys = ['A', 'B', 'C', 'D'];
    optionKeys.forEach(key => {
      if (!currentQ.options || !currentQ.options[key]) return;

      const optDiv = document.createElement('div');
      optDiv.className = 'option-item';
      optDiv.id = `option-${key}`;

      const isSelected = Array.isArray(this.selectedOption) 
        ? this.selectedOption.includes(key) 
        : this.selectedOption === key;

      if (isSelected) {
        optDiv.classList.add('selected');
      }

      if (isConfirmed) {
        optDiv.classList.add('locked');
        if (correctLetters.includes(key)) {
          optDiv.classList.add('confirmed-correct');
        } else if (chosenLetters.includes(key)) {
          optDiv.classList.add('confirmed-wrong');
        }
      } else {
        optDiv.addEventListener('click', () => {
          this.selectOption(key);
        });
      }

      let resultIcon = '';
      if (isConfirmed) {
        if (correctLetters.includes(key)) {
          resultIcon = '<i class="fa-solid fa-circle-check option-result-icon" style="color: var(--success);"></i>';
        } else if (chosenLetters.includes(key)) {
          resultIcon = '<i class="fa-solid fa-circle-xmark option-result-icon" style="color: var(--danger);"></i>';
        }
      }

      const optNormalizedText = escapeHtml(normalizeText(currentQ.options[key]));
      optDiv.innerHTML = `
        <div class="option-letter-badge">${key}</div>
        <div class="option-label">${optNormalizedText}</div>
        ${resultIcon}
      `;

      optionsList.appendChild(optDiv);
    });

    // Render Explanation Section if Confirmed
    const explanationContainer = document.getElementById('explanation-area');
    if (isConfirmed) {
      this.renderExplanation(currentQ, savedAnswer);
      explanationContainer.style.display = 'block';
    } else {
      explanationContainer.style.display = 'none';
      explanationContainer.innerHTML = '';
    }

    // Update Nav Buttons
    const prevBtn = document.getElementById('btn-prev');
    const nextBtn = document.getElementById('btn-next');
    const confirmBtn = document.getElementById('btn-confirm');

    if (prevBtn) prevBtn.disabled = this.currentIndex === 0;
    if (nextBtn) nextBtn.disabled = this.currentIndex === qCount - 1;

    if (confirmBtn) {
      if (isConfirmed) {
        confirmBtn.innerHTML = '<i class="fa-solid fa-check"></i> Answered';
        confirmBtn.disabled = true;
      } else {
        confirmBtn.innerHTML = '<i class="fa-solid fa-circle-check"></i> Confirm Answer';
        const hasSelection = isMulti 
          ? (Array.isArray(this.selectedOption) && this.selectedOption.length > 0)
          : !!this.selectedOption;
        confirmBtn.disabled = !hasSelection;
      }
    }

    // Update Palette active state
    document.querySelectorAll('.palette-item').forEach((item, idx) => {
      item.classList.toggle('active', idx === this.currentIndex);
    });
  }

  selectOption(key) {
    const currentQ = this.chapterData.questions[this.currentIndex];
    if (this.progress.confirmed[currentQ.id]) return; // already locked

    const isMulti = String(currentQ.correct).includes('and') || currentQ.question.toLowerCase().includes('select two');

    if (isMulti) {
      let current = Array.isArray(this.selectedOption) ? [...this.selectedOption] : (this.selectedOption ? [this.selectedOption] : []);
      if (current.includes(key)) {
        current = current.filter(k => k !== key);
      } else {
        if (current.length >= 2) {
          current.shift();
        }
        current.push(key);
      }
      this.selectedOption = current.sort();
      this.progress.answers[currentQ.id] = this.selectedOption;
    } else {
      this.selectedOption = key;
      this.progress.answers[currentQ.id] = key;
    }

    Storage.saveProgress(this.chapterId, this.progress);

    document.querySelectorAll('.option-item').forEach(el => {
      const optKey = el.id.replace('option-', '');
      const isSel = Array.isArray(this.selectedOption) 
        ? this.selectedOption.includes(optKey) 
        : this.selectedOption === optKey;
      el.classList.toggle('selected', isSel);
    });

    const confirmBtn = document.getElementById('btn-confirm');
    if (confirmBtn) {
      const hasSelection = isMulti 
        ? (Array.isArray(this.selectedOption) && this.selectedOption.length > 0)
        : !!this.selectedOption;
      confirmBtn.disabled = !hasSelection;
    }
  }

  confirmAnswer() {
    if (!this.selectedOption) return;

    const currentQ = this.chapterData.questions[this.currentIndex];
    this.progress.confirmed[currentQ.id] = true;
    Storage.saveProgress(this.chapterId, this.progress);

    this.renderQuestion();
    this.renderPalette();
    this.updateStats();
  }

  renderExplanation(question, selectedKey) {
    const container = document.getElementById('explanation-area');
    const isCorrect = isAnswerCorrect(question, selectedKey);

    const chosenDisplay = Array.isArray(selectedKey) 
      ? selectedKey.join(' and ') 
      : (selectedKey || 'None');

    const bannerClass = isCorrect ? 'success' : 'wrong';
    const bannerIcon = isCorrect ? 'fa-circle-check' : 'fa-circle-xmark';
    const bannerText = isCorrect 
      ? `Correct! Excellent work. You selected (${question.correct}).`
      : `Incorrect. You chose (${chosenDisplay}), but the correct answer is (${question.correct}).`;

    // Format distractor analysis (why other options are not correct)
    let distractorHtml = '';
    const otherKeys = ['A', 'B', 'C', 'D'].filter(k => k !== question.correct && question.options && question.options[k]);
    
    if (question.why_incorrect && Object.keys(question.why_incorrect).length > 0) {
      const items = otherKeys.map(k => {
        const rawReason = question.why_incorrect[k] || `Option ${k} is incorrect in this context.`;
        const reason = formatNormalizedHtml(rawReason);
        return `
          <div class="distractor-item">
            <span class="opt-tag">Option ${k}:</span>
            <div>${reason}</div>
          </div>
        `;
      }).join('');

      distractorHtml = `
        <div style="margin-top: 18px;">
          <h4 class="distractor-analysis-title">
            <i class="fa-solid fa-triangle-exclamation" style="color: var(--danger);"></i> 
            Why Other Options Are Incorrect:
          </h4>
          <div class="distractor-grid">
            ${items}
          </div>
        </div>
      `;
    }

    const expText = formatNormalizedHtml(question.explanation) || '<p>Detailed explanation will be provided upon verification.</p>';

    container.innerHTML = `
      <div class="explanation-card glass">
        <div class="explanation-banner ${bannerClass}">
          <i class="fa-solid ${bannerIcon}"></i>
          <span>${bannerText}</span>
        </div>
        <div class="explanation-core-box">
          <h4><i class="fa-solid fa-lightbulb"></i> Detailed Explanation:</h4>
          <div>${expText}</div>
        </div>
        ${distractorHtml}
      </div>
    `;
  }

  prevQuestion() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.renderQuestion();
    }
  }

  nextQuestion() {
    if (this.currentIndex < this.chapterData.questions.length - 1) {
      this.currentIndex++;
      this.renderQuestion();
    }
  }

  goToQuestion(idx) {
    if (idx >= 0 && idx < this.chapterData.questions.length) {
      this.currentIndex = idx;
      this.renderQuestion();
    }
  }

  resetQuiz() {
    if (confirm(`Are you sure you want to reset your answers and progress for Chapter ${this.chapterId}?`)) {
      this.progress = { answers: {}, confirmed: {} };
      Storage.saveProgress(this.chapterId, this.progress);
      this.currentIndex = 0;
      this.renderQuestion();
      this.renderPalette();
      this.updateStats();
    }
  }

  openPdfModal() {
    downloadChapterPdfDirectly(this.chapterId);
  }
}
window.QuizEngine = QuizEngine;

// ============================================================
// PDF GENERATION & PRINT ENGINE
// ============================================================
function downloadChapterPdfDirectly(chapterId) {
  // Retrieve data
  const custom = Storage.getCustomChapter(chapterId);
  const chData = custom || (window.CHAPTER_DATA && window.CHAPTER_DATA[chapterId]);
  
  if (!chData || !chData.questions || chData.questions.length === 0) {
    alert(`No questions found in Chapter ${chapterId} to generate PDF.`);
    return;
  }

  // Build clean printable document in an offscreen iframe or printable container
  let printArea = document.getElementById('printable-pdf-area');
  if (!printArea) {
    printArea = document.createElement('div');
    printArea.id = 'printable-pdf-area';
    printArea.className = 'print-pdf-header';
    document.body.appendChild(printArea);
  }

  let questionsHtml = '';
  chData.questions.forEach((q, idx) => {
    let optionsHtml = '';
    ['A', 'B', 'C', 'D'].forEach(letter => {
      if (q.options && q.options[letter]) {
        const isCorrect = letter === q.correct;
        const optText = escapeHtml(normalizeText(q.options[letter]));
        optionsHtml += `
          <div class="print-opt-item" style="margin: 4px 0; color: ${isCorrect ? '#047857' : '#374151'}; font-weight: ${isCorrect ? 'bold' : 'normal'};">
            <strong>${letter})</strong> ${optText} ${isCorrect ? ' ✓ (Correct Answer)' : ''}
          </div>
        `;
      }
    });

    let whyIncorrectHtml = '';
    if (q.why_incorrect && Object.keys(q.why_incorrect).length > 0) {
      whyIncorrectHtml = '<div style="margin-top: 6px; font-size: 10pt; color: #6b7280;"><strong>Distractor Analysis (Why others are incorrect):</strong><ul style="margin: 4px 0 0 18px;">';
      Object.entries(q.why_incorrect).forEach(([opt, why]) => {
        whyIncorrectHtml += `<li><strong>Option ${opt}:</strong> ${escapeHtml(normalizeText(why))}</li>`;
      });
      whyIncorrectHtml += '</ul></div>';
    }

    const qText = escapeHtml(normalizeText(q.question));
    const expText = escapeHtml(normalizeText(q.explanation || 'N/A'));

    questionsHtml += `
      <div class="print-q-block" style="page-break-inside: avoid; border-bottom: 1.5px solid #e5e7eb; padding: 18px 0; font-family: sans-serif;">
        <div class="print-q-text" style="font-size: 12pt; font-weight: 700; color: #111827; margin-bottom: 8px; line-height: 1.6; white-space: normal;">
          Q${idx + 1}. ${qText}
        </div>
        <div class="print-options" style="margin-left: 14px;">
          ${optionsHtml}
        </div>
        <div class="print-answer-key" style="margin-top: 10px; background: #f8fafc; border-left: 4px solid #2563eb; padding: 8px 12px; font-size: 10pt; color: #1e293b; line-height: 1.5;">
          <strong>Explanation:</strong> ${expText}
          ${whyIncorrectHtml}
        </div>
      </div>
    `;
  });

  const now = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  printArea.innerHTML = `
    <div style="font-family: sans-serif; padding: 20px;">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2563eb; padding-bottom: 12px; margin-bottom: 20px;">
        <div>
          <h1 style="font-size: 18pt; color: #0f172a; margin: 0;">${escapeHtml(chData.title)}</h1>
          <p style="color: #64748b; margin: 4px 0 0; font-size: 10pt;">Comprehensive MCQ Question Bank with Detailed Explanations</p>
        </div>
        <div style="text-align: right; font-size: 9pt; color: #64748b;">
          <div>Total Questions: <strong>${chData.questions.length}</strong></div>
          <div>Generated: ${now}</div>
        </div>
      </div>
      <div>
        ${questionsHtml}
      </div>
      <div style="text-align: center; margin-top: 30px; font-size: 9pt; color: #94a3b8; border-top: 1px solid #e2e8f0; padding-top: 10px;">
        Panaversity Exam Portal • Chapter ${chapterId} Question Bank
      </div>
    </div>
  `;

  // Trigger print dialog
  window.print();
}

// ============================================================
// MARKDOWN IMPORT MODAL CONTROLLER
// ============================================================
function openImportModal(chapterId = 1) {
  let modal = document.getElementById('import-modal');
  if (!modal) return;
  const select = document.getElementById('import-chapter-select');
  if (select) select.value = chapterId;
  modal.classList.add('active');
}

function closeImportModal() {
  const modal = document.getElementById('import-modal');
  if (modal) modal.classList.remove('active');
}

// Client-side instant Markdown Parser
function parseMarkdownInBrowser(mdText, chapterId) {
  const lines = mdText.split('\n');
  const questions = [];
  let currentQ = null;
  let collectingExplanation = false;
  let collectingOptionBreakdowns = null;

  lines.forEach(line => {
    const stripped = line.trim();
    if (!stripped) return;

    // Check Question Start
    const qMatch = stripped.match(/^(?:###?\s*|)(?:Question\s*|Q\s*|)(\d+)[\.:\s]+(.*)/i);
    if (qMatch && (stripped.includes('?') || stripped.split(' ').length > 3 || stripped.includes('Question') || stripped.includes('Q.'))) {
      if (currentQ && currentQ.question) {
        questions.push(currentQ);
      }
      currentQ = {
        id: parseInt(qMatch[1]) || (questions.length + 1),
        question: qMatch[2].trim(),
        options: {},
        correct: 'A',
        explanation: '',
        why_incorrect: {}
      };
      collectingExplanation = false;
      collectingOptionBreakdowns = null;
      return;
    }

    if (!currentQ) return;

    // Correct Answer
    const corrMatch = stripped.match(/^\s*[-*]?\s*(?:\*\*)?(?:Correct\s*(?:Answer|Option)?|Answer)\s*(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*\(?([A-Da-d])\)?/i);
    if (corrMatch) {
      currentQ.correct = corrMatch[1].toUpperCase();
      collectingExplanation = false;
      collectingOptionBreakdowns = null;
      return;
    }

    // Why incorrect breakdown
    const distrMatch = stripped.match(/^\s*[-*]?\s*(?:\*\*)?(?:Why\s+([A-Da-d])\s+is\s+(?:not\s+correct|incorrect)|Option\s+([A-Da-d]))(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*(.*)/i);
    if (distrMatch) {
      const letter = (distrMatch[1] || distrMatch[2]).toUpperCase();
      const reason = (distrMatch[3] || '').trim();
      currentQ.why_incorrect[letter] = reason;
      collectingOptionBreakdowns = letter;
      collectingExplanation = false;
      return;
    }

    // Explanation
    const expMatch = stripped.match(/^\s*[-*]?\s*(?:\*\*)?(?:Detailed\s+Explanation|Explanation)(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*(.*)/i);
    if (expMatch) {
      currentQ.explanation = (expMatch[1] || '').trim();
      collectingExplanation = true;
      collectingOptionBreakdowns = null;
      return;
    }

    // Option (A, B, C, D)
    const optMatch = stripped.match(/^[-*]?\s*(?:([A-Da-d])[\.\)]|\(([A-Da-d])\))\s*(.*)/);
    if (optMatch && !collectingExplanation && !collectingOptionBreakdowns) {
      const letter = (optMatch[1] || optMatch[2]).toUpperCase();
      const content = (optMatch[3] || '').trim();
      currentQ.options[letter] = content;
      return;
    }

    if (collectingExplanation) {
      currentQ.explanation = (currentQ.explanation + ' ' + stripped).trim();
      return;
    }

    if (collectingOptionBreakdowns) {
      const letter = collectingOptionBreakdowns;
      currentQ.why_incorrect[letter] = (currentQ.why_incorrect[letter] + ' ' + stripped).trim();
      return;
    }

    if (Object.keys(currentQ.options).length === 0) {
      currentQ.question = (currentQ.question + ' ' + stripped).trim();
    }
  });

  if (currentQ && currentQ.question) {
    questions.push(currentQ);
  }

  return {
    chapterId: parseInt(chapterId),
    title: `Chapter ${chapterId}`,
    totalQuestions: questions.length,
    questions: questions
  };
}

function handleImportSubmit() {
  const select = document.getElementById('import-chapter-select');
  const textarea = document.getElementById('import-markdown-text');
  if (!select || !textarea) return;

  const chapterId = parseInt(select.value);
  const mdText = textarea.value.trim();

  if (!mdText) {
    alert('Please paste some Markdown questions first.');
    return;
  }

  const parsed = parseMarkdownInBrowser(mdText, chapterId);
  if (parsed.questions.length === 0) {
    alert('No questions were recognized. Please ensure questions follow the standard markdown format.');
    return;
  }

  // Save to Storage
  Storage.saveCustomChapter(chapterId, parsed);
  alert(`Success! Successfully parsed and saved ${parsed.questions.length} questions for Chapter ${chapterId}.`);
  closeImportModal();

  // If on quiz page and same chapter, reload
  if (window.location.pathname.includes('quiz.html')) {
    window.location.reload();
  } else {
    // If on index page, refresh cards
    initIndexPage();
  }
}

// Global initialization
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  const themeToggle = document.getElementById('theme-toggle-btn');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }

  if (document.getElementById('chapters-grid')) {
    initIndexPage();
  }

  if (document.getElementById('question-area')) {
    window.quizEngine = new QuizEngine();
    window.quizEngine.init();
  }
});
