# Importing module 
import mysql.connector

class mydb:
    def __init__(self):
    # Creating connection object
        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Minhhuy2310@",
            database = "librarydb"
        )
    # Printing the connection object 
    def handleRegister(self, account):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO taikhoan (username, pass) VALUES (%s, %s)"
        val = (account['username'], account['pass'])
        cursor.execute(sql, val)

        self.mydb.commit()

        print(cursor.rowcount, "record inserted.")
        
    def handleLogin(self, username, password):
        cursor = self.mydb.cursor()
        sql = "SELECT pass FROM taikhoan WHERE username = %s"
        val = (username,)
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        return (password == myresult[0][0])

        
db = mydb()
print(db.handleLogin('admin', 'admin'))