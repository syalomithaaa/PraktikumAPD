nama = input("Syalomitha Novindriani Depe:")
hari = input("senin, selasa, rabu, kamis, jumat, sabtu, minggu): ")
harga_tiket = 0

if hari.lower() in ['senin', 'selasa', 'rabu', 'kamis']:
    harga_tiket = 40000
elif hari.lower() == 'jumat':
    harga_tiket = 45000
elif hari.lower() == 'sabtu':
    harga_tiket = 55000
elif hari.lower() == 'minggu':
    harga_tiket = 60000
else:
    print("hari yang dimasukkan tidak valid.")
    exit()

uang = int(input("masuk jumlah uang yang kalian miiki: Rp "))

if uang < harga_tiket:
    print(f"maaf {nama}, uang kamu tidak cukup untuk membeli tiket pada hari {hari}.")
else:
    print(f"selamat {nama}, kamu bisa membeli tiket pada hari {hari}!")