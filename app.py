import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ResearchMind",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Cabinet+Grotesk:wght@400;500;700;800&display=swap');

:root {
    --bg:       #09090b;
    --surface:  #111114;
    --card:     #18181b;
    --border:   #27272a;
    --border-hi:#3f3f46;
    --accent:   #a78bfa;
    --accent2:  #34d399;
    --accent3:  #fb923c;
    --red:      #f87171;
    --text:     #fafafa;
    --muted:    #71717a;
    --mono:     'DM Mono', monospace;
    --sans:     'Cabinet Grotesk', sans-serif;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: var(--sans) !important;
}
[data-testid="stHeader"], #MainMenu, footer,
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-thumb { background: var(--border-hi); border-radius: 2px; }

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

.stSelectbox label, .stSlider label,
.stToggle label, [data-testid="stWidgetLabel"] p {
    font-family: var(--mono) !important;
    font-size: 10px !important;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--muted) !important;
}
[data-testid="stSelectbox"] > div > div {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: var(--mono) !important;
    font-size: 13px !important;
}

.main .block-container {
    padding: 2rem 2.5rem 6rem !important;
    max-width: 860px !important;
}

.stTextInput > div > div > input {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--text) !important;
    font-family: var(--sans) !important;
    font-size: 15px !important;
    padding: 0 !important;
}
.stTextInput > div { border: none !important; background: transparent !important; }

.stButton > button {
    background: var(--accent) !important;
    color: #09090b !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: var(--sans) !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    padding: 8px 22px !important;
    letter-spacing: .02em;
    transition: opacity .15s !important;
    white-space: nowrap;
}
.stButton > button:hover    { opacity: .8 !important; }
.stButton > button:disabled { opacity: .4 !important; }

.step-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 14px;
    position: relative;
    overflow: hidden;
}
.step-card.active  { border-color: var(--accent); }
.step-card.done    { border-color: var(--accent2); }
.step-card.pending { opacity: .4; }

.step-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:2px;
}
.step-card.active::before  { background: var(--accent); animation: pulse 1.4s infinite; }
.step-card.done::before    { background: var(--accent2); }
.step-card.pending::before { background: var(--border); }

@keyframes pulse   { 0%,100%{opacity:1} 50%{opacity:.3} }
@keyframes fadeUp  { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:none} }

.step-header { display:flex; align-items:center; gap:10px; margin-bottom:10px; }
.step-icon {
    width:32px; height:32px; border-radius:8px;
    display:flex; align-items:center; justify-content:center;
    font-size:15px; background:var(--surface);
    border:1px solid var(--border); flex-shrink:0;
}
.step-title { font-family:var(--sans); font-weight:700; font-size:14px; color:var(--text); flex:1; }
.step-badge {
    font-family:var(--mono); font-size:10px;
    padding:3px 9px; border-radius:20px;
    text-transform:uppercase; letter-spacing:.06em;
}
.badge-active  { background:rgba(167,139,250,.15); color:var(--accent);  border:1px solid rgba(167,139,250,.3); }
.badge-done    { background:rgba(52,211,153,.12);  color:var(--accent2); border:1px solid rgba(52,211,153,.25); }
.badge-pending { background:rgba(113,113,122,.1);  color:var(--muted);   border:1px solid var(--border); }

.step-output {
    font-family:var(--mono); font-size:11.5px; color:#a1a1aa;
    line-height:1.7; white-space:pre-wrap; word-break:break-word;
    background:var(--surface); border:1px solid var(--border);
    border-radius:8px; padding:12px 14px;
    max-height:200px; overflow-y:auto;
}

.report-card {
    background:var(--card); border:1px solid var(--accent2);
    border-radius:14px; padding:24px 26px; margin-top:12px;
    animation: fadeUp .5s ease both;
}
.report-header {
    display:flex; align-items:center; gap:10px;
    margin-bottom:16px; padding-bottom:14px;
    border-bottom:1px solid var(--border);
}
.report-title { font-family:var(--sans); font-weight:800; font-size:16px; color:var(--text); }
.report-label {
    font-family:var(--mono); font-size:10px; text-transform:uppercase;
    letter-spacing:.1em; color:var(--accent2);
    background:rgba(52,211,153,.1); border:1px solid rgba(52,211,153,.2);
    padding:2px 8px; border-radius:20px;
}
.report-body {
    font-size:14px; line-height:1.75; color:#d4d4d8;
    font-family:var(--sans); white-space:pre-wrap; word-break:break-word;
}

