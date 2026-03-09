import sqlite3

def create_tables():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Enable foreign key enforcement
    cursor.execute('PRAGMA foreign_keys = ON')

    # Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            cust_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            address  TEXT,
            email    TEXT    UNIQUE NOT NULL
        )
    ''')

    # Accounts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Accounts (
            acc_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            cust_id  INTEGER NOT NULL,
            acc_type TEXT    NOT NULL CHECK(acc_type IN ('SAVINGS', 'CURRENT', 'CHECKING')),
            balance  REAL    NOT NULL DEFAULT 0.0,
            FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
        )
    ''')

    # Transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transactions (
            trans_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            acc_id     INTEGER NOT NULL,
            trans_type TEXT    NOT NULL CHECK(trans_type IN ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER')),
            amount     REAL    NOT NULL,
            date       TEXT    NOT NULL DEFAULT (DATE('now')),
            FOREIGN KEY (acc_id) REFERENCES Accounts(acc_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    create_tables()
