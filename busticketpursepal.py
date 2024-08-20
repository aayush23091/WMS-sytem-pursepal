import tkinter as tk
 
def search_bus_tickets():
    from_location = from_entry.get()
    to_location = to_entry.get()
    departure_date = departure_entry.get()
 
    # Handle the search functionality here
    # For now, let's print the details to the console
    print(f"Searching for buses from {from_location} to {to_location} on {departure_date}...")
 
# Initialize the main window
root = tk.Tk()
root.title("Bus Ticket")
root.geometry("800x300")
root.config(bg='#f4f3f1')
 
# Bus Ticket Label
bus_ticket_label = tk.Label(root, text="Bus Ticket", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
bus_ticket_label.pack(pady=20)
 
# Frame to contain the form elements
form_frame = tk.Frame(root, bg='#f4f3f1')
form_frame.pack(padx=20, pady=20)
 
# From Entry
from_label = tk.Label(form_frame, text="From", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
from_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky='w')
from_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
from_entry.grid(row=1, column=0, padx=10, pady=(0, 10), ipady=5)
 
# To Entry
to_label = tk.Label(form_frame, text="To", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
to_label.grid(row=0, column=1, padx=10, pady=(0, 10), sticky='w')
to_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
to_entry.grid(row=1, column=1, padx=10, pady=(0, 10), ipady=5)
 
# Departure Entry
departure_label = tk.Label(form_frame, text="Departure", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
departure_label.grid(row=0, column=2, padx=10, pady=(0, 10), sticky='w')
departure_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
departure_entry.grid(row=1, column=2, padx=10, pady=(0, 10), ipady=5)
 
# Search Button
search_button = tk.Button(root, text="Search", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=search_bus_tickets)
search_button.pack(pady=20)
 
# Run the application
root.mainloop()