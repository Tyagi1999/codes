from tkinter import*
import random
import time
counter=0
tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.config(bg="white")
canvas.pack()
tk.update()
class Ball:
    def _init_(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle=paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                self.score(True)
                return True
            return False
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
            canvas.create_text(250,100,text="GAME OVER.",font=("Pursia",30),fill="Blue")
            canvas.create_text(245,148,font=("Roman",14),text="Better Luck Next Time!",fill="Green")
            canvas.create_text(247,175,font=("Pursia",12),text="Score: "+str(counter),fill="white")
            if counter>=50:
                canvas.create_text(240,200,text="EXCELLENT  ;-)",font=("Arial",10),fill="magenta")
                canvas.create_text(245,225,text="*****",font=("Pursia",20),fill="yellow")
            if counter>=35 and counter<50:
                canvas.create_text(240,200,text="NICE  :-)",font=("Arial",10),fill="magenta")
                canvas.create_text(246,225,text="****",font=("Pursia",20),fill="yellow")
            if counter>=20 and counter<35:
                canvas.create_text(240,200,text="GOOD  :-)",font=("Arial",10),fill="magenta")
                canvas.create_text(245,225,text="***",font=("Pursia",20),fill="yellow")
            if counter>10 and counter<20:
                canvas.create_text(240,200,text="TRY A LITTLE HARD  :-(",font=("Arial",10),fill="magenta")
                canvas.create_text(252,225,text="**",font=("Pursia",20),fill="yellow")
            if counter<=10:
                canvas.create_text(240,200,text="IMPROVE YOUR GAME  :-(",font=("Arial",10),fill="magenta")
                canvas.create_text(248,225,text="*",font=("Pursia",20),fill="yellow")
   

        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
    def score(self,val):
        global counter
        if val==True:
            a=self.canvas.create_text(120,50,text=counter,font=("Arial",30),fill="white")
            canvas.itemconfig(a,fill="white")
            counter+=1
            a=self.canvas.create_text(120,50,text=counter,font=("Arial",30),fill="black")
class Paddle:
    def _init_(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,330)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0   
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2
paddle=Paddle()
paddle._init_(canvas,'Purple')
ball = Ball()
ball._init_(canvas,paddle,'red')
while 1:
   if ball.hit_bottom==False: 
       ball.draw()
       paddle.draw()
   tk.update_idletasks()
   tk.update()
   time.sleep(0.01)
   









