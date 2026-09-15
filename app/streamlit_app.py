from pathlib import Path
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TX = pd.read_csv(ROOT / "data/processed/transactions_enriched.csv")
ALERTS = pd.read_csv(ROOT / "data/processed/fraud_alerts.csv")
RISK = pd.read_csv(ROOT / "data/processed/customer_fraud_risk.csv")

st.set_page_config(
    page_title="Fraud Pattern Detection",
    layout="wide"
)

st.title("Fraud & Suspicious Transaction Pattern Detection")
st.caption(
    "Synthetic portfolio project | A simple view of suspicious patterns, customer risk, "
    "fraud exposure, confirmed fraud, and recommended investigation actions."
)

with st.sidebar:
    st.header("Filters")
    st.caption("Use the dropdowns below to filter the dashboard.")

    pattern_options = ["All"] + sorted(
        ALERTS.detected_pattern.dropna().astype(str).unique().tolist()
    )
    selected_pattern_filter = st.selectbox(
        "Pattern",
        pattern_options,
        index=0,
        key="sidebar_pattern_filter"
    )

    channel_options = ["All"] + sorted(
        ALERTS.channel.dropna().astype(str).unique().tolist()
    )
    selected_channel_filter = st.selectbox(
        "Channel",
        channel_options,
        index=0,
        key="sidebar_channel_filter"
    )

    risk_score_options = ["All", "40+", "50+", "60+", "70+", "80+", "90+"]
    selected_risk_score = st.selectbox(
        "Minimum Risk Score",
        risk_score_options,
        index=0,
        key="sidebar_risk_filter"
    )

f = ALERTS.copy()

if selected_pattern_filter != "All":
    f = f[
        f.detected_pattern.astype(str).eq(selected_pattern_filter)
    ]

if selected_channel_filter != "All":
    f = f[
        f.channel.astype(str).eq(selected_channel_filter)
    ]

if selected_risk_score != "All":
    min_score = int(selected_risk_score.replace("+", ""))
    f = f[
        pd.to_numeric(f.fraud_risk_score, errors="coerce").fillna(0) >= min_score
    ]

# -------------------------
# Portfolio KPIs
# -------------------------
fraud_alerts = len(f)
high_critical = f.risk_level.isin(["High", "Critical"]).sum() if fraud_alerts else 0
flagged_customers = f.customer_id.nunique() if fraud_alerts else 0
flagged_exposure = float(f.amount.sum()) if fraud_alerts else 0.0
confirmed_fraud = (f.disposition == "Confirmed Fraud").sum() if fraud_alerts else 0

high_critical_pct = (high_critical / fraud_alerts * 100) if fraud_alerts else 0.0
confirmed_rate = (confirmed_fraud / fraud_alerts * 100) if fraud_alerts else 0.0

# -------------------------
# Portfolio decision logic
# -------------------------
def get_portfolio_status():
    signals = 0

    if high_critical_pct >= 30:
        signals += 1
    if confirmed_fraud > 0:
        signals += 1
    if flagged_exposure >= 1_000_000:
        signals += 1

    if signals >= 3:
        return (
            "Heightened Fraud Risk",
            "The selected alert population shows elevated fraud risk, confirmed fraud activity, and material exposure."
        )
    elif signals >= 1:
        return (
            "Targeted Investigation Required",
            "Some alerts or customers require deeper review, although risk is not elevated across the entire portfolio."
        )
    else:
        return (
            "Routine Monitoring",
            "The selected population does not show a broad concentration of severe fraud indicators."
        )

portfolio_status, portfolio_message = get_portfolio_status()

# -------------------------
# Executive summary
# -------------------------
st.subheader("Executive Summary")

if fraud_alerts == 0:
    st.warning("No fraud alerts match the selected filters.")
