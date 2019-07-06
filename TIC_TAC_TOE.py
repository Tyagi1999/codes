from tkinter import*
from tkinter import messagebox
tk=Tk()
tk.title("TIC TAC TOE")
click=True
def checker(b):
    global click
    if b["text"]==" " and click==True:
        b["text"]="X"
        click=False
    elif b["text"]==" " and click==False:
        b["text"]="O"
        click=True
    elif(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
         b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
         b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
         b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
         b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
         b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or
         b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
         b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        tk.messagebox.showinfo("WINNER X","You have just won the game.")

    elif(b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
         b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
         b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
         b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
         b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
         b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or
         b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
         b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        tk.messagebox.showinfo("WINNER O","You have just won the game.")

buttons=StringVar()
b1=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b1))
b1.grid(row=1,column=0,sticky=S+N+E+W)

b2=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b2))
b2.grid(row=1,column=1,sticky=S+N+E+W)

b3=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b3))
b3.grid(row=1,column=2,sticky=S+N+E+W)

b4=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b4))
b4.grid(row=2,column=0,sticky=S+N+E+W)

b5=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b5))
b5.grid(row=2,column=1,sticky=S+N+E+W)

b6=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b6))
b6.grid(row=2,column=2,sticky=S+N+E+W)

b7=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b7))
b7.grid(row=3,column=0,sticky=S+N+E+W)

b8=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b8))
b8.grid(row=3,column=1,sticky=S+N+E+W)

b9=Button(tk,text=" ",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(b9))
b9.grid(row=3,column=2,sticky=S+N+E+W)

tk.mainloop()

































        
    

    
