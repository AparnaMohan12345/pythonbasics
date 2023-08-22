import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password ="aparnamohan@123", port =3306)
print(mydb)
mycursur = mydb.cursor()
#mycursur.execute("create database puthonconnect")
mycursur.execute("use puthonconnect")
#mycursur.execute("create table students(name varchar(250), age int, roll_no int)")
#mycursur.execute(" insert into students values('Aparna',26,1)")
#mycursur.execute(" insert into students values('Ann',26,2),('Ammu',26,3)")
#mycursur.execute("select * from students")
sql = " insert into students(name,age,roll_no)values(%s,%s,%s)"
val = ('Aparna',26,1)
mycursur.execute(sql, val)
mydb.commit()