from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Look! I clicked a button!!")
    myLabel.pack()

#myButton = Button(root, text="Click me!", state=DISABLED)
myButton = Button(root, text="Click me!", command=myClick, padx=50, pady=50, fg="#ffffff", bg="black")
#padx and pady changes size of button
myButton.pack()

root.mainloop()