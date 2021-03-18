# Data diri awal
data_diri = {'nama':'Dwi Zaki Nurfaizi', 'hobi':{1:'bernyanyi', 2:'mendengarkan musik', 3:'main game', 4:'nongkrong'},
             'sosmed':{1:'ig @dwizaki86_', 2:'line : dwi.zaki', 3:'fb : Dwi Zaki Nurfaizi'},
             'lagu fav':{1:'Mungkin Hari Ini Esok Atau Nanti', 2:'Pengungkapan Hatimu', 3:'Untuk Perempuan Yang Sedang Di Pelukan'},
             'makanan fav':{1:'nasi goreng', 2:'sate', 3:'indomie kuah soto + cabe potong'}}
print ("\nData diri awal :\n", data_diri)

# Mengubah salah satu hobi
data_diri['hobi'] = {1:'berlari', 2:'mendengarkan musik', 3:'main game', 4:'nongkrong'}

# Mengubah salah satu sosmed
data_diri['sosmed'] = {1:'ig @dwizaki86_', 2:'line : dwi.zaki', 3:'wa 081804129213'}

# Menghapus 2 makanan favorit
data_diri['makanan fav'] = 'indomie kuah soto + cabe potong'

# Menambahkan 1 hobi
data_diri['hobi'] = {1:'berlari', 2:'mendengarkan musik', 3:'main game', 4:'nongkrong', 5:'main basket'}

# Data diri akhir
print('\nData diri setelah diproses :\n', data_diri)