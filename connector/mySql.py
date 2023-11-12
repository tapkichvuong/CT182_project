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
            host = "localhost",
            user = "root",
            password = "123456",
            database = "qlthuvien"
        )
    def handleLoadTinhTrang_CBB(self):
        cursor = self.mydb.cursor()
        sql= "select * from tinhtrang"
        cursor.execute(sql)
        tt =cursor.fetchall()
        return tt
    # xu ly tim nhanh sach muon
    def handleSearchSachNhanh(self,masach):
        cursor = self.mydb.cursor()
        sql = """
                SELECT masach,tensach,sl
                FROM sach
                WHERE masach = %s
                
            """
        val = (masach,)
        
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    # xu ly tim nhanh doc gia
    def handleSearchDocGiaNhanh(self,madocgia):
        cursor = self.mydb.cursor()
        sql = """
                SELECT madocgia,RTRIM(LTRIM(
        CONCAT(
            COALESCE(firstname + ' ', '')
            , COALESCE(lastname, '')
        )
        )) AS Name
                FROM docgia
                WHERE madocgia =%s
                
            """
        val = (madocgia,)
        
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    #xu ly them muon sach
    def handleThemSachMuon(self,muon,masach):
        try:
            cursor = self.mydb.cursor()
            
            sql = "INSERT INTO muon(masach,madocgia,ngaymuon,matt) VALUES (%s, %s, %s, %s)"
            val = (masach, muon['madocgia'], muon['ngaymuon'],muon['matt'])
            cursor.execute(sql, val)
            
            # sql1 = "UPDATE SACH SET sl =(sl - 1) WHERE masach = %s"
            # val1 = (masach)
            # cursor.execute(sql1,val1)
            cursor.close()

            
            self.mydb.commit()
            
            return True
        except Error  as e:
            
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close() 
    #xu ly xoa muon
    def handleXoaSachMuon(self, masach,madocgia):
        if not masach:
            return False
        else:
            sql = "DELETE FROM sach WHERE masach = %s"
            val = (masach,)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly cap nhat muon tra sach
    def handleUpdateSachMuon(self,masach,muon):
        if not masach and not muon['madocgia']:
            return False
        else: 
            sql = "UPDATE muon SET ngaytra=%s ,matt=%s WHERE madocgia =%s and masach=%s"
            val = (muon['ngaytra'],muon['matt'],muon['madocgia'],masach)
            
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False  
    #xu ly tim ls muon cua doc gia
    def handleTimLsMuon(self,madocgia):
        cursor = self.mydb.cursor()
        sql = """
                SELECT docgia.madocgia,RTRIM(LTRIM(CONCAT(COALESCE(docgia.firstname + ' ', ''),COALESCE(docgia.lastname, '')))) AS Name,muon.masach,sach.tensach,
                muon.ngaymuon,muon.ngaytra,tinhtrang.tinhtrang
                FROM muon
                    
                    
                    JOIN docgia ON docgia.madocgia =%s
                    
                    JOIN sach ON muon.masach =sach.masach
                    JOIN tinhtrang ON tinhtrang.matt = muon.matt
                WHERE  muon.madocgia =%s
                order by muon.madocgia
                    
            """
        val = (madocgia,madocgia)
        
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    # lay du lieu cua ban sach
    def handleLoadSach(self):
        cursor = self.mydb.cursor()
        sql = """
                        SELECT sach.masach, sach.tensach, nxb.tennxb, tacgia.tentacgia, theloai.tenloai, sach.sl, sach.mota, sach.masach
                        FROM sach
                            JOIN tacgia ON tacgia.matacgia = sach.matacgia
                            JOIN nxb ON nxb.manxb = sach.manxb
                            JOIN theloai ON theloai.maloai = sach.maloai
                        ORDER BY masach
                """
        cursor.execute(sql)
        results =cursor.fetchall()
        return results
    #xu ly them sach
    def handleThemSach(self,sach):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO sach (tensach, matacgia, manxb, maloai ,sl, mota) VALUES (%s, %s, %s, %s, %s,%s)"
            val = (sach['tensach'], sach['matacgia'], sach['manxb'],sach['maloai'],sach['sl'], sach['mota'])
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            
            return True
        except Error  as e:
            
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close() 
    #xu ly xoa sach
    def handleXoaSach(self, masach):
        if not masach:
            return False
        else:
            sql = "DELETE FROM sach WHERE masach = %s"
            val = (masach,)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly cap nhat sach
    def handleUpdateSach(self,masach,tensach,matacgia,manxb,maloai,sl,mota):
        if not masach:
            return False
        else: 
            sql = "UPDATE sach SET tensach = %s,matacgia = %s,manxb = %s,maloai = %s,sl = %s,mota = %s WHERE masach =%s"
            val = (tensach,matacgia,manxb,maloai,sl,mota,masach)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False  
    #xu ly tim sach
    def handleTimSach(self, masach, tensach, tacgia, nxb, theloai):
        cursor = self.mydb.cursor()
        sql = """
                SELECT sach.masach, sach.tensach, nxb.tennxb, tacgia.tentacgia, theloai.tenloai,sach.sl, sach.mota
                FROM sach
                    JOIN tacgia ON tacgia.matacgia = sach.matacgia
                    JOIN nxb ON nxb.manxb = sach.manxb
                    JOIN theloai ON theloai.maloai = sach.maloai
                WHERE  sach.masach LIKE %s
                    AND sach.tensach LIKE %s
                    AND tacgia.tentacgia LIKE %s
                    AND nxb.tennxb LIKE %s
                    AND theloai.tenloai LIKE %s 
                ORDER BY masach
            """
        val = (f'{masach}%', f'{tensach}%', f'%{tacgia}%', f'%{nxb}%', f'%{theloai}%')
        print(masach, tensach, tacgia, nxb, theloai)
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    #lay du lieu cua ban NXB
    def handleLoadNXB(self):
        cursor = self.mydb.cursor()
        sql= "select * from nxb"
        cursor.execute(sql)
        nxb =cursor.fetchall()
        return nxb
    #xu ly them nxb
    def handleThemNXB(self,tennxb):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO nxb(tennxb) VALUES (%s)"
            val = (tennxb,)
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close()
    #xu ly xoa nxb
    def handleXoaNXB(self, manxb, tennxb):
        if not manxb and not tennxb:
            return False
        if not manxb:
            sql = "DELETE FROM nxb WHERE tennxb = %s"
            val = (tennxb,)
        elif not tennxb:
            sql = "DELETE FROM nxb WHERE manxb = %s"
            val = (manxb,)
        else: 
            sql = "DELETE FROM nxb WHERE manxb = %s AND tennxb = %s"
            val = (manxb,tennxb)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly cap nhat nxb
    def handleSuaNXB(self, manxb, tennxb):
        if not manxb or not tennxb:
            return False
        else: 
            sql = "UPDATE nxb SET tennxb = %s WHERE manxb = %s"
            val = (tennxb, manxb)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False  
    #xu ly tim nxb
    def handleTimNxb(self, manxb, tennxb):
        cursor = self.mydb.cursor()
        sql = """
                SELECT *
                FROM nxb
                WHERE  manxb LIKE %s AND tennxb LIKE %s
                ORDER BY manxb
            """
        val = (f'{manxb}%', f'{tennxb}%')
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    #lay du lieu cua ban Tac Gia
    def handleLoadTacGia(self):
        cursor = self.mydb.cursor()
        sql= "select * from tacgia"
        cursor.execute(sql)
        results =cursor.fetchall()
        return results  
    #xu ly them tac gia
    def handleThemTacGia(self,tentacgia):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO tacgia(tentacgia) VALUES (%s)"
            val = (tentacgia,)
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close()
    #xu ly xoa tac gia
    def handleXoaTacGia(self, matacgia, tentacgia):
        if not matacgia and not tentacgia:
            return False
        if not matacgia:
            sql = "DELETE FROM tacgia WHERE tentacgia = %s"
            val = (tentacgia,)
        elif not tentacgia:
            sql = "DELETE FROM tacgia WHERE matacgia = %s"
            val = (matacgia,)
        else: 
            sql = "DELETE FROM tacgia WHERE matacgia = %s AND tentacgia = %s"
            val = (matacgia,tentacgia)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly cap nhat tac gia
    def handleSuaTacGia(self, matacgia, tentacgia):
        if not matacgia or not tentacgia:
            return False
        else: 
            sql = "UPDATE tacgia SET tentacgia = %s WHERE matacgia = %s"
            val = (tentacgia, matacgia)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False  
    #xu ly tim tac gia
    def handleTimTacGia(self, matacgia, tentacgia):
        cursor = self.mydb.cursor()
        sql = """
                SELECT *
                FROM tacgia
                WHERE  matacgia LIKE %s AND tentacgia LIKE %s
                ORDER BY matacgia
            """
        val = (f'{matacgia}%', f'{tentacgia}%')
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    #lay du lieu cua ban The Loai
    def handleLoadTheLoai(self):
        cursor = self.mydb.cursor()
        sql= "select * from theloai"
        cursor.execute(sql)
        theloai =cursor.fetchall()

        return theloai
    #xu ly them the loai
    def handleThemTheLoai(self,tenloai):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO theloai(tenloai) VALUES (%s)"
            val = (tenloai,)
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            if "1062" in str(e):
                print("Error: Duplicate entry detected!")
                return False
            else:
                print("Error:", e)
                return False
        finally:
            self.mydb.close()
    #xu ly xoa the loai
    def handleXoaTheLoai(self, maloai, tenloai):
        if not maloai and not tenloai:
            return False
        if not maloai:
            sql = "DELETE FROM theloai WHERE tenloai = %s"
            val = (tenloai,)
        elif not tenloai:
            sql = "DELETE FROM theloai WHERE maloai = %s"
            val = (maloai,)
        else: 
            sql = "DELETE FROM theloai WHERE maloai = %s AND tenloai = %s"
            val = (maloai,tenloai)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly cap nhat loai
    def handleSuaTheLoai(self, maloai, tenloai):
        if not maloai or not tenloai:
            return False
        else: 
            sql = "UPDATE theloai SET tenloai = %s WHERE maloai = %s"
            val = (tenloai, maloai)
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql, val)
            # print(cursor)
            cursor.close()
            self.mydb.commit()
            return True
        except Error  as e:
            print(e)
            return False
    #xu ly tim the loai
    def handleTimTheLoai(self, maloai, tenloai):
        cursor = self.mydb.cursor()
        sql = """
                SELECT *
                FROM theloai
                WHERE  maloai LIKE %s AND tenloai LIKE %s
                ORDER BY maloai
            """
        val = (f'{maloai}%', f'{tenloai}%')
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    # xu li dang ky
    def handleRegister(self, account):
        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO taikhoan (username, pass) VALUES (%s, %s)"
            #Bam mat khau 
            hash_pass = sha256(account['pass'].encode('utf-8')).hexdigest()
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
            return madocgia[0]
        except Error as e:
            print(e)
        finally:
            self.mydb.close()          
    # lay mat khau hien tai        
    def getCurrentPassword(self, madocgia):
        try:
            cursor = self.mydb.cursor()
            sql = """SELECT taikhoan.pass 
                        FROM docgia JOIN taikhoan ON docgia.username = taikhoan.username
                        WHERE docgia.madocgia = %s
                    """
            val = (madocgia,)
            cursor.execute(sql, val)
            password = cursor.fetchone()
            return password[0]
        except Error as e:
            print(e)
    #lay thay doi mat khau
    def changePassword(self, madocgia, password):
        try:
            hash_pass = sha256(password.encode('utf-8')).hexdigest()
            cursor = self.mydb.cursor()
            procName = "ChangePassword"
            val = (madocgia, hash_pass)
            cursor.callproc(procName, val)
            results = cursor.fetchall()
            self.mydb.commit()
        except Error as e:
            print(e) 
    #load du lieu huyen
    def handleLoadHuyen(self):
        cursor = self.mydb.cursor()
        sql = """
                SELECT *
                FROM huyen;
            """
        cursor.execute(sql)
        results =cursor.fetchall()
        return results
    #load du lieu phuong
    def handleLoadPhuong(self, mahuyen):
        cursor = self.mydb.cursor()
        sql = """
                SELECT *
                FROM phuong
                WHERE mahuyen = %s;
            """
        val = (mahuyen, )
        cursor.execute(sql, val)
        results =cursor.fetchall()
        return results
    #load profile data
    def handleLoadProfile(self, madocgia):
        cursor = self.mydb.cursor()
        sql = """
                        SELECT dg.firstname, dg.lastname, dg.gender, DAY(dg.birth), MONTH(dg.birth), YEAR(dg.birth), dg.phone, dg.email, h.tenhuyen, p.tenphuong, dg.diachi
                        FROM docgia dg
                            LEFT JOIN phuong p ON dg.maphuong = p.maphuong
                            LEFT JOIN huyen h ON p.mahuyen = h.mahuyen
                        WHERE dg.madocgia LIKE %s;
                """
        val = (madocgia,)
        cursor.execute(sql, val)
        results =cursor.fetchone()
        return results
    #edit profile
    def handleEditProfile(self, madocgia, profile):
        try:
            cursor = self.mydb.cursor()
            sql = "CALL UpdateDocGia (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (madocgia, 
                   profile['firstname'], 
                   profile['lastname'], 
                   profile['gender'],
                   profile['birthday'],
                   profile['phone'], 
                   profile['email'], 
                   profile['tenphuong'], 
                   profile['diachi'])
            cursor.execute(sql, val)
            self.mydb.commit()
            return True
        except Error as e:
            print(e)
            return False
        

    def generate_random_string(self):
        characters = string.ascii_letters + string.digits  # Use uppercase letters and digits
        random_string = ''.join(random.choice(characters) for _ in range(8))
        return random_string
