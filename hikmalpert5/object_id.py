# Sumber PDF: A.21.1. Object ID
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Di Python, semua object atau data memiliki identifier, yaitu angka unik yang | merepresentasikan data tersebut. Sebagai contoh, pada kode berikut nilai | numerik 24 tersimpan pada variabel number , ID nya adalah | 140728206353928 . | Output program di atas jika di-run:

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))
print(a == b)
print(a is b)
