import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Flight Booking")
root.geometry("550x500")
root.configure(bg='#643c3c')

# Title Label
title_label = tk.Label(root, text="Flight", font=("Arial", 16, "bold"), bg='#643c3c', fg="white")
title_label.pack(pady=10)

# Frame for flight type selection
flight_type_frame = tk.Frame(root, bg='#643c3c')
flight_type_frame.pack(pady=5)

flight_type_label = tk.Label(flight_type_frame, text="Book Domestic Flight", bg='#643c3c', fg="white")
flight_type_label.grid(row=0, column=0, columnspan=2)

# Radio buttons for flight type
flight_type = tk.StringVar(value="One Way")
one_way_radio = tk.Radiobutton(flight_type_frame, text="One Way", variable=flight_type, value="One Way", bg='#643c3c', fg="white", selectcolor='#643c3c')
return_radio = tk.Radiobutton(flight_type_frame, text="Return", variable=flight_type, value="Return", bg='#643c3c', fg="white", selectcolor='#643c3c')

one_way_radio.grid(row=1, column=0, padx=10)
return_radio.grid(row=1, column=1, padx=10)

# Frame for form inputs
form_frame = tk.Frame(root, bg='#643c3c')
form_frame.pack(pady=10)

# 'From' Label and Combobox
from_label = tk.Label(form_frame, text="From", bg='#643c3c', fg="white")
from_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
from_combobox = ttk.Combobox(form_frame)
from_combobox.grid(row=0, column=1, pady=5)

# 'To' Label and Combobox
to_label = tk.Label(form_frame, text="To", bg='#643c3c', fg="white")
to_label.grid(row=0, column=2, sticky='w', padx=10, pady=5)
to_combobox = ttk.Combobox(form_frame)
to_combobox.grid(row=0, column=3, pady=5)

# 'Departure Date' Label and Entry
departure_label = tk.Label(form_frame, text="Departure Date", bg='#643c3c', fg="white")
departure_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
departure_entry = tk.Entry(form_frame)
departure_entry.grid(row=1, column=1, pady=5)

# 'Adult' Label and Entry
adult_label = tk.Label(form_frame, text="Adult", bg='#643c3c', fg="white")
adult_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
adult_entry = tk.Entry(form_frame)
adult_entry.grid(row=2, column=1, pady=5)

# 'Child' Label and Entry
child_label = tk.Label(form_frame, text="Child", bg='#643c3c', fg="white")
child_label.grid(row=2, column=2, sticky='w', padx=10, pady=5)
child_entry = tk.Entry(form_frame)
child_entry.grid(row=2, column=3, pady=5)

# Search Button
search_button = tk.Button(root, text="Search", bg="white", fg="#643c3c")
search_button.pack(pady=20)

# Run the application
root.mainloop()