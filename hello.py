from tkinter import *

root = Tk()
#create a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is John Elder")

#shoving it onto the screen
#myLabel.pack

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
root.mainloop()