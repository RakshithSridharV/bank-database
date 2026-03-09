from database import create_tables
from operations import (
    add_customer, get_customer, get_all_customers,
    create_account, get_account, get_balance,
    get_accounts_by_customer
)
from transactions import deposit, withdraw, transfer, get_transaction_history

def print_menu():
    print("\n===== BANK DATABASE SYSTEM =====")
    print("1.  Add Customer")
    print("2.  View Customer")
    print("3.  View All Customers")
    print("4.  Create Account")
    print("5.  View Account")
    print("6.  Check Balance")
    print("7.  Deposit")
    print("8.  Withdraw")
    print("9.  Transfer")
    print("10. Transaction History")
    print("0.  Exit")
    print("================================")

def main():
    create_tables()

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == '1':
                name    = input("Name: ")
                email   = input("Email: ")
                address = input("Address: ")
                add_customer(name, email, address)

            elif choice == '2':
                cust_id = int(input("Customer ID: "))
                c = get_customer(cust_id)
                print(f"\nID: {c[0]} | Name: {c[1]} | Address: {c[2]} | Email: {c[3]}")

            elif choice == '3':
                customers = get_all_customers()
                if not customers:
                    print("No customers found.")
                else:
                    print("\n--- All Customers ---")
                    for c in customers:
                        print(f"ID: {c[0]} | Name: {c[1]} | Address: {c[2]} | Email: {c[3]}")

            elif choice == '4':
                cust_id  = int(input("Customer ID: "))
                acc_type = input("Account type (SAVINGS / CURRENT / CHECKING): ").upper().strip()
                balance  = float(input("Initial balance: "))
                create_account(cust_id, acc_type, balance)

            elif choice == '5':
                acc_id = int(input("Account ID: "))
                a = get_account(acc_id)
                print(f"\nAcc ID: {a[0]} | Customer ID: {a[1]} | Type: {a[2]} | Balance: {a[3]:.2f}")

            elif choice == '6':
                acc_id = int(input("Account ID: "))
                bal = get_balance(acc_id)
                print(f"Current Balance: {bal:.2f}")

            elif choice == '7':
                acc_id = int(input("Account ID: "))
                amount = float(input("Amount to deposit: "))
                deposit(acc_id, amount)

            elif choice == '8':
                acc_id = int(input("Account ID: "))
                amount = float(input("Amount to withdraw: "))
                withdraw(acc_id, amount)

            elif choice == '9':
                from_id = int(input("From Account ID: "))
                to_id   = int(input("To Account ID: "))
                amount  = float(input("Amount to transfer: "))
                transfer(from_id, to_id, amount)

            elif choice == '10':
                acc_id = int(input("Account ID: "))
                history = get_transaction_history(acc_id)
                if not history:
                    print("No transactions found for this account.")
                else:
                    print("\n--- Transaction History ---")
                    for t in history:
                        print(f"Trans ID: {t[0]} | Type: {t[2]} | Amount: {t[3]:.2f} | Date: {t[4]}")

            elif choice == '0':
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