else:
    s1, s2, s3 = st.columns([1.2, 1.0, 2.8])

    with s1:
        st.metric("Portfolio Status", portfolio_status)

    with s2:
        st.metric("Confirmed Fraud", f"{confirmed_fraud:,}")

    with s3:
        st.info(portfolio_message)

    st.markdown(
        f"""
        The selected view contains **{fraud_alerts:,} fraud alerts**
        across **{flagged_customers:,} customer(s)**. **{high_critical_pct:.1f}%** of alerts are
        High or Critical risk. The total flagged transaction exposure is approximately
        **${flagged_exposure/1e6:.1f}M**, and **{confirmed_fraud:,} alert(s)** were confirmed as fraud.
        """
    )

    st.markdown("#### What this means")

    insights = []

    if high_critical_pct >= 30:
        insights.append(
            "A significant share of the alert population is High/Critical risk, so investigator resources should be concentrated there first."
        )
    else:
        insights.append(
            "High/Critical alerts are present but do not dominate the selected population."
        )

    if confirmed_fraud > 0:
        insights.append(
            f"{confirmed_fraud} confirmed-fraud alert(s) show that suspicious behavior in the portfolio has already produced validated fraud outcomes."
        )

    if flagged_exposure > 0:
        insights.append(
            f"Approximately ${flagged_exposure:,.0f} in transaction value is associated with the selected fraud alerts."
        )

    if len(f):
        top_pattern = f.detected_pattern.value_counts().index[0]
        top_channel = f.channel.value_counts().index[0]
        insights.append(
            f"The most common suspicious pattern is **{top_pattern}**, and the most frequently involved channel is **{top_channel}**."
        )

    for item in insights:
        st.write(f"• {item}")

    st.markdown("#### Final Portfolio Decision")

    if portfolio_status == "Heightened Fraud Risk":
        st.error(
            "Prioritize High/Critical alerts, confirmed-fraud cases, and high-value exposures for immediate investigation. "
            "Review the most common fraud patterns and channels for recurring control weaknesses."
        )
    elif portfolio_status == "Targeted Investigation Required":
        st.warning(
            "Continue routine monitoring across the broader portfolio, but investigate the highest-risk alerts, "
            "repeat suspicious patterns, and customers with elevated fraud scores."
        )
    else:
        st.success(
            "Maintain normal fraud monitoring. No broad portfolio-level escalation is indicated by the selected alerts."
        )

st.divider()

# -------------------------
# KPI scorecard
# -------------------------
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Fraud Alerts", f"{fraud_alerts:,}")
c2.metric("High/Critical", f"{high_critical:,}")
c3.metric("Flagged Customers", f"{flagged_customers:,}")
c4.metric("Flagged Exposure", f"${flagged_exposure/1e6:.1f}M")
c5.metric("Confirmed Fraud", f"{confirmed_fraud:,}")

# -------------------------
# Customer-level explanation
# -------------------------
st.subheader("Customer Fraud Decision Summary")

available_customers = RISK.sort_values(
    "customer_fraud_score",
    ascending=False
).customer_id.tolist()

selected_customer = st.selectbox(
    "Select a customer to understand the fraud risk",
    available_customers
)

r = RISK[RISK.customer_id == selected_customer].iloc[0]

customer_tx = TX[TX.customer_id == selected_customer].copy()
customer_alerts = ALERTS[ALERTS.customer_id == selected_customer].copy()

a, b, c, d = st.columns(4)
a.metric("Customer Fraud Score", int(r.customer_fraud_score))
b.metric("Risk Level", r.customer_risk_level)
c.metric("Flagged Transactions", int(r.flagged_transactions))
d.metric("Flag Rate", f"{r.flag_rate:.1%}")

st.markdown("#### Why this customer matters")

reasons = [
    f"The customer has a fraud risk score of **{int(r.customer_fraud_score)}** and is classified as **{r.customer_risk_level} risk**.",
    f"There are **{int(r.flagged_transactions)} flagged transaction(s)** with a flag rate of **{r.flag_rate:.1%}**."
]

if len(customer_alerts):
    top_pattern_customer = customer_alerts.detected_pattern.value_counts().index[0]
    top_channel_customer = customer_alerts.channel.value_counts().index[0]
    confirmed_customer = (customer_alerts.disposition == "Confirmed Fraud").sum()

    reasons.append(
        f"The most common suspicious pattern for this customer is **{top_pattern_customer}** through the **{top_channel_customer}** channel."
    )

    if confirmed_customer > 0:
        reasons.append(
            f"**{confirmed_customer} alert(s)** for this customer were confirmed as fraud."
        )

st.write(" ".join(reasons))

st.markdown("#### Final Customer Decision")

confirmed_customer = (
    (customer_alerts.disposition == "Confirmed Fraud").sum()
    if len(customer_alerts)
    else 0
)

