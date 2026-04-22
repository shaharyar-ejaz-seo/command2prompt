import streamlit as st
import requests

st.set_page_config(
    page_title="Shaharyar Ejaz Prompt Studio",
    page_icon="✨",
    layout="wide",
)

BRAND_NAME = "Shaharyar Ejaz Prompt Studio"
BRAND_TAGLINE = "Premium AI Prompt Systems for SEO, AI Search, Content, Stories, and Conversions"
BRAND_OWNER = "Shaharyar Ejaz"
LINKEDIN_URL = "https://www.linkedin.com/in/shaharyar-ejaz-seo/"
APP_URL = https://shaharyarpropmtseo.streamlit.app/

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0B1220 0%, #111827 45%, #172033 100%);
            color: white;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .hero-box {
            padding: 30px;
            border-radius: 22px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 10px 30px rgba(0,0,0,0.20);
            margin-bottom: 18px;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.10);
            color: #E2E8F0;
            font-size: 13px;
            margin-bottom: 14px;
        }

        .hero-title {
            font-size: 46px;
            font-weight: 800;
            line-height: 1.05;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }

        .hero-subtitle {
            color: #CBD5E1;
            font-size: 17px;
            margin-bottom: 8px;
        }

        .hero-meta {
            color: #94A3B8;
            font-size: 14px;
        }

        .mini-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            padding: 18px;
            border-radius: 18px;
            height: 100%;
            margin-bottom: 12px;
        }

        .mini-card h4 {
            margin: 0 0 8px 0;
            font-size: 16px;
        }

        .mini-card p {
            margin: 0;
            color: #CBD5E1;
            font-size: 14px;
        }

        .main-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
            padding: 22px;
            border-radius: 20px;
            margin-top: 12px;
        }

        .result-card {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.10);
            padding: 22px;
            border-radius: 20px;
            margin-top: 20px;
        }

        div[data-testid="stTextArea"] textarea {
            border-radius: 16px !important;
            min-height: 150px;
        }

        div[data-testid="stSelectbox"] > div {
            border-radius: 14px !important;
        }

        div[data-testid="stButton"] button {
            width: 100%;
            border-radius: 14px !important;
            font-weight: 700 !important;
        }

        div[data-testid="stDownloadButton"] button {
            width: 100%;
            border-radius: 14px !important;
            font-weight: 700 !important;
        }

        .footer {
            text-align: center;
            color: #94A3B8;
            margin-top: 24px;
            font-size: 14px;
        }

        .status-ok {
            color: #86efac;
            font-size: 13px;
            margin-top: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

PROMPT_CATEGORIES = [
    "Custom Prompt",
    "SEO Blog Prompt",
    "Meta Title / Description Prompt",
    "Website Copy Prompt",
    "Story Prompt",
    "Children Story Prompt",
    "YouTube Script Prompt",
    "Thumbnail Prompt",
    "Ad Copy Prompt",
    "Product Description Prompt",
    "Social Media Prompt",
    "Email Prompt",
    "Brand Voice Prompt",
]

def build_system_prompt(category: str, tone: str, length: str) -> str:
    return f"""
You are the core AI engine behind Shaharyar Ejaz Prompt Studio.

Brand Owner: Shaharyar Ejaz
Brand Positioning: Premium AI Prompt Systems for Brands, Agencies, Creators, and Storytellers
LinkedIn: {LINKEDIN_URL}

Your mission is to convert short user commands into premium, professional, high-performance prompts that are:
- AI-friendly
- SEO-aware
- EEAT-focused
- conversion-oriented
- human-sounding
- cleanly structured
- ready to copy and use instantly

The generated prompt must feel like it was written by a top-tier agency prompt strategist, not by a generic AI tool.

PROMPT CATEGORY:
{category}

TONE:
{tone}

OUTPUT LENGTH:
{length}

CORE REQUIREMENTS:
- Upgrade weak or short user input into a premium prompt
- Preserve the original user intent
- Fill reasonable gaps intelligently
- Never sound robotic
- Never produce generic fluff
- Make the output copy-paste ready
- Use polished, premium, agency-level language
- Keep the prompt strategic and practical
- Prefer clarity over hype
- When relevant, optimize for both Google SEO and AI search engines
- When relevant, make it conversion-friendly

OUTPUT STRUCTURE SHOULD INCLUDE WHEN RELEVANT:
1. ROLE
2. MISSION
3. CONTEXT
4. OBJECTIVE
5. TARGET AUDIENCE
6. TONE / STYLE
7. STRUCTURE
8. SEO LAYER
9. EEAT LAYER
10. AI SEARCH OPTIMIZATION
11. CONVERSION LAYER
12. CONSTRAINTS
13. FINAL OUTPUT FORMAT

CATEGORY-SPECIFIC HANDLING:
- SEO Blog Prompt: include primary keyword, secondary keywords, semantic terms, search intent, internal link ideas, featured snippet angle, EEAT signals, CTA
- Meta Title / Description Prompt: include CTR optimization, pixel awareness, intent alignment, keyword placement, trust angle
- Website Copy Prompt: include positioning, trust, pain points, benefit hierarchy, CTA flow, premium tone
- Story Prompt: include genre/theme, main character, emotional hook, conflict, pacing, climax, ending style, audience, tone
- Children Story Prompt: include simple language, warm emotional tone, lesson/moral, engaging hook, memorable ending
- YouTube Script Prompt: include opening hook, retention strategy, pacing, audience engagement, CTA
- Thumbnail Prompt: include visual scene, emotion, framing, contrast, click-driving angle
- Ad Copy Prompt: include pain points, value proposition, hook, objection handling, CTA, testing angles
- Product Description Prompt: include features, benefits, emotional value, buyer angle, persuasive but clean copy
- Social Media Prompt: include hook, body, engagement line, CTA, platform-fit style
- Email Prompt: include purpose, tone, structure, CTA, clarity, response objective
- Brand Voice Prompt: include brand personality, tone rules, language style, do/don't list, sample phrasing
- Custom Prompt: infer the best professional structure based on user command

QUALITY STANDARD:
Every final prompt must feel:
- premium
- strategic
- useful
- brandable
- expert-led
- client-ready

At the end of the generated prompt, add this line when appropriate:
Prepared by Shaharyar Ejaz Prompt Studio | LinkedIn: {LINKEDIN_URL}
"""

def generate_prompt(command: str, category: str, tone: str, length: str):
    api_key = st.secrets.get("OPENROUTER_API_KEY")

    if not api_key:
        return None, "OPENROUTER_API_KEY missing hai. Settings > Secrets mein real key add karo."

    system_prompt = build_system_prompt(category, tone, length)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": APP_URL,
        "X-Title": BRAND_NAME,
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
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

        if response.status_code != 200:
            return None, f"API Error: {data}"

        if "choices" in data and len(data["choices"]) > 0:
            message = data["choices"][0].get("message", {})
            content = message.get("content")
            if content:
                return content, None

        return None, f"Unexpected API response: {data}"

    except requests.exceptions.Timeout:
        return None, "Request timeout ho gaya. Thori der baad dubara try karo."
    except requests.exceptions.RequestException as e:
        return None, f"Network/API request error: {e}"
    except Exception as e:
        return None, f"Unexpected error: {e}"

if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

with st.sidebar:
    st.markdown("## Prompt Studio")
    st.caption("Professional AI prompt engine with SEO, EEAT, AI search, and story support.")

    if st.secrets.get("OPENROUTER_API_KEY"):
        st.markdown('<div class="status-ok">● API key connected</div>', unsafe_allow_html=True)
    else:
        st.warning("API key connect nahi hui. Secrets mein OPENROUTER_API_KEY add karo.")

    st.markdown("---")
    st.markdown("### Brand")
    st.write("**Shaharyar Ejaz**")
    st.markdown(f"[LinkedIn Profile]({LINKEDIN_URL})")

st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-badge">Premium AI Prompt Studio</div>
        <div class="hero-title">{BRAND_NAME}</div>
        <div class="hero-subtitle">{BRAND_TAGLINE}</div>
        <div class="hero-meta">Built by {BRAND_OWNER} • <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a></div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="mini-card">
            <h4>AI-Friendly</h4>
            <p>Prompt outputs are structured for ChatGPT, Gemini, Claude, and answer engines.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="mini-card">
            <h4>SEO + EEAT</h4>
            <p>Built to generate prompts with authority, trust, semantic depth, and search intent.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="mini-card">
            <h4>Stories + Marketing</h4>
            <p>Create prompts for stories, thumbnails, blogs, ads, product copy, and more.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="main-card">', unsafe_allow_html=True)

left_col, right_col = st.columns([1.35, 0.65])

with left_col:
    command = st.text_area(
        "Enter your short command",
        placeholder="Example: Create a premium SEO blog prompt for a Florida permit services website targeting property owners and investors.",
    )

with right_col:
    category = st.selectbox("Prompt Category", PROMPT_CATEGORIES)
    tone = st.selectbox(
        "Tone",
        ["Professional", "Premium", "Authoritative", "Creative", "Emotional", "Humanized", "Cinematic"],
    )
    length = st.selectbox("Output Length", ["Short", "Medium", "Detailed"])

b1, b2 = st.columns(2)
with b1:
    generate_clicked = st.button("Generate Prompt")
with b2:
    clear_clicked = st.button("Clear Output")

if clear_clicked:
    st.session_state.generated_prompt = ""

if generate_clicked:
    if not command.strip():
        st.warning("Please enter a short command first.")
    else:
        with st.spinner("Generating your premium prompt..."):
            result, error = generate_prompt(command, category, tone, length)
            if error:
                st.error(error)
            else:
                st.session_state.generated_prompt = result

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.generated_prompt:
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("Generated Prompt")
    st.code(st.session_state.generated_prompt, language="markdown")

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            "Download Prompt (.txt)",
            data=st.session_state.generated_prompt,
            file_name="generated_prompt.txt",
            mime="text/plain",
        )
    with d2:
        st.text_area("Copy Prompt", value=st.session_state.generated_prompt, height=180)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="footer">
        Built by {BRAND_OWNER} • <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)
