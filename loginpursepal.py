import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import subprocess  # Use subprocess to run another Python script

def add_placeholder(entry, placeholder_text, color):
    entry.insert(0, placeholder_text)
    entry['fg'] = color

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, 'end')
            entry['fg'] = 'black'

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry['fg'] = color

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def make_circle_image(image_path, size):
    image = Image.open(image_path).resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    circular_image = Image.new("RGBA", (size, size))
    circular_image.paste(image, (0, 0), mask=mask)
    return ImageTk.PhotoImage(circular_image)


def login_user():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or email == "Email":
        messagebox.showerror("Error", "Please enter your email.")
        return
    if password == "" or password == "Password":
        messagebox.showerror("Error", "Please enter your password.")
        return

    # Here, you would validate the user credentials
    # For demonstration, assume the credentials are correct
    print("User Logged In:")
    print(f"Email: {email}")
    print(f"Password: {password}")

    messagebox.showinfo("Success", "Login successful!")
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "dashboardpursepal.py"]) 

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

def go_to_register(event=None):
    root.destroy()  # Close the current login window
    subprocess.Popen(["python", "registerpursepal.py"])  # Launch the registration page script

def on_closing():
    root.destroy()

# Main application window
root = tk.Tk()
root.title("Purse Pal Login")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-fullscreen', True)

left_frame = tk.Frame(root, bg='#4b2e2a')
left_frame.pack(side='left', fill='both', expand=True)

image_path = r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pic2.0.png"
photo = make_circle_image(image_path, 500)

image_label = tk.Label(left_frame, image=photo, bg='#4b2e2a')
image_label.image = photo
image_label.pack(pady=20)

text_label = tk.Label(left_frame, text="Welcome Back!\nReady to Log In?", fg='white', bg='#4b2e2a', font=('Jacques Francois', 16))
text_label.pack(pady=20)

right_frame = tk.Frame(root, bg='#f4f3f1')
right_frame.pack(side='right', fill='both', expand=True)

logo_path = r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\1.jpg"
logo_image = Image.open(logo_path).resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(right_frame, image=logo_photo, bg='#f4f3f1')
logo_label.image = logo_photo
logo_label.place(x=20, y=20)

login_label = tk.Label(right_frame, text="Login", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
login_label.pack(anchor='n', pady=(80, 10))

register_link = tk.Label(right_frame, text="Go to Register ▸", font=('Jacques Francois', 12), fg='#4b2e2a', bg='#f4f3f1', cursor="hand2")
register_link.pack(anchor='ne', padx=20, pady=20)
register_link.bind("<Button-1>", go_to_register)  # Bind the click event to go to the registration page

form_frame = tk.Frame(right_frame, bg='#f4f3f1')
form_frame.pack(pady=20, padx=50, anchor='n')

# Load the icons
person_icon_path = r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\person.jpg"
person_icon = Image.open(person_icon_path).resize((20, 20), Image.LANCZOS)
person_icon_photo = ImageTk.PhotoImage(person_icon)

password_icon_path = r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\password.png"
password_icon = Image.open(password_icon_path).resize((20, 20), Image.LANCZOS)
password_icon_photo = ImageTk.PhotoImage(password_icon)

# Create entry fields with icons
email_entry = create_form_entry_with_icon("Email", person_icon_photo)
password_entry = create_form_entry_with_icon("Password", password_icon_photo)

login_button = tk.Button(form_frame, text="Login", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=login_user)
login_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
