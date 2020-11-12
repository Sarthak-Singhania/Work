import mysql.connector
mysql=mysql.connector.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
sid=['W001','W003','W002','W003','W001','W002','W005','W003']
name=[10,5,20,10,15,20,10,15]
dept=[1,1,2,2,3,3,3,4]
gen=['Unisex','Ladies','Gents','Unisex','Gents']
exp=[100,150,200,250,100]
for i in range(len(sid)):
    com='insert into sale values(%s,%s,%s)'
    val=(sid[i],name[i],dept[i])
    cur.execute(com,val)
    mysql.commit()
