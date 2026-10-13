# Sumber PDF: A.24.1. Pengenalan Args
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Args (atau yang umumnya ditulis sebagai *args) merupakan notasi penulisan | parameter spesial dengan kapabilitas bisa menampung banyak positional | argument untuk ditampung dalam 1 parameter saja. | Agar lebih jelas tentang kegunaan args, mari pelajari terlebih dahulu kode | berikut:

def jumlahkan(*args):
    print("args:", args)
    return sum(args)
print(jumlahkan(1, 2, 3, 4))
