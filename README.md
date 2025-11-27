## Nama : Ananda Eka Delima Putri
## Kelas : TI.25.A.2
## NIM : 312510210
## Pertemuan : 11

## Kode Latihan 1

<img width="1597" height="663" alt="Screenshot 2025-11-27 080656" src="https://github.com/user-attachments/assets/44d379b5-e947-4daa-b22c-a39efdb58f49" />


## Output Latihan 1

<img width="1519" height="366" alt="Screenshot 2025-11-27 081041" src="https://github.com/user-attachments/assets/5b1e47f6-2e8c-476f-8818-cfa7127154f4" />


## Kode Tugas Praktikum

<img width="1789" height="944" alt="Screenshot 2025-11-27 081207" src="https://github.com/user-attachments/assets/464d3c87-403b-4171-8c78-b7866cf31569" />

## Output Tugas Praktikum

<img width="1240" height="990" alt="Screenshot 2025-11-27 080506" src="https://github.com/user-attachments/assets/a4229f4e-e07f-4364-8259-5a2222d5d9d0" />

## Flowchart

```
                 ┌────────────────────┐
                 │      MULAI         │
                 └─────────┬──────────┘
                           │
                 ┌─────────▼──────────┐
                 │   Tampilkan Menu   │
                 └─────────┬──────────┘
                           │
                ┌──────────▼───────────┐
                │ Pilih Menu (1 - 5)?  │
                └───────┬───┬───┬───┬──┘
                        │   │   │   │
         ┌──────────────▼┐ ▼ ┌─▼─┐ ▼ ┌───────────────┐
         │   Menu 1?     │ │ │Menu│ │   Menu 5?      │
         │ (Tambah Data) │ │ │ 3? │ │  (Keluar)      │
         └───────┬───────┘ │ │(Hapus)│ └───────┬─────┘
                 │         │ └───┬───┘         │
                 │         │     │             │
        ┌────────▼───┐ ┌──▼──────▼───┐ ┌──────▼──────┐
        │ Input Nama │ │ Input Nama   │ │ Tampilkan   │
        │ Input Nilai│ │ Hapus Data   │ │ "Selesai"   │
        │ Simpan     │ │ Tampilkan Msg│ │   Selesai   │
        └───────┬────┘ └─────────────┘ └─────────────┘
                │
                │
        ┌───────▼─────┐
        │ Kembali ke  │
        │     MENU    │
        └───────┬─────┘
                │
     ┌──────────▼───────────┐
     │ Menu 2? (Tampilkan?) │
     └──────────┬───────────┘
                │
       ┌────────▼─────────┐
       │ Tampilkan Data    │
       │ (Cek Kosong atau  │
       │ tampilkan isi)    │
       └────────┬─────────┘
                │
                │
     ┌──────────▼───────────┐
     │ Menu 4? (Ubah Data?) │
     └──────────┬───────────┘
                │
       ┌────────▼──────────┐
       │ Input Nama         │
       │ Jika Ada → Input   │
       │ Nilai Baru & Ubah  │
       │ Jika Tidak → Msg   │
       └────────┬──────────┘
                │
                │
                ▼
           (Kembali ke MENU)
```
Fungsi-Fungsi dalam Program
1. tambah()

Digunakan untuk menambahkan data mahasiswa baru.
Program akan meminta:

Nama mahasiswa

Nilai mahasiswa

Kemudian data akan disimpan pada dictionary data_mahasiswa.

2. tampilkan()

Menampilkan seluruh data mahasiswa yang tersimpan.
Jika data masih kosong, program menampilkan pesan “Data masih kosong.”

Data ditampilkan dalam format:
```
Nama: <nama> | Nilai: <nilai>
```

3. hapus(nama)

Menghapus data mahasiswa berdasarkan nama.

*Jika nama ditemukan → data akan dihapus

*Jika tidak ditemukan → muncul pesan “Data 'nama' tidak ditemukan.”

4. ubah(nama)

Mengubah nilai mahasiswa berdasarkan nama.

*Jika nama ada → pengguna memasukkan nilai baru

*Jika nama tidak ada → muncul pesan “Data ‘nama’ tidak ditemukan.”


