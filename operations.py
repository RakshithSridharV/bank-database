import sqlite3

DB = 'bank.db'

def get_connection():
    conn = sqlite3.connect(DB)
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

# ── CUSTOMERS ──────────────────────────────────────────

def add_customer(name, email, address=''):
    """Add a new customer with input validation."""
    if not name or not name.strip():
        raise ValueError("Customer name cannot be empty.")
    if not email or '@' not in email:
        raise ValueError("Invalid email address.")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO Customers (name, email, address) VALUES (?, ?, ?)',
            (name.strip(), email.strip(), address.strip())
        )
        conn.commit()
        print(f"Customer '{name}' added with ID {cursor.lastrowid}.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise ValueError(f"Email '{email}' is already registered.")
    finally:
        conn.close()

def get_customer(cust_id):
    """Retrieve a customer by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers WHERE cust_id = ?', (cust_id,))
    customer = cursor.fetchone()
    conn.close()
    if not customer:
        raise ValueError(f"No customer found with ID {cust_id}.")
    return customer

def get_all_customers():
    """Retrieve all customers."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers')
    customers = cursor.fetchall()
    conn.close()
    return customers

# ── ACCOUNTS ───────────────────────────────────────────

def create_account(cust_id, acc_type, initial_balance=0.0):
    """Create a bank account for an existing customer."""
    if acc_type not in ('SAVINGS', 'CURRENT', 'CHECKING'):
        raise ValueError("Account type must be SAVINGS, CURRENT, or CHECKING.")
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    # Verify customer exists
    get_customer(cust_id)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Accounts (cust_id, acc_type, balance) VALUES (?, ?, ?)',
        (cust_id, acc_type, initial_balance)
    )
    conn.commit()
    acc_id = cursor.lastrowid
    conn.close()
    print(f"Account created with ID {acc_id} for customer {cust_id}.")
    return acc_id

def get_account(acc_id):
    """Retrieve an account by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Accounts WHERE acc_id = ?', (acc_id,))
    account = cursor.fetchone()
    conn.close()
    if not account:
        raise ValueError(f"No account found with ID {acc_id}.")
    return account

def get_accounts_by_customer(cust_id):
    """Retrieve all accounts for a customer."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Accounts WHERE cust_id = ?', (cust_id,))
    accounts = cursor.fetchall()
    conn.close()
    return accounts

def get_balance(acc_id):
    """Get the current balance of an account."""
    account = get_account(acc_id)
    return account[3]  # balance column
