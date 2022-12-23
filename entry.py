from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=10)
e.pack()
#e.get() #gets what the user has typed
e.insert(0, "Enter Your Name")

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

#myButton = Button(root, text="Click me!", state=DISABLED)
myButton = Button(root, text="Enter Your Name", command=myClick, padx=50, pady=50, fg="#ffffff", bg="black")
#padx and pady changes size of button
myButton.pack()

root.mainloop()