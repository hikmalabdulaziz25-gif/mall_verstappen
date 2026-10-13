# Sumber PDF: A.20.3. Negative index slicing
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Selain menggunakan index positif (dimulai dari 0 ), Python juga mendukung | index negatif untuk mengakses element dari akhir sequence. Index -1 | mengacu pada element terakhir, -2 pada element kedua dari akhir, dan | seterusnya. | Notasi slice juga bisa menggunakan index negatif:

text = "hello python"
print(text[-1])
print(text[-6:])
print(text[:-7])
print(text[::-1])
