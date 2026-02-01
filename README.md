# 📄 Job Genie – AI Resume & Hiring Assistant

An **AI-powered resume evaluation and job discovery platform** that helps candidates analyze resumes, discover relevant jobs, and prepare for interviews — all in one place.

Built using **Groq LLM**, **Tavily Web Search**, and **Streamlit**, designed for **hackathons, demos, and real-world scalability**.

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
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env                  # API keys (local only)
├── .env.example          # Environment variable template
├── .gitignore            # Prevents secret leakage
└── README.md             # Project documentation
```

---

## ✨ Features

### 1️⃣ Resume Evaluation
- Resume score (out of 10)
- Clear improvement suggestions
- Skill & role alignment analysis
- AI-powered, concise feedback

### 2️⃣ Job Search (Web-Powered)
- AI extracts suitable job titles from resume
- Searches latest jobs using Tavily
- Sources include LinkedIn & Indeed
- No scraping → production-safe

### 3️⃣ Interview Preparation
- Technical interview questions
- Non-technical / HR questions
- Questions tailored directly from resume content

### 4️⃣ Skill Test Integration
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
| Backend | Python |
| Deployment | Streamlit Cloud / Render / Vercel |

---

## 🔒 Security & Best Practices

- ✅ No API keys hard-coded
- ✅ Environment variables only
- ✅ `.env` excluded via `.gitignore`
- ✅ GitHub Secret Scanning safe
- ✅ Hackathon & production ready

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

---

## 📌 Notes

- Uses Groq's ultra-fast LLMs for real-time responses
- Tavily ensures legal & reliable job discovery
- Designed to scale into:
  - Live mock interviews
  - Skill-gap analysis
  - AI recruiter dashboards
  - Hiring automation platforms

---

## 🌱 Future Enhancements

- 🎤 AI voice-based mock interviews
- 📊 Resume vs job-market gap analysis
- 🧠 Personalized learning paths
- 🤝 Recruiter dashboard
- 📹 Video interview evaluation

---

## 🙌 Built For

- Hackathons
- College projects
- Startup MVPs
- AI hiring platforms

---

Good luck & happy building 🚀
