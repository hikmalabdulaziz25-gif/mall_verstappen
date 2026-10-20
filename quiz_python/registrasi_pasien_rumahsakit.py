import json
import os

FILE_DATA = "data_pasien.json"



def muat_data():
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Data pasien tidak dapat dibaca.")

    return []


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def registrasi_pasien(data):
    print("\n========== REGISTRASI PASIEN ==========")

    nama = input("Nama lengkap       : ").strip()

    if not nama:
        print("Nama tidak boleh kosong!")
        return

    umur_input = input("Umur               : ").strip()

    if not umur_input.isdigit() or int(umur_input) <= 0:
        print("Umur harus berupa angka lebih dari 0!")
        return

    umur = int(umur_input)

    print("\nJenis Kelamin:")
    print("1. Laki-laki")
    print("2. Perempuan")

    pilihan = input("Pilih [1/2]        : ").strip()

    if pilihan == "1":
        jenis_kelamin = "Laki-laki"
    elif pilihan == "2":
        jenis_kelamin = "Perempuan"
    else:
        print("Pilihan tidak valid!")
        return

    alamat = input("Alamat             : ").strip()
    telepon = input("Nomor telepon      : ").strip()

    print("\nJenis Pasien:")
    print("1. Umum")
    print("2. BPJS")

    pilihan = input("Pilih [1/2]        : ").strip()

    if pilihan == "1":
        jenis_pasien = "Umum"
    elif pilihan == "2":
        jenis_pasien = "BPJS"
    else:
        print("Pilihan tidak valid!")
        return

    print("\nPilihan Poli:")
    print("1. Poli Umum")
    print("2. Poli Gigi")
    print("3. Poli Anak")
    print("4. Poli Penyakit Dalam")

    pilihan = input("Pilih poli [1-4]   : ").strip()

    daftar_poli = {
        "1": "Poli Umum",
        "2": "Poli Gigi",
        "3": "Poli Anak",
        "4": "Poli Penyakit Dalam"
    }

    if pilihan not in daftar_poli:
        print("Pilihan poli tidak valid!")
        return

    poli = daftar_poli[pilihan]
    keluhan = input("Keluhan pasien     : ").strip()

    # Membuat nomor antrean yang tidak digunakan sebelumnya
    nomor_antrean = max(
        (pasien["nomor_antrean"] for pasien in data),
        default=0
    ) + 1

    pasien = {
        "nomor_antrean": nomor_antrean,
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "alamat": alamat,
        "telepon": telepon,
        "jenis_pasien": jenis_pasien,
        "poli": poli,
        "keluhan": keluhan
    }

    data.append(pasien)
    simpan_data(data)

    print("\n========================================")
    print("       REGISTRASI BERHASIL!")
    print("========================================")
    print(f"Nomor Antrean : {nomor_antrean:03d}")
    print(f"Nama          : {nama}")
    print(f"Umur          : {umur} tahun")
    print(f"Poli Tujuan   : {poli}")
    print(f"Jenis Pasien  : {jenis_pasien}")
    print("Silakan menunggu panggilan antrean.")
    print("========================================")


# MENAMPILKAN SEMUA DATA PASIEN
def lihat_data_pasien(data):
    print("\n========== DATA PASIEN ==========")

    if not data:
        print("Belum ada pasien yang terdaftar.")
        return

    for pasien in data:
        print("----------------------------------------")
        print(f"Nomor Antrean : {pasien['nomor_antrean']:03d}")
        print(f"Nama          : {pasien['nama']}")
        print(f"Umur          : {pasien['umur']} tahun")
        print(f"Jenis Kelamin : {pasien['jenis_kelamin']}")
        print(f"Alamat        : {pasien['alamat']}")
        print(f"Telepon       : {pasien['telepon']}")
        print(f"Jenis Pasien  : {pasien['jenis_pasien']}")
        print(f"Poli          : {pasien['poli']}")
        print(f"Keluhan       : {pasien['keluhan']}")

    print("----------------------------------------")


# MENCARI PASIEN
def cari_pasien(data):
    print("\n========== CARI PASIEN ==========")

    nama_cari = input("Masukkan nama pasien: ").strip().lower()

    hasil = [
        pasien for pasien in data
        if nama_cari and nama_cari in pasien["nama"].lower()
    ]

    if not hasil:
        print("Pasien tidak ditemukan.")
        return

    for pasien in hasil:
        print("----------------------------------------")
        print(f"Nomor Antrean : {pasien['nomor_antrean']:03d}")
        print(f"Nama          : {pasien['nama']}")
        print(f"Umur          : {pasien['umur']} tahun")
        print(f"Poli          : {pasien['poli']}")
        print(f"Jenis Pasien  : {pasien['jenis_pasien']}")


# MENGHAPUS DATA PASIEN
def hapus_pasien(data):
    print("\n========== HAPUS DATA PASIEN ==========")

    if not data:
        print("Belum ada data pasien.")
        return

    try:
        nomor = int(input("Masukkan nomor antrean: "))
    except ValueError:
        print("Nomor antrean harus berupa angka!")
        return

    for pasien in data:
        if pasien["nomor_antrean"] == nomor:
            print(f"Nama pasien: {pasien['nama']}")

            konfirmasi = input(
                "Yakin menghapus data? (y/n): "
            ).strip().lower()

            if konfirmasi == "y":
                data.remove(pasien)
                simpan_data(data)
                print("Data pasien berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

            return

    print("Nomor antrean tidak ditemukan.")


# MENU UTAMA
def menu_utama():
    data = muat_data()

    while True:
        # Tidak membersihkan terminal agar hasil sebelumnya tetap terlihat
        print("\n\n")
        print("=" * 44)
        print("  SISTEM REGISTRASI PASIEN RUMAH SAKIT")
        print("=" * 44)
        print("1. Registrasi Pasien")
        print("2. Lihat Data Pasien")
        print("3. Cari Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        print("=" * 44)

        pilihan = input("Pilih menu [1-5]: ").strip()

        if pilihan == "1":
            registrasi_pasien(data)

        elif pilihan == "2":
            lihat_data_pasien(data)

        elif pilihan == "3":
            cari_pasien(data)

        elif pilihan == "4":
            hapus_pasien(data)

        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")


# MENJALANKAN PROGRAM
if __name__ == "__main__":
    menu_utama()