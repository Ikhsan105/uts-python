# kasir.py

# Daftar harga barang
harga_barang = {
    "apel": 3000,
    "pisang": 2500,
    "jeruk": 4000
}

def hitung_total(pesanan):
    total = 0
    for nama_barang, jumlah in pesanan.items():
        harga = harga_barang.get(nama_barang, 0)
        total += harga * jumlah
    return total

# Contoh pesanan
pesanan_pelanggan = {
    "apel": 2,
    "jeruk": 1
}

# Hitung dan tampilkan total
total_bayar = hitung_total(pesanan_pelanggan)
print(f"Total yang harus dibayar: Rp{total_bayar}")

# harga_barang: dictionary berisi nama barang dan harganya.

# hitung_total: fungsi untuk menghitung total belanja berdasarkan pesanan.

# pesanan_pelanggan: contoh input pesanan.

# print: menampilkan total harga yang harus dibayar.