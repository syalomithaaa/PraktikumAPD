attempts = 0
while attempts < 3 :

    username = input("masukkan username anda : ")
    password = int(input("masukkan password : "))
    if username == "mita" and password == 98:
        lanjut = input("mau lanjut apa ga? : ")
        if lanjut == "berhenti" :
            print("program sudah dihentikan : ")
        else : 
            print("yeyy berhasil masuk : ")
        hari = input("ingin membeli tiket dihari apa? : ")
        uang = int(input("masukkan jumlah uangnya : "))
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" :
            if uang >= 40000:
                print("asik berhasil beli tiketnya di hari {hari}")
                break
            else:
                print(f"yahh uangnya ga cukup")
                break
        elif hari == "jumat" :
            if uang >= 45000 :
                print(f"asik berhasil beli tiketnya di hari {hari}")
                break
            else:
                print(f"yahh uangnya ga cukup")
                break
        elif hari == "sabtu" :
            if uang >=55000 :
                print(f"asik berhasil beli tiketnya di hari {hari}")
                break
            else :
                print(f"yahh uangnya ga cukup")
                break
        elif hari == "minggu" :
            if uang >= 60000 :
                print(f"asik berhasil beli tiketnya di hari {hari}")
                break
            else:
                print(f"yahh uangnya ga cukup")
                break
        else:
            print(f"hari yang anda masukkan kurang jelas!")
    else :
        print("username atau passwordnya salah, coba lagi!")
        lanjut = input("mau lanjut apa ga? : ")
        if lanjut == "berhenti" :
            print("program telah berhenti")
        else :
            attempts += 1
            print(f"akses ditolak kah uda gagal {attempts}")
