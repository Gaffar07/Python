from tkinter import *
from yahoo_fin import stock_info as sp



try:
    root=Tk()
    root.title("simple calculator")
    e=Entry(root,width=35,borderwidth=5)
    e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    # l1=Label(root,text="Enter scrip Name")
    def buttonclick(number):
        #e.delete(0,END)
        current=e.get()
        e.delete(0, END)
        e.insert(0,str(current)+str(number))
    def buttonclear():
         e.delete(0, END)
    def buttonadd():
        fnumber=e.get()
        # if x==None:
        #     e.insert(0,"provode any value")
        global f_number
        global math
        math="addition"
        f_number=int(fnumber)
        e.delete(0, END)
    def buttonequal():
        snumber=e.get()
        e.delete(0, END)
        if math=="addition":
            e.insert(0,f_number+int(snumber))
        if math=="subtraction":
            e.insert(0,f_number-int(snumber))
        if math=="multiplication":
            e.insert(0,f_number*int(snumber))
        if math == "division":
            e.insert(0, f_number / int(snumber))
    def btnsub():
        fnumber = e.get()
        # if x==None:
        #     e.insert(0,"provode any value")
        global f_number
        global math
        math = "subtraction"
        f_number = int(fnumber)
        e.delete(0, END)
    def btnmul():
        fnumber = e.get()
        # if x==None:
        #     e.insert(0,"provode any value")
        global f_number
        global math
        math = "multiplication"
        f_number = int(fnumber)
        e.delete(0, END)
    def btndiv():
        fnumber = e.get()
        # if x==None:
        #     e.insert(0,"provode any value")
        global f_number
        global math
        math = "division"
        f_number = int(fnumber)
        e.delete(0, END)

    btn1=  Button(root,text="1",padx=40,pady=20,command=lambda :buttonclick(1))
    btn2 = Button(root, text="2", padx=40, pady=20, command=lambda :buttonclick(2))
    btn3 = Button(root, text="3", padx=40, pady=20, command=lambda :buttonclick(3))
    btn4 = Button(root, text="4", padx=40, pady=20, command=lambda :buttonclick(4))
    btn5 = Button(root, text="5", padx=40, pady=20, command=lambda :buttonclick(5))
    btn6 = Button(root, text="6", padx=40, pady=20, command=lambda :buttonclick(6))
    btn7 = Button(root, text="7", padx=40, pady=20, command=lambda :buttonclick(7))
    btn8 = Button(root, text="8", padx=40, pady=20, command=lambda :buttonclick(8))
    btn9 = Button(root, text="9", padx=40, pady=20, command=lambda :buttonclick(9))
    btn0 = Button(root, text="0", padx=40, pady=20, command=lambda :buttonclick(0))


    btnadd = Button(root, text="+", padx=39, pady=20, command=buttonadd)
    btnequal = Button(root, text="=", padx=40, pady=20, command=buttonequal)
    btnclear = Button(root, text="C", padx=40, pady=20, command=buttonclear)

    btnsub = Button(root, text="-", padx=39, pady=20,command=btnsub)
    btnmul = Button(root, text="*", padx=39, pady=20,command=btnmul)
    btndiv = Button(root, text="/", padx=39, pady=20,command=btndiv)

#put btn oomn screen
    btn1.grid(row=3,column=0)
    btn2.grid(row=3, column=1)
    btn3.grid(row=3, column=2)

    btn4.grid(row=2, column=0)
    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)

    btn7.grid(row=1, column=0)
    btn8.grid(row=1, column=1)
    btn9.grid(row=1, column=2)

    btn0.grid(row=4, column=1)
    btnclear.grid(row=4, column=0)
    btnequal.grid(row=4, column=2)


    btnadd.grid(row=5, column=0)


    btnsub.grid(row=6,column=0)
    btnmul.grid(row=6,column=1)
    btndiv.grid(row=5,column=1)




except:
    raise TypeError("scrip name not found")

root.mainloop()










