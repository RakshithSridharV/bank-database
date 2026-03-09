import sqlite3
from operations import get_connection, get_account

def deposit(acc_id, amount):
    """Deposit money into an account."""
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    # Verify account exists
    get_account(acc_id)

    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Update balance
        cursor.execute(
            'UPDATE Accounts SET balance = balance + ? WHERE acc_id = ?',
            (amount, acc_id)
        )

        # Log the transaction
        cursor.execute(
            'INSERT INTO Transactions (acc_id, trans_type, amount) VALUES (?, ?, ?)',
            (acc_id, 'DEPOSIT', amount)
        )

        conn.commit()
        print(f"Deposited {amount:.2f} into account {acc_id}.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def withdraw(acc_id, amount):
    """Withdraw money from an account."""
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    account = get_account(acc_id)
    current_balance = account[3]

    if current_balance < amount:
        raise ValueError(
            f"Insufficient funds. Available balance: {current_balance:.2f}"
        )

    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Update balance
        cursor.execute(
            'UPDATE Accounts SET balance = balance - ? WHERE acc_id = ?',
            (amount, acc_id)
        )

        # Log the transaction
        cursor.execute(
            'INSERT INTO Transactions (acc_id, trans_type, amount) VALUES (?, ?, ?)',
            (acc_id, 'WITHDRAWAL', amount)
        )

        conn.commit()
        print(f"Withdrew {amount:.2f} from account {acc_id}.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def transfer(from_acc_id, to_acc_id, amount):
    """Transfer money between two accounts atomically."""
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero.")
    if from_acc_id == to_acc_id:
        raise ValueError("Cannot transfer to the same account.")

    from_account = get_account(from_acc_id)
    get_account(to_acc_id)  # verify destination exists

    if from_account[3] < amount:
        raise ValueError(
            f"Insufficient funds. Available balance: {from_account[3]:.2f}"
        )

    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Deduct from source
        cursor.execute(
            'UPDATE Accounts SET balance = balance - ? WHERE acc_id = ?',
            (amount, from_acc_id)
        )

        # Add to destination
        cursor.execute(
            'UPDATE Accounts SET balance = balance + ? WHERE acc_id = ?',
            (amount, to_acc_id)
        )

        # Log both sides
        cursor.execute(
            'INSERT INTO Transactions (acc_id, trans_type, amount) VALUES (?, ?, ?)',
            (from_acc_id, 'TRANSFER', amount)
        )
        cursor.execute(
            'INSERT INTO Transactions (acc_id, trans_type, amount) VALUES (?, ?, ?)',
            (to_acc_id, 'TRANSFER', amount)
        )

        conn.commit()
        print(f"Transferred {amount:.2f} from account {from_acc_id} to {to_acc_id}.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def get_transaction_history(acc_id):
    """Get all transactions for an account."""
    get_account(acc_id)  # verify account exists

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Transactions WHERE acc_id = ? ORDER BY date DESC',
        (acc_id,)
    )
    transactions = cursor.fetchall()
    conn.close()
    return transactions
