import mysql.connector
from datetime import date

# ---------- Database Connection ----------
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        database='bankproject',
        user='root',
        password='1234'
    )

# ---------- Utility ----------
def clear():
    print("\n" * 50)

# ---------- Account Helper ----------
def account_status(acno):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT status, balance FROM customer WHERE acno = %s", (acno,))
    result = cursor.fetchone()
    conn.close()
    return result

# ---------- Deposit ----------
def deposit_amount():
    conn = connect_db()
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No: ')
    amount = float(input('Enter amount: '))
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active':
        cursor.execute("UPDATE customer SET balance = balance + %s WHERE acno = %s", (amount, acno))
        cursor.execute("INSERT INTO transaction (amount, type, acno, dot) VALUES (%s, %s, %s, %s)",
                       (amount, 'deposit', acno, today))
        conn.commit()
        print('\n✅ Amount deposited successfully.')
    else:
        print('\n⚠️ Closed or suspended account.')
    conn.close()
    input('\nPress any key to continue...')

# ---------- Withdraw ----------
def withdraw_amount():
    conn = connect_db()
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No: ')
    amount = float(input('Enter amount: '))
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active' and result[1] >= amount:
        cursor.execute("UPDATE customer SET balance = balance - %s WHERE acno = %s", (amount, acno))
        cursor.execute("INSERT INTO transaction (amount, type, acno, dot) VALUES (%s, %s, %s, %s)",
                       (amount, 'withdraw', acno, today))
        conn.commit()
        print('\n✅ Amount withdrawn successfully.')
    else:
        print('\n⚠️ Closed/suspended account or insufficient balance.')
    conn.close()
    input('\nPress any key to continue...')

# ---------- Add Account ----------
def add_account():
    conn = connect_db()
    cursor = conn.cursor()
    clear()
    name = input('Enter Name: ')
    addr = input('Enter Address: ')
    phone = input('Enter Phone No: ')
    email = input('Enter Email: ')
    aadhar = input('Enter Aadhar No: ')
    actype = input('Account Type (saving/current): ')
    balance = float(input('Enter Opening Balance: '))
    cursor.execute("""
        INSERT INTO customer (name, address, phone, email, aadhar_no, acc_type, balance, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')
    """, (name, addr, phone, email, aadhar, actype, balance))
    conn.commit()
    conn.close()
    print('\n✅ New account created successfully!')
    input('\nPress any key to continue...')

# ---------- Modify Account ----------
def modify_account():
    conn = connect_db()
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No: ')
    print('\nModify Menu:')
    print('1. Name')
    print('2. Address')
    print('3. Phone')
    print('4. Email')
    choice = input('\nWhat do you want to change? ')
    new_data = input('Enter new value: ')
    fields = {'1': 'name', '2': 'address', '3': 'phone', '4': 'email'}
    if choice in fields:
        sql = f"UPDATE customer SET {fields[choice]} = %s WHERE acno = %s"
        cursor.execute(sql, (new_data, acno))
        conn.commit()
        print('\n✅ Customer information updated successfully.')
    else:
        print('\n⚠️ Invalid choice.')
    conn.close()
    input('\nPress any key to continue...')

# ---------- Close Account ----------
def close_account():
    conn = connect_db()
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No: ')
    cursor.execute("UPDATE customer SET status='closed' WHERE acno=%s", (acno,))
    conn.commit()
    conn.close()
    print('\n✅ Account closed successfully.')
    input('\nPress any key to continue...')

# ---------- Search Menu ----------
def search_menu():
    conn = connect_db()
    cursor = conn.cursor()
    while True:
        clear()
        print(' SEARCH MENU')
        print('1. Account No')
        print('2. Aadhar No')
        print('3. Phone No')
        print('4. Email')
        print('5. Back')
        choice = input('\nEnter your choice: ')
        field_map = {'1': 'acno', '2': 'aadhar_no', '3': 'phone', '4': 'email'}
        if choice in field_map:
            value = input(f'Enter {field_map[choice]}: ')
            cursor.execute(f"SELECT * FROM customer WHERE {field_map[choice]} = %s", (value,))
            records = cursor.fetchall()
            clear()
            print('Search Results:')
            print('-'*100)
            for r in records:
                print(r)
            if not records:
                print('⚠️ No record found.')
            input('\nPress any key to continue...')
        elif choice == '5':
            break
    conn.close()

# ---------- Reports ----------
def daily_report():
    clear()
    conn = connect_db()
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("SELECT tid, dot, amount, type, acno FROM transaction WHERE dot = %s", (today,))
    records = cursor.fetchall()
    print('Daily Report:', today)
    print('-'*100)
    for record in records:
        print(record)
    print('-'*100)
    conn.close()
    input('\nPress any key to continue...')

def monthly_report():
    clear()
    conn = connect_db()
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("SELECT tid, dot, amount, type, acno FROM transaction WHERE MONTH(dot) = MONTH(%s)", (today,))
    records = cursor.fetchall()
    print('Monthly Report:', today.strftime('%B %Y'))
    print('-'*100)
    for record in records:
        print(record)
    print('-'*100)
    conn.close()
    input('\nPress any key to continue...')

def account_details():
    clear()
    acno = input('Enter account no: ')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE acno = %s", (acno,))
    customer = cursor.fetchone()
    clear()
    if customer:
        print('Account Details')
        print('-'*100)
        print('Account No:', customer[0])
        print('Name:', customer[1])
        print('Address:', customer[2])
        print('Phone:', customer[3])
        print('Email:', customer[4])
        print('Aadhar:', customer[5])
        print('Account Type:', customer[6])
        print('Balance:', customer[7])
        print('Status:', customer[8])
        print('-'*100)
        cursor.execute("SELECT tid, dot, amount, type FROM transaction WHERE acno = %s", (acno,))
        trans = cursor.fetchall()
        print('Transactions:')
        for t in trans:
            print(t)
    else:
        print('⚠️ Account not found.')
    conn.close()
    input('\nPress any key to continue...')

# ---------- Report Menu ----------
def report_menu():
    while True:
        clear()
        print(' REPORT MENU')
        print('1. Daily Report')
        print('2. Monthly Report')
        print('3. Account Details')
        print('4. Back')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            daily_report()
        elif choice == '2':
            monthly_report()
        elif choice == '3':
            account_details()
        elif choice == '4':
            break

# ---------- Transaction Menu ----------
def transaction_menu():
    while True:
        clear()
        print(' TRANSACTION MENU')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Back')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            deposit_amount()
        elif choice == '2':
            withdraw_amount()
        elif choice == '3':
            break

# ---------- Main Menu ----------
def main_menu():
    while True:
        clear()
        print(' MAIN MENU')
        print('1. Add Account')
        print('2. Modify Account')
        print('3. Close Account')
        print('4. Transaction Menu')
        print('5. Search Menu')
        print('6. Report Menu')
        print('7. Exit')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            add_account()
        elif choice == '2':
            modify_account()
        elif choice == '3':
            close_account()
        elif choice == '4':
            transaction_menu()
        elif choice == '5':
            search_menu()
        elif choice == '6':
            report_menu()
        elif choice == '7':
            print('Thank you for using the Banking System!')
            break
        else:
            print('⚠️ Invalid choice.')
            input('\nPress any key to continue...')

# ---------- Program Start ----------
if __name__ == "__main__":
    main_menu()