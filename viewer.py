from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("working with images")
root.iconbitmap('N:/Git/interface/image.png')

my_img = ImageTk.PhotoImage(Image.open("bene gesserit.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("mentat.jpg"))

image_list = [my_img, my_img2]

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<")
button_forward = Button(root, text=">>")

button_quit = Button(root, text="exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_quit.grid(row=1, column=1)


root.mainloop()