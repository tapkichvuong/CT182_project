# Importing module 
import mysql.connector
from hashlib import sha256

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
        #Bam mat khau 
        hash_pass = sha256(account['pass'].encode('utf-8')).hexdigest()
        print(hash_pass)
        val = (account['username'], hash_pass)
        cursor.execute(sql, val)

        self.mydb.commit()

        print(cursor.rowcount, "record inserted.")
        
    def handleLogin(self, username, password):
        cursor = self.mydb.cursor()
        sql = "SELECT GetUserPassword(%s)"
        val = (username,)
        cursor.execute(sql, val)
        myresult = cursor.fetchone()
        print(myresult)
        #Bam mat khau 
        hash_pass = sha256(password.encode('utf-8')).hexdigest()
        return (hash_pass == myresult[0])

        
db = mydb()
print(db.handleLogin('admin', 'admin'))