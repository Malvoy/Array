#Mendeklarasikan Array
array=[]

#Membuat Variabel Total
total=0

#Variabel n menampung jumlah array
#n=jumlah elemen
n= int(input('Masukan jumlah elemen array :'))
for x in range(n):
    nilai=float(input('Masukan nilai ke- {} : '.format(x+1)))
    array.append(nilai)
    #menampilkan jumlah dari nilai
    print('\nhasil nilai total adalah : {}'.format(sum(array)))
    #menampilkan Rata rata
    print('hasil rata r ata adalah : {}'.format(sum(array)/n))