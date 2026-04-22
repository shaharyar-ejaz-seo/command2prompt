import streamlit as st
import requests
from datetime import datetime

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Command2Prompt",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# BRAND SETTINGS
# ----------------------------
BRAND_NAME = "Shaharyar Ejaz Prompt Studio"
BRAND_TAGLINE = "Professional AI prompt systems for brands, agencies, creators, and storytellers."
BRAND_OWNER = "Shaharyar Ejaz"
BRAND_EMAIL = "contact@shaharyarejaz.com"
PRIMARY_COLOR = "#334155"
SECONDARY_COLOR = "#64748B"
ACCENT_COLOR = "#94A3B8"
CARD_BG = "rgba(255,255,255,0.05)"
BORDER_COLOR = "rgba(255,255,255,0.09)"
TEXT_MUTED = "#CBD5E1"
DEFAULT_MODEL = "openai/gpt-4o-mini"

# ----------------------------
# CSS
# ----------------------------
st.markdown(
    f"""
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(100,116,139,0.12), transparent 24%),
                radial-gradient(circle at bottom right, rgba(51,65,85,0.16), transparent 22%),
                linear-gradient(135deg, #0B1220 0%, #111827 45%, #172033 100%);
            color: white;
        }}
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }}
        .brand-hero {
            padding: 30px;
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(51,65,85,0.28), rgba(255,255,255,0.03));
            border: 1px solid rgba(203,213,225,0.10);
            box-shadow: 0 12px 40px rgba(0,0,0,0.22);
            margin-bottom: 18px;
        }}
        .brand-pill {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(148,163,184,0.10);
            border: 1px solid rgba(203,213,225,0.14);
            color: #E2E8F0;
            font-size: 13px;
            margin-bottom: 14px;
        }}
        .brand-title {{
            font-size: 52px;
            font-weight: 800;
            line-height: 1.05;
            margin: 0 0 8px 0;
            letter-spacing: -0.03em;
        }}
        .brand-subtitle {{
            font-size: 18px;
            color: {TEXT_MUTED};
            margin-bottom: 8px;
        }}
        .brand-owner {{
            font-size: 14px;
            color: #D1D5DB;
        }}
        .section-card {{
            background: {CARD_BG};
            border: 1px solid {BORDER_COLOR};
            border-radius: 22px;
            padding: 22px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.18);
        }}
        .mini-card {{
            background: rgba(255,255,255,0.04);
            border: 1px solid {BORDER_COLOR};
            border-radius: 18px;
            padding: 16px;
            height: 100%;
        }}
        .mini-card h4 {{
            margin: 0 0 8px 0;
            font-size: 16px;
        }}
        .mini-card p {{
            margin: 0;
            color: {TEXT_MUTED};
            font-size: 14px;
        }}
        .result-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.035));
            border: 1px solid rgba(148,163,184,0.18);
            border-radius: 22px;
            padding: 22px;
            margin-top: 18px;
        }}
        .sidebar-brand {
            padding: 16px 14px;
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(51,65,85,0.24), rgba(255,255,255,0.03));
            border: 1px solid rgba(203,213,225,0.10);
            margin-bottom: 12px;
        }}
        .sidebar-brand h3 {{
            margin: 0;
            font-size: 20px;
        }}
        .sidebar-brand p {{
            margin: 6px 0 0 0;
            color: #D1D5DB;
            font-size: 13px;
        }}
        div[data-testid="stTextArea"] textarea {{
            border-radius: 18px !important;
            min-height: 160px;
        }}
        div[data-testid="stSelectbox"] > div {{
            border-radius: 16px !important;
        }}
        div[data-testid="stButton"] button {
            background: linear-gradient(135deg, #334155, #64748B);
            color: white;
            border: 0;
            border-radius: 14px;
            padding: 0.8rem 1.2rem;
            font-weight: 700;
            width: 100%;
        }}
        div[data-testid="stDownloadButton"] button {{
            border-radius: 14px;
            width: 100%;
        }}
        .footer-note {{
            text-align: center;
            font-size: 13px;
            color: {TEXT_MUTED};
            margin-top: 18px;
        }}
        .status-ok {{
            color: #86efac;
            font-size: 13px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


PROMPT_GUIDES = {
    "Custom Prompt": "Create the best professional prompt based on the user's short command.",
    "SEO Blog Prompt": "Generate a premium SEO blog prompt optimized for rankings, EEAT, semantic SEO, and conversions.",
    "Meta Prompt": "Generate a prompt for meta title, meta description, and focus keyword creation.",
    "Thumbnail Prompt": "Generate a high-CTR thumbnail design prompt with strong emotion, scene setup, and visual hierarchy.",
    "Product Description Prompt": "Generate a prompt for premium product descriptions focused on conversion and benefits.",
    "Social Media Prompt": "Generate a prompt for social media captions, hooks, CTA, and platform-friendly structure.",
    "Sales Prompt": "Generate a persuasive sales copy prompt focused on leads, objections, and conversion.",
    "Ad Copy Prompt": "Generate a paid ad copy prompt for compelling headlines, primary text, and CTA angles.",
    "Story Prompt": "Generate a professional story-writing prompt with character setup, emotional arc, hook, conflict, climax, and ending style.",
    "YouTube Script Prompt": "Generate a structured prompt for engaging YouTube scripts with hooks, retention beats, pacing, and CTA.",
    "Email Prompt": "Generate a professional email writing prompt with tone, context, CTA, and response goal.",
    "Landing Page Prompt": "Generate a prompt for a high-converting landing page with sections, copy angles, and CTA flow.",
    "Brand Voice Prompt": "Generate a prompt to define a unique brand voice, tone rules, audience language, and messaging style.",
    "Website Copy Prompt": "Generate a prompt for homepage or service page copy with positioning, trust, and conversion focus.",
    "Case Study Prompt": "Generate a prompt for persuasive case studies with challenge, process, results, and proof points.",
    "Proposal Prompt": "Generate a prompt for premium proposals with scope, deliverables, authority, and persuasive framing.",
    "Children Story Prompt": "Generate a child-friendly story prompt with clear moral, emotional progression, and simple engaging structure.",
}


STORY_MODE_RULES = """
For story prompts, always include:
- Story genre or theme
- Main character profile
- Emotional hook in the opening
- Conflict or challenge
- Pacing guidance
- Climax direction
- Ending type
- Tone and target audience
- Output format if useful
"""


def build_system_prompt(category: str, tone: str, length: str, audience: str, platform: str) -> str:
    extra_rule = STORY_MODE_RULES if category == "Story Prompt" else ""
    return f"""
You are an elite prompt engineer and premium AI workflow designer.

Your job is to convert a short user command into a professional, premium, agency-quality, ready-to-use AI prompt.

Prompt Category: {category}
Category Goal: {PROMPT_GUIDES.get(category, '')}
Tone: {tone}
Output Length: {length}
Target Audience: {audience}
Target Platform: {platform}

Core rules:
- Understand the user's real intent behind the short command
- Fill reasonable gaps intelligently without changing the main goal
- Make the final prompt polished, structured, practical, and copy-paste ready
- Use strong structure where useful, such as Role, Objective, Context, Inputs, Instructions, Constraints, Output Format
- Keep the writing premium, clear, specific, and non-robotic
- Avoid fluff, vagueness, and repetition
- Write in clean English
- Make the output look like it was prepared by a premium agency

{extra_rule}
"""


def extract_result(data: dict):
    if isinstance(data, dict):
        choices = data.get("choices")
        if isinstance(choices, list) and choices:
            first = choices[0] or {}
            message = first.get("message") or {}
            content = message.get("content")
            if content:
                return content

        error_data = data.get("error")
        if error_data:
            if isinstance(error_data, dict):
                return None, error_data.get("message", "Unknown API error")
            return None, str(error_data)

    return None, "API se valid response nahi aaya. Please model, API key, ya request format check karo."


def generate_prompt(command: str, category: str, tone: str, length: str, audience: str, platform: str):
    api_key = st.secrets.get("OPENROUTER_API_KEY")
    if not api_key:
        return None, "OPENROUTER_API_KEY missing hai. Settings > Secrets mein API key add karo."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://command2prompt.streamlit.app",
        "X-Title": BRAND_NAME,
    }

    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": build_system_prompt(category, tone, length, audience, platform)},
            {"role": "user", "content": command},
        ],
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )
        data = response.json()

        if response.status_code >= 400:
            _, err = extract_result(data)
            return None, f"API error: {err}"

        content = extract_result(data)
        if isinstance(content, tuple):
            return content
        return content, None

    except requests.exceptions.Timeout:
        return None, "Request timeout ho gaya. Thori der baad dubara try karo."
    except requests.exceptions.RequestException as e:
        return None, f"Network/API request error: {e}"
    except Exception as e:
        return None, f"Unexpected error: {e}"


if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""
if "last_error" not in st.session_state:
    st.session_state.last_error = ""


with st.sidebar:
    st.markdown(
        f"""
        <div class="sidebar-brand">
            <h3>{BRAND_NAME}</h3>
            <p>{BRAND_TAGLINE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Brand Panel")
    st.caption("Brand name, owner name, email, colors aur tagline ko code ke top section se change karo.")

    audience = st.selectbox(
        "Target Audience",
        [
            "General users",
            "SEO professionals",
            "Freelancers",
            "Agencies",
            "Business owners",
            "Ecommerce brands",
            "Writers and storytellers",
            "Custom audience",
        ],
    )

    platform = st.selectbox(
        "Target Platform",
        ["ChatGPT", "Claude", "Gemini", "Perplexity", "Generic AI"],
    )

    st.markdown("### Pro Notes")
    st.info(
        "Story Prompt category add ho chuki hai. App error-safe bhi kar di gayi hai taa ke invalid API response par app crash na ho."
    )

    if st.secrets.get("OPENROUTER_API_KEY"):
        st.markdown("<div class='status-ok'>● API key connected</div>", unsafe_allow_html=True)
    else:
        st.warning("API key connect nahi hui. Secrets mein OPENROUTER_API_KEY add karo.")


st.markdown(
    f"""
    <div class="brand-hero">
        <div class="brand-pill">✨ Premium Prompt Studio</div>
        <div class="brand-title">{BRAND_NAME}</div>
        <div class="brand-subtitle">{BRAND_TAGLINE}</div>
        <div class="brand-owner">{BRAND_OWNER} • {BRAND_EMAIL}</div>
    </div>
    """,
    unsafe_allow_html=True,
)


col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown(
        """
        <div class="mini-card">
            <h4>Premium UX</h4>
            <p>Modern cards, cleaner spacing, stronger visual hierarchy, and better usability.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_b:
    st.markdown(
        """
        <div class="mini-card">
            <h4>Error Safe</h4>
            <p>Better API handling, cleaner fallbacks, and safer response parsing.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_c:
    st.markdown(
        """
        <div class="mini-card">
            <h4>Story Mode Added</h4>
            <p>Generate story prompts with character arc, hook, conflict, climax, and ending flow.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div class='section-card'>", unsafe_allow_html=True)
left, right = st.columns([1.3, 0.7])

with left:
    command = st.text_area(
        "Enter your short command",
        placeholder="Example: Create a premium story prompt about a poor boy who becomes a hero after one life-changing event",
    )

with right:
    category = st.selectbox(
        "Prompt Category",
        list(PROMPT_GUIDES.keys()),
    )

    tone = st.selectbox(
        "Tone",
        ["Professional", "Premium", "Authoritative", "Humanized", "Creative", "Emotional", "Cinematic"],
    )

    length = st.selectbox(
        "Output Length",
        ["Short", "Medium", "Detailed"],
    )

cta1, cta2 = st.columns(2)
with cta1:
    generate_clicked = st.button("Generate Prompt")
with cta2:
    clear_clicked = st.button("Clear Output")

if clear_clicked:
    st.session_state.generated_prompt = ""
    st.session_state.last_error = ""

if generate_clicked:
    if not command.strip():
        st.warning("Please enter a short command first.")
    else:
        with st.spinner("Generating your premium prompt..."):
            result, err = generate_prompt(command, category, tone, length, audience, platform)
            if err:
                st.session_state.last_error = err
                st.session_state.generated_prompt = ""
            else:
                st.session_state.generated_prompt = result or ""
                st.session_state.last_error = ""

st.markdown("</div>", unsafe_allow_html=True)


if st.session_state.last_error:
    st.error(st.session_state.last_error)


if st.session_state.generated_prompt:
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.subheader("Your Generated Prompt")
    st.code(st.session_state.generated_prompt, language="markdown")

    dl1, dl2 = st.columns(2)
    with dl1:
        st.download_button(
            "Download Prompt (.txt)",
            data=st.session_state.generated_prompt,
            file_name=f"prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
        )
    with dl2:
        st.text_area("Copy Prompt", value=st.session_state.generated_prompt, height=180)

    st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="footer-note">
        {BRAND_NAME} • {BRAND_OWNER} • {BRAND_EMAIL} • Premium AI Prompt Studio
    </div>
    """,
    unsafe_allow_html=True,
)
