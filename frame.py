from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

frame = LabelFrame(root, text="this is my frame", padx=5, pady=5) #background="blue")
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click!")
b2 = Button(frame, text="Don't click Here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()