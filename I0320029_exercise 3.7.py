# Contoh cara menghapus pada dictionary Python

dict = {'Nama':'Zaki', 'Umur':19, 'Member':'Platinum'}

#hapus entri dengan key 'Umur'
del dict['Umur']  
print (dict)
print ("dict['Nama']: ", dict['Nama'])

#hapus semua entri di dict
dict.clear()  
print (dict)

#hapus dictionary yang sudsah ada
del dict  
print (dict)