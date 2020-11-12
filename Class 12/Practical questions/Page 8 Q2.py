import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
try:
    cur.execute('create table Bill(Order_ID int, Cust_ID int,Item char(50),Ord_Date date,QTY int,Price int)')
except:
    pass
ordid=[1]gi
cust=[101]
item=['watch']
date=['19/03/20']
qty=[10]
price=[100]
for i in range(len(ordid)):
    com='insert into bill values(%s,%s,%s,%s,%s,%s)'
    val=(str(ordid[i]),str(cust[i]),str(item[i]),str(date[i]),str(qty[i]),str(price[i]))
    cur.execute(com,val)
    mysql.commit()
cur.execute('select count(item) from bill where month(ord_date)=3')
cur.execute('select count(item) from bill where qty*price>1700')
cur.execute('update bill set price=price+50')