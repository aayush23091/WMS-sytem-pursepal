import tkinter as tk
 
def search_hotel():
    city = city_entry.get()
    checkin_date = checkin_entry.get()
    checkout_date = checkout_entry.get()
    adults = adults_entry.get()
    children = children_entry.get()
    rooms = rooms_entry.get()
 
    # Handle the search functionality here
    # For now, let's print the details to the console
    print(f"Searching for hotels in {city} from {checkin_date} to {checkout_date}...")
    print(f"Adults: {adults}, Children: {children}, Rooms: {rooms}")
 
# Initialize the main window
root = tk.Tk()
root.title("Search Hotel")
root.geometry("800x400")
root.config(bg='#f4f3f1')
 
# Search Hotel Label
search_hotel_label = tk.Label(root, text="Search Hotel", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
search_hotel_label.pack(pady=20)
 
# Frame to contain the form elements
form_frame = tk.Frame(root, bg='#f4f3f1')
form_frame.pack(padx=20, pady=20)
 
# Select City Entry
city_label = tk.Label(form_frame, text="Select City", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
city_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky='w')
city_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
city_entry.grid(row=1, column=0, padx=10, pady=(0, 10), ipady=5)
 
# CheckIn Date Entry
checkin_label = tk.Label(form_frame, text="CheckIn Date", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
checkin_label.grid(row=0, column=1, padx=10, pady=(0, 10), sticky='w')
checkin_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
checkin_entry.grid(row=1, column=1, padx=10, pady=(0, 10), ipady=5)
 
# CheckOut Date Entry
checkout_label = tk.Label(form_frame, text="CheckOut Date", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
checkout_label.grid(row=0, column=2, padx=10, pady=(0, 10), sticky='w')
checkout_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
checkout_entry.grid(row=1, column=2, padx=10, pady=(0, 10), ipady=5)
 
# Adults Entry
adults_label = tk.Label(form_frame, text="Adults", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
adults_label.grid(row=2, column=0, padx=10, pady=(20, 10), sticky='w')
adults_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
adults_entry.grid(row=3, column=0, padx=10, pady=(0, 10), ipady=5)
 
# Children Entry
children_label = tk.Label(form_frame, text="Children", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
children_label.grid(row=2, column=1, padx=10, pady=(20, 10), sticky='w')
children_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
children_entry.grid(row=3, column=1, padx=10, pady=(0, 10), ipady=5)
 
# Rooms Entry
rooms_label = tk.Label(form_frame, text="Rooms", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
rooms_label.grid(row=2, column=2, padx=10, pady=(20, 10), sticky='w')
rooms_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=20)
rooms_entry.grid(row=3, column=2, padx=10, pady=(0, 10), ipady=5)
 
# Search Button
search_button = tk.Button(root, text="Search", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=search_hotel)
search_button.pack(pady=20)
 
# Run the application
root.mainloop()