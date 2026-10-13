# Sumber PDF: A.24.2. Pengenalan Kwargs
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Kwargs (atau yang umumnya ditulis sebagai **kwargs atau keyword | arguments) merupakan notasi penulisan parameter spesial dengan | kapabilitas bisa menampung banyak keyword argument pemanggilan fungsi | dalam 1 parameter saja. | def sum_then_print(message, *numbers, suffix_message):

def tampilkan(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
tampilkan(nama="Ahmad", prodi="Sistem Informasi")
