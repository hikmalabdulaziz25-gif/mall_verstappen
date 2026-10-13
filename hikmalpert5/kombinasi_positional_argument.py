# Sumber PDF: A.23.4. Kombinasi positional argument,
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: keyword argument, dan optional | argument | Parameter fungsi bisa berisi nilai default (seperti pada contoh sebelumnya) | atau tidak, atau bisa juga kombinasi keduanya. | Kode program berikut adalah contoh pengaplikasiannya. Fungsi

def profil(nama, umur, prodi="Sistem Informasi"):
    print(nama, umur, prodi)
profil("Ahmad", 20)
profil("Budi", 21, prodi="Teknik Informatika")
