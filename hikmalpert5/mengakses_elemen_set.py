# Sumber PDF: A.15.3. Mengakses elemen set
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Nilai set by default hanya bisa diakses menggunakan perulangan: | data_1 = {1, 'abc', False, ('banana', 'spaghetti')} | print("data:", data_1) | # output ➜ data: {1, 'abc', False, ('banana', 'spaghetti')} | print("len:", len(data_1))

fellowship = {"aragorn", "gimli", "legolas"}
for anggota in fellowship:
    print(anggota)
print("gimli ada?", "gimli" in fellowship)
