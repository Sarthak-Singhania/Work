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
