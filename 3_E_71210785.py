daftar = (input("Masukan daftar siswa : "))
print ("Daftar siswa :" ,daftar.title().split(","))
tambah = (input("Masukan siswa yang ingin ditambahkan : "))
wak = ([daftar.title(), tambah.upper()])
if tambah not in daftar:
    print ("Hasil penambahan pada daftar siswa : " , wak)
else:
    print ("Siswa atas nama" ,tambah.upper(),"sudah berada dalam daftar siswa.")
