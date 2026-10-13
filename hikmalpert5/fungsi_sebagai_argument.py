# Sumber PDF: A.25.3. Fungsi sebagai argument
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: parameter | Selain disimpan dalam variabel, fungsi/closure bisa juga dijadikan sebagai nilai | argument suatu parameter fungsi. Metode seperti ini cukup sering digunakan | terutama pada operasi data sequence atau agregasi data numerik. | Contoh penerapan fungsi/closure sebagai argument pemanggilan fungsi bisa

def terapkan(fungsi, nilai):
    return fungsi(nilai)
def kuadrat(x):
    return x * x
print(terapkan(kuadrat, 4))
