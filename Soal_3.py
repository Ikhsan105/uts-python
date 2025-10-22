# Daftar tarif dasar per kota
tarif_dasar = {
    "Jakarta": 10000,
    "Bandung": 12000,
    "Surabaya": 15000
}

def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkos kirim berdasarkan kota, berat, dan asuransi.
    """
    tarif = tarif_dasar.get(kota, 0)  # Ambil tarif dasar kota, default 0 jika tidak ditemukan
    tarif += 2000 * berat_kg          # Tambah biaya berdasarkan berat
    if asuransi:
        tarif += 3000                 # Tambah biaya asuransi jika dipilih
    return tarif

# Contoh 1: Kirim ke Jakarta, 2 kg, tanpa asuransi
print(hitung_ongkir(2, "Jakarta"))  # Output: 14000

# Contoh 2: Kirim ke Surabaya, 3 kg, dengan asuransi
print(hitung_ongkir(3, "Surabaya", asuransi=True))  # Output: 21000

# tarif_dasar: dictionary berisi tarif dasar tiap kota.

# berat_kg: parameter berat kiriman.

# asuransi=False: parameter opsional, default-nya tidak diasuransikan.

# get(kota, 0): jika kota tidak ditemukan, tarif dasar dianggap 0.

# Fungsi fleksibel dan mudah digunakan untuk berbagai skenario pengiriman.