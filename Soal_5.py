import os
import csv
import json
import logging

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 1) Membuat folder 'data' jika belum ada
folder = "data"
os.makedirs(folder, exist_ok=True)

# 2) Menulis file CSV presensi
csv_path = os.path.join(folder, "presensi.csv")
data_presensi = [
    {"nim": "A001", "nama": "Andi", "hadir_uts": 1},
    {"nim": "A002", "nama": "Budi", "hadir_uts": 0},
    {"nim": "A003", "nama": "Citra", "hadir_uts": 1}
]

try:
    logging.info("Menulis file presensi.csv...")
    with open(csv_path, mode="w", newline="") as file_csv:
        fieldnames = ["nim", "nama", "hadir_uts"]
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_presensi)
    logging.info("File presensi.csv berhasil ditulis.")
except Exception as e:
    logging.error(f"Gagal menulis file CSV: {e}")

# 3) Membaca kembali CSV dan menghitung ringkasan
json_path = os.path.join(folder, "ringkasan.json")

try:
    logging.info("Membaca file presensi.csv dan menghitung ringkasan...")

    with open(csv_path, mode="r") as file_csv:
        reader = csv.DictReader(file_csv)
        total = 0
        hadir = 0

        for row in reader:
            total += 1
            if int(row["hadir_uts"]) == 1:
                hadir += 1

        persentase = (hadir / total) * 100 if total > 0 else 0

    # Simpan hasil ringkasan ke file JSON
    ringkasan = {
        "total_mahasiswa": total,
        "jumlah_hadir": hadir,
        "persentase_hadir": f"{persentase:.2f}%"
    }

    with open(json_path, mode="w") as file_json:
        json.dump(ringkasan, file_json, indent=4)

    logging.info("Ringkasan berhasil disimpan ke ringkasan.json.")
except Exception as e:
    logging.error(f"Gagal membaca/menulis file: {e}")

# os.makedirs(..., exist_ok=True): membuat folder jika belum ada.

# csv.DictWriter: menulis data ke file CSV.

# csv.DictReader: membaca kembali file CSV.

# json.dump: menyimpan ringkasan ke file JSON.

# try/except: menangani error saat baca/tulis file. 
# try: digunakan untuk mencoba menjalankan proses baca/tulis file.
# except Exception as e: akan menangkap error-nya

# logging: mencatat proses dengan level INFO dan ERROR.