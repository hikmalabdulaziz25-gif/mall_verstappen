# Sumber PDF: A.16.3. Perulangan item dictionary
# Praktik terpisah sesuai subbab dalam PDF.
# Cuplikan materi: Gunakan keyword for dan in untuk mengiterasi data tiap key milik | profile = dict( | identifier="set", | name="john wick", | hobbies=["playing with pencil"],

profile = {"id": 2, "name": "mario", "is_female": False}
for key in profile:
    print("key:", key, "\t value:", profile[key])
