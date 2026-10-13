# Sumber PDF: A.18.1. Pengenalan Unicode String
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Dalam dunia per-Unicode-an, ada yang disebut dengan code point yaitu suatu angka numerik (bisa desimal maupun | hexadecimal) yang merepresentasikan karakter tertentu. Jadi bisa diibaratkan identifier dari suatu karakter. Semua | karakter ada code point-nya, termasuk huruf A, B, C, maupun karakter lainnya (angka, tulisan romawi, symbol, dll). | Cara penulisan karakter unicode sendiri bisa dengan langsung menuliskan karakternya, atau bisa juga deng

print("Bahasa Indonesia")
print("مرحبا")
print("こんにちは")
print("😀 🚀")
for char in "A✓":
    print(char, ord(char), hex(ord(char)))
