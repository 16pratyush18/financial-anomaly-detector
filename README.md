# Financial Transaction Anomaly & Risk Monitoring System

## Overview

A Python and SQL-based financial fraud detection system that simulates banking transactions and identifies suspicious activities using rule-based analytics and statistical anomaly detection.

The project generates synthetic banking data, stores it in a SQLite database, analyzes transaction patterns, and flags potentially fraudulent activities such as transaction structuring, velocity anomalies, and abnormal transaction amounts.

This project demonstrates practical applications of SQL, data analysis, and financial risk monitoring concepts commonly used in Anti-Money Laundering (AML) systems.

---

## Features

* Generate realistic synthetic banking accounts and transaction data.
* Store financial data using SQLite.
* Detect **Structuring (Smurfing)** transactions using SQL.
* Detect **Velocity Anomalies** using SQL aggregation queries.
* Detect **Statistical Outliers** using Z-Score analysis in Python.
* Export flagged transactions for further investigation.
* Modular codebase that can be extended with machine learning models.

---

## Technology Stack

* Python 3.12
* SQLite
* SQL
* Pandas
* NumPy

---

## Project Structure

```text
financial-anomaly-detector/
│
├── generate_data.py        # Generates synthetic banking data
├── detect_anomalies.py     # Detects suspicious transactions
├── schema.sql              # Database schema
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Detection Techniques

### 1. Structuring Detection

Detects multiple cash deposits between predefined thresholds that may indicate attempts to avoid reporting requirements.

### 2. Velocity Detection

Identifies accounts with an unusually high number of transactions or unusually high transaction volume within a single day.

### 3. Statistical Outlier Detection

Calculates Z-Scores for transaction amounts within each account and flags unusually large transactions.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/16pratyush18/financial-anomaly-detector.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate synthetic banking data:

```bash
python generate_data.py
```

Run anomaly detection:

```bash
python detect_anomalies.py
```

Detected anomalies will be exported to:

```text
flagged_transactions.csv
```

---

## Future Enhancements

* Machine Learning–based anomaly detection (Isolation Forest)
* Spring Boot REST API
* React Dashboard
* Docker support
* PostgreSQL integration
* Cloud deployment
* Real-time transaction monitoring

---

## Author

**Pragya Pratyush Sinha**

GitHub: https://github.com/16pratyush18
