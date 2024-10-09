daftar_buku = {
    "buku1" : "harry potter",
    "buku2" : "percy jackson",
    "buku3" : "twillight"
}
print(daftar_buku["buku1"])
print(daftar_buku["buku2"])
print(daftar_buku["buku3"])
print(daftar_buku)

Biodata = {
"Nama" : "Aldy Ramadhan Syahputra",
"NIM" : 2109106079,
"KRS" : ["Program Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" :True,
"Social Media" : {
"Instagram" : "@aldyrmdhns_",
"Discord" : "\'Izanami#6848"
}
}

# print(biodata["krs"][0])
# print(biodata["social media"]["email"])
games = {
    "game1" : "PUBG MOBILE",
}
games = dict(sekiro = "action", pokemon = "adventure",
valorant = {"nama" : {123 : "informatika"}} )
print(games['valorant']['nama'][123])

games = {
    "game1" : "PUBG Mobile",
    "game2" : "mobile legends",
    "game3" : {
        "nama" : "COC",
        "genre" : "strategy"
    }
}
print((games.get('game3')).get('genre'))

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#tanpa menggunakan items
for i in Nilai:
    print(i)
print("")
#menggunakan items
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Sebelum Ditambah
print(Film)


Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})


#Setelah Ditambah
print(Film)


Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Sebelum Diubah
print(Film)
Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})

#Setelah diubah
print(Film)

data = {
"Nama" : "Aldy",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
del data["Nama"]
#Setelah diubah
print(data)
#memanggil data yang telah dihapus
print(data.get("Nama"))

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "TheParis"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
for song in j:
    print(song)
print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
for key_a, value_a in value.items():
    print (key_a, " : ", value_a)
print("")

mahasiswa = {
    "nama": "mita",
    "umur": "17",
    "nim": "098",
    "jurusan": "informatika",
    "angkatan": "24"
}

mahasiswa["fakultas"] = input("masukkan fakultas:")
print(mahasiswa)
