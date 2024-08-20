import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import sqlite3
import os
import subprocess

# Placeholder functionality
def add_placeholder(entry, placeholder_text, color):
    entry.insert(0, placeholder_text)
    entry['fg'] = color

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, 'end')
            entry['fg'] = 'black'

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry['fg'] = color

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Circular image function
def make_circle_image(image_path, size):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    image = Image.open(image_path).resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    circular_image = Image.new("RGBA", (size, size))
    circular_image.paste(image, (0, 0), mask=mask)
    return ImageTk.PhotoImage(circular_image)

# Close window function
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Function to go to login page
def go_to_login(event=None):
    root.destroy()  # Close the current registration window
    subprocess.Popen(["python", "loginpursepal.py"])  # Import the login page module (assuming the login page is in 'login_page.py')

# Register user function
def register_user():
    full_name = full_name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if (not full_name or full_name == "Full Name" or
        not email or email == "Email" or
        not mobile or mobile == "Mobile Number" or
        not dob or dob == "Date of Birth" or
        not gender or
        not password or password == "Password" or
        not confirm_password or confirm_password == "Confirm Password"):

        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # Save user info to the database
    try:
        conn = sqlite3.connect('pursepal.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY,
                          full_name TEXT NOT NULL,
                          email TEXT NOT NULL,
                          mobile TEXT NOT NULL,
                          dob TEXT NOT NULL,
                          gender TEXT NOT NULL,
                          password TEXT NOT NULL)''')

        cursor.execute('''INSERT INTO users (full_name, email, mobile, dob, gender, password)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (full_name, email, mobile, dob, gender, password))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Registration successful!")
        root.destroy()
        go_to_login()  # Go to login page after successful registration
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# Create form entry with icon
def create_form_entry_with_icon(placeholder_text, icon_photo):
    entry_frame = tk.Frame(form_frame, bg='#f4f3f1')
    entry_frame.pack(fill='x', pady=10)

    icon_label = tk.Label(entry_frame, image=icon_photo, bg='#f4f3f1')
    icon_label.pack(side='left', padx=(0, 10))

    entry = tk.Entry(entry_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', highlightthickness=0, relief='flat', bd=0)
    entry.pack(side='left', fill='x', expand=True)

    add_placeholder(entry, placeholder_text, 'grey')

    line = tk.Frame(form_frame, height=2, bg='#4b2e2a')
    line.pack(fill='x', pady=(0, 10))

    return entry

# Initialize main window
root = tk.Tk()
root.title("Purse Pal Registration")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-fullscreen', True)

# Left frame (image and text)
left_frame = tk.Frame(root, bg='#4b2e2a')
left_frame.pack(side='left', fill='both', expand=True)

# Update the image path
image_path = r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pic2.0.png"
photo = make_circle_image(image_path, 500)

image_label = tk.Label(left_frame, image=photo, bg='#4b2e2a')
image_label.image = photo
image_label.pack(pady=20)

text_label = tk.Label(left_frame, text="No Cash!\nNo Card!\nNo Worries\nWe got You 👍\nWelcome to PursePal 🙏", fg='white', bg='#4b2e2a', font=('Jacques Francois', 16))
text_label.pack(pady=20)

# Right frame (form)
right_frame = tk.Frame(root, bg='#f4f3f1')
right_frame.pack(side='right', fill='both', expand=True)

# Update the logo image path
logo_path = r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\picture\1.png"
if not os.path.exists(logo_path):
    raise FileNotFoundError(f"Logo image not found: {logo_path}")

logo_image = Image.open(logo_path).resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(right_frame, image=logo_photo, bg='#f4f3f1')
logo_label.image = logo_photo
logo_label.place(x=20, y=20)

register_label = tk.Label(right_frame, text="Register", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
register_label.pack(anchor='n', pady=(80, 10))

# Create the "Go to Login" link with the click event
login_link = tk.Label(right_frame, text="Go to Login ▸", font=('Jacques Francois', 12), fg='#4b2e2a', bg='#f4f3f1', cursor="hand2")
login_link.pack(anchor='ne', padx=20, pady=20)
login_link.bind("<Button-1>", go_to_login)  # Bind the click event to go to the login page

form_frame = tk.Frame(right_frame, bg='#f4f3f1')
form_frame.pack(pady=20, padx=50, anchor='n')

# Load icons for form fields
def load_icon(icon_path):
    if not os.path.exists(icon_path):
        raise FileNotFoundError(f"Icon not found: {icon_path}")
    return ImageTk.PhotoImage(Image.open(icon_path).resize((20, 20), Image.LANCZOS))

person_icon_photo = load_icon(r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pictures\person.jpg")
email_icon_photo = load_icon(r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pictures\email.jpg")
mobile_icon_photo = load_icon(r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pictures\phone.jpg")
dob_icon_photo = load_icon(r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pictures\dob.jpg")
password_icon_photo = load_icon(r"C:\Users\ASUS\OneDrive\Desktop\codeforpursepal\python\pictures\password.png")

# Create entry fields with icons
full_name_entry = create_form_entry_with_icon("Full Name", person_icon_photo)
email_entry = create_form_entry_with_icon("Email", email_icon_photo)
mobile_entry = create_form_entry_with_icon("Mobile Number", mobile_icon_photo)
dob_entry = create_form_entry_with_icon("Date of Birth", dob_icon_photo)

# Gender selection
gender_label = tk.Label(form_frame, text="Gender", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
gender_label.pack(anchor='w', pady=(10, 5))
gender_frame = tk.Frame(form_frame, bg='#f4f3f1')
gender_frame.pack(anchor='w', pady=10)

genders = ["Male", "Female", "Other"]
gender_var = tk.StringVar()

for gender in genders:
    rb = tk.Radiobutton(gender_frame, text=gender, variable=gender_var, value=gender, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', selectcolor='#f4f3f1')
    rb.pack(side='left', padx=10)

# Password fields
password_entry = create_form_entry_with_icon("Password", password_icon_photo)
confirm_password_entry = create_form_entry_with_icon("Confirm Password", password_icon_photo)

# Join button
join_button = tk.Button(form_frame, text="Join", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=register_user)
join_button.pack(pady=20)

# Protocol for closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
