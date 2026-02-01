import streamlit as st
import os
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
import requests
import time

# ===================== ENV SETUP =====================
load_dotenv()  # works locally, ignored in GitHub if .env not present

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in environment variables")
    st.stop()

# ===================== LLM INIT =====================
llm = ChatGroq(
    model="qwen/qwen3-32b",
    api_key=GROQ_API_KEY
)

# ===================== PROMPTS =====================
evaluation_prompt = ChatPromptTemplate.from_template("""
Analyze this resume and provide ONLY:
1. Resume Score (out of 10)
2. Key Changes Needed (3 bullet points)
3. Eligible Job Roles (3 roles)

Resume:
{context}
""")

job_search_prompt = ChatPromptTemplate.from_template("""
Based on this resume, give ONLY 3 job titles (one per line).

Resume:
{context}
""")

technical_prompt = ChatPromptTemplate.from_template("""
Generate exactly 10 technical interview questions.
Only questions. No answers.

Resume:
{context}
""")

non_technical_prompt = ChatPromptTemplate.from_template("""
Generate exactly 10 non-technical interview questions.
Only questions. No answers.

Resume:
{context}
""")

# ===================== HELPERS =====================
def extract_resume_text(uploaded_file):
    try:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            path = tmp.name

        loader = PyPDFLoader(path)
        docs = loader.load()
        os.remove(path)

        return "\n".join([d.page_content for d in docs])

    except Exception as e:
        st.error(f"Resume error: {e}")
        return None


def ask_llm(prompt, text):
    try:
        return llm.invoke(prompt.format(context=text)).content
    except Exception as e:
        return f"LLM Error: {e}"


def tavily_search(query, max_results=5):
    if not TAVILY_API_KEY:
        return []

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "max_results": max_results,
                "search_depth": "basic"
            },
            timeout=10
        )
        return response.json().get("results", [])
    except:
        return []


def search_jobs(job_titles):
    jobs = []
    titles = [t.strip() for t in job_titles.split("\n") if t.strip()]

    for title in titles[:3]:
        results = tavily_search(f"latest {title} jobs site:linkedin.com OR site:indeed.com")
        for r in results:
            jobs.append({
                "title": title,
                "company": r.get("title", "Unknown"),
                "url": r.get("url"),
                "source": "Web"
            })
        time.sleep(0.5)

    return jobs[:10]

# ===================== UI =====================
st.set_page_config(page_title="Job Genie", layout="centered")
st.title("📄 Job Genie – AI Resume & Hiring Assistant")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_resume_text(uploaded_file)

    if resume_text:
        option = st.radio(
            "Choose Feature",
            ["Resume Evaluation", "Job Search", "Interview Preparation"]
        )

        # -------- Resume Evaluation --------
        if option == "Resume Evaluation":
            st.header("📊 Resume Evaluation")
            result = ask_llm(evaluation_prompt, resume_text)
            st.markdown(result)

        # -------- Job Search --------
        elif option == "Job Search":
            st.header("🔍 Job Opportunities")
            titles = ask_llm(job_search_prompt, resume_text)
            jobs = search_jobs(titles)

            if jobs:
                for i, job in enumerate(jobs, 1):
                    with st.expander(f"{i}. {job['title']}"):
                        st.write(f"**Company:** {job['company']}")
                        st.write(f"**Source:** {job['source']}")
                        st.markdown(f"[Apply Here]({job['url']})")
            else:
                st.info("No jobs found")

        # -------- Interview Prep --------
        else:
            st.header("🎤 Interview Preparation")
            itype = st.radio("Select Type", ["Technical", "Non-Technical"])

            if st.button("Generate Questions"):
                if itype == "Technical":
                    questions = ask_llm(technical_prompt, resume_text)
                else:
                    questions = ask_llm(non_technical_prompt, resume_text)

                for q in questions.split("\n"):
                    if q.strip():
                        st.write(q)

            st.markdown(
                "[➡️ Take Live Skill Test](https://skill-proof-u76q.vercel.app/)",
                unsafe_allow_html=True
            )
else:
    st.info("📁 Upload a resume to get started")
