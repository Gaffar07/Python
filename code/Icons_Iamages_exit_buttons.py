from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("icon example")
root.iconbitmap('F:/Python/venv/data/twitter.png')


my_img1=ImageTk.PhotoImage(Image.open("F:/Python/venv/data/1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("F:/Python/venv/data/2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("F:/Python/venv/data/3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("F:/Python/venv/data/4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("F:/Python/venv/data/5.jpg"))

my_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Image of 1 of "+str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)



my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global btnforward
    global btnback

    my_label.grid_forget()
    my_label=Label(image=my_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)
    btnforward=Button(root,text=">>",command=lambda:forward(image_number+1))
    btnback=Button(root,text="<<",command=lambda :backward(image_number-1))

    if image_number==5:
        btnforward =Button(root,text=">>",state=DISABLED)
    btnback.grid(row=1, column=0)
    btnforward.grid(row=1, column=2)

    status = Label(root, text="Image of "+str(image_number)+" of " + str(len(my_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def backward(image_number):
    global my_label
    global btnforward
    global btnback

    my_label.grid_forget()
    my_label = Label(image=my_list[image_number - 1])
    btnforward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    btnback = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number==1:
        btnback =Button(root,text="<<",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btnback.grid(row=1, column=0)
    btnforward.grid(row=1, column=2)

    status = Label(root, text="Image of " + str(image_number) + " of " + str(len(my_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

btnback=Button(root,text="<<",command=backward,state=DISABLED)
btnquit=Button(root,text="Exit Programe",command=root.quit)
btnforward=Button(root,text=">>",command=lambda:forward(2))


btnback.grid(row=1,column=0)
btnquit.grid(row=1,column=1)
btnforward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)







root.mainloop()
