# Menampilkan list 10 teman
list = ['Deadila','Bagus','Aratia','Sekar','Alifiana','Funny','Ayu','Hana','Candrika','Angela']

# Menampilkan isi list indeks nomor 4, 6, dan 7
print("List indeks nomor 4,6, dan 7 yaitu", list[4],",", list[6], ",","dan", list[7])

# Mengganti nama teman di list 3, 5, 9
list[3] = 'Divana'
list[5] = 'Cita'
list[6] = 'Tsania'

# Menambahkan 2 nama teman
list.append('Maurich')
list.append('Zafira')

# Menampilkan semua teman dengan pengulangan
thaitea = 0
for matcha in range (0,12) :
    print (list[thaitea])
    thaitea+=1

# Menampilkan panjang list
print("Panjang indeks list adalah", len(list))
