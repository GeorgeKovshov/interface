from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("working with images")
root.iconbitmap('N:/Git/interface/image.png')

my_img = ImageTk.PhotoImage(Image.open("bene gesserit.jpg"))
my_label = Label(image=my_img)
my_label.pack()





button_quit = Button(root, text="exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
