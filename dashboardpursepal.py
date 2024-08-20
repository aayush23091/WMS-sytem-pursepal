import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
import sqlite3
import subprocess

# Function to set up the database and create the necessary tables
def setup_database():
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    
    # Create the balance table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance REAL,
            rewards REAL
        )
    ''')
    
    # Insert a default user if the table is empty
    cursor.execute('SELECT COUNT(*) FROM balance')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO balance (name, balance, rewards)
            VALUES ('User', 20000.00, 350.00) 
        ''')
    
    conn.commit()
    conn.close()

def update_balance():
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM balance WHERE id=1')  # Example user ID
    balance = cursor.fetchone()[0]
    conn.close()
    balance_label.config(text=f"Balance: NPR {balance:.2f}")
    
def fetch_user_data():
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name, balance, rewards FROM balance WHERE id=1')
    user_data = cursor.fetchone()
    
    conn.close()
    return user_data

def send_money():
    print("Send Money clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "sendmoneypursepal.py"]) 

def add_money():
    print("Add Money clicked")

def banking_service():
    print("Banking Service clicked")

def remittance():
    print("Remittance clicked")

def show_qr():
    print("Show QR clicked")

def topup_data():
    print("Topup & Data clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "topuppursepal.py"]) 

def pay_utilities():
    print("Water & Electricity clicked")

def internet_tv():
    print("Internet & TV clicked")

def airlines():
    print("Airlines clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "flightspursepal.py"]) 

def movies():
    print("Movies clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "movieticketpursepal.py"]) 

def bus_ticket():
    print("Bus Ticket clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "busticketpursepal.py"]) 

def hotel_booking():
    print("Hotel Booking clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "hotelpursepal.py"]) 

def education_fee():
    print("Education Fee clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "educationpursepal.py"]) 

def insurance():
    print("Insurance clicked")

def others():
    print("Others clicked")

def view_statement():
    print("View Statement clicked")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "transactionpursepal.py"]) 

def transaction_limit():
    print("Transaction Limit clicked")

def my_payments():
    print("My Payments clicked")

def support_call():
    print("Support & Call clicked")

def about_us():
    print("About Us clicked")

def settings():
    print("Settings clicked")

# Set up the database
setup_database()

# Initialize main window
root = tk.Tk()
root.title("Purse Pal Dashboard")
root.geometry("1200x800")
root.configure(bg='#5D2E2E')  # Main background color

# Load the Purse Pal logo image
logo_path = 'C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New python/pictures/1.jpg'  # Update with the correct image path
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Resize image
logo = ImageTk.PhotoImage(logo_image)

# Header Section
header_frame = tk.Frame(root, bg='#5D2E2E')
header_frame.pack(fill='x', pady=10)

# Logo and App Name
logo_label = tk.Label(header_frame, image=logo, bg='#5D2E2E')
logo_label.pack(side='left', padx=10)

app_name = tk.Label(header_frame, text="Purse Pal", font=("Arial", 30, "bold"), bg='#5D2E2E', fg='white')
app_name.pack(side='left', padx=10)

# Fetch user data
user_data = fetch_user_data()
if user_data:
    user_name, user_balance, user_rewards = user_data
else:
    user_name, user_balance, user_rewards = "User", 0.00, 0.00

# Right Side of Header
header_right_frame = tk.Frame(header_frame, bg='#5D2E2E')
header_right_frame.pack(side='right')

user_icon = tk.Label(header_right_frame, text="👤", font=("Arial", 25), bg='#5D2E2E', fg='white')
user_icon.pack(side='right', padx=5)

user_label = tk.Label(header_right_frame, text=f"Hello, {user_name}", font=("Arial", 20), bg='#5D2E2E', fg='white')
user_label.pack(side='right', padx=5)

# Balance and Reward Section
balance_frame = tk.Frame(root, bg='#845353')
balance_frame.pack(fill='x', pady=10, padx=20)

balance_label = tk.Label(balance_frame, text=f"NPR {user_balance:.2f}\nBalance", font=("Arial", 20, "bold"), bg='#845353', fg='white')
balance_label.pack(side='left', padx=20, pady=20)

eye_icon = tk.Label(balance_frame, text="👁", font=("Arial", 30), bg='#845353', fg='white')
eye_icon.pack(side='left', padx=20)

reward_label = tk.Label(balance_frame, text=f"{user_rewards:.2f}\nReward points", font=("Arial", 20, "bold"), bg='#845353', fg='white')
reward_label.pack(side='left', padx=20)

gift_icon = tk.Label(balance_frame, text="🎁", font=("Arial", 30), bg='#845353', fg='white')
gift_icon.pack(side='left', padx=20)

# Action Buttons Section
action_frame = tk.Frame(root, bg='#5D2E2E')
action_frame.pack(fill='x', pady=10)

button_texts = ["Send Money", "Add Money", "Banking Service", "Remittance", "Show QR"]
button_commands = [send_money, add_money, banking_service, remittance, show_qr]
for text, command in zip(button_texts, button_commands):
    btn = tk.Button(action_frame, text=text, font=("Arial", 15, "bold"), bg='#845353', fg='white', padx=20, pady=10, command=command)
    btn.pack(side='left', padx=20)

# Promotional Section
promo_frame = tk.Frame(root, bg='#5D2E2E')
promo_frame.pack(fill='x', pady=10, padx=20)

promo_image_path = 'C:/Users/ASUS/OneDrive/Desktop/codingpursepal/New python/pic2.0.png'  # Update with the correct image path
promo_image = Image.open(promo_image_path)
promo_image = promo_image.resize((250, 150), Image.LANCZOS)
promo_photo = ImageTk.PhotoImage(promo_image)

promo_label = tk.Label(promo_frame, image=promo_photo, bg='#5D2E2E')
promo_label.pack(side='left', padx=10)

promo_text = tk.Label(promo_frame, text="No Cash!\nNo Card!\nNo Worries\nWe got You 👍", font=("Arial", 20, "bold"), bg='#5D2E2E', fg='white', justify='left')
promo_text.pack(side='left', padx=20)

# Services Section
services_frame = tk.LabelFrame(root, text="*Our Services", font=("Arial", 20, "italic"), bg='#5D2E2E', fg='white', padx=20, pady=20)
services_frame.pack(fill='x', pady=20, padx=20)

service_texts = ["Topup & Data", "Water & Electricity", "Internet & TV", "Airlines", "Movies", "Bus Ticket", "Hotel Booking", "Education Fee", "Insurance", "Others"]
service_commands = [topup_data, pay_utilities, internet_tv, airlines, movies, bus_ticket, hotel_booking, education_fee, insurance, others]
for text, command in zip(service_texts, service_commands):
    btn = tk.Button(services_frame, text=text, font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=command)
    btn.pack(side='left', padx=20, pady=10)

# More Section (On the right side)
def open_more_popup():
    # Create a new Toplevel window for the popup
    more_popup = tk.Toplevel(root)
    more_popup.title("More Features")
    more_popup.geometry("400x600")
    more_popup.configure(bg='#5D2E2E')
    
    # Add a label to the popup
    tk.Label(more_popup, text="More Features", font=("Arial", 20, "bold"), bg='#5D2E2E', fg='white').pack(pady=10)
    
    # Create buttons for each feature in the popup
    more_buttons_texts = ["View Statement", "Transaction Limit", "My Payments", "Support & Call", "About Us", "Settings"]
    more_buttons_commands = [view_statement, transaction_limit, my_payments, support_call, about_us, settings]
    
    for text, command in zip(more_buttons_texts, more_buttons_commands):
        btn = tk.Button(more_popup, text=text, font=("Arial", 15), bg='#845353', fg='white', padx=10, pady=10, command=command)
        btn.pack(fill='x', pady=10, padx=20)
    
    # Add a close button
    close_button = tk.Button(more_popup, text="Close", font=("Arial", 15), bg='#845353', fg='white', command=more_popup.destroy)
    close_button.pack(pady=20)

# Main window setup and other UI components...

# Replace the 'More....' section with a single button
more_frame = tk.Frame(root, bg='#5D2E2E')
more_frame.pack(side='right', pady=20, padx=20)

more_button = tk.Button(more_frame, text="More....", font=("Arial", 20, "bold"), bg='#845353', fg='white', padx=20, pady=10, command=open_more_popup)
more_button.pack()

root.mainloop()