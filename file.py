from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Main window")

'''
root.filename = filedialog.askopenfilename(initialdir="N:/Git/interface", title="select a file",
                                           filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()
my_image=ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()
'''
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="N:/Git/interface", title="select a file",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text="Open file", command=open).pack()

mainloop()