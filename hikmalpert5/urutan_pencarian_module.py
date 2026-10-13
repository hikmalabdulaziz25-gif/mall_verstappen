# Sumber PDF: A.27.7. Urutan pencarian module
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Ketika suatu module di-import, Python akan melakukan pencarian file module | di beberapa tempat berikut secara berurutan: | 1. Pertama, Python akan mencari module di folder yang sama dimana | statement import digunakan. | 2. Jika pencarian pertama tidak menemukan hasil, maka Python lanjut

import sys
print("Jalur pencarian module Python:")
for path in sys.path:
    print(path)
