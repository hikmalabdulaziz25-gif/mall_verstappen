# Sumber PDF: A.17.3. String formatting
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: String formatting adalah teknik untuk mem-format string agar menghasilkan | text sesuai dengan format yang diinginkan. | Cara termudah melakukan string formatting adalah dengan menggunakan f- | strings (atau formatted string literals). Tulis string seperti biasa tapi diawali | dengan huruf f atau F sebelum penulisan " " .

name = "Hikmal Abdul Aziz"
occupation = "IT support"
print(f"hello, my name is {name}, I'm an {occupation}")
print("hello, my name is {}, I'm an {}".format(name, occupation))
