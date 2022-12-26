from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Main window")
root.geometry("400x400")#change window size

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("choose day of the week")

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

#drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()