from tkinter.ttk import *
from tkinter import *
import matplotlib.pyplot as plt
import random
import time
import mysql.connector
file=open('country name.txt','r')
counter=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
first=''
last=''
age=0
region=''
gender=''
tk=''
try:
    def close():
        master.destroy()
    def show():
        global first
        global last
        global age
        global region
        global gender
        global v
        a=v.get()
        if a==1:
            gender='Male'
        elif a==2:
            gender='Female'
        elif a==3:
            gender='Other'
        first,last,age,region=e1.get(),e2.get(),spin.get(),combo.get()
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='')
        cur=sql.cursor()
        try:
            cur.execute('create database game')
        except:
            pass    
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        try:
            cur.execute('create table score (Name char(100),Score int(2),Age int(2),Region char(100),Gender char(100))')
        except:
            pass
    def game():
        global tk
        gameover=0
        tk=Toplevel(master)
        tk.wm_iconbitmap('logo.ico')
        tk.title('Brick Breacker')
        tk.resizable(0,0)
        tk.wm_attributes('-topmost',1)
        canvas=Canvas(tk,width=535,height=400,bd=0,highlightthickness=0)
        canvas.pack()
        canvas.update()
        class Ball:
            def __init__(self,canvas,paddle,block,color):
                self.canvas=canvas
                self.paddle=paddle
                self.block=block
                self.id=canvas.create_oval(5,5,25,25,fill=color)
                self.canvas.move(self.id,245,100)
                starts=[-3,-2,-1,1,2,3]
                random.shuffle(starts)
                self.x=starts[0]
                self.y=-10
                self.canvas_height=self.canvas.winfo_height()
                self.canvas_width=self.canvas.winfo_width()
                self.hit_bottom=False
            def score(self):
                global counter
                counter+=1
                tk.title('Score: '+str(counter))
            def hit_block(self,pos):
                block_pos=self.canvas.coords(self.block.id)
                List=[block_pos]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global a
                            a+=1
                            return True
                return False
            def hit_block1(self,pos):
                block_pos1=self.canvas.coords(self.block.id1)
                List=[block_pos1]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global b
                            b+=1
                            return True           
                return False
            def hit_block2(self,pos):
                block_pos2=self.canvas.coords(self.block.id2)
                List=[block_pos2]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global c
                            c+=1
                            return True
                return False
            def hit_block3(self,pos):
                block_pos3=self.canvas.coords(self.block.id3)
                List=[block_pos3]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global d
                            d+=1
                            return True
                return False
            def hit_block4(self,pos):
                block_pos4=self.canvas.coords(self.block.id4)
                List=[block_pos4]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global e
                            e+=1
                            return True
                return False
            def hit_block5(self,pos):
                block_pos5=self.canvas.coords(self.block.id5)
                List=[block_pos5]
                for i in List:
                    if (pos[0] >=i[0] and pos[2]<=i[2]): 
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global f
                            f+=1
                            return True
                    if pos[2]>=i[0] and pos[0]<=i[2]:
                        if pos[3]>=i[1] and pos[3]<=i[3]:
                            f+=1
                            return False
            def hit_block6(self,pos):
                block_pos6=self.canvas.coords(self.block.id6)
                List=[block_pos6]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global g
                            g+=1
                            return True
                    if pos[2]>=i[0] and pos[0]<=i[2]:
                        if pos[3]>=i[1] and pos[3]<=i[3]:
                            g+=1
                            return False
            def hit_paddle(self,pos):
                paddle_pos=self.canvas.coords(self.paddle.id)
                if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                    if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                        self.x+=self.paddle.x
                        self.y+=1
                        return True
                return False
            def draw(self):
                self.canvas.move(self.id,self.x,self.y)
                pos=self.canvas.coords(self.id)
                if pos[1]<=0:
                    self.y=3
                if self.hit_block(pos)==True:
                    self.y=3
                    self.block.id=canvas.create_rectangle(10,10,110,20,fill='yellow')
                if self.hit_block1(pos)==True:
                    self.y=3
                    self.block.id1=canvas.create_rectangle(115,10,215,20,fill='yellow')
                if self.hit_block2(pos)==True:
                    self.y=3
                    self.block.id2=canvas.create_rectangle(220,10,320,20,fill='yellow')
                if self.hit_block3(pos)==True:
                    self.y=3
                    self.block.id3=canvas.create_rectangle(325,10,425,20,fill='yellow')
                if self.hit_block4(pos)==True:
                    self.y=3
                    self.block.id4=canvas.create_rectangle(430,10,530,20,fill='yellow')
                if self.hit_block5(pos)==True:
                     self.y=3
                     self.block.id5=canvas.create_rectangle(100,150,200,160,fill='yellow')
                if self.hit_block5(pos)==False:
                     self.y=-3
                     self.block.id5=canvas.create_rectangle(100,150,200,160,fill='yellow') 
                if self.hit_block6(pos)==False:
                     self.y=-3
                     self.block.id6=canvas.create_rectangle(350,150,450,160,fill='yellow')
                if self.hit_block6(pos)==True:
                    self.y=3
                    self.block.id6=canvas.create_rectangle(350,150,450,160,fill='yellow')
                if pos[3]>=self.canvas_height:
                    self.hit_bottom=True
                if pos[3]>=self.canvas_height:
                    self.y=3
                if self.hit_paddle(pos)==True:
                    self.y=-3
                    canvas.delete(block)
                if pos[0]<=0:
                    self.x=3
                if pos[2]>=self.canvas_width:
                    self.x=-3
        class Block:
            def __init__(self,canvas,color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(10,10,110,20,fill=color )
                self.id1=canvas.create_rectangle(115,10,215,20,fill=color)
                self.id2=canvas.create_rectangle(220,10,320,20,fill=color)
                self.id3=canvas.create_rectangle(325,10,425,20,fill=color)
                self.id4=canvas.create_rectangle(430,10,530,20,fill=color)
                self.id5=canvas.create_rectangle(100,150,200,160,fill=color)
                self.id6=canvas.create_rectangle(350,150,450,160,fill=color)
                self.x=0
        class Paddle:
            def __init__(self,canvas,color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(0,0,100,10,fill=color)
                self.canvas.move(self.id,230,300)
                self.x=0
                self.canvas_width=self.canvas.winfo_width()
                self.started=False
                self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
                self.canvas.bind_all('<Button-1>',self.start_game)
            def draw(self):
                self.canvas.move(self.id,self.x,0)
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                    self.x=0
                elif pos[2]>=self.canvas_width:
                    self.x=0
            def turn_left(self,evt):
                pos=self.canvas.coords(self.id)
                if pos[0]>=0:
                    self.x=-5
            def turn_right(self,evt):
                pos=self.canvas.coords(self.id)
                if pos[2]<=self.canvas_width:
                    self.x=5
            def start_game(self,evt):
                self.started=True
        paddle=Paddle(canvas,'blue')
        block=Block(canvas,'green')
        ball=Ball(canvas,paddle,block,'red')
        while True:
            if ball.hit_bottom==False and paddle.started==True:
                ball.draw()
                paddle.draw()
                gameover=0
            if ball.hit_bottom==True:
                canvas.create_text(270,200,text='GAME OVER',font=28)
                canvas.create_text(270,250,text='Score='+str(counter),font=28)
                gameover=1
            if a and b and c and d and e and f and g>=1:
                ball.y=0
                ball.x=0
                paddle.x=0
                canvas.create_text(270,200,text='YOU WIN!',font=28)
                canvas.create_text(270,250,text=' Score='+str(counter),font=28)
                gameover=1
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
            if gameover==1:
                time.sleep(2)
                tk.destroy()
                insert()
                leaderboard()
            else:
                pass
        
        tk.mainloop()
        
    def search():
        tk1=Tk()
        tk1.wm_iconbitmap('logo.ico')
        tk1.title('Brick Breaker')
        tk1.configure(background='#002240')
        style=ttk.Style()
        style.configure("TLabel", foreground="#04BF10", background="#002240", font=("Times New Roman Bold", 20), anchor="center")
        global first
        global last
        first,last=e1.get(),e2.get()
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        n=str(first+' '+last)
        sco='select Name,Score from score where Name="%s"'%n
        cur.execute(sco,n)
        listfound=[]
        for x in cur:
            personname=str(x[0])
            personscore=str(x[1])
            found=personname+' has scored '+personscore
            listfound.append(found)
        for y in range (len(listfound)):
            ttk.Label(tk1,text=listfound[y],anchor="w",background="#002240",foreground="#04BF10",font=("Times New Roman Bold", 20)).grid(row=1+y,column=1)    
    def insert():
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='')
        cur=sql.cursor()
        try:
            cur.execute('create database game')
        except:
            pass
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        try:
            cur.execute('create table score (Name char(100),Score int(2),Age int(2),Region char(100),Gender char(100))')
        except:
            pass
        com='insert into score values(%s,%s,%s,%s,%s)'
        val=(str(first+' '+last),str(counter),str(age),str(region),str(gender))
        cur.execute(com,val)
        sql.commit()
        file.close()
    def graph():
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        cur.execute('select  * from score')
        names=[]
        scores=[]
        for x in cur:
            names.append(x[0])
            scores.append(x[1])
        plt.bar(names,scores,color='#00ff11')
        plt.xlabel('User')
        plt.ylabel('Score')
        scale_y=1
        plt.savefig('graph.png')
        plt.show()
    
    def leaderboard():
        leadwin=Toplevel(master)
        leadwin.wm_iconbitmap('logo.ico')
        leadwin.title('Brick Breacker')
        style.configure("TLabel", foreground="#04BF10", background="#002240", font=("Times New Roman Bold", 20), anchor="center")
        ttk.Label(leadwin,text='Leaderboard').grid(row=0,column=3)
        scoretree=ttk.Treeview(leadwin,column=("column1", "column2", "column3","column4","column5"), show='headings')
        scoretree.heading('#1',text='Name')
        scoretree.heading('#2',text='Score')
        scoretree.heading('#3',text='Age')
        scoretree.heading('#4',text='Region')
        scoretree.heading('#5',text='Gender')
        scoretree.grid(row=1,column=0,columnspan=5)

        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        cur.execute('select * from score order by score desc')
        for row in cur:
            scoretree.insert("","end",values=row)
        leadwin.mainloop()
    master=Tk()
    master.wm_iconbitmap('logo.ico')
    master.title('Brick Breaker')
    master.configure(background='#002240')
    topframe=Frame(master, bg='#002240')
    topframe.grid(row=1,column=1,pady=(20,0))
    bottomframe=Frame(master, bg='#002240')
    bottomframe.grid(row=2,column=1,padx=20,pady=(0,20))
    
    style=ttk.Style()
    style.configure("TButton", foreground="#066ED6", background="#022873", font=("Times New Roman Bold", 17), anchor="center")
    style.configure("TLabel", foreground="#04BF10", background="#002240", font=("Times New Roman Bold", 20), anchor="center")                 
    style.configure("TEntry", foreground="#04BF10",anchor="center")
    style.configure("TRadiobutton", foreground="#04BF10", background="#002240", font=("Times New Roman Bold", 15))
    style.configure("TCombobox", foreground="#04BF10", background="#002240", font=("Times New Roman Bold", 15), anchor="center")

    ttk.Label(master,text='Welcome to Brick Breaker Ultimate!!',font=('Jokerman', 30),foreground='#D9560B').grid(row=0,column=1,padx=20)
    ttk.Label(topframe,text='First Name:').grid(row=0,padx=(0,50))
    ttk.Label(topframe,text='Last Name:').grid(row=1,padx=(0,50))
    e1=ttk.Entry(topframe,width=20,font=('Times New Roman', 15), justify= LEFT)
    e1.grid(row=0,column=100,pady=5,padx=5)
    e2=ttk.Entry(topframe,width=20,font=('Times New Roman', 15), justify= LEFT)
    e2.grid(row=1,column=100,pady=5,padx=5)
    ttk.Label(topframe,text='Age:').grid(row=2,padx=(0,50))
    spin=Spinbox(topframe,from_=1,to=90,width=19,font=('Times New Roman', 15), foreground="#04BF10")
    spin.grid(row=2,column=100,pady=5)
    ttk.Label(topframe,text='Region:').grid(row=3,padx=(0,50))
    combo=ttk.Combobox(topframe,width=19,font=('Times New Roman', 15))
    combo['values']=tuple(file.readlines())
    combo.current(0)
    combo.grid(column=100,row=3,pady=5)
    ttk.Label(topframe,text='Gender:').grid(row=4,pady=2,padx=(0,50))
    v=IntVar()
    ttk.Radiobutton(topframe,text='Male',variable=v,value=1).grid(row=4,column=100)
    ttk.Radiobutton(topframe,text='Female',variable=v,value=2).grid(row=5,column=100)
    ttk.Radiobutton(topframe,text='Other',variable=v,value=3).grid(row=6,column=100,pady=(0,50))

    ttk.Button(bottomframe,text='Search',command=search).grid(row=0,column=1,padx=5)
    ttk.Button(bottomframe,text='Enter',command=lambda:[show(),game()]).grid(row=0,column=0,padx=5)
    ttk.Button(bottomframe,text='Exit',command=master.destroy).grid(row=0,column=3,padx=5)
    ttk.Button(bottomframe,text='Graph',command=graph).grid(row=0,column=2,padx=5)
    master.mainloop()
    
except:
    print()