if r.customer_risk_level in ["High", "Critical"] and confirmed_customer > 0:
    st.error(
        "Decision: **PRIORITY FRAUD INVESTIGATION**. The customer combines elevated fraud risk with confirmed fraud activity and should receive immediate investigator attention."
    )
elif r.customer_risk_level in ["High", "Critical"]:
    st.warning(
        "Decision: **ENHANCED FRAUD REVIEW**. The customer's elevated fraud score supports deeper investigation even if fraud has not yet been confirmed."
    )
elif confirmed_customer > 0:
    st.warning(
        "Decision: **TARGETED FRAUD REVIEW**. Confirmed fraud exists even though the overall customer risk level is not High/Critical."
    )
else:
    st.success(
        "Decision: **ROUTINE MONITORING**. The current record does not show a strong combination of elevated customer risk and confirmed fraud."
    )

if len(customer_alerts):
    st.markdown("#### Main Fraud Signal")
    top_pattern_customer = customer_alerts.detected_pattern.value_counts().index[0]
    top_channel_customer = customer_alerts.channel.value_counts().index[0]

    st.info(
        f"Most common pattern: **{top_pattern_customer}** | "
        f"Primary channel: **{top_channel_customer}** | "
        f"Alerts reviewed: **{len(customer_alerts):,}**"
    )

st.divider()

# -------------------------
# Detailed tabs
# -------------------------
tabs = st.tabs([
    "Alert Queue",
    "Customer 360",
    "Pattern Explorer",
    "Portfolio Analytics",
    "Tableau Gallery"
])

with tabs[0]:
    st.subheader("Fraud Alert Queue")
    st.caption(
        "Alerts are ranked by fraud risk score and transaction amount so reviewers can quickly identify the highest-priority items."
    )

    st.dataframe(
        f.sort_values(
            ["fraud_risk_score", "amount"],
            ascending=[False, False]
        ),
        use_container_width=True,
        hide_index=True
    )

with tabs[1]:
    st.subheader("Customer 360")
    st.caption(
        "Detailed transaction-level view for the selected customer."
    )

    st.dataframe(
        customer_tx.sort_values(
            "fraud_risk_score",
            ascending=False
        ).head(100),
        use_container_width=True,
        hide_index=True
    )

with tabs[2]:
    st.subheader("Pattern Explorer")
    st.caption(
        "Select a suspicious transaction pattern to see the alerts most strongly associated with it."
    )

    selected_pattern = st.selectbox(
        "Suspicious pattern",
        sorted(ALERTS.detected_pattern.dropna().unique()),
        key="pattern_explorer_select"
    )

    pattern_df = ALERTS[
        ALERTS.detected_pattern == selected_pattern
    ].sort_values(
        "fraud_risk_score",
        ascending=False
    )

    st.dataframe(
        pattern_df,
        use_container_width=True,
        hide_index=True
    )

    if len(pattern_df):
        st.markdown("##### Pattern Summary")

        p1, p2, p3 = st.columns(3)
        p1.metric("Alerts", f"{len(pattern_df):,}")
        p2.metric(
            "High/Critical",
            f"{pattern_df.risk_level.isin(['High','Critical']).sum():,}"
        )
        p3.metric(
            "Confirmed Fraud",
            f"{(pattern_df.disposition == 'Confirmed Fraud').sum():,}"
        )

with tabs[3]:
    st.subheader("Portfolio Analytics")

    a, b = st.columns(2)

    with a:
        st.markdown("##### Suspicious Patterns")
        st.caption("Shows which fraud patterns appear most often in the selected alert population.")
        st.bar_chart(f.detected_pattern.value_counts())

    with b:
        st.markdown("##### Fraud Channels")
        st.caption("Shows which transaction channels generate the most fraud alerts.")
        st.bar_chart(f.channel.value_counts())

with tabs[4]:
    st.subheader("Tableau Analytics Gallery")
    st.caption(
        "Final Executive Dashboard synchronized with the current processed datasets and verified KPI results."
    )

    images = [
        ("02_executive_dashboard.png", "Fraud & Suspicious Transaction Pattern Detection — Final Executive Dashboard"),
    ]
    for filename, caption in images:
        img = ROOT / "images" / filename
        if img.exists():
            st.image(
                str(img),
                caption=caption,
                use_container_width=True
            )

st.caption(
    "Synthetic educational portfolio project. No real bank or customer data."
)
