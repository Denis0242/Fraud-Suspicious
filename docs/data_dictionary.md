# Data Dictionary

## Fraud & Suspicious Transaction Pattern Detection

This data dictionary documents the customer, transaction, customer fraud-risk, fraud-alert, and enriched-transaction datasets used in this portfolio project. It distinguishes source fields from derived and engineered analytical features so the project's EDA and feature-engineering work is clear to GitHub reviewers.

> **Portfolio note:** These datasets are structured for analytical demonstration. Definitions describe their use within this project and do not represent any specific financial institution's production data standards.

## Dataset Overview

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| `customers(20260914-025421).csv` | 750 | 6 | Customer reference dataset providing profile and baseline risk context. |
| `transactions(20260914-025422).csv` | 28,000 | 18 | Raw transaction-level dataset used for suspicious-pattern and fraud analysis. |
| `customer_fraud_risk.csv` | 750 | 18 | Customer-level analytical dataset containing fraud-risk indicators and derived risk measures. |
| `fraud_alerts.csv` | 1,628 | 14 | Alert-level dataset used to review detected fraud and suspicious-transaction activity. |
| `transactions_enriched.csv` | 28,000 | 18 | Analytics-ready transaction dataset containing original transaction attributes plus enriched or engineered features. |

## `customers(20260914-025421).csv`

Customer reference dataset providing profile and baseline risk context.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST20000` |
| `customer_type` | String | Source / Operational | Field representing customer type within the fraud and suspicious-transaction analytics workflow. | `Individual` |
| `home_country` | String | Derived / Analytical | Count used to measure home country. | `Mexico` |
| `account_tenure_months` | Integer | Derived / Analytical | Count used to measure account tenure months. | `37` |
| `expected_monthly_volume` | Float | Source / Operational | Field representing expected monthly volume within the fraud and suspicious-transaction analytics workflow. | `27306.42` |
| `baseline_risk` | String | Source / Operational | Attribute used to assess baseline risk. | `Low` |

## `transactions(20260914-025422).csv`

Raw transaction-level dataset used for suspicious-pattern and fraud analysis.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `TX300000` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST20469` |
| `transaction_time` | String | Source / Operational | Date/time attribute associated with transaction. | `2026-03-25 11:12:00` |
| `channel` | String | Source / Operational | Field representing channel within the fraud and suspicious-transaction analytics workflow. | `ACH` |
| `merchant_category` | String | Source / Operational | Category assigned to the merchant or transaction. | `Crypto Exchange` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction or activity. | `2361.93` |
| `country` | String | Derived / Analytical | Country associated with the customer or transaction. | `United States` |
| `device_id` | String | Source / Operational | Identifier associated with the device used for the transaction. | `DEV2977` |
| `counterparty_id` | String | Derived / Analytical | Unique identifier for the counterparty. | `CP15008` |
| `injected_pattern` | String | Source / Operational | Field representing injected pattern within the fraud and suspicious-transaction analytics workflow. | `Normal` |
| `expected_monthly_volume` | Float | Source / Operational | Field representing expected monthly volume within the fraud and suspicious-transaction analytics workflow. | `19639` |
| `home_country` | String | Derived / Analytical | Count used to measure home country. | `Mexico` |
| `amount_to_expected_ratio` | Float | Derived / Analytical | Derived measure representing amount to expected ratio. | `0.1203` |
| `cross_border_flag` | Integer | Source / Operational | Indicator identifying whether cross border applies. | `1` |
| `fraud_risk_score` | Integer | Derived / Analytical | Numeric analytical score representing fraud risk. | `29` |
| `risk_level` | String | Source / Operational | Attribute used to assess risk level. | `Low` |
| `flagged` | Integer | Source / Operational | Indicator identifying whether flagged applies. | `0` |
| `detected_pattern` | String | Source / Operational | Field representing detected pattern within the fraud and suspicious-transaction analytics workflow. | `Behavioral Anomaly` |

## `customer_fraud_risk.csv`

