# Daftar pengguna: [username, password, role]
users = [["admin", "admin123", "admin"], ["user", "user123", "user"]]

# Daftar cuaca: [tanggal, kota, cuaca]
weather_list = [
    ["2024-10-01", "Jakarta", "Cerah"],
    ["2024-10-02", "Bandung", "Hujan"],
]

# Flag untuk memeriksa login
logged_in = False
current_user = None

# Pendaftaran pengguna baru
print("=== REGISTER ===")
username = input("Masukkan username: ")
password = input("Masukkan password: ")
users.append([username, password, "user"])
print("Pendaftaran berhasil!\n")

# Login pengguna
while not logged_in:
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    # Memeriksa kredensial pengguna
    for user in users:
        if user[0] == username and user[1] == password:
            logged_in = True
            current_user = user
            print(f"Selamat datang, {username}!")
            break
    if not logged_in:
        print("Login gagal, coba lagi.\n")

# Menu utama
while True:
    if current_user[2] == "admin":
        print("\n=== MENU ADMIN ===")
        print("1. Lihat daftar cuaca")
        print("2. Tambah data cuaca")
        print("3. Update data cuaca")
        print("4. Hapus data cuaca")
        print("5. Logout")
    else:
        print("\n=== MENU PENGGUNA ===")
        print("1. Lihat daftar cuaca")
        print("2. Logout")

    choice = input("Pilih opsi: ")

    if current_user[2] == "admin":
        if choice == "1":
            print("\n=== Daftar Cuaca ===")
            for weather in weather_list:
                print(f"Tanggal: {weather[0]}, Kota: {weather[1]}, Cuaca: {weather[2]}")
        elif choice == "2":
            print("\n=== Tambah Data Cuaca ===")
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            kota = input("Masukkan kota: ")
            cuaca = input("Masukkan cuaca: ")
            weather_list.append([tanggal, kota, cuaca])
            print("Data cuaca berhasil ditambahkan.")
        elif choice == "3":
            print("\n=== Update Data Cuaca ===")
            for i, weather in enumerate(weather_list):
                print(f"{i + 1}. Tanggal: {weather[0]}, Kota: {weather[1]}, Cuaca: {weather[2]}")
            index = int(input("Pilih nomor data yang ingin diupdate: ")) - 1
            if 0 <= index < len(weather_list):
                tanggal = input("Masukkan tanggal baru (YYYY-MM-DD): ")
                kota = input("Masukkan kota baru: ")
                cuaca = input("Masukkan cuaca baru: ")
                weather_list[index] = [tanggal, kota, cuaca]
                print("Data cuaca berhasil diupdate.")
            else:
                print("Nomor tidak valid.")
        elif choice == "4":
            print("\n=== Hapus Data Cuaca ===")
            for i, weather in enumerate(weather_list):
                print(f"{i + 1}. Tanggal: {weather[0]}, Kota: {weather[1]}, Cuaca: {weather[2]}")
            index = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
            if 0 <= index < len(weather_list):
                weather_list.pop(index)
                print("Data cuaca berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        elif choice == "5":
            print("Logout berhasil.\n")
            break
        else:
            print("Pilihan tidak valid.")

    elif current_user[2] == "user":
        if choice == "1":
            print("\n=== Daftar Cuaca ===")
            for weather in weather_list:
                print(f"Tanggal: {weather[0]}, Kota: {weather[1]}, Cuaca: {weather[2]}")
        elif choice == "2":
            print("Logout berhasil.\n")
            break
        else:
            print("Pilihan tidak valid.")
