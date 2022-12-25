from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello world!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()