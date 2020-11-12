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