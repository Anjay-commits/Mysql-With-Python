import pymysql

# Type your username in user and its corresponding password
mydb = pymysql.connect(
  host="localhost",
  user="test",
  passwd="123"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE IF NOT EXISTS myd")
mycursor.execute("show ")
for i in mycursor:
    print(i)