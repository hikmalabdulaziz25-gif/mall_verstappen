# Sumber PDF: A.21.5. Reference pada data hasil slicing
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Bagaimana dengan slicing, apakah ada efeknya ke object ID dan reference | data? Yap, ada. Coba saja test program berikut: | numbers1 = [1, 2, 3, 4] | numbers2 = numbers1 | numbers3 = numbers1[:]

a = [1, 2, 3, 4]
b = a[:]
b[0] = 99
print("a:", a)
print("b:", b)
print(id(a) == id(b))
