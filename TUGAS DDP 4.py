dataBUKU = {
    "judul" : "Islam ala Prabowo",
    "penulis" : "Rikal Dikri",
    "tahun_terbit" : 2025
}
while True :
    print("=================")
    print( "  MENU PILIHAN")
    print("=================")
    print("1. Tampilkan data buku")
    print("2. Tambahkan data Penerbit")
    print('3. Ubah data Penulis')
    print("4. Hapus data Penerbit")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan anda :")

    if pilihan == "1":
        print("Data buku saat ini :")
        print (dataBUKU)

    elif pilihan == "2":
        while True:
            penerbit = input("Masukkan nama penerbit:")
            dataBUKU ["penerbit"] = penerbit
            if penerbit != "":
                print("Data baru berhasil ditambahkan!")
                print("Data setelah diubah:")
                print (dataBUKU)
                break
            else :
                print("Nama penerbit tidak boleh kosong!")

    elif pilihan == "3":
        while True:
            penulisBARU = input("Ubah nama penulis:")
            dataBUKU["penulis"] = penulisBARU
            if penulisBARU != "":
                print("Data penulis berhasil diubah!")
                print("Data setelah diubah:")
                print(dataBUKU)
                break
            else:
                print("Nama penulis tidak boleh kosong!")

    elif pilihan == "4":
        if 'penerbit' in dataBUKU:
            del dataBUKU["penerbit"]
            print("Data penerbit berhasil dihapus!")
            print("Data setelah diubah:")
            print(dataBUKU)
        else: 
            print("Data penerbit tidak di temukan")

    elif pilihan =="5":
        print("Program Selesai.")
        break

    else:
        print("Pilihan harus berupa angka (1-5)")
