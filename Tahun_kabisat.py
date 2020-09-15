# Tahun kabisat merupakan tahun yang mengalami penambahan satu hari dengan tujuan untuk menyesuaikan penanggalan dengan tahun astronomi. 
# Dalam satu tahun tidak secara persis terdiri dari 365 hari, tetapi 365 hari 5 jam 48 menit 45,1814 detik. 
# Jika hal ini tidak dihiraukan, maka setiap empat tahun akan kekurangan hampir 1 hari. 
# Maka untuk mengkompensasi hal ini, setiap 4 tahun sekali, diberi 1 hari ekstra: 29 Februari.

# Buatlah sebuah file python interaktif (.py) yang dapat menentukan suatu input dari user tergolong tahun kabisat atau tidak. 
# Saat file dieksekusi, user diminta memasukkan angka tahun tertentu, 
# kemudian akan muncul hasil yang menyatakan input user tersebut tergolong tahun kabisat atau tidak. 
# Contoh hasil yang diharapkan: (Gunakan Penanggalan Gregorian)

# Input tahun : 2019
# Hasil : BUKAN TAHUN KABISAT

# Input tahun : 2020
# Hasil : TAHUN KABISAT

tahun = int(input('Masukkan Tahun: ')) # Untuk memasukkan tahun

if tahun % 4 == 0: #jika tahun dibagi 4 = 0 maka tahun kabisat
    print('Tahun Kabisat') # print tahun kabisat

else: #jika dibagi 4 != 0 atau lainnya maka bukan tahun kabisat
    print('Bukan Tahun Kabisat')


# import calendar
# year = int(input('Masukkan tahun: '))

# print(calendar.isleap(year))