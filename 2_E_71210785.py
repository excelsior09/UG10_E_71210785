# s = suhu tubuh 
s = float(input("Masukan Suhu tubuh Anda : "))
if s > 50:
    print ("Anda bukan Manusia :)")
elif s < 32:
    print ("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif (s > 37.5) and  (s <= 50):
    print ("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
elif (s >= 32) and (s <= 37.5):
    print ("Suhu Anda normal!")