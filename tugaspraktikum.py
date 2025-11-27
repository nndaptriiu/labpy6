data_mahasiswa = {}

def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Masukkan nama: ")
    nilai = float(input("Masukkan nilai: "))
    data_mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan!\n")


def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not data_mahasiswa:
        print("Data masih kosong.\n")
        return
    for nama, nilai in data_mahasiswa.items():
        print(f"Nama: {nama} | Nilai: {nilai}")
    print()


def hapus(nama):
    print("\n=== Hapus Data Mahasiswa ===")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan.\n")


def ubah(nama):
    print("\n=== Ubah Data Mahasiswa ===")
    if nama in data_mahasiswa:
        nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
        data_mahasiswa[nama] = nilai_baru
        print("Data berhasil diubah!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan.\n")


# Program utama
while True:
    print("=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Ubah data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang ingin diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")
