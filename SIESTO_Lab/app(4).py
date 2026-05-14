import streamlit as st
import os
import base64
import time

# 1. 基础配置
st.set_page_config(page_title="SIESTO Lab", layout="wide")

# 2. 视觉引擎（复刻你最喜欢的 Apple 级动效）
st.markdown("""
<style>
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    .stApp { background-color: white !important; color: #1d1d1f !important; }
    .apple-card {
        background-color: #f5f5f7 !important;
        color: #1d1d1f !important;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 20px;
        border: 1px solid #e5e5e7;
        transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
        animation: fadeInUp 0.8s ease-out backwards;
    }
    .apple-card:hover {
        transform: translateY(-10px);
        border-color: #0071e3 !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1) !important;
    }
    h1, h2, h3, h4, p, span, div { color: #1d1d1f !important; }
    .caption-text { text-align: center; color: #86868b !important; font-size: 14px; display: block; }
</style>
""", unsafe_allow_html=True)

# --- 3. 边框导航（侧边栏）：AI 助理常驻这里 ---
with st.sidebar:
    st.markdown("## 🤖 SIESTO AI 助理")
    st.caption("基于《实体构筑》资产包实时驱动")
    
    # AI 对话交互界面
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "你好，刘婧主理人。我已准备好解构具身智能的工程逻辑。"}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("询问工程逻辑..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # 这里的回答逻辑严格参考你提供的文档 [cite: 7, 8, 11, 30, 40]
            if "指南车" in prompt:
                response = "指南车是通过离合齿轮组捕捉左右轮路程差（微分平衡） ，并反向强迫手臂旋转（差速控制）来抵消位移的 [cite: 8]。它证明了最底层的平衡不该占用算力，而应靠硬件实现物理对齐 。"
            elif "死穴" in prompt or "本能" in prompt:
                response = "具身智能的‘本能’资产（如指南车或人形玩偶）解决了高频动作可靠性死穴 [cite: 30]。它强调救命的本能应直接刻在关节结构里，实现零延迟的‘肌肉反射’ [cite: 30, 40]。"
            else:
                response = "这是一个深刻的工程问题。我们需要从‘实体构筑’出发，拆解其物理对冲逻辑 [cite: 9, 10]。"
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.divider()
    page = st.radio("切换内容板块", ["实验室总览", "指南车专题模型"])

# --- 4. 主内容区 ---
if page == "实验室总览":
    # --- 第一屏：Logo ---
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
        logo_file = next((f for f in os.listdir('.') if 'logo' in f.lower()), None)
        if logo_file: st.image(logo_file, use_container_width=True)
        else: st.title("SIESTO 十万个怎么办")
        st.markdown("<p style='text-align:center; font-size:20px; font-weight:300;'>从“为什么”到“怎么办”的科创范式革命</p>", unsafe_allow_html=True)

    st.divider()
    c1, c2, c3 = st.columns([0.1, 10, 0.1])
    with c2:
        # 1. 空间站
        if os.path.exists("space.jpg"):
            with open("space.jpg", "rb") as f: s_data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div style="border-radius:24px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1); height:350px;"><img src="data:image/jpeg;base64,{s_data}" style="width:100%; height:100%; object-fit:cover;"></div>', unsafe_allow_html=True)
        st.markdown("<p class='caption-text'>中国空间站：极致工程答案 </p>", unsafe_allow_html=True)

        # 2. 院士矩阵
        st.markdown("<br><h2 style='text-align: center;'>46 位院士领航：数智化矩阵</h2>", unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="apple-card"><h4>航空航天</h4><p>叶培建 院士<br>龙乐豪 院士</p></div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="apple-card"><h4>生命科学</h4><p>刘昌胜 院士<br>陈凯先 院士</p></div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="apple-card"><h4>轨道交通</h4><p>何华武 院士<br>孙永福 院士</p></div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="apple-card"><h4>人工智能</h4><p>王天然 院士<br>吴志强 院士</p></div>', unsafe_allow_html=True)

        # 3. 具身智能目录
        st.markdown("<br><h2 style='text-align: center;'>具身智能数字化资产解构</h2>", unsafe_allow_html=True)
        if os.path.exists("robot.jpg"):
            with open("robot.jpg", "rb") as f: r_data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div style="border-radius:24px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1); height:320px;"><img src="data:image/jpeg;base64,{r_data}" style="width:100%; height:100%; object-fit:cover;"></div>', unsafe_allow_html=True)

        # 4. SOP 表格
        st.markdown("""
        <div class="apple-card" style="background: white;">
            <h3 style="margin-top:0;">数字化交付标准 (SOP)</h3>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="border-bottom: 2px solid #f5f5f7;"><th style="text-align:left; padding:12px;">维度</th><th style="text-align:left; padding:12px; color:#0071e3;">方案</th></tr>
                <tr style="border-bottom: 1px solid #f5f5f7;"><td><b>资产解构</b></td><td>院士思维 → 数字化指令集 [cite: 19]</td></tr>
                <tr><td><b>表现形式</b></td><td>静态图文 → 毫秒级数字资产 </td></tr>
            </table>
        </div>""", unsafe_allow_html=True)

else:
    # --- 指南车模型页 ---
    st.markdown("<h1 style='text-align:center;'>🏯 指南车：物理级稳态资产模型</h1>", unsafe_allow_html=True)
    cl, cr = st.columns(2)
    with cl:
        st.markdown('<div class="apple-card"><h3>📜 实体构筑逻辑</h3><p>解决底盘稳态死穴：不靠算力，靠硬件自动抵消 。</p></div>', unsafe_allow_html=True)
    with cr:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/South-pointing_chariot_gearing.png", caption="差速齿轮组模型 [cite: 10]")

st.markdown("<p style='text-align:center; color:gray; font-size:12px;'><br>© 2026 少儿社数智化实验室 | 主理人：刘婧</p>", unsafe_allow_html=True)