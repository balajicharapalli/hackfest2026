# 📄 Job Genie – AI Resume & Hiring Assistant

An **AI-powered resume evaluation and job discovery platform** that helps candidates analyze resumes, discover relevant jobs, and prepare for interviews — all in one place.

Built using **Groq LLM**, **Tavily Web Search**, and **Streamlit**, designed for **hackathons, demos, and real-world scalability**.

---

## 🎯 Core Promise

**Take 3 inputs → Give 1 intelligent decision**

- Resume text (what they claim)
- GitHub summary (what they've built)
- Coding challenge submission (how they solve problems)

**Output:**
- Skill score (0-100)
- Strengths & weaknesses
- Hire / Maybe / Not Ready recommendation
- Confidence level

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/job-genie.git
cd job-genie
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project root (do not commit this file):

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

**🔑 Get API Keys From:**
- **Groq** → https://console.groq.com
- **Tavily** → https://tavily.com

📌 **Important:** Make sure `.env` is added to `.gitignore`.

### Step 4: Run the App

```bash
streamlit run app.py
```

The app will open at: 👉 **`http://localhost:8501`**

---

## 📁 Project Structure

```
job-genie/
├── app.py                      # Main Streamlit application
├── skill_validator.py          # AI Skill Validator prototype
├── requirements.txt            # Python dependencies
├── .env                        # API keys (local only)
├── .env.example                # Environment variable template
├── .gitignore                  # Prevents secret leakage
└── README.md                   # Project documentation
```

---

## ✨ Features

### 1️⃣ **AI Skill Validator** (⭐ CORE PROTOTYPE)

The heart of Job Genie. A process-based evaluation system that validates real-world developer readiness by analyzing three evidence sources:

**What it evaluates:**
- **Practical Coding Ability** — Does the code show logical thinking? Is the solution reasonable?
- **Code Quality & Practices** — Readability, naming, structure, simplicity
- **Learning & Problem-Solving** — Time vs complexity, attempts, trial-and-error vs clear thinking
- **Consistency of Claims** — Resume vs GitHub activity alignment
- **Communication Clarity** — Code comments, explanations, documentation

**Output (JSON):**
```json
{
  "overall_skill_score": 78,
  "skill_level": "Intermediate",
  "hire_recommendation": "Hire",
  "confidence": 85,
  "strengths": [
    "Clean, readable code with good naming conventions",
    "Solved challenge efficiently with minimal attempts"
  ],
  "weaknesses": [
    "Limited GitHub contributions in past 3 months",
    "Resume claims advanced Python but only 2 GitHub repos"
  ],
  "evidence_summary": {
    "resume_vs_github": "slightly mismatched",
    "coding_challenge": "strong",
    "learning_behavior": "good"
  },
  "final_feedback": "Solid intermediate developer with good problem-solving skills. Resume slightly overstates experience, but coding challenge shows genuine capability. Ready to hire with proper onboarding."
}
```

**🎤 How to Demo:**
> "We give the AI three things — what the candidate claims, what they actually coded before, and how they solve a problem live. The AI doesn't just score output. It judges thinking, consistency, and readiness."

---

### 2️⃣ Resume Evaluation
- Resume score (out of 10)
- Clear improvement suggestions
- Skill & role alignment analysis
- AI-powered, concise feedback

### 3️⃣ Job Search (Web-Powered)
- AI extracts suitable job titles from resume
- Searches latest jobs using Tavily
- Sources include LinkedIn & Indeed
- No scraping → production-safe

### 4️⃣ Interview Preparation
- Technical interview questions
- Non-technical / HR questions
- Questions tailored directly from resume content

### 5️⃣ Skill Test Integration
- Redirects users to SkillProof live skill assessments
- Enables an end-to-end hiring workflow

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| LLM | Groq (Qwen 32B) |
| Web Search | Tavily API |
| PDF Parsing | LangChain + PyPDFLoader |
| Skill Validation | Custom AI Prompt + JSON Output |
| Backend | Python |
| Deployment | Streamlit Cloud / Render / Vercel |

---

## 🔒 Security & Best Practices

- ✅ No API keys hard-coded
- ✅ Environment variables only
- ✅ `.env` excluded via `.gitignore`
- ✅ GitHub Secret Scanning safe
- ✅ Hackathon & production ready
- ✅ Process-based evaluation (not ML model bias)
- ✅ Transparent reasoning for all scores

---

## 🧠 The AI Skill Validator Prompt

This is the **single, copy-paste-ready prompt** that powers the evaluation:

```
You are an AI hiring assistant evaluating a software developer for real-world job readiness.
This is a PROTOTYPE evaluation, not a final hiring decision.

Your task is to analyze THREE sources of evidence and give a simple, honest assessment.

================================
INPUT DATA
================================
1) RESUME (claims and background):
{resume_text}

2) GITHUB EVIDENCE:
- Commit count
- Recent activity
- Languages used
- Sample code snippet
{github_summary}

3) CODING CHALLENGE PERFORMANCE:
- Submitted code
- Time taken
- Number of attempts
{challenge_data}

================================
WHAT YOU MUST EVALUATE
================================
Focus on REAL SKILL, not certificates.

Evaluate the candidate on:
1. Practical Coding Ability  
   - Does the code show logical thinking?
   - Is the approach reasonable?
   - Is the solution understandable?

2. Code Quality & Practices  
   - Readability
   - Naming
   - Structure
   - Simplicity vs over-engineering

3. Learning & Problem-Solving Process  
   - Time taken vs complexity
   - Number of attempts
   - Signs of trial-and-error vs clear thinking

4. Consistency of Claims  
   - Do resume claims match GitHub activity?
   - Does challenge performance align with claimed skills?

5. Communication Clarity (if visible in explanations/comments)

================================
OUTPUT FORMAT (JSON ONLY)
================================
{
  "overall_skill_score": <0-100>,
  "skill_level": "<Beginner | Intermediate | Advanced>",
  "hire_recommendation": "<Hire | Maybe | Not Ready>",
  "confidence": <0-100>,
  "strengths": [
    "strength 1",
    "strength 2"
  ],
  "weaknesses": [
    "weakness 1",
    "weakness 2"
  ],
  "evidence_summary": {
    "resume_vs_github": "<consistent | slightly mismatched | mismatched>",
    "coding_challenge": "<strong | average | weak>",
    "learning_behavior": "<good | moderate | poor>"
  },
  "final_feedback": "2–3 sentences explaining the decision in simple language"
}

Be strict but fair.
Base everything ONLY on the given evidence.
Do not assume or exaggerate.
```

---

## 🛠️ Troubleshooting

### GROQ_API_KEY Not Found
- Ensure `.env` file exists
- Verify key names match exactly
- Restart Streamlit after updating `.env`

### Tavily Search Not Working
- Verify `TAVILY_API_KEY`
- App still runs with job search disabled (graceful fallback)

### PDF Not Loading
```bash
pip install pypdf
```

### Skill Validator Not Returning JSON
- Ensure all three inputs are filled (Resume, GitHub, Challenge)
- Check Groq API quota
- Verify prompt format matches exactly

---

## 📌 Notes

- Uses Groq's ultra-fast LLMs for real-time responses
- Tavily ensures legal & reliable job discovery
- **AI Skill Validator uses process-based evaluation** (not opaque ML scoring)
- Designed to scale into:
  - Live coding assessment platform
  - Recruiter dashboard with candidate insights
  - Skill-gap analysis & learning recommendations
  - Hiring automation workflows
  - API for third-party integration

---

## 🌱 Future Enhancements

- 🎤 AI voice-based mock interviews
- 📊 Resume vs job-market gap analysis
- 🧠 Personalized learning paths based on skill gaps
- 🤝 Recruiter dashboard with batch candidate evaluation
- 📹 Video interview evaluation & body language analysis
- 🔄 Skill trend analysis (improvement over time)
- 🏆 Benchmark against industry standards
- 🌐 Multi-language code evaluation




## 📖 How to Use (User Guide)

### For Candidates:
1. Paste your resume text
2. Provide GitHub summary (commits, languages, code snippet)
3. Submit your coding challenge solution
4. Get instant feedback with concrete next steps

### For Recruiters:
1. Load candidate profile
2. Get structured evaluation in seconds
3. See consistency check between claims and evidence
4. Make data-backed hiring decisions



Good luck & happy building 🚀

