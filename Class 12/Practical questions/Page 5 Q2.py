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
