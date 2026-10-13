# Sumber PDF: A.15.4. Operasi pada set
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: ◉ Menambah element | Method add() milik tipe data set digunakan untuk menambahkan element baru. O iya, perlu diingat bahwa tipe | data ini didesain untuk mengabaikan urutan elemen, jadi urutan tersimpannya elemen bisa saja acak. | ◉ Menghapus element secara acak | Gunakan method pop() untuk menghapus satu elemen secara acak atau random.

a = {"apel", "jeruk", "mangga"}
b = {"jeruk", "anggur"}
print("union:", a.union(b))
print("intersection:", a.intersection(b))
print("difference:", a.difference(b))
a.add("pisang")
a.discard("apel")
print("set a:", a)
