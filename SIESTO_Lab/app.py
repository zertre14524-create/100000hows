import streamlit as st
import os
import base64

# 1. 基础配置
st.set_page_config(page_title="SIESTO Lab | 十万个怎么办", layout="wide")

# 2. 视觉引擎：黑金、流光、毛玻璃
st.markdown("""
<style>
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    @keyframes glow-pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 0.6; } }

    .stApp { background: #000 !important; color: #fff !important; }

    /* 首屏引擎容器 */
    .knowledge-engine {
        position: relative;
        height: 650px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background: radial-gradient(circle at center, #0a1d37 0%, #000 85%);
    }

    .discipline-tag {
        position: absolute;
        font-family: sans-serif;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
        padding: 8px 18px;
        border: 1px solid rgba(0, 113, 227, 0.4);
        border-radius: 20px;
        background: rgba(0, 113, 227, 0.1);
        backdrop-filter: blur(8px);
        animation: float 4s infinite ease-in-out;
        z-index: 20;
    }

    .apple-card {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 35px;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.5s ease;
        animation: fadeInUp 0.8s ease-out backwards;
    }
    .apple-card:hover {
        transform: translateY(-8px);
        border-color: #0071e3;
        box-shadow: 0 20px 40px rgba(0, 113, 227, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 首屏：【知识之圆与搭线引擎】 ---
# 这里完美嵌入了你刚才调整的 HTML 逻辑
st.markdown("""
<div class="knowledge-engine">
    <div style="position:absolute; width:450px; height:450px; border-radius:50%; border:1px solid rgba(0,113,227,0.2); animation: glow-pulse 5s infinite alternate;"></div>
    
    <div class="discipline-tag" style="top: 200px; left: 25%; animation-delay: 0s;">机械工程</div>
    <div class="discipline-tag" style="top: 350px; left: 30%; animation-delay: 0.5s;">电子信息</div>
    <div class="discipline-tag" style="top: 150px; left: 50%; animation-delay: 1s;">人工智能</div>
    <div class="discipline-tag" style="top: 450px; left: 45%; animation-delay: 1.5s;">材料科学</div>
    <div class="discipline-tag" style="top: 280px; left: 65%; animation-delay: 2s;">自动化</div>
    <div class="discipline-tag" style="top: 400px; left: 70%; animation-delay: 2.5s;">航空航天</div>

    <svg viewBox="0 0 1000 600" style="position:absolute; width:100%; height:100%; pointer-events:none; z-index:5;">
        <defs>
            <linearGradient id="flowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#0071e3; stop-opacity:0" />
                <stop offset="50%" style="stop-color:#0071e3; stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ffd700; stop-opacity:1" />
            </linearGradient>
            <filter id="blurFilter"><feGaussianBlur stdDeviation="3"/></filter>
        </defs>
        <path d="M 500 300 Q 700 100 900 300" stroke="url(#flowGrad)" stroke-width="2" fill="none" stroke-dasharray="1000" stroke-dashoffset="1000">
            <animate attributeName="stroke-dashoffset" from="1000" to="0" dur="3s" repeatCount="indefinite" />
        </path>
        <path d="M 500 300 Q 700 500 900 300" stroke="url(#flowGrad)" stroke-width="2" fill="none" stroke-dasharray="1000" stroke-dashoffset="1000">
            <animate attributeName="stroke-dashoffset" from="1000" to="0" dur="4s" repeatCount="indefinite" />
        </path>
    </svg>

    <div style="z-index: 10; text-align: center;">
        <h1 style="font-size: 72px; letter-spacing: -2px; margin-bottom:0; font-weight:700;">SIESTO 十万个怎么办</h1>
        <p style="font-size: 22px; color: #86868b; font-weight: 200; margin-top:15px; max-width:800px;">
            认知越大，未知越大 | <span style="color:#0071e3;">创新就是搭线</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. 核心资产区 ---
st.markdown("<br>", unsafe_allow_html=True)
main_col_l, main_col_r, main_col_last = st.columns([0.1, 10, 0.1])

with main_col_r:
    # 院士矩阵
    st.markdown("<h2 style='text-align:center;'>46 位院士领航：从思维点到工程线</h2>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="apple-card"><h4>航空航天</h4><p style="color:#86868b;">叶培建 院士<br>龙乐豪 院士</p></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="apple-card"><h4>生命健康</h4><p style="color:#86868b;">刘昌胜 院士<br>陈凯先 院士</p></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="apple-card"><h4>轨道交通</h4><p style="color:#86868b;">何华武 院士<br>孙永福 院士</p></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="apple-card"><h4>人工智能</h4><p style="color:#86868b;">王天然 院士<br>吴志强 院士</p></div>', unsafe_allow_html=True)

    st.divider()

    # 天宫成果
    t_col1, t_col2 = st.columns([1.5, 1])
    with t_col1:
        if os.path.exists("space.jpg"):
            with open("space.jpg", "rb") as f: s_data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div style="border-radius:24px; overflow:hidden; border:1px solid #333;"><img src="data:image/jpeg;base64,{s_data}" style="width:100%; height:420px; object-fit:cover;"></div>', unsafe_allow_html=True)
    with t_col2:
        st.markdown('<div class="apple-card" style="height:420px;"><h3>🚀 天宫资产封存</h3><p style="color:#a1a1a6; line-height:1.8;">中国空间站是 18 个战略方向中“怎么办”的极致答案。通过数智化资产封存，我们将复杂的工程指令转化为可复现的数字回放。</p><h4 style="color:#0071e3;">→ 已封存 320 项工程 SOP</h4></div>', unsafe_allow_html=True)

    st.divider()

    # 指南车案例
    st.markdown("<h2 style='text-align:center;'>突破案例：指南车物理对冲</h2>", unsafe_allow_html=True)
    cl, cr = st.columns(2)
    with cl:
        st.markdown('<div class="apple-card" style="min-height:420px;"><h3>📜 实体构筑：物理级稳态</h3><p>解决底盘稳态死穴：不靠大脑，靠身体。搭线好了，突破就发生了。</p><ul><li><b>找差值</b>：齿轮捕捉位移偏差。</li><li><b>反向掰</b>：自动抵消偏航。</li></ul><p style="color:#ffd700; font-weight:bold;">结论：底层稳态应由硬件实现。</p></div>', unsafe_allow_html=True)
    with cr:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/South-pointing_chariot_gearing.png", caption="指南车差速齿轮组：物理搭线突破")

    st.divider()

    # SOP 表格
    st.markdown("""
        <div class="apple-card" style="background:#ffffff !important; color:#000000 !important;">
            <h3 style="color:#000000 !important; margin-top:0;">数字化交付标准 (SOP)</h3>
            <table style="width:100%; border-collapse: collapse; color:#333;">
                <tr style="border-bottom: 2px solid #eee;"><th style="padding:15px; text-align:left;">维度</th><th style="padding:15px; text-align:left; color:#0071e3;">模型网站（How / 怎么办）</th></tr>
                <tr style="border-bottom: 1px solid #eee;"><td style="padding:15px;">表现形式</td><td style="padding:15px; color:#0071e3;">交互式 3D / 物理逻辑回放</td></tr>
                <tr><td style="padding:15px;">知识密度</td><td style="padding:15px; color:#0071e3;">毫秒级数字化工程资产</td></tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#424245; font-size:12px;'><br>© 2026 SIESTO Lab | 主理人：刘婧</p>", unsafe_allow_html=True)