import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


# Function to connect to SQLite and create the transactions table if it doesn't exist
def create_db():
    conn = sqlite3.connect('purse pal.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_name TEXT,
            amount REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balance (
            id INTEGER PRIMARY KEY,
            balance REAL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO balance (id, balance) VALUES (1, 1000.0)
    ''')
    conn.commit()
    conn.close()


# Function to switch to the Send Money page
def show_send_money():
    for widget in main_content.winfo_children():
        widget.pack_forget()
    send_money_frame.pack(fill='both', expand=True)


# Function to switch to the Transactions page
def show_transactions():
    for widget in main_content.winfo_children():
        widget.pack_forget()
    transactions_frame.pack(fill='both', expand=True)
    refresh_transactions()


# Function to validate the amount
def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


# Function to handle sending money
def send_money():
    pursepal_id = pursepal_id_entry.get()
    amount = amount_entry.get()
    purpose = purpose_entry.get()
    remarks = remarks_entry.get("1.0", tk.END).strip()  # Get text from Text widget

    # Validate fields
    if not pursepal_id or not amount or not purpose or not remarks:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not is_valid_amount(amount):
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    amount = float(amount)

    # Connect to the database
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()

    # Get the current balance
    cursor.execute('SELECT balance FROM balance WHERE id=1')
    current_balance = cursor.fetchone()[0]

    if amount > current_balance:
        messagebox.showerror("Error", "Insufficient balance.")
        conn.close()
        return

    # Update the balance
    new_balance = current_balance - amount
    cursor.execute('UPDATE balance SET balance=? WHERE id=1', (new_balance,))
    conn.commit()

    # Insert transaction record
    insert_transaction(f"Sent to {pursepal_id}", -amount)  # Record as a negative amount for outgoing

    conn.close()

    # Success message
    messagebox.showinfo("Success", f"Money sent to {pursepal_id} successfully!")


# Function to insert a new transaction into the database
def insert_transaction(name, amount):
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (transaction_name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()
    refresh_transactions()  # Refresh the GUI after inserting


# Function to fetch all transactions from the database
def fetch_transactions():
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, transaction_name, amount FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Function to populate the list of transactions in the GUI
def populate_transactions():
    transactions = fetch_transactions()
    for transaction in transactions:
        tree.insert("", "end", values=(transaction[0], transaction[1], f"{transaction[2]:+.2f}"))


# Function to refresh the list of transactions in the GUI
def refresh_transactions():
    tree.delete(*tree.get_children())  # Clear the Treeview
    populate_transactions()  # Repopulate it with updated data


# Create the main application window
root = tk.Tk()
root.title("PursePal")
root.geometry("600x600")
root.config(bg='#f4f3f1')

# Main Content Frame
main_content = tk.Frame(root, bg='#f4f3f1')
main_content.pack(fill='both', expand=True)

# Sidebar
sidebar = tk.Frame(root, bg='#5e3b3b', width=150)
sidebar.pack(side='left', fill='y')

# Buttons for sidebar
tk.Button(sidebar, text="Send Money", command=show_send_money, bg='#5e3b3b', fg='white').pack(pady=10)
tk.Button(sidebar, text="Transactions", command=show_transactions, bg='#5e3b3b', fg='white').pack(pady=10)

# Send Money Frame
send_money_frame = tk.Frame(main_content, bg='#f4f3f1')

tk.Label(send_money_frame, text="Send Money", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1').pack(pady=20)

entry_settings = {
    'font': ('Jacques Francois', 14),
    'fg': '#4b2e2a',
    'bg': '#f4f3f1',
    'relief': 'solid',
    'borderwidth': 1,
    'highlightthickness': 0,
    'insertbackground': '#4b2e2a',
    'cursor': 'xterm',
    'width': 40
}

# Create Send Money form
tk.Label(send_money_frame, text="PursePal Id (mobile/email)", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1').pack(pady=(10, 0))
pursepal_id_entry = tk.Entry(send_money_frame, **entry_settings)
pursepal_id_entry.pack(pady=10)

tk.Label(send_money_frame, text="Amount", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1').pack(pady=(10, 0))
amount_entry = tk.Entry(send_money_frame, **entry_settings)
amount_entry.pack(pady=10)

tk.Label(send_money_frame, text="Purpose", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1').pack(pady=(10, 0))
purpose_entry = tk.Entry(send_money_frame, **entry_settings)
purpose_entry.pack(pady=10)

tk.Label(send_money_frame, text="Remarks", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1').pack(pady=(10, 0))
remarks_entry = tk.Text(send_money_frame, **entry_settings, height=5)
remarks_entry.pack(pady=10)

tk.Button(send_money_frame, text="Send", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=send_money).pack(pady=20)

# Transactions Frame
transactions_frame = tk.Frame(main_content, bg='#f4f3f1')

tk.Label(transactions_frame, text="Recent Transactions", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1').pack(pady=20)

columns = ('ID', 'Transaction', 'Amount')
tree = ttk.Treeview(transactions_frame, columns=columns, show='headings', height=15)
tree.heading('ID', text='ID')
tree.heading('Transaction', text='Transaction')
tree.heading('Amount', text='Amount')

tree.column("ID", width=50, anchor="center")
tree.column("Transaction", width=400, anchor="w")
tree.column("Amount", width=100, anchor="center")

tree.pack(padx=20, pady=20)

# Populate the table with transactions from the database
populate_transactions()

# Set the default view to Send Money
show_send_money()

# Start the GUI
root.mainloop()