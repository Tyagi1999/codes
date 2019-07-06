from tkinter import*
tk=Tk()
eq=""
equation=StringVar()
calculation=Label(tk,textvariable=equation)
equation.set("ENTER YOUR EQUATION:")
calculation.grid(columnspan=4)
def btnpress(n):
    global eq
    eq=eq+str(n)
    equation.set(eq)
def equalpress():
    global eq
    result=str(eval(eq))
    equation.set(result)
    eq=""
def clear():
    global eq
    eq=""
    equation.set("")

b1=Button(tk,text="1",font=("Times",20),command=lambda:btnpress(1),fg="red")
b1.grid(row=2,column=0)
b2=Button(tk,text="2",font=("Times",20),command=lambda:btnpress(2),fg="red")
b2.grid(row=2,column=1)
b3=Button(tk,text="3",font=("Times",20),command=lambda:btnpress(3),fg="red")
b3.grid(row=2,column=2)
b4=Button(tk,text="4",font=("Times",20),command=lambda:btnpress(4),fg="red")
b4.grid(row=3,column=0)
b5=Button(tk,text="5",font=("Times",20),command=lambda:btnpress(5),fg="red")
b5.grid(row=3,column=1)
b6=Button(tk,text="6",font=("Times",20),command=lambda:btnpress(6),fg="red")
b6.grid(row=3,column=2)
b7=Button(tk,text="7",font=("Times",20),command=lambda:btnpress(7),fg="red")
b7.grid(row=4,column=0)
b8=Button(tk,text="8",font=("Times",20),command=lambda:btnpress(8),fg="red")
b8.grid(row=4,column=1)
b9=Button(tk,text="9",font=("Times",20),command=lambda:btnpress(9),fg="red")
b9.grid(row=4,column=2)
b0=Button(tk,text="0",font=("Times",20),command=lambda:btnpress(0),fg="red")
b0.grid(row=5,column=0)
bp=Button(tk,text="+",font=("Times",20),command=lambda:btnpress("+"),fg="green",bg="black")
bp.grid(row=5,column=1)
bs=Button(tk,text="-",font=("Times",20),command=lambda:btnpress("-"),fg="green",bg="black")
bs.grid(row=5,column=2)
bm=Button(tk,text="x",font=("Times",20),command=lambda:btnpress("*"),fg="green",bg="black")
bm.grid(row=6,column=0)
bd=Button(tk,text="/",font=("Times",20),command=lambda:btnpress("/"),fg="green",bg="black")
bd.grid(row=6,column=1)
beq=Button(tk,text="=",font=("Times",20),command=equalpress,fg="magenta")
beq.grid(row=6,column=2)
bc=Button(tk,text="C",font=("Times",20),command=clear,fg="cyan")
bc.grid(row=7,column=0)
tk.mainloop()
