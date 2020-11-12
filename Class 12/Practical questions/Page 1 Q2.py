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