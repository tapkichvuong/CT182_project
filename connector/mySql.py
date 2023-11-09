# Importing module 
import mysql.connector
from mysql.connector import Error
from hashlib import sha256
import random
import string

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

    # lay du lieu cua ban sach
    def handleLoadSach(self):
        cursor = self.mydb.cursor()
        sql= "select sach.masach,sach.tensach,nxb.tennxb,tacgia.tentacgia,theloai.tenloai,sach.mota,sach.masach from sach join tacgia on tacgia.matacgia=sach.matacgia join nxb on nxb.manxb=sach.manxb join theloai on theloai.maloai=sach.maloai order by masach"
        cursor.execute(sql)
        results =cursor.fetchall()
        return results
    #xu ly them sach
    #xu ly xoa sach
    #xu ly cap nhat sach
    #xu ly tim sach

    #lay du lieu cua ban NXB
    def handleLoadNXB(self):
        cursor = self.mydb.cursor()
        sql= "select * from nxb"
        cursor.execute(sql)
        nxb =cursor.fetchall()
        return nxb
      
    #xu ly them nxb
    #xu ly xoa nxb
    #xu ly cap nhat nxb
    #xu ly tim xnb

    #lay du lieu cua ban Tac Gia
    def handleLoadTacGia(self):
        cursor = self.mydb.cursor()
        sql= "select * from tacgia"
        cursor.execute(sql)
        results =cursor.fetchall()
        return results  
    #xu ly them tac gia
    #xu ly xoa tac gia
    #xu ly cap nhat tac gia
    #xu ly tim tac gia

    #lay du lieu cua ban The Loai
    def handleLoadTheLoai(self):
        cursor = self.mydb.cursor()
        sql= "select * from theloai"
        cursor.execute(sql)
        theloai =cursor.fetchall()
        return theloai
    #xu ly them the loai
    #xu ly xoa the loai
    #xu ly cap nhat loai
    #xu ly tim the loai

    # xu li dang ky
    def handleRegister(self, account):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO taikhoan (username, pass) VALUES (%s, %s)"
            #Bam mat khau 
            hash_pass = sha256(account['pass'].encode('utf-8')).hexdigest()
            print(hash_pass)
            val = (account['username'], hash_pass)
            cursor.execute(sql, val)
            madocgia = self.generate_random_string()
            sql = "INSERT INTO docgia (madocgia, firstname, lastname, phone, email, username) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (madocgia, account['firstName'], account['lastName'], account['phone'], account['email'], account['username'])
            cursor.execute(sql, val)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            # bao loi neu tai khoan da ton tai
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close() 

    # xu li dang nhap
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
    
    # lay ma doc gia nguoi dung dang nhap
    def authenticate(self, username):
        try:
            cursor = self.mydb.cursor()
            sql = "SELECT madocgia FROM docgia WHERE username = %s"
            val = (username,)
            cursor.execute(sql, val)
            madocgia = cursor.fetchone()
            print(madocgia)
            return madocgia[0]
        except Error as e:
            print(e)
        finally:
            self.mydb.close()
            
    def generate_random_string(self):
        characters = string.ascii_letters + string.digits  # Use uppercase letters and digits
        random_string = ''.join(random.choice(characters) for _ in range(8))
        return random_string
