# Sumber PDF: A.26.4. Lambda dengan parameter *args
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: & **kwargs | Penerapan *args dan **kwargs pada parameter lambda tidak berbeda | dengan penerapannya di fungsi biasa. Sebagai perbandingan Silakan pelajari 2 | contoh berikut yang masing-masing berisi contoh penulisan lambda vs versi | fungsi biasa.

jumlah = lambda *args: sum(args)
print(jumlah(1, 2, 3, 4))
