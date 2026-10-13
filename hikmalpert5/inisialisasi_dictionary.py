# Sumber PDF: A.16.2. Inisialisasi dictionary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Pembuatan data dictionary bisa dilakukan menggunakan beberapa cara: | • Menggunakan { } : | import json | print(json.dumps(profile, indent=4)) | profile = {

a = {"name": "john wick"}
b = dict(name="john wick", is_female=False)
c = dict([("name", "john wick"), ("is_female", False)])
print(a, b, c)
print("kosong:", {})
