# Sumber PDF: A.25.1. Pengenalan Closure
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Di Python, fungsi bisa dideklarasikan di-dalam suatu fungsi. Penerapannya | cukup berguna pada kasus dimana ada blok kode yang perlu di-eksekusi lebih | dari satu kali tetapi eksekusinya hanya di dalam fungsi tertentu, atau | eksekusinya setelah pemanggilan fungsi tertentu. | Permisalan ada fungsi inner() yang dideklarasikan di dalam fungsi

def buat_sapaan(sapaan):
    def sapa(nama):
        return f"{sapaan}, {nama}"
    return sapa
halo = buat_sapaan("Halo")
print(halo("Ahmad"))
