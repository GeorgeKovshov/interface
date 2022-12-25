from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

#r = IntVar()
#r = StringVar()
#r.set("2") # in tkinter you can "get" and you can "set" a variable

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

mainloop()