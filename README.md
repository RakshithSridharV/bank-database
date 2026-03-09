# 🏦 Bank Database Management System

A command-line banking database system built with **Python** and **SQLite**, simulating core banking operations including customer management, account creation, deposits, withdrawals, and fund transfers.

> This project is the Python/SQLite implementation of a banking system.
> A REST API version built with Java and Spring Boot is available here: [banking-api](https://github.com/RakshithSridharV/banking-api)

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| Database | SQLite |
| DB Library | sqlite3 (built-in) |
| Interface | Command-line menu |

---

## 📁 Project Structure

```
bank-database/
│
├── database.py       # Schema creation — customers, accounts, transactions tables
├── operations.py     # CRUD operations with input validation and error handling
├── transactions.py   # Deposit, withdraw, transfer with atomic transaction handling
└── main.py           # Menu-driven CLI interface
```

---

## 🗄️ Database Schema

### Customers
| Column | Type | Constraint |
|--------|------|-----------|
| cust_id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| name | TEXT | NOT NULL |
| address | TEXT | |
| email | TEXT | UNIQUE, NOT NULL |

### Accounts
| Column | Type | Constraint |
|--------|------|-----------|
| acc_id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| cust_id | INTEGER | FOREIGN KEY → Customers |
| acc_type | TEXT | SAVINGS / CURRENT / CHECKING |
| balance | REAL | DEFAULT 0.0 |

### Transactions
| Column | Type | Constraint |
|--------|------|-----------|
| trans_id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| acc_id | INTEGER | FOREIGN KEY → Accounts |
| trans_type | TEXT | DEPOSIT / WITHDRAWAL / TRANSFER |
| amount | REAL | NOT NULL |
| date | TEXT | DEFAULT current date |

---

## ▶️ Running the Project

### Prerequisites
- Python 3.x (no external libraries needed)

### Run
```bash
python main.py
```

The database file `bank.db` is created automatically on first run.

---

## 🖥️ Menu Options

```
===== BANK DATABASE SYSTEM =====
1.  Add Customer
2.  View Customer
3.  View All Customers
4.  Create Account
5.  View Account
6.  Check Balance
7.  Deposit
8.  Withdraw
9.  Transfer
10. Transaction History
0.  Exit
================================
```

---

## 🧪 Example Usage

```
Enter choice: 1
Name: Rakshith
Email: rakshith@example.com
Address: Chennai
Customer 'Rakshith' added with ID 1.

Enter choice: 4
Customer ID: 1
Account type (SAVINGS / CURRENT / CHECKING): SAVINGS
Initial balance: 5000
Account created with ID 1 for customer 1.

Enter choice: 7
Account ID: 1
Amount to deposit: 1000
Deposited 1000.00 into account 1.

Enter choice: 8
Account ID: 1
Amount to withdraw: 9000
Error: Insufficient funds. Available balance: 6000.00
```

---

## 🧠 Key Design Decisions

- **Parameterized queries** — all SQL uses `?` placeholders instead of string formatting, preventing SQL injection
- **Atomic transactions** — deposit, withdraw, and transfer use `commit` and `rollback` to ensure the database is never left in a partial state
- **Input validation** — all inputs are validated before hitting the database (empty names, invalid emails, negative amounts, insufficient funds)
- **Foreign key enforcement** — `PRAGMA foreign_keys = ON` ensures referential integrity between tables
- **Layered structure** — schema, business logic, and interface are separated into independent files for maintainability

---

## 🔗 Related Project

This project shares the same banking domain as the [Banking Account REST API](https://github.com/RakshithSridharV/banking-api) — a Spring Boot REST API implementation of the same system built with Java, JPA, Hibernate, and Docker.

| Feature | This Project | REST API |
|---------|-------------|----------|
| Language | Python | Java |
| Interface | CLI | REST (HTTP) |
| Database | SQLite | H2 / PostgreSQL |
| Framework | None | Spring Boot |
| Deployment | Local | Docker |
