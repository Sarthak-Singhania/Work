#1a-histogram - dict - longest, filter, etc

f=open('myfile.txt','w')
f.write(input('Enter a sentence:'))
f.close()
f=open('myfile.txt','r')
a=f.read()
l=a.split()
d={}                            #histogram
for i in l:
    d[i]=0
for x in l:
    d[x]+=1
v=list(d.values())
k=list(d.keys())
print('Total number of words are',sum(v))           
print('Number of different words are',len(k))
print('The most common word is',k[v.index(max(v))])
d={}
d[len(l[0])]=[l[0]]
for i in range(1,len(l)):
    if len(l[i]) in d:
        d[len(l[i])].append(l[i])
    else:
        d[len(l[i])]=[l[i]]
print(d)
def find_longest_word():
    print('The longest words are:',d[max(d)])
find_longest_word()
def filter_long_words(n):
    for i in d:
        if i>n:
            return ' '.join(map(str,d[i]))
f1=open('newfile.txt','w')
f1.write(filter_long_words(int(input('Enter the number:'))))
find_longest_word()
f.close()
f1.close()

#1b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
try:
    cur.execute('create table EMP (EMP_No int,EMP_Name char(20),Job char(30),Manager int,Salary int,Comm int,Dept_No int)')
except:
    pass
