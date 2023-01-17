#Judul
print('<<<Nilai>>>')

#Keterangan
print('A=Sangat Baik')
print('B=Baik')
print('C=Cukup')
print('D=Kurang')
print('E=Gagal')
print('________________________________________')

#Proses/Deskripsi

N= int(input('Masukan nilai :'))

if   N >= 80 and N  <100:
    print(' kriteria : A')
elif N >= 70 and N  <80:
    print(' kriteria : B')
elif N >= 60 and N  <70:
    print(' Kriteria : C')
elif N >= 50 and N  <60:
    print(' Kriteria : D')
elif N <= 60:
    print(' Kriteria : E')
else:
    print('Nilainya Kelebihan anjay')
if N >= 105:
    print('Mohon Masukkan Nilai dengan benar ya Sayang...')

#Tanggapan
if   N >= 90 and N <105:
    print('Nilai Yang sangat Hebat kawan :)  ')
elif N >= 80 and N < 90:
    print('Nilai Yang Baik Kawan             ')
elif N >= 70 and N < 80:
    print('Nilai yang cukup Baik kawan       ')
elif N >= 60 and N < 70:
    print('Nilai yang Kurang baik kawan      ')
elif N <= 60:
    print('Nilai mu gagal kawan... :(        ')

exit('NICE TRY!!!')
