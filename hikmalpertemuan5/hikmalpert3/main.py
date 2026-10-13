# MENU UTAMA - semua kode dari PDF

latihan = {
    "1": "01_for_range.py",
    "2": "02_range_dan_list.py",
    "3": "03_range_start_stop.py",
    "4": "04_range_start_stop_step.py",
    "5": "05_tiga_range_setara.py",
    "6": "06_range_tambahan.py",
    "7": "07_iterasi_list_tuple.py",
    "8": "08_iterasi_string.py",
    "9": "09_iterasi_dictionary.py",
    "10": "10_iterasi_set.py",
    "11": "11_nested_for.py",
    "12": "12_print_end.py",
    "13": "13_while_bool.py",
    "14": "14_while_logika.py",
    "15": "15_increment_decrement.py",
    "16": "16_while_vs_for.py",
    "17": "17_nested_while.py",
    "18": "18_nested_for_sebelumnya.py",
    "19": "19_kombinasi_for_while.py",
    "20": "20_break.py",
    "21": "21_continue.py",
    "22": "22_label_perulangan.py",
    "23": "23_list_dasar.py",
    "24": "24_index_list.py",
    "25": "25_perulangan_list.py",
    "26": "26_enumerate.py",
    "27": "27_nested_list.py",
    "28": "28_list_range.py",
    "29": "29_list_range_lanjutan.py",
    "30": "30_list_string_tuple.py",
    "31": "31_latihan_gabungan.py",
}

print("=== PYTHON - PERULANGAN & LIST ===")
for nomor, nama in latihan.items():
    print(f"{nomor}. {nama}")

pilihan = input("Masukkan nomor latihan: ").strip()

if pilihan in latihan:
    with open(latihan[pilihan], encoding="utf-8") as file:
        exec(file.read())
else:
    print("Pilihan tidak tersedia.")
