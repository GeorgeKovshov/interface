from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("working with images")
root.iconbitmap('N:/Git/interface/image.png')

my_img = ImageTk.PhotoImage(Image.open("bene gesserit.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("mentat.jpg"))

image_list = [my_img, my_img2]

#status = Label(root, text="Image 1 of 5")

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 2:
        button_forward = Button(root, text = ">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_num - 1))

    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<",command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda : forward(2))

button_quit = Button(root, text="exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_quit.grid(row=1, column=1)


root.mainloop()