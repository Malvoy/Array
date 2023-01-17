#menginput angka
angka= int(input('masukkan angka:'))

#jika habis dibagi 0 maka genap
if(angka % 2) == 0:
    print('{0} adalah bilangan genap'.format(angka))

#jika tidak habis dibagi 0 maka ganjil
else:
    print('{0} adalah bilangan ganjil'.format(angka))