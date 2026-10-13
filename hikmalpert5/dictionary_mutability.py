# Sumber PDF: A.16.5. Dictionary mutability
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Item dictionary adalah mutable, perubahan value item bisa dilakukan langsung | menggunakan operator assignment = . | value = profile["affiliations"][0]["name"], | profile["affiliations"][0]["affiliation"] | print("  ➜ %s (%s)" % (value))

profile = {"id": 2, "name": "mario"}
print(profile)
profile["name"] = "Ahmad"
print(profile)
