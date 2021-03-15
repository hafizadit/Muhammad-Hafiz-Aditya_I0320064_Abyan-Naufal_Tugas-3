# Membuat list berisikan minimal 10 nama teman
lstTeman = ["Ilham","Aji","Danen","Zafira","Rimma","Fairuzaman","Catur","Ojat","Alam","Azrul"]

# Menampilkan isi list yang memiliki index 4,6,7
print("")
print("Nilai pada index 4 :",lstTeman[4])
print("Nilai pada index 6 :",lstTeman[6])
print("Nilai pada index 7 :",lstTeman[7])
print("")

# Mengganti nama teman pada index 3,5,9
lstTeman[3] = "Nana"
lstTeman[5] = "Maulana"
lstTeman[9] = "Reza"

print("")
print("Setelah diubah, lstTeman menjadi :",lstTeman)
print("")

# Menambahkan 2 nama teman
lstTeman.append("Hafid")
lstTeman.append("Hasan")
print("")
print("lstTeman setelah ditambahkan 2 nilai :",lstTeman)
print("")

# Menampilkan nama teman dengan perulangan
print("Nama teman saya adalah :")
for x in lstTeman:
    print(x)
print("")

# Menampilkan panjang list
print("Panjang list lstTeman adalah ",len(lstTeman),"\n")