import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host="localhost",
    user="test",  #change the user
    password="Testeando1.",  #change the password
    database="py_password")
mycursor = mydb.cursor()


def register(c_user, c_password):
    sql =("INSERT INTO user (`username`,`password`) VALUES (%s, %s);")
    adr = (c_user, c_password, )
    mycursor.execute(sql, adr)
    mydb.commit()
    print("User inserted")


def check_user(c_user):
    sql = ("SELECT username FROM user where username = %s;")
    adr = (c_user, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if len(myresult)== 0:#User Free
        return True
    return False

def logging(c_user,c_password):
    sql = ("SELECT * FROM user where username = %s and password = %s;")
    adr = (c_user, c_password, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:#User Free
        return False
    return True