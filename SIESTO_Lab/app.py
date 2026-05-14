import os
import base64

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="十万个怎么办", layout="wide")


def image_as_base64(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


st.markdown(
    """
<style>
    :root {
        --ink: #15171d;
        --muted: #667085;
        --line: rgba(30, 34, 44, 0.12);
        --blue: #0071e3;
        --cyan: #00c2ff;
        --pink: #ff4fd8;
        --green: #4ade80;
        --orange: #ff9f1c;
        --panel: #f6f7fb;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(28px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes breathe {
        0%, 100% { transform: scale(1); opacity: 0.92; }
        50% { transform: scale(1.035); opacity: 1; }
    }

    @keyframes orbit {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    @keyframes dashFlow {
        from { stroke-dashoffset: 900; }
        to { stroke-dashoffset: 0; }
    }

    @keyframes pulseNode {
        0%, 100% { box-shadow: 0 0 0 0 rgba(0,113,227,0.28); }
        50% { box-shadow: 0 0 0 12px rgba(0,113,227,0); }
    }

    @keyframes dataMove {
        0% { offset-distance: 0%; opacity: 0; }
        10% { opacity: 1; }
        85% { opacity: 1; }
        100% { offset-distance: 100%; opacity: 0; }
    }

    @keyframes beamFlow {
        0% { background-position: 0% 50%; filter: hue-rotate(0deg); }
        100% { background-position: 220% 50%; filter: hue-rotate(22deg); }
    }

    @keyframes floatNode {
        0%, 100% { transform: translate3d(0, 0, 0); }
        50% { transform: translate3d(0, -10px, 0); }
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0, 194, 255, 0.08), transparent 32rem),
            radial-gradient(circle at top right, rgba(255, 79, 216, 0.07), transparent 30rem),
            #ffffff !important;
        color: var(--ink) !important;
    }

    h1, h2, h3, h4, p, span, div, label {
        color: var(--ink) !important;
        letter-spacing: 0 !important;
    }

    .block-container {
        padding-top: 2rem;
        max-width: 1180px;
    }

    .hero {
        min-height: 68vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 56px 18px 34px;
        border-bottom: 1px solid var(--line);
    }

    .hero h1 {
        font-size: clamp(44px, 7vw, 92px);
        line-height: 1.02;
        margin: 0;
        font-weight: 800;
    }

    .hero p {
        max-width: 780px;
        margin: 22px auto 0;
        font-size: 20px;
        line-height: 1.7;
        color: var(--muted) !important;
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border: 1px solid var(--line);
        border-radius: 999px;
        margin-bottom: 22px;
        color: var(--muted) !important;
        background: rgba(255,255,255,0.72);
        backdrop-filter: blur(12px);
    }

    .apple-card {
        background-color: var(--panel) !important;
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 20px;
        border: 1px solid rgba(30, 34, 44, 0.1);
        transition: all 0.45s cubic-bezier(0.25, 0.1, 0.25, 1);
        animation: fadeInUp 0.8s ease-out backwards;
    }

    .apple-card:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 113, 227, 0.5) !important;
        box-shadow: 0 24px 50px rgba(20, 30, 60, 0.10) !important;
    }

    .caption-text {
        text-align: center;
        color: #86868b !important;
        font-size: 14px;
        display: block;
    }

    .section-title {
        text-align: center;
        font-size: 38px;
        margin: 64px 0 26px;
        font-weight: 760;
    }

    .knowledge-stage {
        position: relative;
        min-height: 560px;
        overflow: hidden;
        border-radius: 8px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.94), rgba(246,247,251,0.9)),
            repeating-linear-gradient(90deg, rgba(0,0,0,0.035) 0 1px, transparent 1px 80px),
            repeating-linear-gradient(0deg, rgba(0,0,0,0.035) 0 1px, transparent 1px 80px);
        border: 1px solid var(--line);
        margin: 20px 0 54px;
    }

    .knowledge-copy {
        position: absolute;
        z-index: 3;
        left: 42px;
        top: 38px;
        width: min(420px, calc(100% - 84px));
    }

    .knowledge-copy h2,
    .wire-copy h2 {
        font-size: 34px;
        line-height: 1.2;
        margin: 0 0 14px;
    }

    .knowledge-copy p,
    .wire-copy p {
        color: var(--muted) !important;
        line-height: 1.8;
        font-size: 16px;
        margin: 0;
    }

    .circle-wrap {
        position: absolute;
        width: 430px;
        height: 430px;
        right: 8%;
        top: 58px;
    }

    .known-circle {
        position: absolute;
        inset: 92px;
        border: 3px solid rgba(0, 113, 227, 0.88);
        border-radius: 50%;
        animation: breathe 4.4s ease-in-out infinite;
        background: rgba(0, 113, 227, 0.055);
    }

    .unknown-ring {
        position: absolute;
        inset: 34px;
        border-radius: 50%;
        border: 1px dashed rgba(255, 79, 216, 0.72);
        animation: orbit 18s linear infinite;
    }

    .unknown-ring:nth-child(2) {
        inset: 0;
        border-color: rgba(0, 194, 255, 0.52);
        animation-duration: 30s;
        animation-direction: reverse;
    }

    .circle-label {
        position: absolute;
        inset: 0;
        display: grid;
        place-items: center;
        text-align: center;
        font-weight: 750;
        font-size: 28px;
    }

    .circle-label small {
        display: block;
        margin-top: 10px;
        font-size: 14px;
        color: var(--muted) !important;
        font-weight: 500;
    }

    .question-dot {
        position: absolute;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: white !important;
        font-weight: 800;
        background: linear-gradient(135deg, var(--pink), var(--blue));
        animation: pulseNode 2.8s ease-in-out infinite;
    }

    .dot-a { right: 8%; top: 12%; animation-delay: 0.1s; }
    .dot-b { right: 39%; bottom: 4%; animation-delay: 0.7s; }
    .dot-c { left: 4%; bottom: 28%; animation-delay: 1.2s; }
    .dot-d { left: 24%; top: 2%; animation-delay: 1.8s; }

    .quote-strip {
        position: absolute;
        left: 42px;
        right: 42px;
        bottom: 34px;
        padding: 18px 22px;
        border-left: 4px solid var(--blue);
        background: rgba(255,255,255,0.78);
        backdrop-filter: blur(12px);
        font-size: 18px;
        line-height: 1.65;
    }

    .wire-stage {
        position: relative;
        min-height: 640px;
        overflow: hidden;
        border-radius: 8px;
        background: #080b12;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 20px 0 46px;
    }

    .wire-stage * {
        color: #f7fbff !important;
    }

    .wire-copy {
        position: absolute;
        z-index: 5;
        left: 42px;
        top: 38px;
        width: min(430px, calc(100% - 84px));
    }

    .wire-copy p {
        color: rgba(247,251,255,0.68) !important;
    }

    .discipline {
        position: absolute;
        z-index: 4;
        min-width: 116px;
        padding: 12px 16px;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.18);
        background: rgba(255,255,255,0.09);
        backdrop-filter: blur(16px);
        text-align: center;
        font-weight: 720;
        animation: pulseNode 3.4s ease-in-out infinite, floatNode 5.2s ease-in-out infinite;
    }

    .d-mech { left: 10%; top: 40%; }
    .d-elec { right: 12%; top: 22%; animation-delay: .4s; }
    .d-ai { right: 8%; bottom: 24%; animation-delay: .8s; }
    .d-material { left: 12%; bottom: 16%; animation-delay: 1.2s; }
    .d-bio { left: 43%; top: 18%; animation-delay: 1.6s; }
    .d-energy { left: 44%; bottom: 11%; animation-delay: 2s; }

    .innovation-core {
        position: absolute;
        z-index: 6;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        width: 190px;
        height: 190px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        text-align: center;
        font-size: 24px;
        font-weight: 820;
        background:
            radial-gradient(circle, rgba(255,255,255,0.18), rgba(0,194,255,0.16) 44%, rgba(255,79,216,0.16));
        border: 1px solid rgba(255,255,255,0.28);
        box-shadow: 0 0 70px rgba(0, 194, 255, 0.26);
        animation: breathe 3.8s ease-in-out infinite;
    }

    .wire-svg {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
    }

    .wire-line {
        fill: none;
        stroke-width: 2.8;
        stroke-linecap: round;
        stroke-dasharray: 12 18;
        animation: dashFlow 8s linear infinite;
        filter: drop-shadow(0 0 8px currentColor);
    }

    .line-cyan { stroke: #00c2ff; color: #00c2ff; }
    .line-pink { stroke: #ff4fd8; color: #ff4fd8; animation-duration: 10s; }
    .line-green { stroke: #4ade80; color: #4ade80; animation-duration: 7s; }
    .line-orange { stroke: #ff9f1c; color: #ff9f1c; animation-duration: 9s; }

    .beam {
        position: absolute;
        z-index: 3;
        left: 50%;
        top: 50%;
        width: 76%;
        height: 4px;
        border-radius: 999px;
        transform-origin: 0 50%;
        background: linear-gradient(90deg, transparent, #00c2ff, #ffffff, #ff4fd8, transparent);
        background-size: 220% 100%;
        box-shadow: 0 0 18px rgba(0,194,255,.8), 0 0 32px rgba(255,79,216,.45);
        animation: beamFlow 2.8s linear infinite;
        opacity: .82;
    }

    .beam.b1 { transform: rotate(18deg) translateX(-50%); }
    .beam.b2 { transform: rotate(-29deg) translateX(-50%); animation-delay: .35s; }
    .beam.b3 { transform: rotate(62deg) translateX(-50%); animation-delay: .7s; }
    .beam.b4 { transform: rotate(-68deg) translateX(-50%); animation-delay: 1.05s; }
    .beam.b5 { transform: rotate(0deg) translateX(-50%); animation-delay: 1.4s; }
    .beam.b6 { transform: rotate(90deg) translateX(-50%); animation-delay: 1.75s; }

    .spark {
        position: absolute;
        z-index: 3;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: white;
        box-shadow: 0 0 18px #00c2ff, 0 0 34px #ff4fd8;
        offset-rotate: auto;
        animation: dataMove 5.5s linear infinite;
    }

    .spark.one {
        offset-path: path("M 130 300 C 320 90, 580 550, 920 170");
    }

    .spark.two {
        offset-path: path("M 160 500 C 360 260, 650 260, 910 430");
        animation-delay: 1.2s;
        animation-duration: 6.4s;
    }

    .spark.three {
        offset-path: path("M 500 120 C 310 330, 700 390, 500 560");
        animation-delay: 2.1s;
        animation-duration: 5.8s;
    }

    .principle-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 18px;
        margin: 20px 0 36px;
    }

    .principle-card {
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 22px;
        background: rgba(255,255,255,0.74);
    }

    .principle-card h3 {
        margin: 0 0 10px;
        font-size: 20px;
    }

    .principle-card p {
        color: var(--muted) !important;
        line-height: 1.7;
        margin: 0;
    }

    @media (max-width: 860px) {
        .hero { min-height: 58vh; }
        .knowledge-stage, .wire-stage { min-height: 760px; }
        .circle-wrap {
            width: 330px;
            height: 330px;
            right: 50%;
            transform: translateX(50%);
            top: 260px;
        }
        .quote-strip { left: 22px; right: 22px; bottom: 24px; font-size: 16px; }
        .knowledge-copy, .wire-copy { left: 24px; top: 28px; width: calc(100% - 48px); }
        .discipline { min-width: 96px; font-size: 14px; }
        .d-mech { left: 7%; top: 39%; }
        .d-elec { right: 6%; top: 38%; }
        .d-ai { right: 6%; bottom: 23%; }
        .d-material { left: 7%; bottom: 23%; }
        .d-bio { left: 35%; top: 52%; }
        .d-energy { left: 33%; bottom: 8%; }
        .innovation-core { width: 150px; height: 150px; font-size: 20px; top: 58%; }
        .principle-grid { grid-template-columns: 1fr; }
    }
</style>
""",
    unsafe_allow_html=True,
)


with st.sidebar:
    st.markdown("## 十万个怎么办 AI 助理")
    st.caption("基于《实体构筑》资产包实时驱动")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "你好，刘婧主理人。我已准备好解构具身智能的工程逻辑。"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("询问工程逻辑..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if "指南车" in prompt:
                response = (
                    "指南车通过离合齿轮组捕捉左右轮路程差，并反向驱动指向机构抵消车身转向。"
                    "它说明：底层稳定性可以先由结构承担，再把算力留给更高层的判断。"
                )
            elif "死穴" in prompt or "本能" in prompt:
                response = (
                    "具身智能的本能资产，是把高频、救命、不可犹豫的动作写进结构里。"
                    "这类能力不是先想再动，而是像肌肉反射一样直接发生。"
                )
            elif "创新" in prompt or "跨界" in prompt or "连接" in prompt:
                response = (
                    "创新常常来自学科之间的非标准连接：机械遇到算法，材料遇到生命，能源遇到控制。"
                    "关键不是重复既有答案，而是在边界处找到新的可行路径。"
                )
            else:
                response = "这是一个工程问题。我们可以从目标、约束、结构、反馈四个层次拆解它。"

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    st.divider()
    page = st.radio("切换内容板块", ["实验室总览", "概念动画馆", "虚拟实验室", "指南车专题模型"])


def render_hero() -> None:
    logo_data = image_as_base64("logo.png")
    logo_html = (
        f'<img src="data:image/png;base64,{logo_data}" style="width:min(760px, 92vw); height:auto; display:block; margin:0 auto 12px;">'
        if logo_data
        else "<h1>十万个怎么办</h1>"
    )
    st.markdown(
        f"""
        <section class="hero">
            <div>
                <div class="eyebrow">从问题走向工程答案</div>
                {logo_html}
                <p>把孩子的“为什么”，推进到可以动手、可以建模、可以验证的“怎么办”。这里不是知识陈列柜，而是一座把科学问题翻译成工程路径的实验室。</p>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_knowledge_circle() -> None:
    st.markdown(
        """
        <div class="knowledge-stage">
            <div class="knowledge-copy">
                <h2>知识之圆</h2>
                <p>已知越多，圆周越长；圆周越长，接触未知的边界也越大。学习不是把世界变小，而是让新的问题不断显影。</p>
            </div>
            <div class="circle-wrap">
                <div class="unknown-ring"></div>
                <div class="unknown-ring"></div>
                <div class="known-circle"></div>
                <div class="circle-label">已知<small>Knowledge</small></div>
                <div class="question-dot dot-a">?</div>
                <div class="question-dot dot-b">?</div>
                <div class="question-dot dot-c">?</div>
                <div class="question-dot dot-d">?</div>
            </div>
            <div class="quote-strip">
                “知识好比一个圆，圆内是已知，圆外是未知；知道得越多，接触未知的边界也越大。”
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_crossed_wires() -> None:
    st.markdown(
        """
        <div class="wire-stage">
            <div class="wire-copy">
                <h2>跨界连接生成创新</h2>
                <p>把工程学科放进同一张神经网络：机械、电子、AI、材料、生物、能源之间的线条不断穿梭，新的连接点就是新的问题解法。</p>
            </div>

            <svg class="wire-svg" viewBox="0 0 1080 640" preserveAspectRatio="none" aria-hidden="true">
                <path class="wire-line line-cyan" d="M120,310 C310,80 620,560 960,160" />
                <path class="wire-line line-pink" d="M130,500 C360,250 670,250 950,440" />
                <path class="wire-line line-green" d="M500,100 C300,330 710,380 510,560" />
                <path class="wire-line line-orange" d="M180,390 C400,600 730,40 910,290" />
                <path class="wire-line line-cyan" d="M260,180 C420,360 620,150 820,520" />
                <path class="wire-line line-pink" d="M240,540 C510,420 540,210 870,190" />
            </svg>

            <div class="beam b1"></div>
            <div class="beam b2"></div>
            <div class="beam b3"></div>
            <div class="beam b4"></div>
            <div class="beam b5"></div>
            <div class="beam b6"></div>

            <div class="spark one"></div>
            <div class="spark two"></div>
            <div class="spark three"></div>

            <div class="discipline d-mech">机械工程</div>
            <div class="discipline d-elec">电子控制</div>
            <div class="discipline d-ai">人工智能</div>
            <div class="discipline d-material">材料科学</div>
            <div class="discipline d-bio">生命科学</div>
            <div class="discipline d-energy">能源系统</div>

            <div class="innovation-core">新通路<br><span style="font-size:14px; opacity:.72;">new path</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_concept_animation() -> None:
    components.html(
        """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
    * { box-sizing: border-box; }
    body {
        margin: 0;
        font-family: "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif;
        color: #111827;
        background: transparent;
    }

    @keyframes expandCircle {
        0%, 100% { transform: translate(-50%, -50%) scale(.92); }
        50% { transform: translate(-50%, -50%) scale(1.08); }
    }

    @keyframes rotateRing {
        from { transform: translate(-50%, -50%) rotate(0deg); }
        to { transform: translate(-50%, -50%) rotate(360deg); }
    }

    @keyframes blink {
        0%, 100% { opacity: .55; transform: scale(.9); }
        50% { opacity: 1; transform: scale(1.16); }
    }

    @keyframes drawLine {
        from { stroke-dashoffset: 1100; }
        to { stroke-dashoffset: 0; }
    }

    @keyframes glowMove {
        0% { background-position: 0% 50%; opacity: .3; }
        35% { opacity: 1; }
        100% { background-position: 240% 50%; opacity: .3; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    @keyframes scan {
        0% { transform: translateX(-110%); }
        100% { transform: translateX(110%); }
    }

    .exhibit {
        width: 100%;
        max-width: 1120px;
        margin: 0 auto;
        display: grid;
        gap: 28px;
    }

    .panel {
        position: relative;
        overflow: hidden;
        min-height: 540px;
        border-radius: 18px;
        border: 1px solid rgba(17,24,39,.12);
        background: #f8fafc;
    }

    .panel::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            linear-gradient(90deg, rgba(15,23,42,.045) 1px, transparent 1px),
            linear-gradient(0deg, rgba(15,23,42,.045) 1px, transparent 1px);
        background-size: 54px 54px;
        mask-image: radial-gradient(circle at center, black, transparent 76%);
    }

    .panel::after {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,.5), transparent);
        animation: scan 5.2s linear infinite;
        pointer-events: none;
    }

    .copy {
        position: absolute;
        z-index: 10;
        left: 36px;
        top: 32px;
        width: min(390px, calc(100% - 72px));
    }

    .tag {
        display: inline-flex;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(0,113,227,.1);
        color: #0066cc;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 14px;
    }

    h2 {
        margin: 0 0 12px;
        font-size: 38px;
        line-height: 1.12;
        letter-spacing: 0;
    }

    p {
        margin: 0;
        color: #5b6472;
        font-size: 16px;
        line-height: 1.8;
    }

    .circle-world {
        position: absolute;
        right: 7%;
        top: 50%;
        width: 460px;
        height: 460px;
        transform: translateY(-50%);
    }

    .ring, .known {
        position: absolute;
        left: 50%;
        top: 50%;
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }

    .ring.big {
        width: 430px;
        height: 430px;
        border: 1px dashed rgba(255,79,216,.8);
        animation: rotateRing 24s linear infinite;
    }

    .ring.mid {
        width: 350px;
        height: 350px;
        border: 1px dashed rgba(0,194,255,.8);
        animation: rotateRing 18s linear infinite reverse;
    }

    .known {
        width: 210px;
        height: 210px;
        border: 4px solid #0071e3;
        background: radial-gradient(circle, rgba(0,113,227,.18), rgba(0,113,227,.04));
        box-shadow: 0 0 48px rgba(0,113,227,.22);
        animation: expandCircle 4s ease-in-out infinite;
        display: grid;
        place-items: center;
        text-align: center;
        font-size: 30px;
        font-weight: 850;
    }

    .known span {
        display: block;
        margin-top: 8px;
        font-size: 13px;
        color: #667085;
        font-weight: 600;
    }

    .q {
        position: absolute;
        z-index: 5;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: white;
        font-size: 22px;
        font-weight: 900;
        background: linear-gradient(135deg, #ff4fd8, #0071e3);
        box-shadow: 0 0 26px rgba(255,79,216,.45);
        animation: blink 2.4s ease-in-out infinite;
    }

    .q1 { right: 24px; top: 78px; }
    .q2 { right: 96px; bottom: 20px; animation-delay: .4s; }
    .q3 { left: 38px; bottom: 96px; animation-delay: .8s; }
    .q4 { left: 96px; top: 36px; animation-delay: 1.2s; }

    .quote {
        position: absolute;
        z-index: 10;
        left: 36px;
        right: 36px;
        bottom: 30px;
        padding: 18px 22px;
        border-left: 4px solid #0071e3;
        background: rgba(255,255,255,.76);
        backdrop-filter: blur(16px);
        border-radius: 0 12px 12px 0;
        color: #1f2937;
        font-size: 18px;
        line-height: 1.7;
    }

    .dark {
        min-height: 620px;
        background:
            radial-gradient(circle at 50% 50%, rgba(0,194,255,.18), transparent 30%),
            radial-gradient(circle at 80% 20%, rgba(255,79,216,.14), transparent 28%),
            #070b13;
        border-color: rgba(255,255,255,.12);
    }

    .dark::before {
        background:
            linear-gradient(90deg, rgba(255,255,255,.055) 1px, transparent 1px),
            linear-gradient(0deg, rgba(255,255,255,.055) 1px, transparent 1px);
        background-size: 46px 46px;
    }

    .dark h2, .dark .node, .core { color: white; }
    .dark p { color: rgba(255,255,255,.66); }
    .dark .tag { background: rgba(255,255,255,.1); color: #9be7ff; }

    svg {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
    }

    path {
        fill: none;
        stroke-width: 3;
        stroke-linecap: round;
        stroke-dasharray: 14 20;
        animation: drawLine 7s linear infinite;
        filter: drop-shadow(0 0 10px currentColor);
    }

    .c1 { stroke: #00c2ff; color: #00c2ff; }
    .c2 { stroke: #ff4fd8; color: #ff4fd8; animation-duration: 8.5s; }
    .c3 { stroke: #4ade80; color: #4ade80; animation-duration: 6.5s; }
    .c4 { stroke: #ffb020; color: #ffb020; animation-duration: 9s; }

    .beam {
        position: absolute;
        z-index: 3;
        left: 50%;
        top: 52%;
        width: 78%;
        height: 5px;
        border-radius: 999px;
        transform-origin: 0 50%;
        background: linear-gradient(90deg, transparent, #00c2ff, #fff, #ff4fd8, transparent);
        background-size: 240% 100%;
        animation: glowMove 2.5s linear infinite;
        box-shadow: 0 0 22px rgba(0,194,255,.8), 0 0 38px rgba(255,79,216,.48);
    }

    .b1 { transform: rotate(18deg) translateX(-50%); }
    .b2 { transform: rotate(-31deg) translateX(-50%); animation-delay: .35s; }
    .b3 { transform: rotate(62deg) translateX(-50%); animation-delay: .7s; }
    .b4 { transform: rotate(-68deg) translateX(-50%); animation-delay: 1.05s; }
    .b5 { transform: rotate(0deg) translateX(-50%); animation-delay: 1.4s; }
    .b6 { transform: rotate(90deg) translateX(-50%); animation-delay: 1.75s; }

    .node {
        position: absolute;
        z-index: 8;
        padding: 13px 18px;
        min-width: 118px;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,.22);
        background: rgba(255,255,255,.1);
        backdrop-filter: blur(14px);
        text-align: center;
        font-weight: 800;
        box-shadow: 0 18px 40px rgba(0,0,0,.18);
        animation: float 5s ease-in-out infinite;
    }

    .n1 { left: 9%; top: 42%; }
    .n2 { right: 9%; top: 22%; animation-delay: .4s; }
    .n3 { right: 8%; bottom: 23%; animation-delay: .8s; }
    .n4 { left: 10%; bottom: 16%; animation-delay: 1.2s; }
    .n5 { left: 44%; top: 18%; animation-delay: 1.6s; }
    .n6 { left: 43%; bottom: 10%; animation-delay: 2s; }

    .core {
        position: absolute;
        z-index: 9;
        left: 50%;
        top: 52%;
        width: 190px;
        height: 190px;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        display: grid;
        place-items: center;
        text-align: center;
        font-size: 28px;
        font-weight: 900;
        background: radial-gradient(circle, rgba(255,255,255,.22), rgba(0,194,255,.2) 44%, rgba(255,79,216,.18));
        border: 1px solid rgba(255,255,255,.3);
        box-shadow: 0 0 76px rgba(0,194,255,.36);
        animation: expandCircle 3.7s ease-in-out infinite;
    }

    .core small {
        display: block;
        margin-top: 8px;
        font-size: 13px;
        opacity: .68;
    }

    @media (max-width: 760px) {
        .panel { min-height: 720px; }
        .copy { left: 24px; top: 24px; width: calc(100% - 48px); }
        h2 { font-size: 31px; }
        .circle-world {
            right: 50%;
            top: 58%;
            width: 340px;
            height: 340px;
            transform: translate(50%, -50%);
        }
        .ring.big { width: 330px; height: 330px; }
        .ring.mid { width: 270px; height: 270px; }
        .known { width: 168px; height: 168px; font-size: 24px; }
        .quote { left: 22px; right: 22px; bottom: 22px; font-size: 15px; }
        .dark { min-height: 760px; }
        .node { min-width: 96px; font-size: 14px; padding: 11px 13px; }
        .n1 { left: 5%; top: 39%; }
        .n2 { right: 5%; top: 39%; }
        .n3 { right: 5%; bottom: 22%; }
        .n4 { left: 5%; bottom: 22%; }
        .n5 { left: 34%; top: 52%; }
        .n6 { left: 32%; bottom: 8%; }
        .core { width: 148px; height: 148px; font-size: 22px; top: 62%; }
    }
</style>
</head>
<body>
<div class="exhibit">
    <section class="panel">
        <div class="copy">
            <div class="tag">爱因斯坦 · 知识之圆</div>
            <h2>知道越多，未知越大</h2>
            <p>圆内是已知，圆外是未知。学习让圆变大，也让孩子看见更多值得追问的边界。</p>
        </div>
        <div class="circle-world">
            <div class="ring big"></div>
            <div class="ring mid"></div>
            <div class="known">已知<span>Knowledge</span></div>
            <div class="q q1">?</div>
            <div class="q q2">?</div>
            <div class="q q3">?</div>
            <div class="q q4">?</div>
        </div>
        <div class="quote">“知识好比一个圆，圆内是已知，圆外是未知；知道得越多，接触未知的边界也越大。”</div>
    </section>

    <section class="panel dark">
        <div class="copy">
            <div class="tag">科技馆 · 跨界连接</div>
            <h2>工程学科穿线成网</h2>
            <p>机械、电子、AI、材料、生命、能源不再各站一边。线条穿过去，新的连接点就长出新的“怎么办”。</p>
        </div>

        <svg viewBox="0 0 1120 620" preserveAspectRatio="none">
            <path class="c1" d="M120,310 C320,70 650,560 1000,150" />
            <path class="c2" d="M140,500 C360,250 700,250 990,440" />
            <path class="c3" d="M550,90 C310,330 750,390 540,570" />
            <path class="c4" d="M190,390 C410,600 780,40 950,290" />
            <path class="c1" d="M260,180 C450,370 640,150 850,520" />
            <path class="c2" d="M260,540 C530,420 560,210 900,190" />
        </svg>

        <div class="beam b1"></div>
        <div class="beam b2"></div>
        <div class="beam b3"></div>
        <div class="beam b4"></div>
        <div class="beam b5"></div>
        <div class="beam b6"></div>

        <div class="node n1">机械工程</div>
        <div class="node n2">电子控制</div>
        <div class="node n3">人工智能</div>
        <div class="node n4">材料科学</div>
        <div class="node n5">生命科学</div>
        <div class="node n6">能源系统</div>

        <div class="core">新通路<small>new path</small></div>
    </section>
</div>
</body>
</html>
        """,
        height=1220,
        scrolling=False,
    )


def render_knowledge_sphere_animation() -> None:
    components.html(
        """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
    html, body {
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
        overflow: hidden;
    }

    .stage {
        position: relative;
        width: 100%;
        height: 720px;
        overflow: hidden;
        background:
            radial-gradient(circle at 48% 48%, rgba(255, 222, 139, .16), transparent 18%),
            radial-gradient(circle at 42% 48%, rgba(0, 113, 227, .20), transparent 28%),
            linear-gradient(90deg, #f8f8f6 0%, #eeeeec 20%, #50555d 43%, #121720 63%, #050812 100%);
        border-radius: 8px;
        border: 1px solid rgba(10, 16, 26, .10);
    }

    canvas {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
    }

    .topbar {
        position: absolute;
        z-index: 4;
        left: 24px;
        right: 24px;
        top: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: none;
    }

    .brand {
        font-size: 24px;
        font-weight: 780;
        color: #111827;
        letter-spacing: 0;
    }

    .brand small {
        font-size: 15px;
        font-weight: 500;
        opacity: .72;
    }

    .menu {
        width: 20px;
        height: 14px;
        display: grid;
        gap: 4px;
    }

    .menu span {
        height: 1px;
        background: rgba(255,255,255,.75);
    }

    .quote {
        position: absolute;
        z-index: 4;
        left: 50%;
        top: 68px;
        transform: translateX(-50%);
        width: min(540px, 72vw);
        text-align: center;
        color: rgba(255,255,255,.88);
        font-size: 14px;
        line-height: 1.55;
        text-shadow: 0 2px 14px rgba(0,0,0,.36);
    }

    .left-title {
        position: absolute;
        z-index: 4;
        left: 9%;
        top: 48%;
        color: #171b22;
        font-size: 22px;
        font-weight: 520;
    }

    .unknown {
        position: absolute;
        z-index: 4;
        right: 10.5%;
        top: 47%;
        color: rgba(255,255,255,.52);
        font-size: 24px;
        font-weight: 360;
    }

    .ni {
        position: absolute;
        z-index: 4;
        right: 8%;
        top: 56%;
        max-width: 360px;
        color: rgba(255,255,255,.92);
        font-size: 16px;
        line-height: 1.55;
    }

    .ni b {
        display: block;
        margin-top: 16px;
        font-weight: 620;
    }

    .bottom {
        position: absolute;
        z-index: 4;
        left: 26px;
        right: 26px;
        bottom: 22px;
        display: flex;
        align-items: end;
        justify-content: space-between;
        color: rgba(255,255,255,.82);
        font-size: 13px;
    }

    .bottom nav {
        display: flex;
        gap: 14px;
        color: #111827;
        font-weight: 640;
    }

    .hint {
        color: rgba(255,255,255,.72);
        text-align: center;
        flex: 1;
    }

    .spark-mark {
        width: 48px;
        height: 48px;
        position: relative;
    }

    .spark-mark::before,
    .spark-mark::after {
        content: "";
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%) rotate(45deg);
        width: 15px;
        height: 46px;
        border-radius: 999px;
        background: rgba(255,255,255,.78);
        box-shadow: 0 0 24px rgba(255,255,255,.4);
    }

    .spark-mark::after {
        width: 46px;
        height: 15px;
    }

    @media (max-width: 760px) {
        .stage { height: 760px; }
        .brand { font-size: 18px; }
        .quote { top: 58px; width: 86vw; font-size: 13px; }
        .left-title { left: 6%; top: 21%; font-size: 17px; }
        .unknown { right: 7%; top: 76%; font-size: 18px; }
        .ni { right: 7%; left: 7%; top: 82%; max-width: none; font-size: 13px; }
        .bottom nav { display: none; }
    }
</style>
</head>
<body>
<section class="stage">
    <canvas id="knowledgeCanvas"></canvas>
    <div class="topbar">
        <div class="brand">十万个怎么办 <small>知识之圆</small></div>
        <div class="menu"><span></span><span></span><span></span></div>
    </div>

    <div class="quote">
        我学得越多，越意识到自己不知道的越多。<br>
        — 阿尔伯特·爱因斯坦
    </div>

    <div class="left-title">知识之圆</div>
    <div class="unknown">未知</div>
    <div class="ni">
        创新不是重复既有连线，<br>
        而是在跨界连接中发现新通路。
        <b>— 跨界连接生成创新</b>
    </div>

    <div class="bottom">
        <nav><span>关于</span><span>|</span><span>研究</span><span>|</span><span>资产</span><span>|</span><span>AI 助理</span></nav>
        <div class="hint">向下滚动，解码创新资产 SOP</div>
        <div class="spark-mark"></div>
    </div>
</section>

<script>
const canvas = document.getElementById("knowledgeCanvas");
const ctx = canvas.getContext("2d");
const terms = [
  "机械工程", "电子信息", "人工智能", "材料科学",
  "自动化", "航空航天", "生命科学", "能源系统",
  "控制论", "仿生结构", "传感器", "算法模型"
];
const newFields = [
  "智能材料", "仿生机器人", "航空智能控制", "能源管理算法",
  "柔性传感系统", "生命工程装备", "自主导航系统", "结构智能"
];
let w = 0, h = 0, dpr = 1, t = 0, lastTime = 0;
let particles = [];
let discoveries = [];
let sphere = { x: 0, y: 0, r: 0 };

function resize() {
  dpr = Math.min(window.devicePixelRatio || 1, 2);
  const rect = canvas.getBoundingClientRect();
  w = rect.width;
  h = rect.height;
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const mobile = w < 760;
  sphere = {
    x: mobile ? w * .50 : w * .455,
    y: mobile ? h * .50 : h * .49,
    r: Math.min(w, h) * (mobile ? .33 : .32)
  };
  initParticles();
}

function drawText(text, x, y, color = "rgba(255,255,255,.9)", size = 10) {
  ctx.font = `500 ${size}px "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif`;
  ctx.fillStyle = color;
  ctx.fillText(text, x, y);
}

function textWidth(text, size) {
  ctx.font = `500 ${size}px "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif`;
  return ctx.measureText(text).width;
}

function initParticles() {
  const mobile = w < 760;
  const size = mobile ? 10 : 12;
  particles = terms.map((text, i) => {
    const angle = (Math.PI * 2 / terms.length) * i + .4;
    const dist = sphere.r * (.22 + (i % 4) * .12);
    const radius = Math.max(25, textWidth(text, size) / 2 + 15);
    return {
      text,
      size,
      radius,
      x: sphere.x + Math.cos(angle) * dist,
      y: sphere.y + Math.sin(angle) * dist * .82,
      vx: Math.cos(angle + Math.PI / 2) * (.10 + (i % 3) * .025),
      vy: Math.sin(angle + Math.PI / 2) * (.10 + (i % 4) * .02),
      hue: i % 2 ? "gold" : "blue",
      cooldown: 0
    };
  });
  discoveries = [];
}

function drawParticle(p) {
  const fill = p.hue === "gold" ? "rgba(255,226,150,.16)" : "rgba(80,145,255,.15)";
  const stroke = p.hue === "gold" ? "rgba(255,226,150,.72)" : "rgba(111,170,255,.68)";
  const mergePulse = p.cooldown > 118 ? .82 : 1;
  ctx.save();
  ctx.shadowBlur = p.cooldown > 0 ? 22 : 10;
  ctx.shadowColor = p.hue === "gold" ? "rgba(255,220,120,.72)" : "rgba(90,150,255,.62)";
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.radius * mergePulse, 0, Math.PI * 2);
  ctx.fillStyle = fill;
  ctx.fill();
  ctx.strokeStyle = stroke;
  ctx.lineWidth = 1;
  ctx.stroke();
  ctx.shadowBlur = 0;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.font = `600 ${p.size}px "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif`;
  ctx.fillStyle = "rgba(255,255,255,.92)";
  ctx.fillText(p.text, p.x, p.y);
  ctx.restore();
}

function addDiscovery(x, y, a, b) {
  const name = newFields[(a.text.length + b.text.length + discoveries.length) % newFields.length];
  discoveries.push({ x, y, name, from: `${a.text} × ${b.text}`, life: 360, max: 360 });
  if (discoveries.length > 4) discoveries.shift();
}

function updateParticles(dt) {
  const speedScale = Math.min(dt, 34) / 16.67;
  particles.forEach((p) => {
    p.x += p.vx * speedScale;
    p.y += p.vy * speedScale;
    p.cooldown = Math.max(0, p.cooldown - speedScale);
    const dx = p.x - sphere.x;
    const dy = p.y - sphere.y;
    const dist = Math.hypot(dx, dy);
    const limit = sphere.r - p.radius - 6;
    if (dist > limit) {
      const nx = dx / dist;
      const ny = dy / dist;
      p.x = sphere.x + nx * limit;
      p.y = sphere.y + ny * limit;
      const dot = p.vx * nx + p.vy * ny;
      p.vx -= 2 * dot * nx;
      p.vy -= 2 * dot * ny;
    }
  });

  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const a = particles[i];
      const b = particles[j];
      const dx = b.x - a.x;
      const dy = b.y - a.y;
      const dist = Math.max(.01, Math.hypot(dx, dy));
      const minDist = a.radius + b.radius + 2;
      if (dist < minDist) {
        const nx = dx / dist;
        const ny = dy / dist;
        const overlap = (minDist - dist) / 2;
        a.x -= nx * overlap;
        a.y -= ny * overlap;
        b.x += nx * overlap;
        b.y += ny * overlap;
        const avx = a.vx, avy = a.vy;
        a.vx = b.vx * .92;
        a.vy = b.vy * .92;
        b.vx = avx * .92;
        b.vy = avy * .92;
        if (a.cooldown <= 0 && b.cooldown <= 0) {
          addDiscovery((a.x + b.x) / 2, (a.y + b.y) / 2, a, b);
          a.cooldown = 160;
          b.cooldown = 160;
          a.vx *= 1.35;
          a.vy *= 1.35;
          b.vx *= 1.35;
          b.vy *= 1.35;
        }
      }
    }
  }
  discoveries.forEach(d => d.life -= speedScale);
  discoveries = discoveries.filter(d => d.life > 0);
}

function drawDiscovery(d) {
  const progress = d.life / d.max;
  const appear = Math.min(1, (1 - progress) * 5);
  const fade = Math.min(1, progress * 2.2);
  const alpha = appear * fade;
  const radius = 22 + appear * 34 + Math.sin((1 - progress) * Math.PI * 5) * 2;
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.shadowBlur = 34;
  ctx.shadowColor = "rgba(255,224,145,.95)";
  ctx.beginPath();
  ctx.arc(d.x, d.y, radius, 0, Math.PI * 2);
  const grad = ctx.createRadialGradient(d.x - radius * .25, d.y - radius * .28, 4, d.x, d.y, radius);
  grad.addColorStop(0, "rgba(255,255,255,.78)");
  grad.addColorStop(.34, "rgba(255,232,166,.42)");
  grad.addColorStop(1, "rgba(0,113,227,.20)");
  ctx.fillStyle = grad;
  ctx.fill();
  ctx.strokeStyle = "rgba(255,232,166,.92)";
  ctx.lineWidth = 1.3;
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(d.x, d.y, radius + 8 * appear, 0, Math.PI * 2);
  ctx.strokeStyle = "rgba(255,232,166,.22)";
  ctx.lineWidth = 1;
  ctx.stroke();
  ctx.shadowBlur = 0;
  ctx.font = `700 13px "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif`;
  ctx.fillStyle = "rgba(255,255,255,.96)";
  ctx.fillText(d.name, d.x, d.y - 3);
  ctx.font = `500 8px "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif`;
  ctx.fillStyle = "rgba(255,255,255,.62)";
  ctx.fillText("新学科", d.x, d.y + 14);
  ctx.restore();
}

function draw(now = 0) {
  const dt = lastTime ? now - lastTime : 16.67;
  lastTime = now;
  t += dt * .36;
  updateParticles(dt);
  ctx.clearRect(0, 0, w, h);

  const mobile = w < 760;
  const cx = sphere.x;
  const cy = sphere.y;
  const r = sphere.r;

  const glow = ctx.createRadialGradient(cx, cy, r * .12, cx, cy, r * 1.05);
  glow.addColorStop(0, "rgba(255,255,255,.18)");
  glow.addColorStop(.42, "rgba(0,113,227,.26)");
  glow.addColorStop(.72, "rgba(255,215,120,.14)");
  glow.addColorStop(1, "rgba(0,0,0,0)");
  ctx.fillStyle = glow;
  ctx.beginPath();
  ctx.arc(cx, cy, r * 1.12, 0, Math.PI * 2);
  ctx.fill();

  ctx.save();
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.clip();

  particles.forEach(drawParticle);
  discoveries.forEach(drawDiscovery);

  ctx.restore();

  for (let i = 0; i < 4; i++) {
    ctx.beginPath();
    ctx.arc(cx, cy, r * (.88 + i * .055 + Math.sin(t * .001 + i) * .015), 0, Math.PI * 2);
    ctx.strokeStyle = i % 2 ? "rgba(0,113,227,.34)" : "rgba(255,220,132,.52)";
    ctx.lineWidth = i === 0 ? 2 : 1;
    ctx.stroke();
  }

  for (let i = 0; i < 46; i++) {
    const a = i * .57 + t * .0014;
    const x = cx + Math.cos(a) * r * (.98 + .04 * Math.sin(i));
    const y = cy + Math.sin(a) * r * (.98 + .04 * Math.cos(i));
    ctx.fillStyle = i % 2 ? "rgba(255,231,160,.7)" : "rgba(79,144,255,.6)";
    ctx.beginPath();
    ctx.arc(x, y, i % 5 === 0 ? 1.8 : 1.1, 0, Math.PI * 2);
    ctx.fill();
  }

  requestAnimationFrame(draw);
}

window.addEventListener("resize", resize);
resize();
draw();
</script>
</body>
</html>
        """,
        height=720,
        scrolling=False,
    )


def render_chariot_virtual_lab() -> None:
    components.html(
        """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
    * { box-sizing: border-box; }
    body {
        margin: 0;
        background: transparent;
        font-family: "HarmonyOS Sans SC", "MiSans", "Source Han Sans SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
        color: #121826;
    }

    .lab {
        width: 100%;
        min-height: 980px;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(18,24,38,.12);
        background:
            radial-gradient(circle at 26% 22%, rgba(0,113,227,.10), transparent 28%),
            radial-gradient(circle at 80% 20%, rgba(255,196,87,.16), transparent 26%),
            linear-gradient(135deg, #f8fafc 0%, #eef2f7 48%, #101722 100%);
        position: relative;
    }

    .header {
        position: absolute;
        left: 34px;
        top: 28px;
        z-index: 10;
        max-width: 560px;
    }

    .kicker {
        display: inline-flex;
        padding: 7px 12px;
        border: 1px solid rgba(18,24,38,.14);
        border-radius: 999px;
        background: rgba(255,255,255,.62);
        backdrop-filter: blur(12px);
        color: #285f9f;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    h1 {
        margin: 0;
        font-size: 38px;
        line-height: 1.16;
        letter-spacing: 0;
    }

    .subtitle {
        margin-top: 12px;
        color: #5b6573;
        font-size: 16px;
        line-height: 1.75;
    }

    .controls {
        position: absolute;
        right: 30px;
        top: 32px;
        z-index: 12;
        display: grid;
        gap: 10px;
        width: 210px;
    }

    button {
        appearance: none;
        border: 1px solid rgba(255,255,255,.24);
        background: rgba(255,255,255,.12);
        color: rgba(255,255,255,.86);
        border-radius: 999px;
        padding: 11px 14px;
        font: inherit;
        font-size: 14px;
        cursor: pointer;
        backdrop-filter: blur(14px);
        transition: .22s ease;
    }

    button.active {
        background: rgba(255,255,255,.92);
        color: #101722;
        border-color: rgba(255,255,255,.92);
        box-shadow: 0 14px 30px rgba(0,0,0,.16);
    }

    .scene {
        position: absolute;
        left: 32px;
        right: 32px;
        top: 170px;
        height: 520px;
        border-radius: 12px;
        overflow: hidden;
        background:
            linear-gradient(90deg, rgba(255,255,255,.72), rgba(255,255,255,.28) 48%, rgba(0,0,0,.10)),
            #dfe6ef;
        border: 1px solid rgba(18,24,38,.10);
        box-shadow: inset 0 0 0 1px rgba(255,255,255,.42);
    }

    canvas {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
    }

    .readout {
        position: absolute;
        z-index: 8;
        left: 22px;
        bottom: 20px;
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }

    .pill {
        padding: 9px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,.72);
        border: 1px solid rgba(18,24,38,.10);
        backdrop-filter: blur(12px);
        font-size: 13px;
        color: #344054;
    }

    .status {
        position: absolute;
        z-index: 8;
        right: 20px;
        bottom: 20px;
        width: min(380px, calc(100% - 40px));
        padding: 16px 18px;
        border-radius: 10px;
        background: rgba(16,23,34,.84);
        color: white;
        backdrop-filter: blur(14px);
        box-shadow: 0 22px 50px rgba(0,0,0,.20);
    }

    .status b {
        display: block;
        margin-bottom: 6px;
        font-size: 16px;
    }

    .status span {
        color: rgba(255,255,255,.76);
        font-size: 14px;
        line-height: 1.65;
    }

    .logic {
        position: absolute;
        left: 32px;
        right: 32px;
        bottom: 30px;
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 14px;
    }

    .card {
        min-height: 196px;
        padding: 18px;
        border-radius: 10px;
        background: rgba(255,255,255,.80);
        border: 1px solid rgba(18,24,38,.10);
        backdrop-filter: blur(16px);
    }

    .card h3 {
        margin: 0 0 8px;
        font-size: 18px;
    }

    .card p {
        margin: 0;
        color: #5b6573;
        font-size: 14px;
        line-height: 1.65;
    }

    .card p span {
        display: block;
        margin-top: 7px;
    }

    .card.active {
        background: rgba(255,255,255,.96);
        border-color: rgba(0,113,227,.42);
        box-shadow: 0 18px 38px rgba(0,113,227,.12);
    }

    @media (max-width: 900px) {
        .lab { min-height: 1240px; }
        .header { left: 22px; right: 22px; top: 22px; }
        h1 { font-size: 30px; }
        .controls { left: 22px; right: 22px; top: 150px; width: auto; grid-template-columns: repeat(3, 1fr); }
        button { padding: 10px 8px; font-size: 13px; }
        .scene { left: 20px; right: 20px; top: 220px; height: 520px; }
        .status { left: 20px; right: 20px; bottom: 18px; width: auto; }
        .logic { left: 20px; right: 20px; bottom: 28px; top: 772px; grid-template-columns: 1fr; }
    }
</style>
</head>
<body>
<section class="lab">
    <div class="header">
        <div class="kicker">虚拟实验器材 · 会自己纠偏的小车</div>
        <h1>为什么有些机器人不用写更多代码，也能走直线？</h1>
        <div class="subtitle">先看一个现象：同一辆履带车，左边地面粗、右边地面滑，它会慢慢偏向一边。这个实验要证明：有些“智能”，可以先藏在机械结构里。</div>
    </div>

    <div class="controls">
        <button class="active" data-mode="runaway">1. 先看走歪</button>
        <button data-mode="couple">2. 接上机关</button>
        <button data-mode="miracle">3. 自己走直</button>
    </div>

    <div class="scene">
        <canvas id="labCanvas"></canvas>
        <div class="readout">
            <div class="pill" id="leftFriction">左地面：粗糙，抓地强</div>
            <div class="pill" id="rightFriction">右地面：光滑，容易滑</div>
            <div class="pill" id="gearState">差值读取：未接入</div>
        </div>
        <div class="status">
            <b id="statusTitle">第 1 步：它为什么会走歪？</b>
            <span id="statusText">左边地面更粗，右边地面更滑。两条履带虽然一起转，但实际走出来的距离不一样，所以车头会慢慢偏过去。</span>
        </div>
    </div>

    <div class="logic">
        <div class="card active" data-step="goal">
            <h3>目标</h3>
            <p>
                让小车在“左边粗糙、右边光滑”的地面上尽量走直。
                <span>青少年观察点：先不要急着写代码，先问一问，能不能让机械结构自己帮忙纠偏？</span>
            </p>
        </div>
        <div class="card" data-step="constraint">
            <h3>约束</h3>
            <p>
                左边抓地强，右边容易打滑。两条履带看起来都在转，但真正“推动车前进”的效果不同。
                <span>工程说法：地面给两侧履带的反作用力不同，所以车身会产生转向力矩。</span>
            </p>
        </div>
        <div class="card" data-step="structure">
            <h3>结构</h3>
            <p>
                把左右履带轴接入一个教学简化版“差值读取 + 补偿”机构：先读出 L 和 R 的差，再把差值用于纠偏。
                <span>严谨点说：普通差速器本身不会自动让两边一样；这里还需要后面的补偿机构把差值反向作用回履带。</span>
            </p>
        </div>
        <div class="card" data-step="feedback">
            <h3>反馈</h3>
            <p>
                车刚一偏，差速结构就产生反向补偿，让两侧重新接近平衡。
                <span>工程说法：反馈闭环先发生在机械结构里，计算机可以留给更复杂的判断任务。</span>
            </p>
        </div>
    </div>
</section>

<script>
const canvas = document.getElementById("labCanvas");
const ctx = canvas.getContext("2d");
const buttons = [...document.querySelectorAll("button[data-mode]")];
const cards = [...document.querySelectorAll(".card")];
const title = document.getElementById("statusTitle");
const text = document.getElementById("statusText");
const gearState = document.getElementById("gearState");
let mode = "runaway";
let dpr = 1, w = 0, h = 0, time = 0;

const modes = {
  runaway: {
    title: "第 1 步：为什么会走歪？",
    text: "俯视图里，左履带压在粗糙地面上，右履带压在光滑地面上。右侧更容易滑，左右两边推动车身的力量不同，所以小车开始偏转。",
    gear: "差值读取：未接入",
    step: "constraint"
  },
  couple: {
    title: "第 2 步：接上机械纠偏机关",
    text: "左右履带轴接入差值读取机构。注意：它不是直接把两边变一样，而是先把“差多少”读出来。",
    gear: "差值读取：已接入",
    step: "structure"
  },
  miracle: {
    title: "第 3 步：没有代码干预，也能走直",
    text: "补偿机构把差值反向作用回履带：慢的一侧得到补偿，快的一侧被约束，修正后的有效前进速度接近一致。",
    gear: "补偿输出：结构反馈",
    step: "feedback"
  }
};

function resize() {
  dpr = Math.min(window.devicePixelRatio || 1, 2);
  const rect = canvas.getBoundingClientRect();
  w = rect.width;
  h = rect.height;
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

buttons.forEach(btn => {
  btn.addEventListener("click", () => setMode(btn.dataset.mode));
});

function setMode(next) {
  mode = next;
  buttons.forEach(btn => btn.classList.toggle("active", btn.dataset.mode === mode));
  title.textContent = modes[mode].title;
  text.textContent = modes[mode].text;
  gearState.textContent = modes[mode].gear;
  cards.forEach(card => card.classList.toggle("active", card.dataset.step === modes[mode].step));
}

function roundedRect(x, y, width, height, radius, fill, stroke) {
  ctx.beginPath();
  ctx.roundRect(x, y, width, height, radius);
  if (fill) {
    ctx.fillStyle = fill;
    ctx.fill();
  }
  if (stroke) {
    ctx.strokeStyle = stroke;
    ctx.stroke();
  }
}

function drawGear(x, y, r, teeth, rot, active) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rot);
  ctx.beginPath();
  for (let i = 0; i < teeth * 2; i++) {
    const a = (Math.PI * 2 / (teeth * 2)) * i;
    const rr = i % 2 ? r * .84 : r;
    ctx.lineTo(Math.cos(a) * rr, Math.sin(a) * rr);
  }
  ctx.closePath();
  ctx.fillStyle = active ? "rgba(255,215,126,.88)" : "rgba(148,163,184,.52)";
  ctx.fill();
  ctx.strokeStyle = active ? "rgba(255,255,255,.82)" : "rgba(255,255,255,.38)";
  ctx.lineWidth = 1.2;
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, r * .34, 0, Math.PI * 2);
  ctx.fillStyle = "rgba(15,23,42,.72)";
  ctx.fill();
  ctx.restore();
}

function drawArrow(x1, y1, x2, y2, color, label) {
  const angle = Math.atan2(y2 - y1, x2 - x1);
  ctx.save();
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - Math.cos(angle - .45) * 9, y2 - Math.sin(angle - .45) * 9);
  ctx.lineTo(x2 - Math.cos(angle + .45) * 9, y2 - Math.sin(angle + .45) * 9);
  ctx.closePath();
  ctx.fill();
  if (label) {
    ctx.font = "700 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(label, (x1 + x2) / 2, (y1 + y2) / 2 - 8);
  }
  ctx.restore();
}

function drawSpeedBar(x, y, label, value, color, suffix = "") {
  ctx.save();
  ctx.fillStyle = "rgba(255,255,255,.76)";
  ctx.font = "700 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText(label, x, y);
  roundedRect(x, y + 8, 118, 8, 999, "rgba(255,255,255,.16)", null);
  roundedRect(x, y + 8, 118 * value, 8, 999, color, null);
  ctx.textAlign = "right";
  ctx.fillStyle = "rgba(255,255,255,.86)";
  ctx.fillText(`${value.toFixed(2)}${suffix}`, x + 118, y);
  ctx.restore();
}

function drawDifferentialCloseup(x, y, width, height) {
  ctx.save();
  roundedRect(x, y, width, height, 18, "rgba(15,23,42,.84)", "rgba(255,255,255,.16)");

  ctx.fillStyle = "rgba(255,255,255,.94)";
  ctx.font = "800 18px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("差值读取 + 机械补偿机构", x + 22, y + 32);
  ctx.fillStyle = "rgba(255,255,255,.62)";
  ctx.font = "500 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.fillText("严谨版：先读出左右差值，再把差值用于反向纠偏", x + 22, y + 54);

  const active = mode !== "runaway";
  const closed = mode === "miracle";
  const rawLeft = .62;
  const rawRight = 1.0;
  const delta = rawRight - rawLeft;
  const correctedLeft = closed ? .90 : mode === "couple" ? .74 : rawLeft;
  const correctedRight = closed ? .90 : mode === "couple" ? .88 : rawRight;

  drawSpeedBar(x + 22, y + height - 96, "左输入 L：粗糙侧", rawLeft, "rgba(111,170,255,.78)", "x");
  drawSpeedBar(x + width - 154, y + height - 96, "右输入 R：光滑侧", rawRight, "rgba(255,198,109,.82)", "x");
  drawSpeedBar(x + 22, y + height - 54, "修正后 L'", correctedLeft, "rgba(74,222,128,.74)", "x");
  drawSpeedBar(x + width - 154, y + height - 54, "修正后 R'", correctedRight, "rgba(74,222,128,.74)", "x");

  const cy = y + height * .52;
  const lx = x + width * .25;
  const mx = x + width * .50;
  const rx = x + width * .75;
  const rotA = time * (mode === "runaway" ? .022 : .032);
  const rotB = -time * (mode === "runaway" ? .041 : .034);
  const rotM = active ? time * .047 : time * .012;

  ctx.strokeStyle = "rgba(255,255,255,.20)";
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.moveTo(lx - 72, cy);
  ctx.lineTo(rx + 72, cy);
  ctx.stroke();

  drawGear(lx, cy, 34, 14, rotA, true);
  drawGear(rx, cy, 34, 14, rotB, true);
  drawGear(mx, cy - 44, 24, 12, -rotM, active);
  drawGear(mx, cy + 44, 24, 12, rotM, active);
  drawGear(mx, cy, 42, 16, active ? -rotM * .72 : 0, active);

  ctx.fillStyle = "rgba(255,255,255,.90)";
  ctx.font = "700 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("左履带轴 L", lx, cy + 58);
  ctx.fillText("右履带轴 R", rx, cy + 58);
  ctx.fillText(`差值 Δ = R - L = ${delta.toFixed(2)}x`, mx, cy + 88);

  roundedRect(x + 22, y + 66, width - 44, 44, 12, "rgba(255,255,255,.08)", "rgba(255,255,255,.12)");
  ctx.fillStyle = "rgba(255,255,255,.78)";
  ctx.font = "600 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("注意：差值机构不会凭空让两边相等，它只负责读出 L 和 R 的差。", x + 38, y + 92);

  if (!active) {
    ctx.setLineDash([7, 8]);
    ctx.strokeStyle = "rgba(239,68,68,.72)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(mx, cy, 62, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "rgba(255,210,210,.92)";
    ctx.font = "800 14px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
    ctx.fillText("未接入：L ≠ R，差值没有被利用", mx, y + height - 18);
  } else {
    drawArrow(lx + 42, cy - 20, mx - 44, cy - 12, "rgba(111,170,255,.86)", "左输入");
    drawArrow(rx - 42, cy + 20, mx + 44, cy + 12, "rgba(255,198,109,.88)", "右输入");
    drawArrow(mx, cy - 76, mx, cy - 118, closed ? "rgba(74,222,128,.92)" : "rgba(255,232,166,.86)", closed ? "补偿输出：L'≈R'" : "读取差值 Δ");

    ctx.fillStyle = closed ? "rgba(74,222,128,.95)" : "rgba(255,232,166,.95)";
    ctx.font = "800 14px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
    ctx.fillText(closed ? "结构反馈：修正后有效速度接近一致" : "已接入：差值开始传递，还未完全补偿", mx, y + height - 18);
  }

  ctx.restore();
}

function drawTrack(x, y, width, height, phase, side, friction) {
  roundedRect(x, y, width, height, 18, "rgba(15,23,42,.88)", "rgba(255,255,255,.18)");
  const count = 9;
  for (let i = 0; i < count; i++) {
    const px = x + 16 + ((i * 28 + phase) % (width - 28));
    roundedRect(px, y + 8, 16, height - 16, 6, side === "left" ? "rgba(111,170,255,.74)" : "rgba(255,198,109,.78)");
  }
  ctx.fillStyle = "rgba(255,255,255,.80)";
  ctx.font = "600 12px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(friction, x + width / 2, y + height + 18);
}

function drawRobot(cx, cy, angle, correction) {
  ctx.save();
  ctx.translate(cx, cy);
  ctx.rotate(angle);

  ctx.shadowBlur = 22;
  ctx.shadowColor = "rgba(0,0,0,.22)";
  roundedRect(-115, -52, 230, 104, 24, "rgba(248,250,252,.92)", "rgba(15,23,42,.18)");
  ctx.shadowBlur = 0;

  const phase = time * (mode === "runaway" ? 1.2 : .95);
  drawTrack(-132, -72, 264, 32, phase * 1.05, "left", "高摩擦");
  drawTrack(-132, 40, 264, 32, phase * (mode === "runaway" ? .62 : .95), "right", "低摩擦");

  ctx.fillStyle = "rgba(15,23,42,.78)";
  ctx.font = "700 15px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("履带机器人", 0, 5);

  const active = mode !== "runaway";
  drawGear(-38, 0, 23, 12, time * .045, active);
  drawGear(0, 0, 27, 14, -time * .038, active);
  drawGear(42, 0, 23, 12, time * .045, active);

  if (active) {
    ctx.beginPath();
    ctx.moveTo(-75, 0);
    ctx.lineTo(-61, 0);
    ctx.moveTo(61, 0);
    ctx.lineTo(75, 0);
    ctx.strokeStyle = "rgba(0,113,227,.70)";
    ctx.lineWidth = 3;
    ctx.stroke();
  }

  if (correction) {
    ctx.beginPath();
    ctx.arc(0, 0, 86, -.7, .7);
    ctx.strokeStyle = "rgba(74,222,128,.76)";
    ctx.lineWidth = 3;
    ctx.stroke();
    ctx.fillStyle = "rgba(74,222,128,.96)";
    ctx.font = "700 13px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
    ctx.fillText("物理差值自动修正", 0, -82);
  }

  ctx.restore();
}

function drawGround() {
  const split = w * .32;
  const y = h * .62;
  ctx.fillStyle = "rgba(255,255,255,.30)";
  ctx.fillRect(0, y, w * .58, h - y);
  ctx.fillStyle = "rgba(71,85,105,.15)";
  ctx.fillRect(0, y, split, h - y);
  ctx.fillStyle = "rgba(255,176,32,.12)";
  ctx.fillRect(split, y, w * .58 - split, h - y);

  ctx.strokeStyle = "rgba(15,23,42,.10)";
  ctx.setLineDash([8, 10]);
  ctx.beginPath();
  ctx.moveTo(split, y);
  ctx.lineTo(split, h);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.fillStyle = "rgba(15,23,42,.60)";
  ctx.font = "700 13px HarmonyOS Sans SC, Microsoft YaHei, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("粗糙地面", split * .5, y + 28);
  ctx.fillText("光滑地面", split + (w * .58 - split) * .5, y + 28);
}

function drawPath() {
  ctx.save();
  ctx.translate(w * .30, h * .42);
  ctx.strokeStyle = mode === "runaway" ? "rgba(239,68,68,.62)" : "rgba(74,222,128,.70)";
  ctx.lineWidth = 3;
  ctx.setLineDash([10, 10]);
  ctx.beginPath();
  if (mode === "runaway") {
    ctx.arc(0, 118, 140, -1.8, 1.2);
  } else if (mode === "couple") {
    ctx.moveTo(-170, 95);
    ctx.quadraticCurveTo(-40, 55, 150, 75);
  } else {
    ctx.moveTo(-190, 72);
    ctx.lineTo(190, 72);
  }
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.restore();
}

function draw() {
  time += 1;
  ctx.clearRect(0, 0, w, h);
  drawGround();
  drawPath();

  const baseX = w * .30;
  const baseY = h * .48;
  let angle = 0;
  let x = baseX;
  let y = baseY;
  if (mode === "runaway") {
    angle = Math.sin(time * .012) * .25 + .38;
    x += Math.sin(time * .009) * 42;
    y += Math.cos(time * .008) * 18;
  } else if (mode === "couple") {
    angle = Math.sin(time * .012) * .12;
    x += Math.sin(time * .01) * 20;
  } else {
    angle = Math.sin(time * .01) * .025;
    x += Math.sin(time * .008) * 10;
  }
  drawRobot(x, y, angle, mode === "miracle");
  drawDifferentialCloseup(w * .58, h * .13, w * .38, h * .74);

  requestAnimationFrame(draw);
}

resize();
setMode("runaway");
window.addEventListener("resize", resize);
draw();
</script>
</body>
</html>
        """,
        height=1020,
        scrolling=False,
    )


if page == "实验室总览":
    render_hero()

    c1, c2, c3 = st.columns([0.08, 10, 0.08])
    with c2:
        st.markdown("<h2 class='section-title'>概念动画：从知识边界到工程创新</h2>", unsafe_allow_html=True)
        render_knowledge_sphere_animation()

        space_data = image_as_base64("space.jpg")
        if space_data:
            st.markdown(
                f"""
                <div style="border-radius:8px; overflow:hidden; box-shadow:0 18px 42px rgba(0,0,0,0.12); height:350px;">
                    <img src="data:image/jpeg;base64,{space_data}" style="width:100%; height:100%; object-fit:cover;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("<p class='caption-text'>中国空间站：极致工程答案</p>", unsafe_allow_html=True)

        st.markdown("<h2 class='section-title'>46 位院士领航：数智化矩阵</h2>", unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown('<div class="apple-card"><h4>航空航天</h4><p>叶培建 院士<br>龙乐豪 院士</p></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="apple-card"><h4>生命科学</h4><p>刘昌胜 院士<br>陈凯先 院士</p></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="apple-card"><h4>轨道交通</h4><p>何华武 院士<br>孙永福 院士</p></div>', unsafe_allow_html=True)
        with m4:
            st.markdown('<div class="apple-card"><h4>人工智能</h4><p>王天然 院士<br>吴志强 院士</p></div>', unsafe_allow_html=True)

        st.markdown("<h2 class='section-title'>具身智能数字化资产解构</h2>", unsafe_allow_html=True)
        robot_data = image_as_base64("robot.jpg")
        if robot_data:
            st.markdown(
                f"""
                <div style="border-radius:8px; overflow:hidden; box-shadow:0 18px 42px rgba(0,0,0,0.12); height:320px;">
                    <img src="data:image/jpeg;base64,{robot_data}" style="width:100%; height:100%; object-fit:cover;">
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div class="apple-card" style="background: white;">
                <h3 style="margin-top:0;">数字化交付标准 (SOP)</h3>
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="border-bottom: 2px solid #f5f5f7;">
                        <th style="text-align:left; padding:12px;">维度</th>
                        <th style="text-align:left; padding:12px; color:#0071e3;">方案</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #f5f5f7;">
                        <td style="padding:12px;"><b>资产解构</b></td>
                        <td style="padding:12px;">院士思维 → 数字化指令集</td>
                    </tr>
                    <tr>
                        <td style="padding:12px;"><b>表现形式</b></td>
                        <td style="padding:12px;">静态图文 → 毫秒级数字资产</td>
                    </tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page == "概念动画馆":
    st.markdown("<h1 style='text-align:center;'>概念动画馆</h1>", unsafe_allow_html=True)
    render_knowledge_sphere_animation()
    st.markdown(
        """
        <div class="principle-grid">
            <div class="principle-card">
                <h3>问题边界</h3>
                <p>用“知识之圆”告诉孩子：问题不是失败，而是认知边界正在扩张。</p>
            </div>
            <div class="principle-card">
                <h3>跨学科连接</h3>
                <p>用“跨界连接”展示创新发生的瞬间：不同工程系统之间出现新的连接路径。</p>
            </div>
            <div class="principle-card">
                <h3>工程落点</h3>
                <p>每个酷炫动画都要回到一个可拆解、可实验、可复现的怎么办。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "虚拟实验室":
    st.markdown("<h1 style='text-align:center;'>虚拟实验室</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#667085; font-size:18px;'>第一件实验器材：指南车差速模型。用结构处理偏差，用物理反馈挑战“智能必须依赖昂贵算力”的偏见。</p>",
        unsafe_allow_html=True,
    )
    render_chariot_virtual_lab()

else:
    st.markdown("<h1 style='text-align:center;'>指南车：物理级稳态资产模型</h1>", unsafe_allow_html=True)
    cl, cr = st.columns(2)
    with cl:
        st.markdown(
            '<div class="apple-card"><h3>实体构筑逻辑</h3><p>解决底盘稳态问题：不先依赖算力，而让硬件结构自动抵消偏转。</p></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="apple-card"><h3>可迁移启发</h3><p>凡是高频、刚性、延迟敏感的控制问题，都值得先问：能不能把一部分智能写进结构？</p></div>',
            unsafe_allow_html=True,
        )
    with cr:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/6/6a/South-pointing_chariot_gearing.png",
            caption="差速齿轮组模型",
            use_container_width=True,
        )

st.markdown(
    "<p style='text-align:center; color:gray; font-size:12px;'><br>© 2026 少儿社数智化实验室 | 主理人：刘婧</p>",
    unsafe_allow_html=True,
)
