# Sumber PDF: A.21.4. Reference data sequence
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Data sequence (entah itu list, string, ataupun lainnya) kalau dilihat dari segi | manajemen memory-nya adalah berbeda dibandingkan dengan bagaimana | data dalam array di-manage di bahasa lain. | List di Python tersimpan pada satu alamat memory. Tidak seperti slice/array | pada bahasa Go (misalnya), yang setiap element-nya merupakan reference.

a = [1, 2, 3]
b = a
b[0] = 99
print("a:", a)
print("b:", b)
