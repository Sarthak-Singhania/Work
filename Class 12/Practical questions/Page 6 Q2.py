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