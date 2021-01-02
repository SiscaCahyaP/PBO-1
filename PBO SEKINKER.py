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
    def totaltransaksi():
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute('SELECT COUNT(*) from transaksi')
        cur_result = cur.fetchone()
        rows = cur_result[0]
        print("Total Transaksi : ",rows)
        con.close()

def intro():
    print("\t\t\t\t____________________________________________________________")
    print("\t\t\t\t\t\tPENGOLAHAN PRODUK BARANG")
    print("\t\t\t\t------------------------------------------------------------")

    print("\t\t\t\t\t\tDibuat Oleh:")
    print("\t\t\t\t\t\tSISCA CAHYA PUSPITA")
    print("\t\t\t\t\t\tALIYA ROHMATUL ULFA")
    print("\t\t\t\t------------------------------------------------------------")	


ch=''
intro()

while ch != 11:
    print("\tMAIN MENU")
    print("\t1. Login")
    print("\t2. Register/Daftar Akun Baru")
    print("\t3. Update Profile")
    print("\t4. Tampilkan Harga dan Detail Produk")
    print("\t5. Tambah Produk Baru")
    print("\t6. Update Produk")
    print("\t7. Hapus Produk")
    print("\t8. Transaksi")
    print("\t9. Total Transaksi")
    print("\t10. Exit")
	
    print("Note : Silahkan Pilih Login Terlebih Dahulu")
    ch = int(input("\tSilahkan Input Nomor Pilihan Anda (1-9) :  "))
    
    if ch == 1:
        print("Login")
        Username = input("Masukkan email Akun Anda : ")
        Password = input("Masukkan Password Anda : ")
        Akun = Pengguna.login(Username,Password)
    
    elif ch == 2:
        print("Daftarkan Akun Baru")
        NamaAdmin= input("Masukkan email : ")
        Password = input("Masukkan Password : ")
        Merk = input("Masukkan Merk : ")
        Pengguna.daftarbaru(NamaAdmin, Password, Merk)
    elif ch == 3:
        print("Update Profil")
        Akun, Pengguna.updateprofile(Username,Password)
    elif ch == 4:
        print("Harga dan Detai Produk")
        print(Produk.hargadandetail())
    elif ch == 5:
        print("Tambah Produk Baru")
        ProdukId= input("Masukkan Kode Produk : ")
        NamaProduk = input("Masukkan Nama Produk : ")
        Harga = input("Masukkan Harga Produk : Rp. ")
        Merk = input("Masukkan Merk Produk : ")
        Akun,Produk.tambahproduk(ProdukId, NamaProduk, Harga, Merk)
    elif ch == 6:
        print("Update Produk")
        ProdukId=input("Masukkan Kode Produk : ")
        Akun,Produk.editdataproduk(ProdukId)

    elif ch == 7:
        print("Hapus Produk")
        ProdukId=input("Masukkan Kode Produk Yang Ingin di Hapus: ")
        Akun,Produk.hapusproduk(ProdukId)
        
    elif ch == 8:
        print("Transaksi Pembelian")
        TanggalOrder= input("Masukkan Tanggal Order (dd/mm/yyyy) : ")
        ProdukID = input("Masukkan Kode Produk : ")
        Akun,Transaksi.transaksiproduk(TanggalOrder,ProdukID)
    elif ch == 9:
        print("Data Transaksi")
        Akun,Transaksi.totaltransaksi()
    elif ch == 10:
        print("\tTerimakasih Sudah Menggunakan SISTEM PENGOLAHAN DATA PRODUK INI")
        break
    else :
        print("Error! Tidak ditemukan pilihan")
    
    ch = input("Apakah Mau kembali melihat MAIN MENU? (y/t) : ")
    if ch == "t":
        break


        
