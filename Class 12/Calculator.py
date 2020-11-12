from tkinter import *
tk=Tk()
num1=0
num2=0
ans=0
def show():
    global num1
    global num2
    num1,num2=int(get1.get()),int(get2.get())
def add():
    global ans
    return num1+num2
def clear():
    get1.delete(0,15)
    get2.delete(0,15)
def minus():
    global ans
    return num1-num2
def multiply():
    global ans
    return num1*num2
def div():
    global ans
    return num1/num2
get1=Entry(tk,width=15)
get1.grid(row=0,column=2)
get2=Entry(tk,width=15)
get2.grid(row=1,column=2)
Label(tk,text='Number 1').grid(row=0,column=1)
Label(tk,text='Number 2').grid(row=1,column=1)
Button(tk,text='+',command=lambda:[add(),show(),clear()]).grid(row=2,column=0)
Button(tk,text='-',command=lambda:[minus(),show(),clear()]).grid(row=2,column=1)
Button(tk,text='*',command=lambda:[multiply(),show(),clear()]).grid(row=2,column=2)
Button(tk,text='/',command=lambda:[div(),show(),clear()]).grid(row=2,column=3)
Label(tk,text=chr(ans)).grid(row=3,column=2)
tk.mainloop()