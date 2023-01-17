#input nilai PTS dan PAs
Tugas = float(input('Masukan nilai tugas:'))
PTS = float(input('Masukan nilai UTS:'))
PAS = float(input('Masukan nilai PAS'))

#menghitung nilai akhir sesuai dengan bobot
nilai = (0,15 * Tugas) + (0,35 * PTS) + (0,50 * PAS)

#grade berdasarkan nilai akhir
if nilai  > 80 :
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'c'
elif nilai > 50:
    grade = 'D'
else:
    grade ='E'

#menentukan status kelulusan berdasarkan bilai
if nilai > 60:
    status='lulus'
else:
    status = "tidak lulus"

#menampilkan nilai akhir,grade,status
print('nilai akhir: &0,2f' % nilai)
print('grade: {}'.format(grade))
print('status: {}'.format(status))
