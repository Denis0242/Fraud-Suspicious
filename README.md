# Fraud & Suspicious Transaction Pattern Detection

**Fraud & Financial Crime Analytics Portfolio Project**

An end-to-end fraud analytics project using **Python, SQL, Tableau, and
Streamlit** to identify suspicious transaction patterns, prioritize
higher-risk alerts, analyze confirmed fraud outcomes, and support
customer-level investigation decisions.

> **Portfolio scope:** This project uses synthetic data for educational
> and portfolio demonstration. Fraud scores, alert dispositions,
> detected patterns, and investigation decisions are illustrative and do
> not represent any financial institution's production fraud rules.

------------------------------------------------------------------------

## Project Overview

Fraud investigations require analysts to connect customer context with
transaction behavior, suspicious patterns, alert outcomes, and
customer-level risk.

This project analyzes:

-   **750 synthetic customers**
-   **28,000 transactions**
-   **1,628 fraud alerts**
-   An enriched transaction layer
-   A customer-level fraud-risk layer

The workflow demonstrates the progression from raw transactions through
EDA and feature engineering into alert review, fraud-risk scoring, and
investigator prioritization.

------------------------------------------------------------------------

## Business & Investigation Questions

The project addresses questions such as:

-   Which transactions and customers show the highest fraud risk?
-   Which suspicious patterns appear most frequently?
-   Which transaction channels generate the most fraud alerts?
-   Which alerts are High or Critical risk?
-   Which alerts resulted in confirmed fraud?
-   Which countries account for the greatest flagged transaction value?
-   Which customers have the highest fraud scores and flag rates?
-   How can fraud alerts be prioritized for investigation?
-   Which patterns or channels may indicate recurring control
    weaknesses?

------------------------------------------------------------------------

## Dataset

  -----------------------------------------------------------------------------------
  Dataset                                               Rows Purpose
  ----------------------------- ---------------------------- ------------------------
  Customer reference                                     750 Customer profile and
                                                             baseline risk

  Raw transactions                                    28,000 Transaction-level fraud
                                                             analysis

  `transactions_enriched.csv`                         28,000 Feature-engineered
                                                             transaction layer

  `fraud_alerts.csv`                                   1,628 Fraud and
                                                             suspicious-transaction
                                                             alert review

  `customer_fraud_risk.csv`                              750 Customer-level
                                                             fraud-risk analytics
  -----------------------------------------------------------------------------------

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for detailed
field definitions and relationships.

------------------------------------------------------------------------

## Exploratory Data Analysis & Data Quality

The notebook includes a practical EDA workflow covering:

-   Dataset/schema review
-   Missing-value analysis
-   Duplicate validation
-   Datatype cleaning
-   Summary statistics
-   Numeric range review
-   IQR-based outlier review
-   Business-rule validation
-   Fraud-alert distribution
-   Customer-risk distribution
-   Final dataset validation

Unusual transaction values are reviewed as potential fraud signals
instead of being automatically removed.

------------------------------------------------------------------------

## Feature Engineering

The project includes explainable analytical features such as:

-   `amount_to_expected_ratio`
-   `cross_border_flag`
-   `fraud_risk_score`
-   `risk_level`
-   `flagged`
-   `detected_pattern`
-   `flag_rate`
-   `customer_fraud_score`
-   `customer_risk_level`

The notebook also demonstrates:

-   `amount_band`
-   `above_median_amount_flag`
-   `alert_amount_band`
-   `confirmed_fraud_flag`
-   `high_fraud_risk_flag`

These features are intentionally straightforward so the fraud logic
remains easy to explain in an interview.

------------------------------------------------------------------------

## Fraud & Suspicious Pattern Analysis

The project focuses on:

**Transaction behavior** --- transaction amount, channel, geography,
merchant category, device and counterparty context.

**Suspicious pattern detection** --- unusual amounts, behavioral
anomalies, velocity/pattern concerns, cross-border behavior and other
fraud indicators.

**Alert prioritization** --- sorting alert populations by fraud risk
score and transaction value.

**Customer risk** --- combining flagged transactions, flag rate,
transaction behavior and customer-level fraud scores.

**Fraud outcomes** --- comparing pending, reviewed, escalated and
confirmed-fraud dispositions.

------------------------------------------------------------------------

## SQL Analysis

The SQL file contains **12 analytical queries/statements** supporting
transaction analysis, alert review, suspicious-pattern analysis,
fraud-risk prioritization, customer analysis, geography, channel
analysis and confirmed-fraud outcomes.

See [`sql/`](sql/) for the full SQL analysis.

------------------------------------------------------------------------

## Verified Current KPIs

The following results were recalculated from the current uploaded
processed datasets:

  KPI                                    Current Result
  -------------------------------- --------------------
  Total Transactions                         **28,000**
  Fraud Alerts                                **1,628**
  Affected Customers                            **595**
  Confirmed Fraud Alerts                        **205**
  Confirmed Fraud Rate                        **12.6%**
  High/Critical Alerts               **1,628 (100.0%)**
  Total Flagged Alert Amount                **\$19.5M**
  Average Alert Fraud Risk Score               **72.9**

------------------------------------------------------------------------

## Key Findings

