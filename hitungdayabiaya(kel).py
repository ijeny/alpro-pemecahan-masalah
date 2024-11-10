def inputan(komen):
    masukan = int(input(komen + ':'))
    return masukan

def masukan(jenis):
    daya = int(input(f"daya pemakaian {jenis} (dalam watt): "))
    waktu = int(input(f"waktu pemakaian {jenis} (jam/hari): "))
    return daya,waktu

def proses(daya, waktu):    
    pemakaianDaya = daya * waktu #hitung daya per alat
    kWhAlatPerHari = pemakaianDaya /1000 #mengubah daya (watt) ke kWh
    beaPakaiHarian = kWhAlatPerHari * 1500 #cari biaya harian per alat 
    beaPakaiBulanan = beaPakaiHarian * 30 #cari biaya bulanan per alat
    return beaPakaiHarian, pemakaianDaya, beaPakaiBulanan 

#program utama 
daya1, waktu1 = masukan ("lampu")
pemakaianDaya1, beaPakaiHarian1, beaPakaiBulanan1 = proses(daya1, waktu1)
daya2, waktu2 = masukan ("kipas")
pemakaianDaya2, beaPakaiHarian2, beaPakaiBulanan2 = proses(daya2, waktu2)
daya3, waktu3 = masukan ("TV")
pemakaianDaya3, beaPakaiHarian3, beaPakaiBulanan3 = proses(daya3, waktu3)

#hitung total biaya untuk semua barang
totalWaktuAlat = waktu1 + waktu2 + waktu3
totalWattAlat = pemakaianDaya1 + pemakaianDaya2 + pemakaianDaya3
totalBeaHarianAlat = (beaPakaiHarian1 + beaPakaiHarian2 + beaPakaiHarian3) 
totalBeaBulananAlat = totalBeaHarianAlat * 30

print("-"*45)
print(f"pemakaian daya lampu : {pemakaianDaya1} watt selama {waktu1} jam")
print(f"pemakaian daya kipas : {pemakaianDaya2} watt selama {waktu2} jam")
print(f"pemakaian daya TV : {pemakaianDaya3} watt selama {waktu3} jam")

print("-"*45)
print(f"pemakaian daya lampu 1 hari     : Rp.{beaPakaiHarian1:,.2f}")
print(f"pemakaian daya kipas 1 hari     : Rp.{beaPakaiHarian2:,.2f}")
print(f"pemakaian daya TV 1 hari        : Rp.{beaPakaiHarian3:,.2f}")

print("-"*45)
print(f"pemakaian daya lampu 1 bulan    : Rp.{beaPakaiBulanan1:,.2f}")
print(f"pemakaian daya kipas 1 bulan    : Rp.{beaPakaiBulanan2:,.2f}")
print(f"pemakaian daya TV 1 bulan       : Rp.{beaPakaiBulanan3:,.2f}")

print("-"*45)
print(f"harga total keseluruhan         : {totalWattAlat} watt selama {totalWaktuAlat} jam")
print(f"harga total keseluruhan 1 hari  : Rp.{totalBeaHarianAlat:,.2f}")
print(f"harga total keseluruhan 1 bulan : Rp.{totalBeaBulananAlat:,.2f}")
print("-"*45)