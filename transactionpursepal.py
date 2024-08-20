import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


# Database Operations
def create_db():
    """Connect to SQLite and create the transactions table if it doesn't exist."""
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_name TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_transaction(name, amount):
    """Insert a new transaction into the database."""
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (transaction_name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()
    refresh_transactions()

def update_transaction(transaction_id, new_name, new_amount):
    """Update an existing transaction in the database."""
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET transaction_name = ?, amount = ? WHERE id = ?", (new_name, new_amount, transaction_id))
    conn.commit()
    conn.close()
    refresh_transactions()

def delete_transaction(transaction_id):
    """Delete a transaction from the database."""
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    refresh_transactions()

def fetch_transactions():
    """Fetch all transactions from the database."""
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, transaction_name, amount FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows


# GUI Operations
def populate_transactions():
    """Populate the list of transactions in the GUI."""
    transactions = fetch_transactions()
    for transaction in transactions:
        tree.insert("", "end", values=(transaction[0], transaction[1], f"{transaction[2]:+.2f}"))

def refresh_transactions():
    """Refresh the list of transactions in the GUI."""
    tree.delete(*tree.get_children())
    populate_transactions()

def on_select(event):
    """Handle selecting a transaction."""
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        transaction_id, transaction_name, amount = item["values"]
        transaction_id_var.set(transaction_id)
        transaction_name_var.set(transaction_name)
        amount_var.set(amount)

def on_add():
    """Handle adding a new transaction."""
    new_name = transaction_name_entry.get()
    try:
        new_amount = float(amount_entry.get())
        if new_name:
            insert_transaction(new_name, new_amount)
            messagebox.showinfo("Success", "Transaction added successfully!")
        else:
            messagebox.showwarning("Error", "Please enter a transaction name!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")

def on_update():
    """Handle updating a transaction."""
    try:
        transaction_id = transaction_id_var.get()
        new_name = transaction_name_entry.get()
        new_amount = float(amount_entry.get())
        if transaction_id and new_name and new_amount:
            update_transaction(transaction_id, new_name, new_amount)
            messagebox.showinfo("Success", "Transaction updated successfully!")
        else:
            messagebox.showwarning("Error", "Please fill out all fields!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")

def on_delete():
    """Handle deleting a transaction."""
    transaction_id = transaction_id_var.get()
    if transaction_id:
        delete_transaction(transaction_id)
        messagebox.showinfo("Success", "Transaction deleted successfully!")
    else:
        messagebox.showwarning("Error", "Please select a transaction to delete!")


# GUI Setup
def create_ui():
    """Set up the graphical user interface."""
    root = tk.Tk()
    root.title("Purse Pal")
   
    # Set window size to match screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(bg='#5e3b3b')

    # Sidebar
    sidebar = tk.Frame(root, bg='#5e3b3b', width=150, height=screen_height)
    sidebar.pack(side='left', fill='y')

    # Load images
    try:
        logo_image = tk.PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/codeforpursepal/python/picture/1.png")
        home_icon = tk.PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New Python/picture/home.png")
        statement_icon = tk.PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New Python/picture/Evaluation.png")
        contact_icon = tk.PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New Python/picture/phone.png")
        settings_icon = tk.PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New Python/picture/setting.png")
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Error loading images: {e}")
        return

    # Keep references to prevent garbage collection
    root.logo_image = logo_image
    root.home_icon = home_icon
    root.statement_icon = statement_icon
    root.contact_icon = contact_icon
    root.settings_icon = settings_icon

    # Purse Pal logo
    logo_label = tk.Label(sidebar, image=logo_image, bg='#5e3b3b')
    logo_label.pack(pady=10)

    # Sidebar buttons with icons
    buttons_info = [
        ("HOME", home_icon),
        ("STATEMENT", statement_icon),
        ("CONTACT", contact_icon),
        ("SETTINGS", settings_icon),
    ]
    for text, icon in buttons_info:
        button = tk.Button(sidebar, text=text, image=icon, compound='left', bg='#5e3b3b', fg='white', font=('Jacques Francois', 12), borderwidth=0)
        button.pack(pady=10)

    # Main Content
    main_content = tk.Frame(root, bg='#5e3b3b')
    main_content.pack(side='right', fill='both', expand=True)

    # Statement Section
    statement_label = tk.Label(main_content, text="STATEMENT", bg='#5e3b3b', fg='white', font=('Jacques Francois', 45))
    statement_label.grid(row=0, column=0, sticky='w', pady=10, padx=20)

    balance_frame = tk.Frame(main_content, bg='#5e3b3b')
    balance_frame.grid(row=1, column=0, sticky='w', pady=10, padx=20)

    balance_label = tk.Label(balance_frame, text="NPR XXXX.XX", bg='#5e3b3b', fg='white', font=('Jacques Francois', 20))
    balance_label.pack(side='left')

    refresh_button = tk.Button(balance_frame, text="↻", bg='#5e3b3b', fg='white', font=('Jacques Francois', 20), borderwidth=0, command=refresh_transactions)
    refresh_button.pack(side='left', padx=10)

    # Recent Transactions
    recent_transactions_label = tk.Label(main_content, text="RECENT TRANSACTIONS", bg='#5e3b3b', fg='white', font=('Jacques Francois', 45))
    recent_transactions_label.grid(row=2, column=0, sticky='w', pady=10, padx=20)

    # Table for transactions
    columns = ('ID', 'Transaction', 'Amount')
    global tree
    tree = ttk.Treeview(main_content, columns=columns, show='headings', height=5)
    tree.heading('ID', text='ID')
    tree.heading('Transaction', text='Transaction')
    tree.heading('Amount', text='Amount')

    tree.column("ID", width=50, anchor="center")
    tree.column("Transaction", width=400, anchor="w")
    tree.column("Amount", width=100, anchor="center")

    tree.grid(row=3, column=0, sticky='nsew', padx=20, pady=10)

    # Bind treeview selection event+++++++
    tree.bind("<<TreeviewSelect>>", on_select)

    # Form for adding/updating transactions
    form_frame = tk.Frame(main_content, bg='#5e3b3b')
    form_frame.grid(row=4, column=0, pady=20, padx=20, sticky='w')

    global transaction_id_var, transaction_name_var, amount_var
    transaction_id_var = tk.IntVar()
    transaction_name_var = tk.StringVar()
    amount_var = tk.StringVar()

    tk.Label(form_frame, text="Transaction ID (Auto):", bg='#5e3b3b', fg='white').grid(row=0, column=0, sticky='w')
    transaction_id_entry = tk.Entry(form_frame, textvariable=transaction_id_var, state='readonly')
    transaction_id_entry.grid(row=0, column=1)

    tk.Label(form_frame, text="Transaction Name:", bg='#5e3b3b', fg='white').grid(row=1, column=0, sticky='w')
    transaction_name_entry = tk.Entry(form_frame, textvariable=transaction_name_var)
    transaction_name_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Amount:", bg='#5e3b3b', fg='white').grid(row=2, column=0, sticky='w')
    amount_entry = tk.Entry(form_frame, textvariable=amount_var)
    amount_entry.grid(row=2, column=1, pady=5)

    button_frame = tk.Frame(form_frame, bg='#5e3b3b')
    button_frame.grid(row=3, column=1, pady=10, sticky='w')

    add_button = tk.Button(button_frame, text="Add", bg='#5e3b3b', fg='white', command=on_add)
    add_button.grid(row=0, column=0, padx=5)

    update_button = tk.Button(button_frame, text="Update", bg='#5e3b3b', fg='white', command=on_update)
    update_button.grid(row=0, column=1, padx=5)

    delete_button = tk.Button(button_frame, text="Delete", bg='#5e3b3b', fg='white', command=on_delete)
    delete_button.grid(row=0, column=2, padx=5)

    # Populate transactions on startup
    populate_transactions()

    # Run the application
    root.mainloop()


if __name__ == "_main_":
    create_db()
create_ui()