-- Fraud & Suspicious Transaction Pattern Detection

-- 1. High-risk transactions
SELECT * FROM transactions_enriched
WHERE fraud_risk_score >= 80
ORDER BY fraud_risk_score DESC, amount DESC;

-- 2. Unusual amount activity
SELECT customer_id, transaction_id, amount, expected_monthly_volume, amount_to_expected_ratio
FROM transactions_enriched
WHERE amount_to_expected_ratio > 1
ORDER BY amount_to_expected_ratio DESC;

-- 3. Cross-border wire / P2P anomalies
SELECT customer_id, transaction_id, channel, country, home_country, amount, fraud_risk_score
FROM transactions_enriched
WHERE cross_border_flag=1 AND channel IN ('Wire','P2P')
ORDER BY fraud_risk_score DESC;

-- 4. Rapid / suspicious transaction patterns
SELECT detected_pattern, COUNT(*) AS transactions, SUM(amount) AS exposure
FROM transactions_enriched
WHERE flagged=1
GROUP BY detected_pattern
ORDER BY transactions DESC;

-- 5. Channel risk
SELECT channel, COUNT(*) AS flagged_transactions, SUM(amount) AS flagged_exposure,
       AVG(fraud_risk_score) AS avg_risk
FROM transactions_enriched
WHERE flagged=1
GROUP BY channel
ORDER BY flagged_exposure DESC;

-- 6. Repeated counterparties
SELECT counterparty_id, COUNT(*) AS tx_count, COUNT(DISTINCT customer_id) AS customers, SUM(amount) AS volume
FROM transactions_enriched
GROUP BY counterparty_id
HAVING COUNT(*) >= 10
ORDER BY volume DESC;

-- 7. Device concentration
SELECT device_id, COUNT(DISTINCT customer_id) AS customers, COUNT(*) AS tx_count
FROM transactions_enriched
GROUP BY device_id
HAVING COUNT(DISTINCT customer_id) >= 3
ORDER BY customers DESC;

-- 8. Top flagged customers
SELECT customer_id, COUNT(*) AS alerts, SUM(amount) AS flagged_amount, AVG(fraud_risk_score) AS avg_risk
FROM transactions_enriched
WHERE flagged=1
GROUP BY customer_id
ORDER BY flagged_amount DESC;

-- 9. Customer fraud risk queue
SELECT customer_id, customer_fraud_score, customer_risk_level, flagged_transactions,
       flag_rate, cross_border_ratio
FROM customer_fraud_risk
ORDER BY customer_fraud_score DESC;

-- 10. Alert disposition
SELECT disposition, COUNT(*) AS alerts
FROM fraud_alerts
GROUP BY disposition
ORDER BY alerts DESC;

-- 11. Confirmed fraud patterns
SELECT detected_pattern, COUNT(*) AS confirmed_cases, SUM(amount) AS confirmed_exposure
FROM fraud_alerts
WHERE disposition='Confirmed Fraud'
GROUP BY detected_pattern
ORDER BY confirmed_exposure DESC;

-- 12. Monthly alert trend
SELECT DATE_TRUNC('month', transaction_time) AS month, COUNT(*) AS alerts
FROM fraud_alerts
GROUP BY DATE_TRUNC('month', transaction_time)
ORDER BY month;
