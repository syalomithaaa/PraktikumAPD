cuaca_hari_ini = []
lokasi = "Bandung"
suhu_total = 0
jumlah_data = 0

def tampilkan_cuaca():
    print("Daftar cuaca hari ini di", lokasi)
    for cuaca in cuaca_hari_ini:
        print(cuaca)

def tambah_cuaca(jenis_cuaca, suhu):
    global suhu_total, jumlah_data
    cuaca_hari_ini.append(f"{jenis_cuaca} dengan suhu {suhu}°C")
    suhu_total += suhu
    jumlah_data += 1

def hitung_suhu_rata_rata():
    if jumlah_data == 0:
        return 0
    return suhu_total / jumlah_data

def hapus_cuaca(index):
    if 0 <= index < len(cuaca_hari_ini):
        global suhu_total, jumlah_data
        # Mengurangi suhu dari total sebelum menghapus
        suhu_lama = int(cuaca_hari_ini[index].split()[-1][:-2])
        suhu_total -= suhu_lama
        del cuaca_hari_ini[index]
        jumlah_data -= 1
        print("Data cuaca di index", index, "telah dihapus.")
    else:
        print("Index tidak valid.")

def update_cuaca(index, jenis_cuaca, suhu):
    if 0 <= index < len(cuaca_hari_ini):
        global suhu_total
        # Mengurangi suhu dari total sebelum update
        suhu_lama = int(cuaca_hari_ini[index].split()[-1][:-2])
        suhu_total -= suhu_lama
        cuaca_hari_ini[index] = f"{jenis_cuaca} dengan suhu {suhu}°C"
        suhu_total += suhu
        print("Data cuaca di index", index, "telah diupdate.")
    else:
        print("Index tidak valid.")

tambah_cuaca("Cerah", 28)
tambah_cuaca("Hujan", 22)
tampilkan_cuaca()
print("Suhu rata-rata:", hitung_suhu_rata_rata(), "°C")

update_cuaca(1, "Hujan Ringan", 20)
tampilkan_cuaca()
print("Suhu rata-rata:", hitung_suhu_rata_rata(), "°C")

hapus_cuaca(0)
tampilkan_cuaca()
print("Suhu rata-rata:", hitung_suhu_rata_rata(), "°C")