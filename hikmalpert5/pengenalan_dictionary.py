# Sumber PDF: A.16.1. Pengenalan Dictionary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Dictionary atau dict adalah tipe data kolektif berbentuk key-value. Contoh | penulisannya: | Literal dictionary ditulis dengan menggunakan { } , mirip seperti tipe data | set, hanya saja bedanya pada tipe dictionary isinya berbentuk key-value. | Pembahasan detail mengenai tipe data set ada di chapter Set

profile = {"id": 2, "name": "john wick", "hobbies": ["playing with pencil"], "is_female": False}
print("data:", profile)
print("total keys:", len(profile))
print("name:", profile["name"])
