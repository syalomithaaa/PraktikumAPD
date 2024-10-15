# List data cuaca
cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]
temperatures = [30, 25, 32, 28]

# Menampilkan data cuaca menggunakan list
print("Data cuaca menggunakan list:")
for i in range(len(cities)):
    print(f"Cuaca di {cities[i]} adalah {temperatures[i]} derajat Celsius.")

# Dictionary data cuaca
weather = {
    "Jakarta": 30,
    "Bandung": 25,
    "Surabaya": 32,
    "Yogyakarta": 28
}

# Menampilkan data cuaca menggunakan dictionary
print("\nData cuaca menggunakan dictionary:")
for city, temp in weather.items():
    print(f"Cuaca di {city} adalah {temp} derajat Celsius.")
