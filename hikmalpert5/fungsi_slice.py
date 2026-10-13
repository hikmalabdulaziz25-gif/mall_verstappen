# Sumber PDF: A.20.2. Fungsi slice()
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Notasi penulisan slice bisa disimpan pada suatu variabel dengan | memanfaatkan fungsi slice() . Nilai start , end , dan step dijadikan | argument pemanggilan fungsi tersebut dengan notasi slice(start, end) | atau slice(start, end, step) . | Pada contoh berikut, perhatikan bagaimana perbedaan slicing pada list1 ,

data = ["a", "b", "c", "d", "e"]
potongan = slice(1, 4)
print(data[potongan])
