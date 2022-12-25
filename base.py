from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
def open():
    top = Toplevel()
    top.title("mentat")
    global my_img
    my_img = ImageTk.PhotoImage(Image.open("mentat.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="open second window", command=open).pack()


#lbl = Label(top, text="Hello World").pack()


mainloop()