-   **205 alerts** are currently labeled Confirmed Fraud.
-   **1,628 alerts (100.0%)** fall into High/Critical risk.
-   The largest suspicious pattern is **Unusual Amount (1,055 alerts)**.
-   The most common fraud-alert channel is **Card (435 alerts)**.
-   The highest flagged transaction value is associated with **United
    States**, with approximately **\$9.2M**.
-   The current alert population contains approximately **\$19.5M** in
    flagged transaction value.

These findings support investigator prioritization rather than automated
fraud disposition.

------------------------------------------------------------------------

## Streamlit Fraud Investigation Application

The Streamlit application provides interactive fraud investigation and
portfolio review.

### Filters

-   Suspicious Pattern
-   Channel
-   Minimum Risk Score

### Portfolio Decision Support

The application classifies the filtered alert population as:

-   **Routine Monitoring**
-   **Targeted Investigation Required**
-   **Heightened Fraud Risk**

The decision logic considers:

-   High/Critical alert concentration
-   Confirmed-fraud activity
-   Total flagged exposure

### Customer Fraud Decision Summary

For a selected customer, the application displays:

-   Customer fraud score
-   Risk level
-   Flagged transactions
-   Flag rate
-   Most common suspicious pattern
-   Main transaction channel
-   Confirmed-fraud history

It then provides an explainable decision:

-   **Priority Fraud Investigation**
-   **Enhanced Fraud Review**
-   **Targeted Fraud Review**
-   **Routine Monitoring**

### Interactive Tabs

-   Fraud Alert Queue
-   Customer 360
-   Pattern Explorer
-   Portfolio Analytics
-   Tableau Gallery

The Tableau Gallery is simplified to display **only the Executive
Dashboard**.

------------------------------------------------------------------------

## Tableau Executive Dashboard

The Tableau workbook supports the fraud investigation story with an
executive dashboard covering:

1.  Transactions, Fraud Alerts & Confirmed Fraud Trend
2.  Fraud Pattern Distribution
3.  Top Countries by Flagged Amount
4.  Fraud Activity Heatmap
5.  Transaction Amount vs Fraud Risk
6.  Alert Disposition

### Dashboard Preview

![Fraud & Suspicious Transaction Pattern Detection Dashboard](images/02_executive_dashboard.png)

> **Dashboard status:** The Executive Dashboard shown below is synchronized with the current processed-data KPIs used throughout this README and the Streamlit application.

------------------------------------------------------------------------

## Analytical Workflow

``` text
Customer Profile
       ↓
Raw Transactions
       ↓
EDA & Data Quality
       ↓
Feature Engineering
       ↓
Enriched Transactions
       ↓
Fraud Alert Detection
       ↓
Customer Fraud Risk
       ↓
Investigation Prioritization
       ↓
Tableau + Streamlit Decision Support
```

------------------------------------------------------------------------

## Tools & Technologies

  Tool                   Use
  ---------------------- --------------------------------------------------------
  **Python / Pandas**    EDA, feature engineering, fraud analysis
  **SQL**                Transaction, alert, pattern and customer-risk analysis
  **Tableau**            Executive fraud dashboard
  **Streamlit**          Interactive fraud investigation and decision support
  **Jupyter Notebook**   Reproducible analytical workflow
  **Git / GitHub**       Version control and portfolio presentation

------------------------------------------------------------------------

## Repository Structure

``` text
Fraud-Suspicious/
├── app/             # Streamlit application
├── data/            # Raw and processed synthetic datasets
├── docs/            # Data dictionary and supporting documentation
├── images/          # Executive dashboard image
├── notebooks/       # EDA and feature engineering
├── sql/             # Fraud analytics queries
├── tableau/         # Tableau workbook
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

------------------------------------------------------------------------

## How to Run

``` bash
git clone https://github.com/Denis0242/Fraud-Suspicious.git
cd Fraud-Suspicious
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

------------------------------------------------------------------------

## Skills Demonstrated

### Fraud / Financial Crime

-   Fraud Alert Review
-   Suspicious Transaction Pattern Analysis
-   Fraud Risk Scoring
-   Customer Fraud Risk
-   Alert Disposition Analysis
-   Cross-Border Risk
-   Transaction Channel Analysis
-   Fraud Investigation Prioritization
-   Confirmed-Fraud Analysis
-   Behavioral Anomaly Review

### Data & Analytics

-   Exploratory Data Analysis
-   Data Quality Validation
-   Feature Engineering
-   SQL
-   Python / Pandas
-   Risk Segmentation
-   KPI Development
-   Trend Analysis
-   Outlier Review
-   Business-Rule Validation

### Visualization & Decision Support

-   Tableau
-   Streamlit
-   Fraud Alert Queues
-   Customer 360
-   Executive Dashboards
-   Interactive Filtering
-   Data Storytelling

------------------------------------------------------------------------

## Disclaimer

This project uses **synthetic data** created for educational and
portfolio purposes. No real customer, account, transaction, fraud alert,
device, counterparty, financial institution, or confidential fraud data
is included.

Fraud scores, suspicious patterns, alert dispositions, engineered
features, investigation decisions, and dashboard metrics are
illustrative and should not be interpreted as actual fraud-control
rules, institution policy, or regulatory determinations.
