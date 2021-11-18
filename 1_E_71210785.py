print ("=== Kalkulator Akar dan Pangkat ===")
print ("Pilihan menu :")
print ("1. Pangkat 2 (Kuadrat)")
print ("2. Pangkat 3 (Kubik)")
print ("3. Akar Kuadrat")
x = int(input("Masukan menu yang anda pilih : ")) 
if x == 1:
    bilangan = int(input("Masukkan bilangan yang ingin di pangkatkan: "))
    hasil = bilangan ** 2
    print ("Hasil dari pemangkatan bilangan" ,bilangan ,"dengan 2 (Kuadrat) adalah" ,hasil)
elif x == 2:
    bilangan = int(input("Masukkan bilangan yang ingin di pangkatkan: "))
    hasil = bilangan ** 3
    print ("Hasil dari pemangkatan bilangan" ,bilangan ,"dengan 3 (Kubik) adalah" ,hasil)
elif x == 3:
    bilangan = int(input("Masukkan bilangan yang ingin di akarkan: "))
    hasil = bilangan ** (1.0/2)
    print ("Hasil dari akar kuadrat dari bilangan" ,bilangan ,"adalah" ,hasil)
else:
    print ("Pilihan menu yang dimasukan tidak sesuai!")