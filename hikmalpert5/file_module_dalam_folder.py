# Sumber PDF: A.27.8. File module dalam folder
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Bagaimana jika suatu file module (misalnya calculate.py ) berada di dalam | suatu sub-folder dalam folder program, apakah cara import-nya sama? | Sebenarnya sama namun ada sedikit perbedaan yang harus diketahui. | Selengkapnya akan kita bahas pada chapter selanjutnya, yaitu Packages. | Catatan chapter 📑

# Buat file helper.py satu folder dengan file ini, berisi:
# def salam(nama):
#     return f"Halo, {nama}!"
# Lalu gunakan di file utama:
# import helper
# print(helper.salam("Ahmad"))
print("Contoh module buatan sendiri dijelaskan di komentar file ini.")
