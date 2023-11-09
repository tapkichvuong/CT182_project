# Importing module 
import mysql.connector
from hashlib import sha256

class mydb:
    def __init__(self):
    # Creating connection object
        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "123456",
            database = "qlthuvien"
        )
    # Printing the connection object 
    def handleLoadSach(self):
        cursor = self.mydb.cursor()
        sql= "select sach.masach,sach.tensach,nxb.tennxb,tacgia.tentacgia,theloai.tenloai,sach.mota,sach.masach from sach join tacgia on tacgia.matacgia=sach.matacgia join nxb on nxb.manxb=sach.manxb join theloai on theloai.maloai=sach.maloai order by masach"
        cursor.execute(sql)
        results =cursor.fetchall()
        return results
    def handleRegister(self, account):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO taikhoan (username, pass) VALUES (%s, %s)"
        #Bam mat khau 
        hash_pass = sha256(account['pass'].encode('utf-8')).hexdigest()
        print(hash_pass)
        val = (account['username'], hash_pass)
        cursor.execute(sql, val)
        cursor.close()
        self.mydb.commit()

        print(cursor.rowcount, "record inserted.")
        
    def handleLogin(self, username, password):
        cursor = self.mydb.cursor()
        sql = "SELECT GetUserPassword(%s)"
        val = (username,)
        cursor.execute(sql, val)
        myresult = cursor.fetchone()
        print(myresult)
        cursor.close()
        #Bam mat khau 
        hash_pass = sha256(password.encode('utf-8')).hexdigest()
        return (hash_pass == myresult[0])