en=[1,2,3]
name=['A','B','C']
job=['D','E','F']
manager=[11,12,13]
salary=[10,20,30]
comm=[5,10,15]
dn=[101,102,103]
for i in range(len(en)):
    com='insert into emp values(%s,%s,%s,%s,%s,%s,%s)'
    val=(str(en[i]),str(name[i]),str(job[i]),str(manager[i]),str(salary[i]),str(comm[i]),str(dn[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select * from emp')
for x in cur:
    print(x)
cur.execute('select EMP_No,EMP_Name from emp')
for z in cur:
    print(z)
cur=mysql.cursor()
cur.execute('select EMP_Name,Salary,salary*12 Annual_Salary from emp')
for q in cur:
    print(cur)

###############

#2a-school-queue
queue = []

def add(data):
    queue.append(data)

def showlen():
    return len(queue)
def showreport():
    nur , kg , i = 0, 0, 0
    for record in queue:
        if record[2] == 'Nur':
            nur += 1
        elif record[2] == 'KG':
            kg += 1
        if record[2] == 'I':
            i += 1
    
    print("Nur: %s\nKG: %s\nIst: %s"%(nur,kg,i))

add([988,"ap","KG"])
showreport()

#2b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
try:
    cur.execute('create table Customer(CustID int,Name char(30),Price int,QTY int,CID int)')
except:
    pass
cust=[x for x in range(101,108)]
name=['Rohan Sharma','Deepak Kumar','Mohan Kumar','Sahil Bansal','Neha Soni','Sonal Aggarwal','Arjun Singh']
price=[70000,50000,30000,35000,25000,20000,50000]
qty=[20,10,5,3,7,5,15]
cid=[222,666,111,33,444,333,666]
for i in range(len(cid)):
    com='insert into customer values(%s,%s,%s,%s,%s)'
    val=(str(cust[i]),str(name[i]),str(price[i]),str(qty[i]),str(cid[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('update customer set price=price+1000 where name like "S%"')
cur.execute('alter table customer add column Total_Price int')
cur.execute('select sum(price*qty) Total_Bill from customer')

###############

#3a-programming-languages-chart
import matplotlib.pyplot as plt
lang=['Java','Python','PHP','Java Script','C#','C++']
pop=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(lang,pop)
fig1,ax1=plt.subplots()
ax1.pie(pop,labels=lang,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

#3b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
try:
    cur.execute('create table EMP (EMP_No int,EMP_Name char(20),Job char(30),Manager int,Salary int,Comm int,Dept_No int)')
except:
    pass
en=[1,2,3]
name=['A','B','C']
job=['D','E','F']
manager=[11,12,13]
salary=[10,20,30]
comm=[5,10,15]
dn=[101,102,103]
for i in range(len(en)):
    com='insert into emp values(%s,%s,%s,%s,%s,%s,%s)'
    val=(str(en[i]),str(name[i]),str(job[i]),str(manager[i]),str(salary[i]),str(comm[i]),str(dn[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select * from emp')
for x in cur:
    print(x)
cur.execute('select EMP_No,EMP_Name from emp')
for z in cur:
    print(z)
cur=mysql.cursor()
cur.execute('select EMP_Name,Salary,Salary+Commission from emp')
for q in cur:
    print(cur)

###############

#4a-UDF-datarepresentation
def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end='')
def octahedral(n,cnt):
    if n>7 or cnt==0:
        if cnt==0:
            return int((n%8)+octahedral(n//8,cnt+1))
        else:
            return int((n%8)*(10**cnt)+octahedral(n//8,cnt+1))
    elif n<=7 and n>0:
        return n*(10**cnt)
def hexadecimal(n):
    l=[]
    x=n//16
    if x<10:
        l.append(x)
    elif x==10:
        l.append('a')
    elif x==11:
        l.append('b')
    elif x==12:
        l.append('c')
    elif x==13:
        l.append('d')
    elif x==14:
        l.append('e')
    elif x==15:
        l.append('f')
    y=n%16
    if y<10:
        l.append(y)
    elif y>=10:
        z=y
        hexadecimal(z)
    return ''.join(map(str,l))
cont='y'
while cont!='n':
    number=int(input('Enter a number:'))
    option=(input('Desired type:'))
    if option=='B' or option=='b':
        print(binary(number))
    elif option=='O' or option=='o':
        print(octahedral(number,0))
    elif option=='H' or option=='h':
        print(hexadecimal(number))
    if input('Do you want to continue(y/n)?')=='n':
        cont='n'

#4b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
cur.execute('create table Sports(Stud_No int,Class int,Name char(50),Game char(50),Grade char(50))')
stud=[x for x in range(10,16)]
class1=[7,8,7,7,9,10]
name=['Sameer','Sujit','Kamal','Veena','Archana','Arpit']
game=['Swimming','Skating','Football','Tennis','Cricket','Athletics']
grade=['A','C','B','A','A','C']
for i in range(len(stud)):
    com='insert into sports values(%s,%s,%s,%s,%s)'
    val=(str(stud[i]),str(class1[i]),str(name[i]),str(game[i]),str(grade[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select count(Stud_No) from Sports where grade="A" and game="Cricket"')
for x in cur:
    print(x)
cur.execute('alter table sports add column Address char(50)')
cur.execute('select Game from sports where name like "A%"')
for y in cur:
    print(y)

###############

#5a-population-density-pie


import matplotlib.pyplot as plt
'''labels=[]
sizes=[]
for i in range(1,11):
    print('Entry number',i)
    labels.append(input('Enter the name of the state:'))
    sizes.append(int(input('Enter the population:')))'''

labels=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand']
sizes=[20,15,5,20,15,15,20,30,10,5]
fig1,ax1=plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal')
plt.show()

#5b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
mycur=mysql.cursor()
mycur.execute('create table club(coach_id int,coachname char(32),age int,sports char(32),dateofapp date,pay int,sex char)')

coachid=[x for x in range(1,11)]
name=[kukreja,ravina]
age=[]
sports=[]
dateofapp=[]
pay=[]
sex=[]

for i in range(len(name)):
    com='insert into club values(%s,%s,%s,%s,%s,%s,%s)'
    var=[str(coachid[i]),str(name[i]),str(age[i]),str(sports[i]),str(dateofapp[i]),str(pay[i]),str(sex[i])]
    mycur.excute(com,var)
    mysql.commit()

mycur.execute('select * from club where sports="swimming"')
mycur.execute('select coachname,pay,age,pay*0.15 Bonus from club')
mycur.execute('insert into table values(11,"Rajender",25,”Football”,“2004/05/27”,4500,”M”)')
mysql.commit()


###############

#6a-doublebar

import numpy as np
import matplotlib.pyplot as plt

Car1 = [50,40,70,80,20]
Car2 = [80,20,20,50,60]

X = np.arange(len(Car1))

plt.bar(X + 0.00, Car1, color = 'b', width = 0.25)
plt.bar(X + 0.25, Car2, color = 'g', width = 0.25)

plt.show() 

'''
import matplotlib.pyplot as plt
x1=[50,40,70,80,20]
y1=[x for x in range(1,6)]
x2=[80,20,20,50,60]
ax=plt.subplot()
ax.bar(x1,y1,color='g',width=3)
ax.bar(x2,y1,color='b',width=3)
plt.title('Information')
plt.xlabel('Days')
plt.ylabel('Distance')
plt.show()'''

#6b-sql

import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
cur.execute('create table Sports(Stud_No int,Class int,Name char(50),Game1 char(50),Grade1 char(50),Game2 char(50),Grade char(50))')
stud=[]
class1=[]
name=[]
game1=[]
grade1=[]
game2=[]
grade2=[]
for i in range(len(stud)):
    com='insert into sports values(%s,%s,%s,%s,%s,%s,%s)'
    val=(str(stud[i]),str(class1[i]),str(name[i]),str(game1[i]),str(grade1[i]),str(game2[i]),str(grade2[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select count(Stud_No) from Sports where grade="A" and game="Cricket"')
for x in cur:
    print(x)
cur.execute('alter table sports add column Address char(50)')
cur.execute('select Game from sports where name like "A%"')

###############

#7a-merge-commonsum-circular
a=input("Enter elements separated by space: ").split()
b=input("Enter elements separated by space: ").split()

#Merge List
L=a+b
print(L)

sum=0
for x in a:
    if x in b:
       sum+=int(x)
    else:
        pass
print (sum)

c=a*2
for x in range(len(a)):
    z=0
    for y in range(x, x + len(a)):
        if b[z]==c[y]:
            z+=1
        else:
            break
    if z == len(a):
        print ('Yes')
        break
else:
    print ('No')
'''
def mands(lst1, lst2):
 #Merge and sort
 outlist = lst1 + lst2
 return (sorted(outlist))
 
def commonsum(lst1, lst2):
 #common elements sum
 sum=0
 for i in lst1:
     for j in lst2:
         if i==j:
             sum+=i
 return (sum)
 
def circheck(lst1, lst2):
 #circular identity check
 a = set (lst1)
 b = set (lst2)
 return (a==b)
 
in1 = input("Enter List 1: ")
lst1 = list(map(int, in1.split()))
 
in2 = input("Enter List 2: ")
lst2 = list(map(int, in2.split()))
 
print("Merged and Sorted", mands(lst1, lst2))
print("Common elements sum", commonsum(lst1, lst2))
print("Circular Identity", circheck(lst1, lst2))
'''

#7b-sql

import mysql.connector as my
mysql=my.connect(host="localhost",user="root",password="root",database="school")
mycur=mysql.cursor()

mycur.execute('create table product(P_ID char(4),Product_Name char(32),Manufacturer char(3),Price int)')
pid=[]
productname=[]
manufacturer=[]
price=[]

for i in range(len(pid)):
    com='insert into table values(%s,%s,%s,%s)'
    values=[str(pid=[i]),str(productname=[i]),str(manufacturer=[i]),str(price=[i])]
    mycur.execute(com,values)
    mysql.commit()
    
mycur.execute('select * from product where price>50 and price<100')
mycur.execute('update product set price=price+10')
mycur.execute('select count(p_id) from product')

###############

#8a-restaurant-order-queue

  
from random import randint
l=[]
def new_order():
    global l
    l.append(randint(100,999))
def diqueue():
    global l
    return l.pop()
def display():
    global l
    print(l)
while True:
    option=(int(input('\n1)Order a meal\n2)Order is ready\n3)Waiting Queue\n4)Exit\nEnter the option number:')))
    if option==1:
        new_order()
    elif option==2:
        print(diqueue())
        if len(l)==0:
            print('Stack is underflow')
    elif option==3:
        if len(l)!=0:
            display()
        else:
            print('Stack is underflow')
    elif option==4:
        break

#8b-sql
import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
cur.execute('create table Bill(Order_ID int, Cust_ID int,Item char(50),Ord_Date date,QTY )')
ordid=[]
cust=[]
item=[]
date=[]
qty[]
price=[]
for i in range(len(ordid)):
    com='insert into bill values(%s,%s,%s,%s,%s,%s)'
    val=(str(ordid[i]),str(cust[i]),str(item[i]),str(date[i]),str(qty[i]),str(price[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select count(item) from bill where ord_date(month)=3')
cur.execute('select count(item) from bill where qty*price>1700')
cur.execute('update bill set price=price+50')

############### fin ###############
