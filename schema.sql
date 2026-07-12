CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    account_type TEXT,
    balance REAL,
    created_date TEXT
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    timestamp TEXT,
    amount REAL,
    transaction_type TEXT,  -- deposit, withdrawal, transfer
    merchant TEXT,
    location TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE VIEW IF NOT EXISTS transaction_summary AS
SELECT account_id, COUNT(*) as tx_count, SUM(amount) as total_amount,
       AVG(amount) as avg_amount
FROM transactions GROUP BY account_id;