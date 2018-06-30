from tkinter import *
import time
import random
import tkinter.messagebox
tk=Tk()
tk.title("Pong")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

l1=Label(tk,text="POINTS",fg="blue")
l1.pack(side="left")
var1=StringVar()
l2=Label(tk,textvariable=var1,fg="blue")
l2.pack(side="left")
l3=Label(tk,text="POINTS",fg="blue")
l3.pack(side="right")
var2=StringVar()
l4=Label(tk,textvariable=var2,fg="blue")
l4.pack(side="right")


canvas=Canvas(tk,height=600,width=900,bd=0)
canvas.config(bg="black")
canvas.pack()
tk.update()


canvas.create_line(450,0,450,600,fill="white")

class Ball:
    def __init__(self,canvas,paddle,paddle1,color):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle1=paddle1
        self.lefthit= False
        self.righthit= False
        self.id=canvas.create_oval(20,20,40,40,fill=color)
        self.canvas.move(self.id,430,270)
        start=[-5,-4,-3,-2,-1,1,2,3,4,5]
        random.shuffle(start)
        self.x=start[0]
        self.y=-2
        self.speedx=3
        self.speedy=3

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                #print("tttttttt")
                return True
            else:
                #print("ffffff")
                return False
    def hit_paddle1(self,pos):
        paddle1_pos=self.canvas.coords(self.paddle1.id)
        if pos[3]>=paddle1_pos[1] and pos[3]<=paddle1_pos[3]:
            if pos[2]>=paddle1_pos[0] and pos[2]<=paddle1_pos[2]:
                #print("tttttttt")
                return True
            else:
                #print("ffffff")
                return False

    def ball_speedxincrese(self):
        self.speedx=self.speedx+0.002

    def ball_speedyincrese(self):
        self.speedy=self.speedy+0.002

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            #self.y=3
            self.y=self.speedy
        if pos[3]>=600:
            #self.y=-3
            self.y=-self.speedy
        if pos[0]<=0:
            self.lefthit=True
        if pos[2]>=900:
            self.righthit=True
        if self.hit_paddle(pos)==True:
            #self.x=3
            self.x=self.speedx
        if self.hit_paddle1(pos)==True:
            #self.x=-3
            self.x=-self.speedx
    def changeleft():
        self.lefthit=False
    def changeright():
        self.righthit=False




class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(20,355,40,445,fill=color)
        self.y=0
        self.speedy=3.5
        self.canvas.bind_all('w',self.uclick)
        self.canvas.bind_all('s',self.dclick)

    def paddle_speedyincrese(self):
        self.speedy=self.speedy+0.001

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=600:
            self.y=0
    def uclick(self,event):
        #self.y=-3.5
        self.y=-self.speedy
    def dclick(self,event):
        #self.y=3.5
        self.y=self.speedy

class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(860,355,880,445,fill=color)
        self.y=0
        self.speedy=3.5
        self.canvas.bind_all("<KeyPress-Up>",self.upclick)
        self.canvas.bind_all("<KeyPress-Down>",self.downclick)

    def paddle1_speedyincrese(self):
        self.speedy=self.speedy+0.001

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=600:
            self.y=0
    def upclick(self,event):
        #self.y=-3.5
        self.y=-self.speedy
        print(self.speedy)
    def downclick(self,event):
        #self.y=3.5
        self.y=self.speedy


paddle=Paddle(canvas,"red")
paddle1=Paddle1(canvas,"brown")
b=Ball(canvas,paddle,paddle1,"orange")
p1=0
p2=0
while 1:
    try:
        if b.lefthit==True or b.righthit==True:
            if b.lefthit==True:
                p2=p2+1
                var2.set(p2)
                b=Ball(canvas,paddle,paddle1,"orange")
            if b.righthit==True:
                p1=p1+1
                var1.set(p1)
                b=Ball(canvas,paddle,paddle1,"orange")

        else:
            if p1==5 or p2==5:
                canvas.create_text(430,100,text="GAME OVER",fill="white")
                if p1==5:
                    canvas.create_text(150,120,text="Player 1 wins",fill="white")
                else:
                    canvas.create_text(700,120,text="Player 2 wins",fill="white")
                break
            b.draw()
            paddle.draw()
            paddle1.draw()
        tk.update()
        time.sleep(0.01)
        b.ball_speedxincrese()
        b.ball_speedxincrese()
        paddle.paddle_speedyincrese()
        paddle1.paddle1_speedyincrese()
        #print(b.speedx)
    except Exception as e:
        break



tk.mainloop()
