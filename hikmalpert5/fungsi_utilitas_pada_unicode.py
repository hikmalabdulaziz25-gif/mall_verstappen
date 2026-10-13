# Sumber PDF: A.18.2. Fungsi utilitas pada Unicode
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: ◉ Fungsi ord() | Fungsi ord() digunakan untuk mengambil nilai code point dari suatu karakter. Nilai baliknya adalah numerik | berbasis desimal. | Untuk menampilkan code point dalam notasi heksadesimal, cukup bungkus menggunakan fungsi hex() . | message = "\N{HANGUL SYLLABLE AN}\N{HANGUL SYLLABLE NYEONG} \N{GRINNING FACE}"

text = "Python ✓"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))
print("karakter:", len(text))
