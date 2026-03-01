# Financial Impulse Behaviour Detection

## Problem Statement
Young adults often engage in impulsive spending driven by emotional, timing-based,
and convenience-related triggers. This project applies behavioural analytics to
detect impulsive spending patterns and assess financial risk.

---

## Dataset Description

### Dataset Type
Synthetic (Simulated)

### Why Synthetic Data?
Real-world financial transaction data is highly sensitive and not publicly
available due to privacy and regulatory constraints. To ensure ethical compliance
while still modelling realistic behavioural patterns, a synthetic dataset was
generated.

### Dataset Generation Method
The dataset was generated using rule-based simulation with probabilistic
distributions to mimic real-world spending behaviour.

Key assumptions:
- Higher spending frequency during late-night hours indicates impulsive behaviour
- Salary-day and month-end periods show spending surges
- Mobile and online transactions increase impulsivity
- UPI-based payments reduce friction and increase impulse buying

### Number of Records
- ~45,000 transactions
- 300 users
- 6 months of simulated activity

### Features Description
| Feature | Description |
|------|------------|
| user_id | Unique user identifier |
| timestamp | Transaction date and time |
| amount | Transaction value |
| category | Merchant category |
| payment_mode | UPI, Credit Card, Debit Card, Wallet |
| merchant_type | Online or Offline |
| device_type | Mobile or Desktop |
| location_type | Home or Outside |
| is_salary_day | Binary indicator of salary period |
| engineered features | Late-night ratio, spend variance, frequency spikes |

---

## Behavioural Feature Engineering
Behavioural indicators were aggregated at user level, including:
- Late-night spending ratio
- Month-end spending intensity
- Salary-day spending ratio
- Mobile + online purchase bias
- Payment friction (UPI usage)
- Spending variability (standard deviation)

---

## Model & Scoring Approach
A weighted, explainable rule-based behavioural scoring model was used to compute
an Impulse Risk Score (0–100). Continuous weights allow proportional risk scaling
based on behavioural intensity.

---

## Output
- Impulse Risk Score
- Risk Level (Low / Medium / High)
- Behaviour Profile
- Behavioural explanations
- Personalized preventive recommendations

---

## Deployment
The solution is deployed using Streamlit Cloud and hosted via GitHub for real-time
interaction.

---

## Ethical Considerations
- No real user data was used
- Behavioural indicators represent risk, not intent
- Recommendations are assistive, not restrictive
