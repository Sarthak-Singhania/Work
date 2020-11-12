import mysql.connector
mysql=mysql.connector.connect(host='localhost',user='root',password='root')
cur=mysql.cursor()
try:
    cur.execute('create database mydb')
except:
    pass
mysql=mysql.connector.connect(host='localhost',user='root',password='root',database='mydb')
cur=mysql.cursor()
try:
    cur.execute('create table Item(Item_code varchar(20),Item_name varchar(20),Price float(11))')
except:
    pass
def insert():
    a=input('Enter Item Code:')
    b=input('Enter Item Name:')
    c=input('Enter Price:')
    com='insert into item values(%s,%s,%s)'
    val=(a,b,c)
    cur.execute(com,val)
    print('Record Inserted')
def view():
    cur.execute('select * from item')
    for i in cur:
        print(i)
def search():
    a=input('Enter Item Code:')
    com='select * from item where Item_code="%s"'%a
    cur.execute(com,a)
    for i in cur:
        print(i)
while True:
    option=(int(input('\n1)Insert Record\n2)View all records\n3)Search\nEnter the option number:')))
    if option==1:
        insert()
    elif option==2:
        view()
    elif option==3:
        search()
    cont=input('Do you want to continue(y/n):')
    if cont=='n':
        break