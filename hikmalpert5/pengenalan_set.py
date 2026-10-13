# Sumber PDF: A.15.2. Pengenalan Set
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Implementasi tipe data set cukup mudah, langsung tulis saja nilai elemen dengan separator , dan diapit | menggunakan tanda kurung kurawal { } . Contoh: | • Set bisa menampung element yang tipe datanya bisa sejenis bisa tidak, sama seperti tuple dan list. | • Fungsi len() digunakan untuk menghitung lebar set. | INFO

data = {1, "abc", False, ("banana", "spaghetti")}
print("data:", data)
print("len:", len(data))
data_kosong = set()
print("set kosong:", data_kosong)
