# Player dengan id Unchyy ingin membeli battle pass di game Genshin Impact. 
# Bila harga battle pass nya adalah Rp179.900,- dan harga setiap tahunnya naik sebesar 5%. 
# Jika ia ingin membeli 10 battle pass di tahun ini dan 7 battle pass dalam 3 tahun yang akan datang. 
# Berapa uang yang ia butuhkan untuk membeli battle pass tahun ini, 3 tahun yang akan datang, dan berapa total pengeluarannya
# Jawaban
#input 
    # Harga battle pass 
    # kenaikan per tahun 
    # jumlah battle pass yang akan dibeli tahun ini
    # jumlah battle pass yang akan dibeli di tahun yang akan datang 
    # berapa tahun lagi akan membeli battle pass
#proses
    # Perkalian harga battle pass dengan jumlah battle pass yang akan dibeli
    # mencari kenaikan harga battle pass tiap tahunnya
    # harga battle pass di tahun yang akan datang
    # total uang yang dikeluarkan
#output
    #uang yang dibutuhkan untuk membeli battle pass tahun ini
    #uang yang dibutuhkan untuk beli battle pass di tahun yang akan datang 
    #total uang yang dikeluarkan

#71200619_Untung Mangkunegara

#input
harga_bp=int(input("Harga Battle Pass: "))
kenaikan_harga=int(input("Kenaikan harga Battle Pass per Tahun (dalam persen): "))
jumlah_bp=int(input("Jumlah Battle Pass yang akan dibeli tahun ini: "))
jumlah_bp_depan=int(input("Jumlah Battle Pass yang akan dibeli tahun yang akan datang: "))
brp_tahun=int(input("Berapa tahun lagi akan membeli Battle Pass?: "))

#proses
#a=uang bp tahun ini            c=harga bp tahun depan
#b=kenaikan harga uang bp       d=total uang

a=harga_bp*jumlah_bp
b=harga_bp*(kenaikan_harga/100)
c=(harga_bp+(b*brp_tahun))*jumlah_bp_depan
d=a+c

#output
print("\n")
print("Uang yang dibutuhkan untuk membeli battle pass tahun ini: ",a)
print("Uang yang dibutuhkan untuk membeli battle pass di tahun yang akan datang: ",c)
print("Total uang yang dikeluarkan: ",d)