Customer-level analytical dataset containing fraud-risk indicators and derived risk measures.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Derived / Analytical | Unique identifier assigned to the customer. | `CUST20000` |
| `total_transactions` | Integer | Derived / Analytical | Field representing total transactions within the fraud and suspicious-transaction analytics workflow. | `24` |
| `total_volume` | Float | Derived / Analytical | Field representing total volume within the fraud and suspicious-transaction analytics workflow. | `47521.92` |
| `avg_amount` | Float | Derived / Analytical | Field representing avg amount within the fraud and suspicious-transaction analytics workflow. | `1980.08` |
| `max_amount` | Float | Derived / Analytical | Field representing max amount within the fraud and suspicious-transaction analytics workflow. | `7631.17` |
| `flagged_transactions` | Integer | Derived / Analytical | Indicator identifying whether flagged transactions applies. | `0` |
| `avg_fraud_risk` | Float | Derived / Analytical | Attribute used to assess avg fraud risk. | `25.6667` |
| `cross_border_ratio` | Float | Derived / Analytical | Derived measure representing cross border ratio. | `1` |
| `unique_devices` | Integer | Derived / Analytical | Field representing unique devices within the fraud and suspicious-transaction analytics workflow. | `24` |
| `unique_counterparties` | Integer | Derived / Analytical | Count used to measure unique counterparties. | `24` |
| `flag_rate` | Float | Derived / Analytical | Indicator identifying whether flag rate applies. | `0` |
| `customer_fraud_score` | Integer | Derived / Analytical | Numeric analytical score representing customer fraud. | `32` |
| `customer_risk_level` | String | Derived / Analytical | Attribute used to assess customer risk level. | `Moderate` |
| `customer_type` | String | Derived / Analytical | Field representing customer type within the fraud and suspicious-transaction analytics workflow. | `Individual` |
| `home_country` | String | Derived / Analytical | Count used to measure home country. | `Mexico` |
| `account_tenure_months` | Integer | Derived / Analytical | Count used to measure account tenure months. | `37` |
| `expected_monthly_volume` | Float | Derived / Analytical | Field representing expected monthly volume within the fraud and suspicious-transaction analytics workflow. | `27306.42` |
| `baseline_risk` | String | Derived / Analytical | Attribute used to assess baseline risk. | `Low` |

## `fraud_alerts.csv`

Alert-level dataset used to review detected fraud and suspicious-transaction activity.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `alert_id` | String | Source / Operational | Unique identifier assigned to the fraud or suspicious-activity alert. | `FRD00001` |
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `TX300030` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST20699` |
| `transaction_time` | String | Source / Operational | Date/time attribute associated with transaction. | `2026-08-20 09:47:00` |
| `channel` | String | Source / Operational | Field representing channel within the fraud and suspicious-transaction analytics workflow. | `P2P` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction or activity. | `250000` |
| `country` | String | Derived / Analytical | Country associated with the customer or transaction. | `United States` |
| `merchant_category` | String | Source / Operational | Category assigned to the merchant or transaction. | `Services` |
| `fraud_risk_score` | Integer | Derived / Analytical | Numeric analytical score representing fraud risk. | `100` |
| `risk_level` | String | Source / Operational | Attribute used to assess risk level. | `Critical` |
| `detected_pattern` | String | Source / Operational | Field representing detected pattern within the fraud and suspicious-transaction analytics workflow. | `Unusual Amount` |
| `device_id` | String | Source / Operational | Identifier associated with the device used for the transaction. | `DEV4769` |
| `counterparty_id` | String | Derived / Analytical | Unique identifier for the counterparty. | `CP14621` |
| `disposition` | String | Source / Operational | Final review outcome of the fraud alert. | `Pending` |

## `transactions_enriched.csv`

Analytics-ready transaction dataset containing original transaction attributes plus enriched or engineered features.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `TX300000` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST20469` |
| `transaction_time` | String | Source / Operational | Date/time attribute associated with transaction. | `2026-03-25 11:12:00` |
| `channel` | String | Source / Operational | Field representing channel within the fraud and suspicious-transaction analytics workflow. | `ACH` |
| `merchant_category` | String | Source / Operational | Category assigned to the merchant or transaction. | `Crypto Exchange` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction or activity. | `2361.93` |
| `country` | String | Source / Operational | Country associated with the customer or transaction. | `United States` |
| `device_id` | String | Source / Operational | Identifier associated with the device used for the transaction. | `DEV2977` |
| `counterparty_id` | String | Source / Operational | Unique identifier for the counterparty. | `CP15008` |
| `injected_pattern` | String | Source / Operational | Field representing injected pattern within the fraud and suspicious-transaction analytics workflow. | `Normal` |
| `expected_monthly_volume` | Float | Source / Operational | Field representing expected monthly volume within the fraud and suspicious-transaction analytics workflow. | `19639` |
| `home_country` | String | Source / Operational | Count used to measure home country. | `Mexico` |
| `amount_to_expected_ratio` | Float | Source / Operational | Derived measure representing amount to expected ratio. | `0.1203` |
| `cross_border_flag` | Integer | Source / Operational | Indicator identifying whether cross border applies. | `1` |
| `fraud_risk_score` | Integer | Source / Operational | Numeric analytical score representing fraud risk. | `29` |
| `risk_level` | String | Source / Operational | Attribute used to assess risk level. | `Low` |
| `flagged` | Integer | Source / Operational | Indicator identifying whether flagged applies. | `0` |
| `detected_pattern` | String | Source / Operational | Field representing detected pattern within the fraud and suspicious-transaction analytics workflow. | `Behavioral Anomaly` |

