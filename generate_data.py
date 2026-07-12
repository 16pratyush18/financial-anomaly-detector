import sqlite3
import random
from datetime import datetime, timedelta

# -----------------------
# Create Database
# -----------------------

conn = sqlite3.connect("financial_db.db")
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# -----------------------
# Clear previous data
# -----------------------

cursor.execute("DELETE FROM transactions")
cursor.execute("DELETE FROM accounts")

# -----------------------
# Merchants & Locations
# -----------------------

merchants = [
    "Amazon",
    "Flipkart",
    "Reliance",
    "DMart",
    "Myntra",
    "Paytm",
    "Swiggy",
    "Zomato",
    "Uber",
    "IRCTC"
]

locations = [
    "Delhi",
    "Mumbai",
    "Hyderabad",
    "Bangalore",
    "Pune",
    "Chennai",
    "Lucknow",
    "Kolkata"
]

transaction_types = [
    "deposit",
    "withdrawal",
    "transfer"
]

# -----------------------
# Generate Accounts
# -----------------------

NUM_ACCOUNTS = 100

for acc in range(1, NUM_ACCOUNTS + 1):

    cursor.execute("""
        INSERT INTO accounts
        VALUES (?, ?, ?, ?, ?)
    """, (
        acc,
        random.randint(10000, 99999),
        random.choice(["Savings", "Current"]),
        round(random.uniform(50000, 500000), 2),
        (datetime.now() - timedelta(days=random.randint(30, 1000))).strftime("%Y-%m-%d")
    ))

# -----------------------
# Normal Transactions
# -----------------------

transaction_id = 1

for account in range(1, NUM_ACCOUNTS + 1):

    num_transactions = random.randint(30, 60)

    for _ in range(num_transactions):

        date = datetime.now() - timedelta(
            days=random.randint(0, 90),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        amount = round(random.uniform(100, 5000), 2)

        cursor.execute("""
            INSERT INTO transactions
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction_id,
            account,
            date.strftime("%Y-%m-%d %H:%M:%S"),
            amount,
            random.choice(transaction_types),
            random.choice(merchants),
            random.choice(locations)
        ))

        transaction_id += 1

# ====================================================
# STRUCTURING ANOMALIES
# ====================================================

for account in random.sample(range(1, NUM_ACCOUNTS + 1), 10):

    anomaly_day = datetime.now() - timedelta(days=random.randint(0, 20))

    for _ in range(4):

        amount = random.randint(8500, 9999)

        cursor.execute("""
            INSERT INTO transactions
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction_id,
            account,
            anomaly_day.strftime("%Y-%m-%d %H:%M:%S"),
            amount,
            "deposit",
            "Cash Deposit",
            random.choice(locations)
        ))

        transaction_id += 1

# ====================================================
# VELOCITY ANOMALIES
# ====================================================

for account in random.sample(range(1, NUM_ACCOUNTS + 1), 10):

    anomaly_day = datetime.now() - timedelta(days=random.randint(0, 20))

    for _ in range(15):

        amount = random.randint(500, 2500)

        cursor.execute("""
            INSERT INTO transactions
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction_id,
            account,
            anomaly_day.strftime("%Y-%m-%d %H:%M:%S"),
            amount,
            random.choice(transaction_types),
            random.choice(merchants),
            random.choice(locations)
        ))

        transaction_id += 1

# ====================================================
# LARGE AMOUNT OUTLIERS
# ====================================================

for account in random.sample(range(1, NUM_ACCOUNTS + 1), 10):

    anomaly_day = datetime.now() - timedelta(days=random.randint(0, 20))

    cursor.execute("""
        INSERT INTO transactions
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        transaction_id,
        account,
        anomaly_day.strftime("%Y-%m-%d %H:%M:%S"),
        random.randint(150000, 350000),
        "transfer",
        "International Transfer",
        random.choice(locations)
    ))

    transaction_id += 1

# -----------------------
# Finish
# -----------------------

conn.commit()

print("===================================")
print("Database Created Successfully")
print("Accounts:", NUM_ACCOUNTS)
print("Transactions:", transaction_id - 1)
print("===================================")

conn.close()