from tkinter import *
from tkinter import messagebox
tk=Tk()
tk.title('Simple Interest')
tk.geometry('300x130')
p,r,t=0,0,0
def calculate():
    global p
    global r
    global t
     p,r,t=int(e1.get()),float(e2.get()),int(e3.get())
    amt=p+(p*r*t)/100
    messagebox.showinfo('Amount','Total loan amount=%s'%amt)
Label(tk,text='Principle Amount:').grid(row=1)
Label(tk,text='Rate of Interest:').grid(row=2)
Label(tk,text='Time(in years):').grid(row=3)
e1=Entry(tk)
e2=Entry(tk)
e3=Entry(tk)
e1.grid(row=1,column=1,padx=5,pady=5)
e2.grid(row=2,column=1,padx=5,pady=5)
e3.grid(row=3,column=1,padx=5,pady=5)
Button(tk,text='Calculate',command=calculate).grid(row=4,column=1,pady=5)
tk.mainloop()
