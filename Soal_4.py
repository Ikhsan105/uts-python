# Data jadwal per hari disimpan dalam dictionary
jadwal = {
    "Senin": ["Matematika", "Fisika"],
    "Selasa": ["Biologi", "Bahasa Inggris"],
    "Rabu": ["Kimia", "Sejarah"],
    "Kamis": ["Ekonomi", "Seni"],
    "Jumat": ["Olahraga", "Agama"]
}

def jadwal_hari(hari):
    """
    Menampilkan jadwal mata kuliah berdasarkan nama hari.
    """
    if hari in jadwal:
        print(f"Jadwal hari {hari}:")
        for mata_kuliah in jadwal[hari]:
            print(f"- {mata_kuliah}")
    else:
        print("Hari tidak ditemukan dalam jadwal.")

jadwal_hari("Rabu")
jadwal_hari("Sabtu")

# Pencarian hari dilakukan dengan mengecek satu per satu isi list kunci dalam dictionary jadwal
# untuk menemukan kecocokan dengan input hari.