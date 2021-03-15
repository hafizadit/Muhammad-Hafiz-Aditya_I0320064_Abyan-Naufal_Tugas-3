# Membuat dictionary yang berisikan nama, hobi (lebih dari dua), sosmed (lebih dari dua), makanan favorit (lebih dari dua)
mydict = {"Nama":"Muhammad Hafiz Aditya",
"Hobi":("Fotografi","Membaca buku","Videografi"),
"Sosmed":("Instagram : @hafiz_adit","Whatsapp : 081393856662","Line : tatank322"),
"Makanan Favorit":("Bakso","Sate","Ayam")}

#Meengubah satu hobi dan sosial media
mydict["Hobi"] = ("Fotografi", "Membaca buku", "Mendengarkan Musik")
mydict["Sosmed"] = ("Instagram : @hafiz_adit","Whatsapp : 081393856662","LikedIn : Muhammad Hafiz Aditya")

# Menghapus dua makanan favorit
mydict["Makanan Favorit"] = ("Sate")

#Menambahkan satu hobi
mydict["Hobi"] = ("Fotografi", "Membaca buku", "Mendengarkan Musik","Tidur")

#Menampilkan dictionary
print("\nDictionary setelah diubah menjadi :\n", mydict,"\n")
