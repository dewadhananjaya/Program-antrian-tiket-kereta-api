# Program-antrian-tiket-kereta-api

Proyek ini adalah program berbasis terminal untuk mengelola antrian tiket kereta api. Program ini memungkinkan pengguna untuk melakukan berbagai operasi terkait antrian tiket, seperti menambah tiket ke dalam antrian, melihat daftar tiket dalam antrian, menghapus tiket dari antrian, dan melihat informasi mengenai antrian saat ini. Program ini menggunakan class `TicketQueue` untuk mengelola antrian dan deque dari modul `collections` untuk menyimpan tiket. Berikut adalah penjelasan detail tentang masing-masing komponen dan fungsinya:

### Class `TicketQueue`

#### Atribut
- `max_size`: Menyimpan kapasitas maksimum dari antrian.
- `queue`: Menggunakan `deque` untuk menyimpan data tiket dalam antrian.

#### Metode
- `is_empty()`: Mengecek apakah antrian kosong.
- `is_full()`: Mengecek apakah antrian penuh.
- `enqueue(ticket)`: Menambahkan tiket ke dalam antrian jika antrian belum penuh, jika penuh akan menampilkan pesan bahwa antrian penuh.
- `dequeue()`: Menghapus tiket paling depan dari antrian jika antrian tidak kosong, jika kosong akan menampilkan pesan bahwa antrian kosong.
- `view_queue()`: Menampilkan semua tiket yang ada dalam antrian.
- `queue_info()`: Menampilkan informasi tentang antrian, seperti kapasitas maksimum, jumlah tiket dalam antrian, tiket paling depan, dan tiket paling belakang.

### Fungsi `main()`

Fungsi ini mengatur alur program dengan menampilkan menu layanan kepada pengguna dan menerima input untuk melakukan operasi yang diinginkan. Menu yang tersedia antara lain:
- Menambah data antrian
- Melihat list data antrian
- Menghapus data antrian terdahulu
- Melihat informasi data antrian
- Keluar dari program

### Alur Program

1. **Inisialisasi**: Program dimulai dengan inisialisasi objek `TicketQueue` dengan kapasitas maksimum antrian sebesar 5 tiket.
2. **Menampilkan Menu**: Program menampilkan menu utama dan menunggu input dari pengguna.
3. **Menangani Input Pengguna**:
    - Jika pengguna memilih untuk menambah tiket, program akan meminta nomor tiket dan menambahkannya ke dalam antrian.
    - Jika pengguna memilih untuk melihat antrian, program akan menampilkan semua tiket dalam antrian.
    - Jika pengguna memilih untuk menghapus tiket, program akan menghapus tiket paling depan dari antrian.
    - Jika pengguna memilih untuk melihat informasi antrian, program akan menampilkan informasi tentang antrian.
    - Jika pengguna memilih untuk keluar, program akan berhenti dan menampilkan pesan terima kasih.
    - Jika pengguna memasukkan pilihan yang tidak valid, program akan menampilkan pesan kesalahan dan kembali ke menu utama.

Program ini menggunakan beberapa perintah `os.system("CLS")` untuk membersihkan layar terminal (khusus untuk sistem operasi Windows) setiap kali menu ditampilkan atau operasi selesai dilakukan, agar tampilan lebih rapi dan mudah dibaca.

### Tujuan Proyek

Proyek ini bertujuan untuk memberikan simulasi sederhana dari sistem antrian tiket kereta api. Ini dapat digunakan sebagai latihan untuk memahami konsep antrian dalam pemrograman serta bagaimana mengimplementasikan dan mengelola antrian menggunakan struktur data yang tepat (deque dalam hal ini). Selain itu, program ini juga memberikan pengalaman dalam membangun antarmuka pengguna berbasis teks yang interaktif.

### Output Proyek

- Menambah data antrian

![Menambah-data-antrian](img/Menambah-data-antrian.png?raw=true)

- Melihat list data antrian

![Melihat-list-data-antrian](img/Melihat-list-data-antrian.png?raw=true)

- Melihat informasi data antrian

![Melihat-informasi-data-antrian](img/Melihat-Informasi-data-antrian.png?raw=true)

- Menghapus data antrian terdahulu

![Menghapus-data-antrian-terdahulu](img/Menghapus-data-antrian-terdahulu.png?raw=true)

- Keluar dari program

![Keluar-dari-program](img/Keluar-dari-program.png?raw=true)
