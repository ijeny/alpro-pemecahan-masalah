import math

bil1 = int(input("jumlah penggunaan daya lampu (dalam watt): "))
bil2 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil1 * bil2
kwh = hasil / 1000

harga_total1 = kwh * harga 
print(f"harga total per hari : Rp {harga_total1:}")
bulan = harga_total1 * 30 
print(f"harga total per bulan: Rp {bulan:}")
print("===========================")
bil3 = int(input("jumlah penggunaan daya kipas (dalam watt): "))
bil4 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil3 * bil4
kwh = hasil / 1000

harga_total2 = kwh * harga 
print(f"harga total per hari : Rp {harga_total2:}")
bulan = harga_total2 * 30 
print(f"harga total per bulan: Rp {bulan:}")
print("===========================")
bil5 = int(input("jumlah penggunaan daya TV (dalam watt): "))
bil6 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil5 * bil6
kwh = hasil / 1000

harga_total3 = kwh * harga 
print(f"harga total per hari : Rp {harga_total3:}")
bulan = harga_total3 * 30 
print(f"harga total per bulan: Rp {bulan:}")
print("===========================")
jumlah_keseluruhan = harga_total1 + harga_total2 + harga_total3 
print(f"harga total keseluruhan = Rp{jumlah_keseluruhan:}")