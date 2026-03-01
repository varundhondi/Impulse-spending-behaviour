import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Financial Impulse Behaviour Analytics",
    page_icon="💳",
    layout="wide"
)

# -------------------- LOAD DATA --------------------
df = pd.read_csv("final_user_behaviour_output.csv")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.metric-card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #22c55e;
}
.metric-title {
    color: #9ca3af;
    font-size: 14px;
}
.metric-value {
    font-size: 32px;
    font-weight: bold;
    color: white;
}
.section-card {
    background-color: #0f172a;
    padding: 25px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("💸 Financial Impulse Behaviour Detection")
st.caption(
    "Behavioural analytics system to identify impulsive spending patterns, "
    "explain risk drivers, and recommend preventive actions."
)

st.markdown("---")

# -------------------- USER SELECT --------------------
user_id = st.selectbox("👤 Select User", sorted(df['user_id'].unique()))
user = df[df['user_id'] == user_id].iloc[0]

# -------------------- KPI CARDS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Impulse Risk Score</div>
            <div class="metric-value">{int(user['impulse_risk_score'])}/100</div>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card" style="border-left-color:#3b82f6;">
            <div class="metric-title">Risk Level</div>
            <div class="metric-value">{user['risk_level']}</div>
        </div>
        """, unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card" style="border-left-color:#eab308;">
            <div class="metric-title">Behaviour Profile</div>
            <div class="metric-value">{user['behaviour_profile']}</div>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("---")

# -------------------- TABS --------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🧠 Behaviour Insights",
    "📊 Risk Analysis",
    "✅ Recommendations",
    "🌍 Population Comparison"
])

# -------------------- TAB 1 --------------------
with tab1:
    st.subheader("Why this user is at risk")

    st.markdown(
        f"""
        <div class="section-card">
            <b>Key Behavioural Triggers:</b><br><br>
            {user['risk_explanation']}
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("### What this means")
    st.write(
        "These behavioural signals indicate impulse-driven decision making, "
        "often influenced by emotional states, convenience, and timing triggers."
    )

# -------------------- TAB 2 --------------------
with tab2:
    st.subheader("Risk Score Breakdown")

    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(df['impulse_risk_score'], bins=25, alpha=0.8)
    ax.axvline(user['impulse_risk_score'], linestyle='--', linewidth=2)
    ax.set_xlabel("Impulse Risk Score")
    ax.set_ylabel("Number of Users")
    ax.set_title("User Risk Position in Population")

    st.pyplot(fig)

    percentile = int(
        (df['impulse_risk_score'] < user['impulse_risk_score']).mean() * 100
    )

    st.info(f"📌 This user is riskier than **{percentile}%** of the population.")

# -------------------- TAB 3 --------------------
with tab3:
    st.subheader("Personalized Preventive Actions")

    st.success(user['recommendation'])

    st.markdown("### Why interventions matter")
    st.write(
        "Early nudges help reduce long-term financial stress by interrupting "
        "impulsive decision loops before they become habits."
    )

# -------------------- TAB 4 --------------------
with tab4:
    st.subheader("How this user compares to others")

    avg_risk = int(df['impulse_risk_score'].mean())

    col1, col2 = st.columns(2)
    col1.metric("User Risk Score", int(user['impulse_risk_score']))
    col2.metric("Average Population Risk", avg_risk)

    st.markdown(
        "This comparison helps institutions or users understand whether "
        "the behaviour is isolated or part of a broader trend."
    )

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption(
    "⚠️ Ethical Note: This system provides assistive insights based on behavioural patterns. "
    "It does not judge intent or enforce restrictions."
)