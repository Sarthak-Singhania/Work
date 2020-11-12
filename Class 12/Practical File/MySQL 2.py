import mysql.connector
mysql=mysql.connector.connect(host='localhost',user='root',password='root',database='mydb')
cur=mysql.cursor()
try:
    cur.execute('create table Student(RollNo int primary key,Name varchar(50),Class int,DOB date,Gender char(2)')
except:
    pass
def insert():
    a=input('Enter Roll No:')
    b=input('Enter Name:')
    c=input('Enter Class:')
    d=input('Enter Date(YY/MM/DD):')
    e=input('Enter Gender(M/F):')
    com='insert into Student values(%s,%s,%s,%s,%s)'
    val=(a,b,c,d,e)
    cur.execute(com,val)
    print('Record Inserted')
def update():
    a=input('Enter Roll No to update details:')
    b=input('Enter Name:')
    c=input('Enter Class:')
    d=input('Enter Date(YY/MM/DD):')
    e=input('Enter Gender(M/F):')
    com='update Student set Name=%s,Class=%s,DOB=%s,Gender=%s where Roll_No=%s'
    val=(b,c,d,e,a)
    cur.execute(com,val)
    print('Updated')
while True:
    option=(int(input('\n1)Insert Record\n2)Update record\nEnter the option number:')))
    if option==1:
        insert()
    elif option==2:
        update()
    cont=input('Do you want to continue(y/n):')
    if cont=='n':
        break