.critic-card {
    background:rgba(251,146,60,.05); border:1px solid rgba(251,146,60,.25);
    border-radius:12px; padding:16px 18px; margin-top:14px;
    animation: fadeUp .4s ease both;
}
.critic-label {
    font-family:var(--mono); font-size:10px; text-transform:uppercase;
    letter-spacing:.1em; color:var(--accent3); margin-bottom:10px;
}
.critic-body { font-size:13px; color:#d4d4d8; line-height:1.7; font-family:var(--sans); white-space:pre-wrap; }

.log-entry {
    display:flex; gap:8px; padding:6px 8px;
    border-radius:6px; background:var(--card);
    border:1px solid var(--border); margin-bottom:5px;
    font-family:var(--mono); font-size:11px; animation:fadeUp .2s ease both;
}
.log-dot  { width:6px; height:6px; border-radius:50%; flex-shrink:0; margin-top:3px; }
.log-time { color:var(--muted); flex-shrink:0; }
.log-msg  { color:#a1a1aa; flex:1; word-break:break-word; }

.page-title {
    font-family:var(--sans); font-weight:800; font-size:28px;
    letter-spacing:-.03em; margin-bottom:4px;
    background:linear-gradient(135deg,#fff 30%,var(--accent));
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.page-sub {
    font-family:var(--mono); font-size:11px; color:var(--muted);
    letter-spacing:.05em; text-transform:uppercase; margin-bottom:28px;
}
hr { border-color: var(--border) !important; margin: 20px 0 !important; }
</style>
""", unsafe_allow_html=True)


# ── Session state ─────────────────────────────────────────────────────────────
for k, v in {"history": [], "log": [], "running": False, "selected_run": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v


def add_log(msg, kind="info"):
    st.session_state.log.append({
        "msg": msg, "kind": kind,
        "ts": datetime.now().strftime("%H:%M:%S")
    })


def card(icon, name, badge_class, badge_txt, output="", extra=""):
    state_class = "active" if badge_class == "badge-active" else ("done" if badge_class == "badge-done" else "pending")
    snippet = str(output)[:600] + ("…" if len(str(output)) > 600 else "")
    output_html = f'<div class="step-output">{snippet}</div>' if output else ""
    return f"""
    <div class="step-card {state_class}">
        <div class="step-header">
            <div class="step-icon">{icon}</div>
            <div class="step-title">{name}</div>
            <div class="step-badge {badge_class}">{badge_txt}</div>
        </div>
        {output_html}
        {extra}
    </div>"""


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:20px 16px 16px;border-bottom:1px solid #27272a;margin-bottom:16px;">
        <div style="font-family:'Cabinet Grotesk',sans-serif;font-size:20px;font-weight:800;
                    background:linear-gradient(135deg,#fff 30%,#a78bfa);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            🧠 ResearchMind
        </div>
        <div style="font-family:'DM Mono',monospace;font-size:10px;color:#71717a;margin-top:4px;
                    text-transform:uppercase;letter-spacing:.1em;">
            LangChain + Groq · 4-Agent Pipeline
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-family:\'DM Mono\',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#52525b;margin-bottom:8px;padding:0 4px;">Pipeline Steps</div>', unsafe_allow_html=True)
    for label in ["🔍 Search Agent", "📄 Reader Agent", "✍️ Writer Chain", "🧐 Critic Chain"]:
        st.markdown(f'<div style="font-family:\'DM Mono\',monospace;font-size:12px;color:#a1a1aa;padding:6px 10px;background:#18181b;border:1px solid #27272a;border-radius:6px;margin-bottom:4px;">{label}</div>', unsafe_allow_html=True)

    if st.session_state.history:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div style="font-family:\'DM Mono\',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#52525b;margin-bottom:8px;padding:0 4px;">Past Runs</div>', unsafe_allow_html=True)
        for i, run in enumerate(reversed(st.session_state.history[-6:])):
            lbl = run["topic"][:26] + "…" if len(run["topic"]) > 26 else run["topic"]
            if st.button(f"📋 {lbl}", key=f"hist_{i}", use_container_width=True):
                st.session_state.selected_run = run
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-family:\'DM Mono\',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#52525b;margin-bottom:8px;padding:0 4px;">Event Log</div>', unsafe_allow_html=True)

    dot_colors = {"info": "#a78bfa", "ok": "#34d399", "warn": "#fb923c", "err": "#f87171"}
    if not st.session_state.log:
        st.markdown('<div style="font-family:\'DM Mono\',monospace;font-size:11px;color:#52525b;padding:6px 4px;">No events yet.</div>', unsafe_allow_html=True)
    for ev in reversed(st.session_state.log[-15:]):
        dc = dot_colors.get(ev["kind"], "#a78bfa")
        st.markdown(f"""
        <div class="log-entry">
            <div class="log-dot" style="background:{dc}"></div>
            <div class="log-time">{ev["ts"]}</div>
            <div class="log-msg">{ev["msg"]}</div>
        </div>""", unsafe_allow_html=True)

    if st.session_state.log:
        if st.button("Clear Log", use_container_width=True):
            st.session_state.log = []
            st.rerun()


# ── Main ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Research Pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">4 agents · search → read → write → critique</div>', unsafe_allow_html=True)

# ── Past run viewer ───────────────────────────────────────────────────────────
if st.session_state.selected_run:
    run = st.session_state.selected_run
    s = run["state"]
    st.markdown(f"### 📋 {run['topic']}")
    st.markdown("<hr>", unsafe_allow_html=True)
    for key, icon, name in [("search_result","🔍","Search Agent"),("reader_result","📄","Reader Agent"),("report","✍️","Writer Chain"),("feedback","🧐","Critic Chain")]:
        val = s.get(key, "")
        if not val:
            continue
        if key == "report":
            st.markdown(f'<div class="report-card"><div class="report-header"><div class="report-title">📄 Research Report</div><div class="report-label">Saved</div></div><div class="report-body">{val}</div></div>', unsafe_allow_html=True)
        elif key == "feedback":
            st.markdown(f'<div class="critic-card"><div class="critic-label">🧐 Critic Feedback</div><div class="critic-body">{val}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(card(icon, name, "badge-done", "Done", str(val)[:500]), unsafe_allow_html=True)
    if st.button("← Back"):
        st.session_state.selected_run = None
        st.rerun()
    st.stop()

# ── Input ─────────────────────────────────────────────────────────────────────
col_in, col_btn = st.columns([5, 1])
with col_in:
    topic = st.text_input("topic", placeholder="e.g. 'Advances in LLM reasoning 2024'",
                          label_visibility="collapsed", disabled=st.session_state.running)
with col_btn:
    run_btn = st.button("Running…" if st.session_state.running else "▶  Run",
                        disabled=st.session_state.running, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Empty state ───────────────────────────────────────────────────────────────
if not st.session_state.running and not run_btn:
    st.markdown("""
    <div style="text-align:center;padding:70px 20px;color:#52525b;">
        <div style="font-size:52px;margin-bottom:16px;">🧠</div>
        <div style="font-family:'Cabinet Grotesk',sans-serif;font-weight:700;font-size:18px;color:#3f3f46;margin-bottom:8px;">Ready to research</div>
        <div style="font-family:'DM Mono',monospace;font-size:12px;">Type a topic above and hit ▶ Run</div>
    </div>""", unsafe_allow_html=True)

# ── Run ───────────────────────────────────────────────────────────────────────
if run_btn and topic.strip():
    st.session_state.running = True
    q = topic.strip()
    add_log(f"Started: {q[:40]}", "info")
    state = {}

    c1, c2, c3, c4 = st.empty(), st.empty(), st.empty(), st.empty()

    # pending placeholders
    c2.markdown(card("📄","Reader Agent","badge-pending","Waiting"), unsafe_allow_html=True)
    c3.markdown(card("✍️","Writer Chain","badge-pending","Waiting"), unsafe_allow_html=True)
    c4.markdown(card("🧐","Critic Chain","badge-pending","Waiting"), unsafe_allow_html=True)

    # ── Step 1: Search ──
    c1.markdown(card("🔍","Search Agent","badge-active","Running","Searching for recent information…"), unsafe_allow_html=True)
    from agents import search_agent
    sa = search_agent()
    sr = sa.invoke({"messages": [("user", f"Find recent, reliable and detailed information about: {q}")]})
    state["search_result"] = sr["messages"][-1].content
    add_log("Search Agent ✓", "ok")
    c1.markdown(card("🔍","Search Agent","badge-done","Done", state["search_result"]), unsafe_allow_html=True)

    # ── Step 2: Reader ──
    c2.markdown(card("📄","Reader Agent","badge-active","Running","Scraping top resource…"), unsafe_allow_html=True)
    from agents import reader_agent
    ra = reader_agent()
    rr = ra.invoke({"messages": [("user",
        f"Based on the following search results about '{q}', "
        f"pick the most relevant URL and scrape it for deeper content.\n\n"
        f"Search Results:\n{state['search_result'][:800]}")]})
    state["reader_result"] = rr["messages"][-1].content
    add_log("Reader Agent ✓", "ok")
    c2.markdown(card("📄","Reader Agent","badge-done","Done", state["reader_result"]), unsafe_allow_html=True)

    # ── Step 3: Writer ──
    c3.markdown(card("✍️","Writer Chain","badge-active","Running","Drafting report…"), unsafe_allow_html=True)
    from agents import writer_chain
    combined = f"SEARCH RESULT:\n{state['search_result']}\n\nDETAILED SCRAPED CONTENT:\n{state['reader_result']}"
    state["report"] = writer_chain.invoke({"topic": q, "research": combined})
    add_log("Writer Chain ✓", "ok")
    report_extra = f"""
    <div class="report-card">
        <div class="report-header">
            <div class="report-title">📄 Research Report</div>
            <div class="report-label">Generated</div>
        </div>
        <div class="report-body">{state['report']}</div>
    </div>"""
    c3.markdown(card("✍️","Writer Chain","badge-done","Done","", report_extra), unsafe_allow_html=True)

    # ── Step 4: Critic ──
    c4.markdown(card("🧐","Critic Chain","badge-active","Running","Reviewing report…"), unsafe_allow_html=True)
    from agents import critic_chain
    state["feedback"] = critic_chain.invoke({"report": state["report"]})
    add_log("Critic Chain ✓", "ok")
    add_log("Pipeline complete 🎉", "ok")
    critic_extra = f"""
    <div class="critic-card">
        <div class="critic-label">🧐 Critic Feedback</div>
        <div class="critic-body">{state['feedback']}</div>
    </div>"""
    c4.markdown(card("🧐","Critic Chain","badge-done","Done","", critic_extra), unsafe_allow_html=True)

    st.session_state.history.append({"topic": q, "state": state})
    st.session_state.running = False