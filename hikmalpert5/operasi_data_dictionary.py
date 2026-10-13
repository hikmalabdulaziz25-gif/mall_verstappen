# Sumber PDF: A.16.6. Operasi data dictionary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: ◉ Pengaksesan item | Pengaksesan item dilakukan lewat notasi dict["key"] , atau bisa dengan | menggunakan method get() . | ◉ Mengubah isi dictionary | Cara mengubah value item dictionary adalah dengan mengaksesnya terlebih

profile = {"id": 2, "name": "mario"}
print(profile.get("name"))
profile["color"] = "red"
profile.update({"race": "italian"})
print("keys:", list(profile.keys()))
print("values:", list(profile.values()))
print("items:", list(profile.items()))
profile.pop("id", None)
print(profile)
