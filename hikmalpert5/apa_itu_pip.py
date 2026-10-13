# Sumber PDF: A.28.1. Apa itu pip?
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: pip adalah package manager resmi untuk Python, digunakan untuk | menginstall, mengupdate, dan menghapus package dari Python Package Index | (PyPI). PyPI adalah repository tempat ribuan package Python open-source | tersedia. | Untuk mengecek apakah pip sudah terinstall, jalankan perintah berikut di

import sys
import subprocess
hasil = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
print(hasil.stdout.strip() if hasil.returncode == 0 else hasil.stderr.strip())
