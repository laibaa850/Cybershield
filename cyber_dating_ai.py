import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random

st.set_page_config(page_title="AI Cyber Love Shield", layout="wide")

# -----------------------------
# 🎨 CYBER UI + HEARTS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f0c29,#302b63,#24243e);
    color:white;
    overflow-x:hidden;
}

/* Floating Hearts */
.heart {
    position: fixed;
    font-size: 30px;
    animation: float 8s infinite ease-in-out;
    opacity: 0.6;
    z-index: 0;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-40px);}
    100% {transform: translateY(0px);}
}

/* Title Gradient */
h1 {
    text-align:center;
    font-size:3rem;
    background: linear-gradient(90deg,#ff416c,#ff4b2b);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* Glass Card */
.glass {
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter:blur(12px);
    box-shadow:0 0 20px rgba(255,0,120,0.3);
    margin-bottom:20px;
}

/* Button */
div.stButton > button {
    background:linear-gradient(45deg,#ff004f,#ff7eb3);
    color:white;
    font-weight:bold;
    border-radius:12px;
    height:3em;
    width:100%;
}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# Add floating hearts randomly
for _ in range(12):
    left = random.randint(0, 100)
    top = random.randint(0, 100)
    st.markdown(
        f"<div class='heart' style='left:{left}%; top:{top}%;'>❤️</div>",
        unsafe_allow_html=True
    )

# -----------------------------
# 🛡 TITLE
# -----------------------------
st.markdown("<h1>🛡 AI Cyber Love Shield</h1>", unsafe_allow_html=True)
st.markdown("<center>Advanced Multi-Layer Romance Scam Intelligence System</center>", unsafe_allow_html=True)
st.write("")

# -----------------------------
# 🧾 INPUT PANEL
# -----------------------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

bio = st.text_area("💬 Profile Bio")

messages_per_day = st.slider("📩 Messages Per Day", 0, 200, 20)
links_shared = st.slider("🔗 Links Shared", 0, 20, 0)

reply_time_avg = st.slider("⏱ Avg Reply Time (seconds)", 1, 600, 60)
reply_variance = st.slider("📊 Reply Time Variance", 0, 300, 50)
night_activity = st.slider("🌙 Night Activity %", 0, 100, 20)

account_age = st.slider("📅 Account Age (days)", 0, 365, 30)
verified = st.selectbox("✅ Verified?", ["Yes","No"])
photos = st.slider("📸 Number of Photos", 0, 10, 3)

vpn_probability = st.slider("🌐 VPN Probability %", 0, 100, 10)
geo_mismatch = st.selectbox("📍 Geo Mismatch?", ["No","Yes"])

love_bomb_score = st.slider("❤️ Love Bombing Score", 0, 100, 20)
financial_intent = st.slider("💰 Financial Intent Probability %", 0, 100, 10)

analyze = st.button("🚀 Run Full Threat Analysis")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 🧠 RISK ENGINE
# -----------------------------
def compute_scores():

    identity = 0
    if account_age < 7: identity += 40
    if verified == "No": identity += 30
    if photos < 2: identity += 30

    behavioral = 0
    if messages_per_day > 120: behavioral += 30
    if reply_variance < 10: behavioral += 30
    if night_activity > 70: behavioral += 20
    if links_shared > 5: behavioral += 20

    emotional = (love_bomb_score * 0.6 + financial_intent * 0.4)

    network = 0
    if vpn_probability > 60: network += 50
    if geo_mismatch == "Yes": network += 50

    normal_mean = 30
    user_behavior = (messages_per_day + night_activity + links_shared) / 3
    anomaly = abs(user_behavior - normal_mean) * 2

    identity = min(identity,100)
    behavioral = min(behavioral,100)
    emotional = min(emotional,100)
    network = min(network,100)
    anomaly = min(anomaly,100)

    return identity, behavioral, emotional, network, anomaly

# -----------------------------
# 📊 DASHBOARD OUTPUT
# -----------------------------
if analyze:

    identity, behavioral, emotional, network, anomaly = compute_scores()
    final_risk = np.mean([identity, behavioral, emotional, network, anomaly])
    trust_score = 100 - final_risk

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("📊 Threat Intelligence Dashboard")

    categories = ['Identity','Behavior','Emotional','Network','Anomaly']
    values = [identity, behavioral, emotional, network, anomaly]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,100])),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.bar_chart({
        "Risk Layer Score": values
    })

    st.metric("🛡 Final Trust Score", f"{round(trust_score,1)}%")
    st.progress(int(final_risk))

    if trust_score > 75:
        st.success("Low Behavioral Risk Detected")
    elif trust_score > 45:
        st.warning("Moderate Risk Indicators Present")
    else:
        st.error("High Manipulation & Scam Risk Detected")

    # Explainability (NO EMPTY SPACE NOW)
    st.subheader("🔎 Key Risk Indicators")

    indicators = []
    if identity > 60: indicators.append("Identity inconsistencies detected")
    if behavioral > 60: indicators.append("Bot-like messaging or link spam pattern")
    if emotional > 60: indicators.append("Rapid emotional escalation detected")
    if network > 60: indicators.append("Suspicious VPN / Geo activity")
    if anomaly > 60: indicators.append("Behavior deviates from normal baseline")

    if indicators:
        for item in indicators:
            st.write(f"• {item}")
    else:
        st.write("No major red flags detected. Profile behavior appears stable.")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 👩‍💻 FOOTER
# -----------------------------
st.write("")
st.markdown(
    "<center style='opacity:0.6;'>Created by Laiba 💖</center>",
    unsafe_allow_html=True
)
