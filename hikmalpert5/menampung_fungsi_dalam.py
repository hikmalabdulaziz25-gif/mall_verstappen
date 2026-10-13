# Sumber PDF: A.25.2. Menampung fungsi dalam
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: variabel | Pada contoh sebelumnya, fungsi inner_func() ditampung ke variabel | bernama f via nilai balik pemanggilan fungsi outer_func() . Dari sini terlihat | bahwa closure bisa disimpan ke variabel. | Tidak hanya closure, fungsi biasa-pun juga bisa disimpan dalam variabel,

def kuadrat(x):
    return x * x
fungsi = kuadrat
print(fungsi(5))
