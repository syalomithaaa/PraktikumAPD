# nama = ["shandy",106,True,
#        ["yuyun",145],3.96,
#        [123,"ALVITO",False,3.66],
#        "rehan"]
# print(nama[4])

# matkul = ["APD",
#          "APL",
#          "WEB",
#          "JARKOM",
#          "BASDAT",
#          "STRUKDAT",
#          "PTI",
#          "KALKULUS",
#          "PROBAS"
# ]
# print(nama[1])
# print(matkul[3])

# makanan = ["bakso","sate","soto","nasi goreng","ayam bakar","cumi goreng"]
# print("sebelum: ")
# print(makanan)
# makanan.append("nasi goreng")
# mkanan.clear()
# data = makanan.pop("5")
# print(makanan)
# print(data)
# print(makanan)
# makanan.insert(2,"nasi goreng")
# makanan[0] = ["AYAM","BEBEK"]
# print(makanan)


# minuman = ["susu","jus mangga","jus sirsak",
#           "es teler","es teh","es buah"]
# print("sebelum")
# print(minuman)
# del minuman[3]
# print("sesudah")
# print(minuman)
# minuman[4] = "air putih"
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)

makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"],
           ["teh","kopi","air"]]

for i in makanan :
    if isinstance(i, list) :
        for j in i :
            print(j)
    else:
        print(i)
# for i in makanan :
#     for j iin i :
#         print(j)


While True:
    print("Hallo! selamat datang di aplikasi catatan")
    print("silahkan pilih 'daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'login' ")
    print("1. daftar akun")
    print("2. login")
    print("3. exit")
    print("----------------------------")
    opsi = input("pilih opsi: ")
    print(" ")

    if opsi == "1":
       print("hallo pengguna baru! ayo buat akun dulu")
       username = input("username: ")
       akuna = False
       for akun in akuns:
           if akun[0] == username:   # memeriksa apakah username sudah ada
               akuna = True
               break
        if akuna:
           print("nama sudah terpakai untuk registrasi silahkan coba lgi")
           