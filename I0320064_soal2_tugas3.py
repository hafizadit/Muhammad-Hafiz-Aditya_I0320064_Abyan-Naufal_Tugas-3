# Membuat dictionary yang berisikan nama, hobi (lebih dari dua), sosmed (lebih dari dua), makanan favorit (lebih dari dua)
mydict = {"Nama":"Muhammad Hafiz Aditya",
"Hobi":["Fotografi","Membaca buku","Videografi"],
"Sosmed":["Instagram : @hafiz_adit","Whatsapp : 081393856662","Line : tatank322"],
"Makanan Favorit":["Bakso","Sate","Ayam"]}
print("\nDictionary sebelum diubah :\n", mydict)

#Meengubah satu hobi dan sosial media
mydict["Hobi"][2] = ("Mendengarkan Musik")
mydict["Sosmed"][2] = ("LinkedIn : Muhammad Hafiz Aditya")

# Menghapus dua makanan favorit
del mydict["Makanan Favorit"][0:2]

#Menambahkan satu hobi
mydict["Hobi"].append("Tidur")

#Menampilkan dictionary
print("\nDictionary setelah diubah menjadi :\n", mydict,"\n")
