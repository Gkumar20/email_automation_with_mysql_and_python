from unicodedata import name
import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password= "",
    database = "projectds"
)
if mydb.is_connected():
    mycursor = mydb.cursor()
    sql= 'SELECT * FROM `email` where 1'
    sqldata = mycursor.execute(sql)
    email_dictionary = {}
    for row in mycursor:
        lst = list(row)
        # print(lst[1])
        email_dictionary[lst[1]]=lst[2]

    