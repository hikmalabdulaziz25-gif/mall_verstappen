# Sumber PDF: A.23.3. Optional argument
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Suatu parameter bisa ditentukan nilai default-nya saat deklarasi fungsi. | Efeknya, saat pemanggilan fungsi diperbolehkan untuk tidak mengisi nilai | argument karena nilai default sudah ditentukan. | Sebagai contoh, pada fungsi print_matrix() berikut, parameter matrix di- | set nilai default-nya adalah list kosong [] . Fungsi print_matrix() dipanggil

def sapa(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")
sapa("Ahmad")
sapa("Ahmad", "Selamat pagi")
