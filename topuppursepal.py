import tkinter as tk
from tkinter import messagebox
 
def proceed_topup():
    mobile_number = mobile_number_entry.get()
    operator = operator_var.get()
 
    if not mobile_number or not operator:
        messagebox.showerror("Error", "Please enter the mobile number and select an operator.")
        return
 
    # Handle the mobile topup functionality here
    messagebox.showinfo("Success", f"Topup initiated for {operator} number {mobile_number}!")
 
# Initialize the main window
root = tk.Tk()
root.title("Mobile Topup")
root.geometry("500x350")
root.config(bg='#f4f3f1')
 
# Mobile Topup Label
mobile_topup_label = tk.Label(root, text="Mobile Topup", font=('Jacques Francois', 24), fg='#4b2e2a', bg='#f4f3f1')
mobile_topup_label.pack(pady=20)
 
# Frame to contain the form elements
form_frame = tk.Frame(root, bg='#f4f3f1')
form_frame.pack(padx=20, pady=20)
 
# Mobile Number Entry
mobile_number_label = tk.Label(form_frame, text="Mobile Number", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1')
mobile_number_label.grid(row=0, column=0, sticky='w', pady=(0, 10))
mobile_number_entry = tk.Entry(form_frame, font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', relief='solid', borderwidth=1, width=35)
mobile_number_entry.grid(row=1, column=0, pady=(0, 10), ipady=5)
 
# Operator selection buttons
operator_var = tk.StringVar(value="")
 
ntc_button = tk.Radiobutton(form_frame, text="NTC", variable=operator_var, value="NTC", font=('Jacques Francois', 12), fg='#4b2e2a', bg='#f4f3f1', selectcolor='#e8e8e8', indicatoron=0, width=10)
ntc_button.grid(row=2, column=0, sticky='w', pady=(0, 10))
 
ncell_button = tk.Radiobutton(form_frame, text="Ncell", variable=operator_var, value="Ncell", font=('Jacques Francois', 12), fg='#4b2e2a', bg='#f4f3f1', selectcolor='#e8e8e8', indicatoron=0, width=10)
ncell_button.grid(row=2, column=0, sticky='e', pady=(0, 10))
 
# Proceed Button
proceed_button = tk.Button(root, text="Proceed", font=('Jacques Francois', 14), fg='#4b2e2a', bg='#f4f3f1', borderwidth=1, relief='solid', command=proceed_topup)
proceed_button.pack(pady=20)
 
# Run the application
root.mainloop()