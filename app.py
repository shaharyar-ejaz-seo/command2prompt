import streamlit as st
import requests

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Shaharyar Ejaz Prompt Studio",
    page_icon="✨",
    layout="wide",
)

BRAND_NAME = "Shaharyar Ejaz Prompt Studio"
TAGLINE = "Premium AI Prompt Systems for SEO, AI Search & Storytelling"
OWNER = "Shaharyar Ejaz"
LINKEDIN = "https://www.linkedin.com/in/shaharyar-ejaz-seo/"
APP_URL = "https://shaharyarpropmtseo.streamlit.app"

# ----------------------------
# UI STYLE
# ----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0B1220 0%, #111827 100%);
    color: white;
}

.main-box {
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
}

.result-box {
    padding: 20px;
    border-radius: 18px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
}

.footer {
    text-align:center;
    margin-top:40px;
    color:#94A3B8;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------
st.markdown(f"""
<div class="main-box">
<h1>{BRAND_NAME}</h1>
<p>{TAGLINE}</p>
<p><b>{OWNER}</b> • <a href="{LINKEDIN}" target="_blank">LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# PROMPT BUILDER
# ----------------------------
def build_prompt(command, category, tone, length):
    return f"""
You are a professional AI Prompt Engineer.

Task:
Convert the following command into a HIGH-END, PROFESSIONAL, AI-OPTIMIZED prompt.

Command:
{command}

Requirements:
- SEO optimized
- EEAT friendly
- Humanized tone
- Clear structure
- Conversion focused
- Ready for AI tools (ChatGPT, Gemini, Claude)

Category: {category}
Tone: {tone}
Length: {length}

Output must include:
- Role
- Objective
- Target Audience
- Structure
- Instructions

End with:
Prepared by Shaharyar Ejaz Prompt Studio
"""

# ----------------------------
# API CALL
# ----------------------------
def generate_prompt(command, category, tone, length):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except:
        return None, "❌ API Key missing. Add it in Secrets."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": APP_URL,
        "X-Title": BRAND_NAME,
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a professional prompt engineer."},
            {"role": "user", "content": build_prompt(command, category, tone, length)}
        ]
    }

    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        data = res.json()

        if res.status_code == 401:
            return None, "❌ API Authentication failed. Check your API key."

        if res.status_code != 200:
            return None, "⚠️ API Error occurred. Try again."

        return data["choices"][0]["message"]["content"], None

    except:
        return None, "⚠️ Network error. Please try again."

# ----------------------------
# UI FORM
# ----------------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

command = st.text_area("Enter your command")

col1, col2, col3 = st.columns(3)

with col1:
    category = st.selectbox("Category", [
        "SEO Blog",
        "Story",
        "Ad Copy",
        "Product",
        "YouTube",
        "Custom"
    ])

with col2:
    tone = st.selectbox("Tone", [
        "Professional",
        "Premium",
        "Humanized",
        "Creative"
    ])

with col3:
    length = st.selectbox("Length", [
        "Short",
        "Medium",
        "Detailed"
    ])

generate = st.button("Generate Prompt")

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# RESULT
# ----------------------------
if generate:
    if not command:
        st.warning("Enter command first.")
    else:
        with st.spinner("Generating..."):
            result, error = generate_prompt(command, category, tone, length)

            if error:
                st.error(error)
            else:
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.code(result)
                st.download_button("Download", result)
                st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# FOOTER
# ----------------------------
st.markdown(f"""
<div class="footer">
Built by {OWNER} • <a href="{LINKEDIN}" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
