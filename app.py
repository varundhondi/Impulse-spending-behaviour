import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Financial Impulse Behaviour Analytics",
    layout="centered"
)

st.title("💸 Financial Impulse Behaviour Detection")

st.markdown("""
This dashboard analyzes spending behaviour to detect impulsive patterns,
explain behavioural triggers, and provide personalized recommendations.
""")

# Load data
df = pd.read_csv("final_user_behaviour_output.csv")

# User selector
user_id = st.selectbox(
    "Select User ID",
    sorted(df['user_id'].unique())
)

user = df[df['user_id'] == user_id].iloc[0]

# Risk score
st.subheader("📊 Impulse Risk Score")
st.metric(
    label="Risk Score",
    value=int(user['impulse_risk_score']),
    delta=f"Risk Level: {user['risk_level']}"
)

# Behaviour profile
st.subheader("🧠 Behaviour Profile")
st.info(user['behaviour_profile'])

# Explanation
st.subheader("🔍 Why this user is at risk?")
st.write(user['risk_explanation'])

# Recommendation
st.subheader("✅ Personalized Recommendation")
st.success(user['recommendation'])

# Distribution plot
st.subheader("📈 Risk Score Distribution")

fig, ax = plt.subplots()
ax.hist(df['impulse_risk_score'], bins=20)
ax.axvline(user['impulse_risk_score'], linestyle='--')
ax.set_xlabel("Impulse Risk Score")
ax.set_ylabel("Users")

st.pyplot(fig)

st.caption("Behavioural Analytics Hackathon Project") 