#Input
gaji_jam = eval(input('Masukkan jumlah gaji si Budi: '))
jam_kerja = eval(input('Masukkan jam kerja si Budi dalam sehari: '))
#Output
pendapatan = gaji_jam * jam_kerja
print('Pendapatan Budi: ', pendapatan)
uang_pajak = 14/100 * pendapatan
sisa1 = pendapatan - uang_pajak
print('Sisa Uang: ', sisa1)

uang_pakaian=10/100*sisa1
print('Uang untuk Pakaian dan Asesoris: ', uang_pakaian)
sisa2 = sisa1 - uang_pakaian

uang_alatulis=1/100*sisa2
print('Uang untuk alat tulis: ', uang_alatulis)
sisa3 = sisa2 - uang_alatulis

uang_sedekah=25/100*sisa3
print('Uang untuk sedekah: ', uang_sedekah)
sisa4 = sisa3- uang_sedekah

uang_yatim= 30/100 * uang_sedekah
print('Uang untuk yatim: ', uang_yatim)

uang_dhuafa= 70/100 * uang_sedekah
print('Uang untuk kaum Dhuafa: ', uang_dhuafa)