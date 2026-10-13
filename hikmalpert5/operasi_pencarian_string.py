# Sumber PDF: A.17.7. Operasi pencarian string &
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: substring | ◉ Pengecekan string menggunakan keyword in | Keyword in bisa digunakan untuk mengecek apakah suatu string merupakan | bagian dari string lain. Nilai balik statement adalah boolean. Contoh: | Teknik tersebut bisa dikombinasikan dengan seleksi kondisi if :

text = "hello world hello world"
print("ello" in text)
print(text.startswith("hell"))
print(text.endswith("world"))
print(text.count("ello"))
print(text.find("worl"))
print(text.rfind("worl"))
