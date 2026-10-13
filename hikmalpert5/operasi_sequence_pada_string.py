# Sumber PDF: A.17.5. Operasi sequence pada string
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: String masih termasuk kategori tipe data sequence, yang artinya bisa | digunakan pada operasi standar sequence, contoh seperti perulangan, | pengaksesan elemen, dan slicing. | ◉ Mengecek jumlah karakter string | Fungsi len() ketika digunakan pada tipe data string mengembalikan

text = "hello python"
print("length:", len(text))
print("index 0:", text[0])
print("slice:", text[1:5])
for char in text:
    print(char)