## Dataset Relationships

- `customers(20260914-025421).csv.customer_id` ↔ `transactions(20260914-025422).csv.customer_id` provides a shared identifier for joins and analysis.
- `customers(20260914-025421).csv.customer_id` ↔ `customer_fraud_risk.csv.customer_id` provides a shared identifier for joins and analysis.
- `customers(20260914-025421).csv.customer_id` ↔ `fraud_alerts.csv.customer_id` provides a shared identifier for joins and analysis.
- `customers(20260914-025421).csv.customer_id` ↔ `transactions_enriched.csv.customer_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.customer_id` ↔ `customer_fraud_risk.csv.customer_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.transaction_id` ↔ `fraud_alerts.csv.transaction_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.customer_id` ↔ `fraud_alerts.csv.customer_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.device_id` ↔ `fraud_alerts.csv.device_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.counterparty_id` ↔ `fraud_alerts.csv.counterparty_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.transaction_id` ↔ `transactions_enriched.csv.transaction_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.customer_id` ↔ `transactions_enriched.csv.customer_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.device_id` ↔ `transactions_enriched.csv.device_id` provides a shared identifier for joins and analysis.
- `transactions(20260914-025422).csv.counterparty_id` ↔ `transactions_enriched.csv.counterparty_id` provides a shared identifier for joins and analysis.
- `customer_fraud_risk.csv.customer_id` ↔ `fraud_alerts.csv.customer_id` provides a shared identifier for joins and analysis.
- `customer_fraud_risk.csv.customer_id` ↔ `transactions_enriched.csv.customer_id` provides a shared identifier for joins and analysis.
- `fraud_alerts.csv.transaction_id` ↔ `transactions_enriched.csv.transaction_id` provides a shared identifier for joins and analysis.
- `fraud_alerts.csv.customer_id` ↔ `transactions_enriched.csv.customer_id` provides a shared identifier for joins and analysis.
- `fraud_alerts.csv.device_id` ↔ `transactions_enriched.csv.device_id` provides a shared identifier for joins and analysis.
- `fraud_alerts.csv.counterparty_id` ↔ `transactions_enriched.csv.counterparty_id` provides a shared identifier for joins and analysis.

## Fraud Analytics Workflow

**Customer Profile → Raw Transactions → EDA & Data Quality Checks → Feature Engineering → Enriched Transactions → Fraud Alerts → Customer Fraud Risk Analysis**

The project structure supports suspicious-pattern detection by combining customer context with transaction behavior, engineered features, alert outcomes, and customer-level risk measures. This allows analysis of anomalous activity, fraud concentration, transaction patterns, and risk prioritization.

## EDA & Feature Engineering Context

The raw customer and transaction datasets provide the operational foundation. `transactions_enriched.csv` represents the feature-engineered transaction layer, while `customer_fraud_risk.csv` provides customer-level analytical measures. This separation makes the progression from raw data through EDA and feature engineering to fraud-risk analysis visible in the portfolio.

## Data Quality Conventions

- Validate customer, transaction, and alert identifiers before joining datasets.
- Check monetary fields for missing, duplicate, negative, or implausible values according to project business rules.
- Standardize date/time fields before temporal and velocity analysis.
- Standardize transaction channels, merchant categories, geography, alert statuses, and dispositions before aggregation.
- Review missing values in context rather than automatically removing them.
- Reconcile engineered features and fraud-risk measures to their underlying transaction/customer data.
- Validate binary indicators and derived scores before using them in dashboards or risk prioritization.

---

*Prepared for the Fraud & Suspicious Transaction Pattern Detection GitHub portfolio project.*