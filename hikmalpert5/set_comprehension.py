# Sumber PDF: A.15.6. Set comprehension
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Metode comprehension juga bisa diterapkan pada set. Contohnya bisa dilihat pada kode berikut, statement set | comprehension dibuat untuk melakukan pengecekan apakah ada element pada set set('abracadabra') yang | bukan anggota element set('abc') . | data = set('abcda') | print('data', data)

res = {x for x in set("abracadabra") if x not in set("abc")}
print(res)
