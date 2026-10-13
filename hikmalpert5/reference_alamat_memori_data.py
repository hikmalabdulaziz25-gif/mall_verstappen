# Sumber PDF: A.21.2. Reference / alamat memori data
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Perlu diketahui bahwa Identifier merupakan metadata informasi yang | menempel pada data atau object, bukan menempel ke variabel. Data yang | sama jika di-assign ke banyak variabel, maka pengecekan ID pada semua | variabel tersebut mengembalikan ID yang sama. | Reference pada konteks programming artinya adalah referensi suatu

a = [1, 2, 3]
b = a
print(id(a), id(b))
b.append(4)
print("a:", a)
print("b:", b)
