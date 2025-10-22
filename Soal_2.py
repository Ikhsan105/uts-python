# Meminta input dari pengguna sebanyak 3 kali
setoran1 = int(input("Masukkan setoran minggu pertama: "))
setoran2 = int(input("Masukkan setoran minggu kedua: "))
setoran3 = int(input("Masukkan setoran minggu ketiga: "))

# Validasi: jika ada setoran yang kurang dari atau sama dengan 0
if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid. Semua setoran harus lebih dari 0.")
else:
    # Menjumlahkan semua setoran
    total = setoran1 + setoran2 + setoran3
    print(f"Total setoran: Rp{total}")

    # Menentukan kategori berdasarkan total
    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")

# input() digunakan untuk menerima angka dari pengguna.

# int() mengubah input string menjadi bilangan bulat.

# if setoran <= 0: memeriksa apakah ada input tidak valid.

# total = ...: menjumlahkan ketiga setoran.

# if-elif-else: menentukan kategori berdasarkan nilai total.