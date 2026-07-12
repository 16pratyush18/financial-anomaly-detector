import sqlite3
import pandas as pd

conn = sqlite3.connect('financial_db.db')
tx_df = pd.read_sql_query("SELECT * FROM transactions", conn)

# SQL: Structuring detection
structuring_query = """
SELECT account_id, COUNT(*) as count, GROUP_CONCAT(transaction_id) as tx_ids
FROM transactions 
WHERE amount BETWEEN 8500 AND 9999 AND transaction_type = 'deposit'
GROUP BY account_id HAVING COUNT(*) >= 2;
"""
struct_flags = pd.read_sql_query(structuring_query, conn)

# SQL: Velocity
velocity_query = """
WITH daily AS (
    SELECT account_id, DATE(timestamp) as tx_date,
           COUNT(*) as daily_count, SUM(amount) as daily_amount
    FROM transactions GROUP BY account_id, DATE(timestamp)
)
SELECT * FROM daily WHERE daily_count > 10 OR daily_amount > 50000;
"""
velocity_flags = pd.read_sql_query(velocity_query, conn)

# Python: Z-score outliers
tx_df['timestamp'] = pd.to_datetime(tx_df['timestamp'])
tx_df['z_score'] = tx_df.groupby('account_id')['amount'].transform(
    lambda x: (x - x.mean()) / x.std() if x.std() > 0 else 0
)
amount_anomalies = tx_df[abs(tx_df['z_score']) > 3]

print("Structuring flags:", len(struct_flags))
print("Velocity flags:", len(velocity_flags))
print("Amount anomalies:", len(amount_anomalies))

amount_anomalies.to_csv("flagged_transactions.csv", index=False)

print("CSV saved successfully!")
conn.close()