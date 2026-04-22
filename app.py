import streamlit as st
import requests

st.set_page_config(page_title="Command2Prompt", layout="centered")

st.title("Command2Prompt")
st.write("Short command do aur professional prompt hasil karo.")

command = st.text_area("Apni short command likho", height=120)

category = st.selectbox(
    "Prompt Category",
    [
        "Custom Prompt",
        "SEO Blog Prompt",
        "Meta Prompt",
        "Thumbnail Prompt",
        "Product Description Prompt",
        "Social Media Prompt"
    ]
)

tone = st.selectbox(
    "Tone",
    ["Professional", "Premium", "Authoritative", "Humanized", "Creative"]
)

length = st.selectbox(
    "Output Length",
    ["Short", "Medium", "Detailed"]
)

if st.button("Generate Prompt"):
    if not command.strip():
        st.warning("Pehle apni command likho.")
    else:
        api_key = st.secrets["OPENROUTER_API_KEY"]

        system_prompt = f"""
You are an elite prompt engineer.

Convert the user's short command into a professional, well-structured, ready-to-use AI prompt.

Category: {category}
Tone: {tone}
Length: {length}

Rules:
- Understand the goal behind the short command
- Infer reasonable missing details intelligently
- Make the output polished, professional, and copy-paste ready
- Use clear structure where helpful
- Include sections like Role, Objective, Inputs, Instructions, Constraints, Output Format if useful
- Avoid fluff
- Write in clean English
"""

        payload = {
            "model": "openrouter/free",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": command}
            ]
        }

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        data = response.json()
        result = data["choices"][0]["message"]["content"]

        st.subheader("Generated Prompt")
        st.code(result, language="markdown")
