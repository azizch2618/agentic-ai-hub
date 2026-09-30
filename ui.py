import html
import re
from urllib.parse import parse_qs, urlparse

import streamlit as st
import streamlit.components.v1 as components

from youtube_analyzer import build_youtube_agent
from finance import build_finance_agent



# PAGE CONFIGURATION

st.set_page_config(
    page_title="🤖 Agentic AI Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# CUSTOM CSS

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1120px;
            padding-top: 0.9rem;
            padding-bottom: 2.5rem;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid rgba(128, 128, 128, 0.16);
        }

        [data-testid="stSidebar"] .stButton > button {
            text-align: left;
            border-radius: 9px;
        }

        /* ---------- Page header ---------- */

        .page-title {
            text-align: center;
            font-size: 2.55rem;
            font-weight: 750;
            line-height: 1.12;
            margin: 0.35rem 0 0 0;
            padding-top: 0.18rem;
        }

        /* ---------- Home page title ---------- */

        .home-title {
            text-align: center;
            font-size: 2.7rem;
            font-weight: 800;
            line-height: 1.15;
            margin: 1.15rem 0 0.25rem 0;
            padding: 0.15rem 0.5rem 0 0.5rem;
            letter-spacing: -0.02em;
        }

        .home-subtitle {
            text-align: center;
            font-size: 1rem;
            line-height: 1.5;
            opacity: 0.68;
            margin: 0 0 1.35rem 0;
        }

        .page-subtitle {
            text-align: center;
            font-size: 1rem;
            line-height: 1.5;
            opacity: 0.68;
            margin: 0.3rem 0 0.55rem 0;
        }

        .status-line {
            text-align: center;
            font-size: 0.83rem;
            opacity: 0.72;
            margin: 0.2rem 0 1.15rem 0;
        }

        .status-dot {
            color: #22c55e;
            font-size: 0.92rem;
        }

        /* ---------- Navigation ---------- */

        .header-back-space {
            padding-top: 0.22rem;
        }

        .header-back-space + div {
            margin-top: 0;
        }

        /* ---------- Section headings ---------- */

        .section-heading {
            font-size: 1.55rem;
            font-weight: 700;
            margin: 0.2rem 0 0.7rem 0;
        }

        .report-heading {
            font-size: 1.55rem;
            font-weight: 700;
            margin: 0;
        }

        .report-meta {
            font-size: 0.8rem;
            opacity: 0.55;
            margin: -0.25rem 0 0.7rem 0;
        }

        .helper-text {
            font-size: 0.84rem;
            opacity: 0.62;
            margin-top: -0.35rem;
            margin-bottom: 0.7rem;
        }

        /* ---------- Home cards ---------- */

        .agent-card-icon {
            font-size: 2.1rem;
            margin-bottom: 0.2rem;
        }

        .agent-card-title {
            font-size: 1.35rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }

        .agent-card-description {
            min-height: 96px;
            font-size: 0.96rem;
            line-height: 1.65;
            opacity: 0.72;
        }

        /* ---------- Empty state ---------- */

        .empty-state {
            text-align: center;
            padding: 2.35rem 1rem 2.45rem 1rem;
        }

        .empty-state-icon {
            font-size: 2.2rem;
            margin-bottom: 0.3rem;
        }

        .empty-state-title {
            font-size: 1.12rem;
            font-weight: 650;
            margin-bottom: 0.35rem;
        }

        .empty-state-text {
            max-width: 620px;
            margin: 0 auto;
            font-size: 0.91rem;
            line-height: 1.6;
            opacity: 0.62;
        }

        /* ---------- Report surface ---------- */

        .report-surface-note {
            font-size: 0.78rem;
            opacity: 0.5;
            margin-bottom: 0.35rem;
        }

        /* ---------- AI activity ---------- */

        .ai-active {
            border-radius: 10px;
            padding: 0.55rem 0.8rem;
            text-align: center;
            font-size: 0.84rem;
            margin: 0.65rem 0;
            border: 1px solid rgba(255, 75, 75, 0.25);
            box-shadow: 0 0 18px rgba(255, 75, 75, 0.08);
        }

        /* ---------- Footer ---------- */

        .footer {
            text-align: center;
            opacity: 0.45;
            margin-top: 3rem;
            padding-top: 0.9rem;
            border-top: 1px solid rgba(128, 128, 128, 0.18);
            font-size: 0.82rem;
        }

        /* ---------- Responsive ---------- */

        @media (max-width: 768px) {
            .block-container {
                padding-top: 0.65rem;
                padding-left: 0.85rem;
                padding-right: 0.85rem;
            }

            .page-title {
                font-size: 2rem;
            }

            .home-title {
                font-size: 2.05rem;
                margin-top: 0.9rem;
            }

            .home-subtitle {
                font-size: 0.94rem;
                margin-bottom: 1rem;
            }

            .page-subtitle {
                font-size: 0.94rem;
            }

            .agent-card-description {
                min-height: auto;
            }

            .report-heading,
            .section-heading {
                font-size: 1.32rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)



# SESSION STATE

DEFAULTS = {
    "page": "home",
    "youtube_url": "",
    "youtube_report": None,
    "finance_query": "",
    "finance_report": None,
    "finance_selected_preset": None,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# AGENT CACHE

@st.cache_resource
def get_youtube_agent():
    return build_youtube_agent()


@st.cache_resource
def get_finance_agent():
    return build_finance_agent()


# NAVIGATION

def go_home():
    st.session_state.page = "home"


def go_youtube():
    st.session_state.page = "youtube"


def go_finance():
    st.session_state.page = "finance"


def render_page_header(title: str, subtitle: str, status: str, back_key: str):
    """
    Back button and title live in the same header row.
    A small top buffer prevents the title glyphs from being clipped
    against Streamlit's top content boundary.
    """
    st.markdown(
        '<div style="height:0.45rem;"></div>',
        unsafe_allow_html=True,
    )

    back_col, title_col, spacer_col = st.columns([1.35, 7.1, 1.35])

    with back_col:
        st.markdown('<div class="header-back-space">', unsafe_allow_html=True)

        if st.button("← Agent Hub", key=back_key):
            go_home()
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with title_col:
        st.markdown(
            f'<div class="page-title">{title}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="page-subtitle">{subtitle}</div>',
            unsafe_allow_html=True,
        )

    with spacer_col:
        st.write("")

    st.markdown(
        f'<div class="status-line">'
        f'<span class="status-dot">●</span> {status}'
        f'</div>',
        unsafe_allow_html=True,
    )


# COPY BUTTON


def render_copy_button(text: str, key: str, label: str = "📋 Copy Report"):
    """
    Small self-contained clipboard button.

    Uses a browser-side clipboard operation so the rendered Markdown
    report remains visually clean instead of being replaced by a code block.
    """
    safe_text = html.escape(text, quote=True)

    components.html(
        f"""
        <style>
            body {{
                margin: 0;
                background: transparent;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }}

            button {{
                width: 100%;
                min-height: 38px;
                border: 1px solid rgba(128,128,128,0.35);
                border-radius: 8px;
                background: #161922;
                color: #f2f2f2;
                cursor: pointer;
                font-size: 14px;
                transition: 0.15s ease;
            }}

            button:hover {{
                border-color: rgba(255,75,75,0.65);
                box-shadow: 0 0 12px rgba(255,75,75,0.12);
            }}
        </style>

        <textarea id="copy-source" style="position:absolute; left:-9999px;">
{safe_text}
        </textarea>

        <button id="copy-btn" type="button">{html.escape(label)}</button>

        <script>
            const button = document.getElementById("copy-btn");
            const source = document.getElementById("copy-source");

            button.addEventListener("click", async () => {{
                const text = source.value;

                try {{
                    await navigator.clipboard.writeText(text);
                }} catch (err) {{
                    source.focus();
                    source.select();
                    document.execCommand("copy");
                }}

                const original = button.innerText;
                button.innerText = "✓ Copied";
                setTimeout(() => {{
                    button.innerText = original;
                }}, 1400);
            }});
        </script>
        """,
        height=46,
        scrolling=False,
    )


# ============================================================
# YOUTUBE URL VALIDATION
# ============================================================

YOUTUBE_ID_PATTERN = r"[A-Za-z0-9_-]{11}"


def _valid_video_id(video_id: str | None) -> bool:
    return bool(video_id and re.fullmatch(YOUTUBE_ID_PATTERN, video_id))


def is_valid_youtube_url(url: str) -> bool:
    """
    Validate common YouTube URL formats.
    """
    if not isinstance(url, str) or not url.strip():
        return False

    try:
        parsed = urlparse(url.strip())

        if parsed.scheme not in {"http", "https"}:
            return False

        hostname = parsed.netloc.lower().split(":")[0]

        valid_hosts = {
            "youtube.com",
            "www.youtube.com",
            "m.youtube.com",
            "youtu.be",
            "www.youtu.be",
        }

        if hostname not in valid_hosts:
            return False

        if hostname in {"youtu.be", "www.youtu.be"}:
            video_id = parsed.path.strip("/").split("/")[0]
            return _valid_video_id(video_id)

        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [None])[0]
            return _valid_video_id(video_id)

        for prefix in ("/shorts/", "/embed/", "/live/"):
            if parsed.path.startswith(prefix):
                video_id = parsed.path[len(prefix):].split("/")[0]
                return _valid_video_id(video_id)

        return False

    except (ValueError, TypeError):
        return False


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 🤖 Agentic AI Hub")
    st.caption("Intelligent agents · Specialized tools · One workspace")

    st.markdown("---")
    st.markdown("### Navigation")

    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        go_home()
        st.rerun()

    if st.button("🎥 YouTube Agent", use_container_width=True, key="nav_youtube"):
        go_youtube()
        st.rerun()

    if st.button("📈 Finance Agent", use_container_width=True, key="nav_finance"):
        go_finance()
        st.rerun()

    st.markdown("---")
    st.caption("Built with Python, Agno, Groq and Streamlit.")


# ============================================================
# HOME PAGE
# ============================================================

def render_home():
    st.markdown(
        '<div class="home-title">🤖 AGENTIC AI HUB</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="home-subtitle">'
        "Intelligent agents. Specialized tools. One workspace."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-heading">Select an AI Agent</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown(
                '<div class="agent-card-icon">🎥</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="agent-card-title">YouTube Video Analyzer</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="agent-card-description">'
                "Analyze YouTube videos using AI. Extract video information, "
                "key topics, important sections, learning points and useful takeaways."
                "</div>",
                unsafe_allow_html=True,
            )

            st.write("")

            if st.button(
                "🎬 Open YouTube Agent",
                use_container_width=True,
                type="primary",
                key="home_youtube",
            ):
                go_youtube()
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown(
                '<div class="agent-card-icon">📈</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="agent-card-title">Finance Research Agent</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="agent-card-description">'
                "Research stocks, company fundamentals, market information, "
                "analyst data and relevant financial news using specialized tools."
                "</div>",
                unsafe_allow_html=True,
            )

            st.write("")

            if st.button(
                "📊 Open Finance Agent",
                use_container_width=True,
                type="primary",
                key="home_finance",
            ):
                go_finance()
                st.rerun()

    st.markdown(
        '<div style="text-align:center; opacity:0.58; margin-top:1.8rem;">'
        "More specialized agents can be added to this workspace in the future."
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# EMPTY STATE
# ============================================================

def render_empty_state(icon: str, title: str, description: str):
    with st.container(border=True):
        st.markdown(
            f"""
            <div class="empty-state">
                <div class="empty-state-icon">{icon}</div>
                <div class="empty-state-title">{title}</div>
                <div class="empty-state-text">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# YOUTUBE PAGE
# ============================================================

def render_youtube():
    render_page_header(
        "🎥 YouTube Video Analyzer",
        "Analyze a YouTube video and generate a structured AI report.",
        "Agent Ready · YouTubeTools enabled",
        "youtube_back",
    )

    youtube_agent = get_youtube_agent()

    st.markdown("##### YouTube Video URL")

    video_url = st.text_input(
        "YouTube Video URL",
        value=st.session_state.youtube_url,
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed",
        key="youtube_url_input",
    )

    st.session_state.youtube_url = video_url

    if st.button(
        "🎬 Analyze Video",
        use_container_width=True,
        type="primary",
        key="analyze_youtube",
    ):
        if not video_url.strip():
            st.warning("Please enter a YouTube video URL before analyzing.")

        elif not is_valid_youtube_url(video_url):
            st.error("Please enter a valid YouTube URL.")
            st.caption(
                "Supported: youtube.com/watch, youtu.be, YouTube Shorts, "
                "YouTube Embed and YouTube Live URLs."
            )

        else:
            st.markdown(
                '<div class="ai-active">✨ AI agent is working · retrieving and analyzing video data</div>',
                unsafe_allow_html=True,
            )

            with st.spinner("🎥 Analyzing the YouTube video..."):
                try:
                    response = youtube_agent.run(
                        f"Analyze this video: {video_url.strip()}"
                    )

                    st.session_state.youtube_report = response.content
                    st.rerun()

                except Exception as error:
                    st.session_state.youtube_report = None
                    st.error("Unable to analyze this video.")
                    st.exception(error)

    st.write("")
    st.markdown("---")

    header_col, copy_col, clear_col = st.columns([5.7, 1.35, 1.05])

    with header_col:
        st.markdown(
            '<div class="report-heading">📋 Analysis Report</div>',
            unsafe_allow_html=True,
        )

    if st.session_state.youtube_report:
        with copy_col:
            render_copy_button(
                st.session_state.youtube_report,
                "youtube_copy",
            )

        with clear_col:
            if st.button(
                "Clear",
                key="youtube_clear",
                use_container_width=True,
            ):
                st.session_state.youtube_report = None
                st.rerun()

        with st.container(border=True):
            st.markdown(
                '<div class="report-meta">'
                "AI-generated analysis from the selected YouTube video"
                "</div>",
                unsafe_allow_html=True,
            )
            st.markdown(st.session_state.youtube_report)

    else:
        render_empty_state(
            "🎬",
            "Ready for analysis",
            "Paste a YouTube video URL above and click Analyze Video to generate your AI report.",
        )


# ============================================================
# FINANCE PAGE
# ============================================================

FINANCE_PRESETS = {
    "📊 Stock Overview": (
        "Provide a current overview of NVDA including stock price, "
        "market data, 52-week range and relevant company information."
    ),
    "🏢 Company Fundamentals": (
        "Analyze NVDA company fundamentals including revenue, earnings, "
        "EPS, margins, valuation metrics, cash position and other relevant "
        "financial information."
    ),
    "📈 Technical Indicators": (
        "Analyze NVDA using available technical indicators including "
        "moving averages, 52-week range and other relevant technical "
        "market data. Explain the findings objectively without providing "
        "an investment recommendation."
    ),
    "📰 Recent Financial News": (
        "Find and summarize recent relevant financial news about NVDA. "
        "Clearly distinguish reported facts, analyst opinions, forecasts "
        "and speculative claims."
    ),
}


def render_finance():
    render_page_header(
        "📈 Finance Research Agent",
        "Research stocks, companies, financial data and relevant news.",
        "Agent Ready · YFinanceTools + DuckDuckGoTools enabled",
        "finance_back",
    )

    finance_agent = get_finance_agent()

    st.markdown("##### Research Query")

    finance_query = st.text_area(
        "What would you like to research?",
        value=st.session_state.finance_query,
        placeholder=(
            "Example: Analyze NVDA market data, fundamentals, "
            "technical indicators and recent financial news."
        ),
        height=105,
        label_visibility="collapsed",
        key="finance_query_input",
    )

    st.session_state.finance_query = finance_query

    st.markdown("##### ⚡ Quick Research")
    st.markdown(
        '<div class="helper-text">'
        "Choose a preset to quickly start a common research task."
        "</div>",
        unsafe_allow_html=True,
    )

    preset_columns = st.columns(4, gap="small")

    for column, label in zip(preset_columns, FINANCE_PRESETS):
        with column:
            is_selected = st.session_state.finance_selected_preset == label

            button_text = f"✓ {label}" if is_selected else label

            if st.button(
                button_text,
                use_container_width=True,
                type="primary" if is_selected else "secondary",
                key=f"preset_{label}",
            ):
                st.session_state.finance_selected_preset = label
                st.session_state.finance_query = FINANCE_PRESETS[label]
                st.rerun()

    st.write("")

    if st.button(
        "🔎 Research",
        use_container_width=True,
        type="primary",
        key="research_finance",
    ):
        if not finance_query.strip():
            st.warning(
                "Enter a research question or choose one of the quick research options."
            )

        else:
            st.markdown(
                '<div class="ai-active">✨ AI agent is working · researching market data and sources</div>',
                unsafe_allow_html=True,
            )

            with st.spinner("🔎 Researching financial information..."):
                try:
                    response = finance_agent.run(finance_query.strip())
                    st.session_state.finance_report = response.content
                    st.rerun()

                except Exception as error:
                    st.session_state.finance_report = None
                    st.error("Unable to complete the financial research.")
                    st.exception(error)

    st.write("")
    st.markdown("---")

    header_col, copy_col, clear_col = st.columns([5.7, 1.35, 1.05])

    with header_col:
        st.markdown(
            '<div class="report-heading">📋 Research Report</div>',
            unsafe_allow_html=True,
        )

    if st.session_state.finance_report:
        with copy_col:
            render_copy_button(
                st.session_state.finance_report,
                "finance_copy",
            )

        with clear_col:
            if st.button(
                "Clear",
                key="finance_clear",
                use_container_width=True,
            ):
                st.session_state.finance_report = None
                st.rerun()

        with st.container(border=True):
            st.markdown(
                '<div class="report-meta">'
                "AI-generated financial research · Verify current market data before decisions"
                "</div>",
                unsafe_allow_html=True,
            )
            st.markdown(st.session_state.finance_report)

    else:
        render_empty_state(
            "📊",
            "Ready for research",
            "Enter a financial question or choose a quick research preset above, then click Research.",
        )

    st.caption(
        "⚠️ This application provides financial information and research for "
        "informational purposes only. It is not personalized financial advice."
    )


# ============================================================
# PAGE ROUTER
# ============================================================

if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "youtube":
    render_youtube()
elif st.session_state.page == "finance":
    render_finance()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    "🤖 Agentic AI Hub · Built with Python · Agno · Groq · Streamlit"
    "</div>",
    unsafe_allow_html=True,
)
