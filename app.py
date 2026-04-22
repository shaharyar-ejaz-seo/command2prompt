import streamlit as st
import requests
from datetime import datetime

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Shaharyar Ejaz Prompt Studio",
    page_icon="✨",
    layout="wide"
)

# ----------------------------
# BRANDING
# ----------------------------
BRAND_NAME = "Shaharyar Ejaz Prompt Studio"
BRAND_TAGLINE = "Professional AI Prompt Systems for Brands, Agencies & Creators"
BRAND_OWNER = "Shaharyar Ejaz"
LINKEDIN = "https://www.linkedin.com/in/shaharyar-ejaz-seo/"

# ----------------------------
# CSS (NO f-string = NO ERROR)
# ----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0B1220, #111827, #172033);
    color: white;
}

.block-container {
    max-width: 1100px;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.title {
    font-size: 44px;
    font-weight: 800;
}

.subtitle {
    color: #CBD5E1;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
}

.result {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
}

button {
    border-radius: 12px !important;
}

.footer {
    text-align:center;
    color:#94A3B8;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# PROMPT TYPES
# ----------------------------
PROMPTS = {
    "Custom Prompt": "General professional prompt",
    "SEO Blog Prompt": "SEO optimized blog writing",
    "Story Prompt": "Story with hook, character, conflict, climax",
    "YouTube Script": "Engaging YouTube script",
    "Ad Copy": "High converting ads",
    "Product Description": "Conversion focused product copy",
    "Social Media": "Engaging social captions",
    "Email": "Professional email writing",
}

# ----------------------------
# AI FUNCTION (SAFE)
# ----------------------------
def generate_prompt(command, category, tone, length):
    api_key = st.secrets.get("OPENROUTER_API_KEY")

    if not api_key:
        return None, "API key missing. Add it in Secrets."

    system = f"""
You are a professional prompt engineer.

Category: {category}
Tone: {tone}
Length: {length}

Convert user command into a premium structured AI prompt.
Make it clean, professional, and ready-to-use.
"""

    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": command}
                ]
            },
            timeout=60
        )

        data = res.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"], None
        else:
            return None, str(data)

    except Exception as e:
        return None, str(e)

# ----------------------------
# UI
# ----------------------------
st.markdown(f"""
<div class="hero">
<div class="title">{BRAND_NAME}</div>
<div class="subtitle">{BRAND_TAGLINE}</div>
<div class="subtitle">{BRAND_OWNER}</div>
</div>
""", unsafe_allow_html=True)

command = st.text_area("Enter your command")

col1, col2, col3 = st.columns(3)

with col1:
    category = st.selectbox("Category", list(PROMPTS.keys()))
with col2:
    tone = st.selectbox("Tone", ["Professional", "Creative", "Emotional"])
with col3:
    length = st.selectbox("Length", ["Short", "Medium", "Detailed"])

if st.button("Generate Prompt"):
    if not command:
        st.warning("Enter command first")
    else:
        with st.spinner("Generating..."):
            result, error = generate_prompt(command, category, tone, length)

            if error:
                st.error(error)
            else:
                st.markdown('<div class="result">', unsafe_allow_html=True)
                st.code(result)
                st.markdown('</div>', unsafe_allow_html=True)

                st.download_button(
                    "Download",
                    result,
                    file_name="prompt.txt"
                )

st.markdown(f"""
<div class="footer">
Built by Shaharyar Ejaz • <a href="{LINKEDIN}" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
