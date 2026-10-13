# Sumber PDF: A.15.7. frozenset
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: frozenset adalah set yang immutable atau tidak bisa diubah nilai elemennya setelah dideklarasikan. | Cara penggunaannya seperti set, perbedaannya pada deklarasi frozenset, fungsi frozenset() digunakan dan | bukan set() . | Semua operasi set, method milik set bisa digunakan pada frozenset, kecuali beberapa operasi yang sifatnya | mutable atau mengubah elemen. Contohnya seperti method add() , pop() , remove() dan lainnya tidak bisa

a = frozenset("abracadabra")
b = frozenset("alacazam")
print(a)
print(b)
print("intersection:", a & b)
