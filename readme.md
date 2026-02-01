# Resume Toolkit - Setup Instructions

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Environment Variables
Create a `.env` file in your project root:

```
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

**Get API Keys From:**
- **HuggingFace**: https://huggingface.co/settings/tokens
- **Groq**: https://console.groq.com
- **Tavily**: https://tavily.com

### Step 3: Run the App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📋 Key Changes Made

### Imports Fixed:
- ✅ `from langchain_core.prompts import ChatPromptTemplate` (correct path)
- ✅ `from langchain.chains import load_qa_chain` (simplified import)
- ✅ `from langchain_text_splitters import RecursiveCharacterTextSplitter` (new location)
- ✅ All other imports from `langchain_community` (unchanged)

### Error Handling:
- ✅ Better error messages
- ✅ Input validation
- ✅ Fallback handling for missing API keys
- ✅ Graceful degradation if Tavily search fails

### UI Improvements:
- ✅ Better visual indicators (✅, 🔄, ❌)
- ✅ Clearer section headers
- ✅ Informative messages when no file uploaded
- ✅ Proper error handling display

---

## 📁 File Structure

```
your-project/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── .env                   # API keys (create this)
├── .env.example          # Template for .env
└── README.md             # Documentation
```

---

## ✨ Features

### 1. Resume Evaluation
- Rates resume 1-10
- Identifies strengths
- Suggests improvements
- Recommends missing skills
- Suggests relevant job roles

### 2. Job Search
- Generates search queries
- Suggests relevant roles
- Searches job portals
- Finds freelance opportunities

### 3. Interview Preparation
- **Technical Questions**: Based on skills & projects
- **Non-Technical Questions**: Behavioral & soft skills

---

## 🛠️ Troubleshooting

### Missing Module Error
```bash
pip install langchain-text-splitters
```

### API Key Not Found
- Check `.env` file exists
- Verify key names match exactly
- Restart Streamlit after changing `.env`

### Memory Error (FAISS/Embeddings)
```bash
pip install --upgrade sentence-transformers
```

### Groq API Error
- Verify `GROQ_API_KEY` is valid
- Check you have API credits

---

## 📝 Notes

- The app uses **Groq's Gemma 2 9B** model (fast & free tier available)
- **HuggingFace embeddings** are used for vector similarity
- **FAISS** creates in-memory vector database
- **Tavily** searches the web for job opportunities

---

Good luck! 🚀