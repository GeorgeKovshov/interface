from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Main window")
root.geometry("400x400")#change window size

def show():
    myLabel = Label(root, text=var.get()).pack()

def show2():
    myLabel = Label(root, text=var2.get()).pack()

var = IntVar()
var2 = StringVar()
c = Checkbutton(root, text="Check this box!", variable=var).pack()
c2 = Checkbutton(root, text="Check this box22!", variable=var2, onvalue="On", offvalue="Off")
c2.deselect() #otherwise it glitches
c2.pack()


myButton = Button(root, text="Show Selection", command=show).pack()
myButton2 = Button(root, text="Show Selection22", command=show2).pack()

mainloop()