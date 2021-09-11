import tkinter as tkr
cal = tkr.Tk(__name__) 
cal.title("My Calculator")
cal.geometry("400x400")

a=tkr.Variable(cal)
b=tkr.Variable(cal)
c=tkr.Variable(cal)


tkr.Label(cal,text="Basic Calculator!").pack()
tkr.Label(cal,text="Enter 1st operand").place(x=10,y=30)
tkr.Label(cal,text="Enter 2nd operand").place(x=250,y=30)
tkr.Label(cal,text="Operators").place(x=150,y=100)
tkr.Label(cal,text="Result :").place(x=10,y=200)
tkr.Label(cal,textvariable=c).place(x=50,y=200)


tkr.Entry(cal,textvariable = a).place(x=10,y=50)
tkr.Entry(cal,textvariable = b).place(x=250,y=50)

def oper1():
    print("First number is:",a.get())
    print(" Operator is : "+")
    print("Second number is:",b.get())
    print(int(a.get())+int(b.get()))
    c.set(int(a.get())+int(b.get()))

def oper2():
    print("First number is:",a.get())
    print(" Operator is : "-")
    print("Second number is:",b.get())
    print(int(a.get())-int(b.get()))
    c.set(int(a.get())-int(b.get()))

def oper3():
    print("First number is:",a.get())
    print(" Operator is : "*")
    print("Second number is:",b.get())
    print(int(a.get())*int(b.get()))
    c.set(int(a.get())*int(b.get()))

def oper4():
    print("First number is:",a.get())
    print(" Operator is : "/")
    print("Second number is:",b.get())
    print(int(a.get())/int(b.get()))
    c.set(int(a.get())/int(b.get())) 


tkr.Button(cal,text="+",command=oper1).place(x=130,y=120)
tkr.Button(cal,text="-",command=oper2).place(x=160,y=120)
tkr.Button(cal,text="*",command=oper3).place(x=190,y=120)
tkr.Button(cal,text="/",command=oper4).place(x=220,y=120)

cal.mainloop()

