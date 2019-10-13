import pymysql

db= pymysql.connect("localhost","test","123","MYD")

try:
    if db:
        print("Connection Successful")

except:
    print("Nahh")

cursor=db.cursor()

## Table Added from Input Successful so its commnted
# tab=input("Enter Table Name:")
# sql=f"""create table {tab} ( SUBJECT char(20) NOT NULL, MARKS int(2) NOT NULL)"""
# cursor.execute(sql)

# Data Added to table Success o commented

# while True:
#     print("1.Insert Data\n")
#     print("2.Exit")
#     c=input("\n")
#     if c=='1':
#         s=input("Enter Subject Name:")
#         m=input("Enter Marks:")
#         sql=f"INSERT INTO Marks VALUES ('{s}','{m}')"
#         try:
#             cursor.execute(sql)
#             print("Data Added Succes")
#             db.commit()
#         
#         except:
#             print("Data Added Failed")
#     elif c=='2':
#         break



## Updating Table Success so Commented


# us=input("Enter Subject Name whose Marks is to be Updated:")
# um=input("Enter Updated Marks:")
# sql=f"UPDATE Marks SET MARKS='{um}' WHERE SUBJECT='{us}'"
# cursor.execute(sql)



# Taking Data from One Table To Another Table and Printing the Data


# sql="INSERT INTO MARKS1 ( SUBJECT,MARKS) SELECT SUBJECT,MARKS FROM Marks WHERE SUBJECT='CCN'"
# cursor.execute(sql)
# 
# cursor.execute("SELECT * FROM MARKS1")
# e=cursor.fetchall()
# 
# for i in e:
#     print(i)

## USING BUILT IN FUNCTIONS TO TABLE

# sql="SELECT AVG(MARKS) FROM Marks"    # MARKS Is the column Name
# cursor.execute(sql)
# e=cursor.fetchall()
# 
# for i in e:
#     print(i)


