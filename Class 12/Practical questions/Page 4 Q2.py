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