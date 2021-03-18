# List teman
teman = ['ilham', 'vizal', 'efa', 'bonang', 'aji', 'rio', 'hani', 'alam', 'rafli', 'ojat']
print (teman)

# Menampilan isi indeks nomor 4, 6, 7
print ('nama teman[4]: ', teman[4])
print ('nama teman[6]: ', teman[6])
print ('nama teman[7]: ', teman[7])

# Mengganti nama teman pada indeks 3, 5, 9
teman[3] = 'uddin'
teman[5] = 'bagus'
teman[9] = 'candrika'
print (teman)

# Menambahkan 2 nama teman
teman.append ('ardjo')
teman.append ('bintul')
print (teman)

# Menampilkan semua nama teman dengan perulangan
for i in teman:
    print (i)

# Menampilkan panjang list
print ("panjang list teman = ", len(teman))