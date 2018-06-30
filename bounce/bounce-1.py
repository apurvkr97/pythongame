from tkinter import *
import time
import random
import tkinter.messagebox
tk=Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)


l1=Label(tk,text="POINTS:",fg="blue")
l1.pack()
var=StringVar()
l2=Label(tk,textvariable=var,fg="blue")
l2.pack()

#initializing labels 1
var.set(0)



canvas=Canvas(tk,height=600,width=600,bd=0)
canvas.pack()
canvas.config(bg="black")
canvas.create_line(0,3,600,3,fill="brown")
tk.update()
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(20,20,35,35,fill=color)
        self.canvas.move(self.id,280,280)
        start=[-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10]
        random.shuffle(start)
        self.x=start[0]
        self.y=-2
        self.bottomhit=False

    def new_game(self):
        self.bottomhit=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[0]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        else:
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        #print(pos)
        if pos[1]<=0:
            self.y=2
        if pos[3]>=600:
            self.bottomhit=True
        if pos[0]<=0:
            self.x=3
        if pos[2]>=600:
            self.x=-3
        if self.hit_paddle(pos)== True:
            self.y=-2


class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,75,10,fill=color)
        self.canvas.move(self.id,280,575)
        self.x=0
        self.canvas.bind_all("<KeyPress-Left>",self.lclick)
        self.canvas.bind_all("<KeyPress-Right>",self.rclick)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        #make sure paddle stays in window
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=600:
            self.x=0
    def lclick(self,event):
        self.x=-3.5
    def rclick(self,event):
        self.x=3.5

paddle=Paddle(canvas,"brown")
b=Ball(canvas,paddle,"red")
attempts=2
tym=0.02
points=0
while 1:
    try:
        if b.bottomhit==True and attempts>0:
            tkinter.messagebox.showinfo("GAME OVER...:-( ")
            ans=tkinter.messagebox.askquestion("you lost","Do u want another try..??")
            if ans=="yes":
                    b.new_game()
                    b=Ball(canvas,paddle,"yellow")
                    attempts=attempts-1;
            if ans=="no":
                break
        else:
            if(attempts>0):
                b.draw()
                paddle.draw()
            else:
                canvas.create_text(250,100,text="NO MORE CHANCES ALLOWED",fill="white")
                #tkinter.messagebox.showinfo("no more attempts")
                break
        #print(b.bottomhit)
        #tk.update_idletasks()
        points+=1
        var.set(points)
        tk.update()
        print(tym)
        time.sleep(tym)
        if tym>0.005:
            tym=tym-0.000009
        else:
            tym=0.005
    except Exception as e:
          break


tk.mainloop()
