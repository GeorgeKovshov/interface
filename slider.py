from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Main window")
#root.geometry("200x200")#change window size

def slide1(var):
    #my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(vertical.get()) + "x400")

vertical = Scale(root, from_=0, to=200, command=slide1)
vertical.pack() #sliders NEED to BE PACKED IN THEIR OWN LINE! LIKE HERE.

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()
def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

my_btn = Button(root, text="click me!", command=slide).pack()

root.mainloop()