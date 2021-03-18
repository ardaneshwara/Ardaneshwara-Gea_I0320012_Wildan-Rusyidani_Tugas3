# Menampilkan list 10 teman
list = ['Deadila','Bagus','Aratia','Divana','Alifiana','Funny','Ayu','Hana','Candrika','Angela']

# Menampilkan isi list indeks nomor 4, 6, dan 7
print("List indeks nomor 4,6, dan 7 yaitu", list[4],",", list[6], ",","dan", list[7])

# Mengganti nama teman di list 3, 5, 9
list[3] = 'Sekar'
list[5] = 'Cita'
list[6] = 'Attar'

# Menambahkan 2 nama teman
list.append('Maurich')
list.append('Zafira')

# Menampilkan semua teman dengan pengulangan
print(list*2)

# Menampilkan panjang list
print(len(list))
