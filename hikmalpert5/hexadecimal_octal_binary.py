# Sumber PDF: A.19.2. Hexadecimal, Octal, Binary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Selain basis 10, bilangan bulat bisa dituliskan menggunakan basis lain, misalnya heksadesimal/oktal/biner, | caranya dengan memanfaatkan prefix atau suatu awalan saat penulisan literalnya. | • Prefix literal untuk heksadesimal: 0x | • Prefix literal untuk oktal: 0o | • Prefix literal untuk biner: 0b

print("hex:", hex(255))
print("oct:", oct(10))
print("bin:", bin(10))
print(int("ff", 16), int("12", 8), int("1010", 2))
