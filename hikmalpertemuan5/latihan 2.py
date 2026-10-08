print("========================================")
print("        GEROBAK FRIEND CHICKEN          ")
print("========================================")
print("Kode        Jenis Potong        Harga   ")
print("----------------------------------------")
print("D            Dada               Rp. 2500")
print("P            Paha               Rp. 2000")
print("S            Sayap              Rp. 1500")
print("----------------------------------------")

banyak_jenis = int(input("Banyak Jenis : "))

total_bayar = 0

for i in range(banyak_jenis) :
    print("\nJjenis Ke-", i + 1)

    kode = input("Kode Potong [D/P/S] : "). upper()
    banyak_beli = int(input ("Banyak Potong : "))

    if kode =="D":
        jenis = "Dada"
        harga = 2500
    elif kode == "P":
        jenis = "Paha"
        harga = 2000
    elif kode == "S":
        jenis = "Sayap"
        harga = 1500
    else:
        print("Kode tidak valid! ")
        continue

    jumlah_harga = harga * banyak_beli
    total_bayar += jumlah_harga

    print("Jenis        :", jenis)
    print("Harga Satuan : Rp.", harga)
    print("Jumlah Harga :Rp.", jumlah_harga)

# Menghitung pajak 10%
pajak = total_bayar * 10 / 100
total = total_bayar + pajak

print("\n=================================")
print("     GEROBAK FRIEND CHICKEN        ")
print("===================================")
print("Jumlah Bayar : Rp.", total_bayar)
print("Pajak 10%    : Rp.", pajak      )
print("Total Bayar  : Rp.", total      )