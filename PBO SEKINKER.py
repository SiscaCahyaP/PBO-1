import sqlite3
class Pengguna:
    def login(Username, Password):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'SELECT namaadmin, password FROM admin \
        where namaadmin=\'%s\' and password=\'%s\' '
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        rows =cur.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False
        if accept_Login == False:
            print("Login Gagal")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True
            print("Login Sukses")
            return Username
        
        con.close()
    def daftarbaru(NamaAdmin, Password, Merk):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'INSERT INTO admin (namaadmin, password, merk) \
            VALUES (\'%s\', \'%s\', \'%s\')' 
        query = query % (NamaAdmin, Password, Merk)
        cur.execute(query)
        con.commit()
        con.close()
        print("Pendaftaran Akun Akun Sukses")
    
    def updateprofile(Username, Password):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = "SELECT password From admin where namaadmin = \'%s\' and password = \'%s\'"
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        quen = cur.fetchall()
        a = input("Masukkan Password Baru : ")
        b = quen[0][0]
        b = a
        query = "UPDATE admin SET password = \'%s\' Where namaadmin = \'%s\' and password = \'%s\'" 
        query = query % (b, Username, Password)
        cur.execute(query)
        con.commit()
        con.close()
        print("Password Berhasil di Ubah")
        

class Produk:
    def hargadandetail():
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        cur.execute("SELECT * From produk")
        rows =cur.fetchall()
        print ("|id | Nama Produk     | Harga     | Merk     |")
        for item in rows :
            print ("|",item[0],"|",item[1]," "*(14-len(item[1])),"| Rp.",item[2],"|",item[3],"|")
            
        con.close()
        
    def tambahproduk(ProdukId, NamaProduk,Harga, Merk):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'INSERT INTO produk (produkid, namaproduk, harga,merk) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (ProdukId, NamaProduk,Harga, Merk)
        cur.execute(query)
        con.commit()
        con.close()
        print("Produk Berhasil di Tambahkan")
        
    def editdataproduk(ProdukId):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = "SELECT * From produk where produkid = \'%s\'"
        query = query % (ProdukId)
        cur.execute(query)
        con.commit()
        quen = cur.fetchall()
        a = input("Masukkan Nama Produk : ")
        b = input("Masukkan Harga Produk : Rp. ")
        c = input("Masukkan Merk Produk : ")
        query = "UPDATE produk SET namaproduk = \'%s\',harga = \'%s\', merk = \'%s\' Where produkid = \'%s\' "
        query = query % (a, b, c,ProdukId)
        cur.execute(query)
        con.commit()
        con.close()
        print("data Berhasil di Ubah")
        
    def hapusproduk(ProdukId):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = "SELECT * From produk where produkid = \'%s\'"
        query = query % (ProdukId)
        cur.execute(query)
        con.commit()
        quen = cur.fetchall()
        query = "DELETE FROM produk Where produkid = \'%s\' "
        query = query % (ProdukId)
        cur.execute(query)
        con.commit()
        con.close()
        print("data Berhasil di Hapus")

class Transaksi:
    def transaksiproduk(TanggalOrder,ProdukID):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = "SELECT namaproduk,[harga] From produk where produkid = \'%s\'"
        query = query % (ProdukID)
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        print("Nama Produk : ",rows[0][0])
        print("Harga Produk : ",rows[0][1])
        harga = rows[0][1]
        jumlah = input("Jumlah Beli (Pcs) : ")
        totalharga = int(harga)* int(jumlah)
        print("Total Harga   :Rp. ",totalharga)
        discon = input("Discon  (%) :")
        seratus = 100
        jumlahdiscon =int(discon)* (int(totalharga)/100)
        print("Total Discon   :Rp. ",jumlahdiscon)
        totalbayar =int(totalharga)-int(jumlahdiscon)
        print("Total Bayar   :Rp. ",totalbayar)
        query = 'INSERT INTO transaksi (tanggalorder,produkid, jumlahbeli, totalharga,discon,totalbayar) \
        VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (TanggalOrder,ProdukID, jumlah,totalharga,jumlahdiscon,totalbayar)
        cur.execute(query)
        con.commit()
        con.close()
        return rows
        print("Transaksi Telah Tersimpan")
        
