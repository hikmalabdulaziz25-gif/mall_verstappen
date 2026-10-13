# Sumber PDF: A.16.4. Nested dictionary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Dictionary bercabang atau nested dictionary bisa dimanfaatkan untuk | menyimpan data dengan struktur yang kompleks, misalnya dictionary yang | salah satu value item-nya adalah list. | Penerapannya tak berbeda seperti inisialisasi dictionary umumnya, langsung | tulis saja dictionary sebagai child dictionary. Contoh:

profile = {"name": "mario", "affiliations": [{"name": "luigi", "affiliation": "brother"}, {"name": "mushroom kingdom", "affiliation": "protector"}]}
print("name:", profile["name"])
for item in profile["affiliations"]:
    print(f'{item["name"]} ({item["affiliation"]})')
