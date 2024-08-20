from tkinter import *
from tkinter import messagebox
 
# Initialize the main window
root = Tk()
root.title("Movie Tickets")
root.geometry("800x600")  # Set the window size
 
# Set background color to brown
root.configure(bg='#5c352b')
 
# Create a Frame for the top search bar
top_frame = Frame(root, bg="#5c352b")
top_frame.pack(side=TOP, fill=X, pady=10)
 
# Add "MOVIE TICKETS:" label
label_title = Label(top_frame, text="MOVIE TICKETS:", bg="#5c352b", fg="white", font=("Helvetica", 18))
label_title.pack(side=LEFT, padx=10)
 
# Add a search box
search_var = StringVar()
search_entry = Entry(top_frame, textvariable=search_var, width=50)
search_entry.pack(side=LEFT, padx=10)
 
# Add a search button (dummy button for layout purposes)
search_button = Button(top_frame, text="🔍", width=3)
search_button.pack(side=LEFT)
 
# Create a Frame for movie posters
movies_frame = Frame(root, bg="#5c352b")
movies_frame.pack(pady=20)
 
# Define a function to handle poster clicks
def on_poster_click(movie_name):
    messagebox.showinfo("Movie Selected", f"You selected {movie_name}")
 
# Function to create movie poster and title
def create_movie_poster(image_path, title_text):
    # Movie poster frame
    movie_frame = Frame(movies_frame, bg="#5c352b")
    movie_frame.pack(side=LEFT, padx=10)
 
    # Load image (you should replace these with actual paths to the images)
    img = PhotoImage(file=image_path)
   
    # Movie poster label
    poster_label = Label(movie_frame, image=img, bg="#5c352b")
    poster_label.image = img  # Keep a reference to avoid garbage collection
    poster_label.pack()
 
    # Bind click event to the movie poster
    poster_label.bind("<Button-1>", lambda e: on_poster_click(title_text))
 
    # Movie title label
    movie_title = Label(movie_frame, text=title_text, font=("Helvetica", 12), bg="#5c352b", fg="white")
    movie_title.pack()
 
# Create posters (replace with actual image paths)
create_movie_poster(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\movie1.png", "Deadpool & Wolverine")
create_movie_poster(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\movie2.png","Stree2")
create_movie_poster(r"C:\Users\ASUS\OneDrive\Desktop\codingpursepal\New Python\pictures\movie3.png","Bulaki")
# Start the Tkinter event loop
root.mainloop()
