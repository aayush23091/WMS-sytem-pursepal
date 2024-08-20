from tkinter import *
from PIL import Image, ImageTk
 
root = Tk()
root.geometry("800x600")
root.configure(bg='#d3d3d3')
 
root.title("Search Your Education Institution")
 
title_label = Label(root, text="Search Your Education Institution", font=("Jacques Francois", 30), bg='#d3d3d3', fg="#5b3636")
title_label.pack(pady=20)
 
# Load images
image1 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\Softwarica.jpg")
image2 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\Deerwalk.jpg")
image3 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\paragon.jpg")
 
# Resize images with larger dimensions (200x200)
image1 = image1.resize((200, 200), Image.LANCZOS)  # If using Pillow 9.0.0+, use Image.Resampling.LANCZOS
image2 = image2.resize((200, 200), Image.LANCZOS)  # If using Pillow 9.0.0+, use Image.Resampling.LANCZOS
image3 = image3.resize((200, 200), Image.LANCZOS)  # If using Pillow 9.0.0+, use Image.Resampling.LANCZOS
 
# Convert images to PhotoImage
image1 = ImageTk.PhotoImage(image1)
image2 = ImageTk.PhotoImage(image2)
image3 = ImageTk.PhotoImage(image3)
 
# Create label for School/College Name
label_name = Label(root, text="School/College Name", font=("Jacques Francois", 18), bg='#d3d3d3', fg="#5b3636")
label_name.pack()
 
# Create entry box for School/College Name
entry_name = Entry(root, width=40, font=("Jacques Francois", 18))
entry_name.pack(pady=10)
 
# Create label for School/College List
label_list = Label(root, text="School / College List", font=("Jacques Francois", 18), bg='#d3d3d3', fg="#5b3636")
label_list.pack(pady=10)
 
# Create image labels
image_label1 = Label(root, image=image1)
image_label1.pack(side=LEFT, padx=10)
 
image_label2 = Label(root, image=image2)
image_label2.pack(side=LEFT, padx=10)
 
image_label3 = Label(root, image=image3)
image_label3.pack(side=LEFT, padx=10)
 
root.mainloop()