import pymysql

# Give your userid and Password here
mydb=pymysql.connect(host="localhost",
                             user='test',
                             passwd="123")

# Checking if Connection Successful or Not
if (mydb):
    print("Connection Successful")

else:
    print("Connection Failed")