# Sumber PDF: A.17.4. Penggabungan string & split
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: string | ◉ Penggabungan string (concatenation) | Ada beberapa metode yang bisa digunakan untuk string concatenation atau | operasi penggabungan string. | text = "hello, my name is {name}, I'm an {occupation}".format(name =

text = "hello" + " " + "python"
print(text)
parts = "hello python 12345".split()
print(parts)
print(" ".join(parts))
