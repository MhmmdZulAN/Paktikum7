Program Python di atas adalah sebuah aplikasi berbasis teks untuk mengelola data mahasiswa. Fitur-fitur utamanya meliputi penambahan, pengubahan, penghapusan, penampilan, dan pencarian data mahasiswa. Berikut adalah penjelasan singkat tentang fungsi dan cara kerjanya:

### **Penjelasan Fitur**
1. **Tambah Data (`tambah_data`)**  
   Memungkinkan pengguna untuk menambahkan data baru ke dalam daftar `mahasiswa`. Data yang diinput adalah:
   - Nama mahasiswa
   - NIM mahasiswa
   - Nilai Tugas, Nilai UTS, dan Nilai UAS  
   Nilai Akhir dihitung dengan bobot:  
   - Tugas: 30%  
   - UTS: 35%  
   - UAS: 35%  

2. **Ubah Data (`ubah_data`)**  
   Memungkinkan pengguna untuk mengubah data mahasiswa berdasarkan NIM. Jika NIM ditemukan, semua data mahasiswa tersebut akan diperbarui dengan data baru yang diinput.

3. **Hapus Data (`hapus_data`)**  
   Menghapus data mahasiswa berdasarkan NIM. Jika NIM ditemukan, data mahasiswa tersebut akan dihapus dari daftar.

4. **Tampilkan Data (`tampilkan_data`)**  
   Menampilkan daftar seluruh data mahasiswa dalam format tabel. Jika tidak ada data, akan ditampilkan pesan bahwa data mahasiswa kosong.

5. **Cari Data (`cari_data`)**  
   Mencari data mahasiswa berdasarkan NIM. Jika ditemukan, data mahasiswa akan ditampilkan. Jika tidak, akan muncul pesan bahwa NIM tidak ditemukan.

6. **Keluar Program**  
   Menghentikan program dengan memilih opsi "6".

### **Cara Kerja Program**
- Program menggunakan dictionary (`mahasiswa`) untuk menyimpan data setiap mahasiswa. Kunci (key) adalah NIM, dan nilainya adalah dictionary berisi detail mahasiswa.
- Fungsi-fungsi diakses melalui menu utama, yang terus berjalan dalam loop hingga pengguna memilih untuk keluar.
- Input dan output dilakukan melalui terminal.

### **Keunggulan**
- Struktur kode sederhana dan mudah dipahami.
- Tabel data yang ditampilkan terorganisir rapi.
- Mendukung operasi CRUD (Create, Read, Update, Delete).

## Hasil Program

#1 Input Data

<img width="495" alt="image" src="https://github.com/user-attachments/assets/ccdf8795-06b4-4fc1-b278-75c7efce0c46">

#2. Ubah Data

bila data terantum

<img width="322" alt="image" src="https://github.com/user-attachments/assets/84ce06d3-13a2-49ef-857f-b24b5ed1bf91">

Bila Data Tidak Tercantum

<img width="381" alt="image" src="https://github.com/user-attachments/assets/8ebdc14a-ada8-4048-81ad-02c47329ffe3">


#3. Hapus Data
Bila Data Tercantum

<img width="341" alt="image" src="https://github.com/user-attachments/assets/5b807dfa-de6e-4c6e-b9a4-b2c8d44e92c2">

Bila Data Tidak Tercantum

<img width="392" alt="image" src="https://github.com/user-attachments/assets/8d98723c-70cd-4aca-a2c3-cc4d96e62e6e">



#4. Tampilkan data 
Sebelum Data Di Hapus

<img width="398" alt="image" src="https://github.com/user-attachments/assets/3fe81e61-cffe-497e-b6c7-e44aa84a4879">

Setelah Data di Hapus atau data belum di input

<img width="457" alt="image" src="https://github.com/user-attachments/assets/1a9bfe72-d280-43a1-8d36-eabf733ece55">

#5. Cari Data

Bila Data Tercantum

<img width="323" alt="image" src="https://github.com/user-attachments/assets/0dbe12d9-2769-47b4-9c80-3e887736fbba">

Bila Data Tidak Tercantum

<img width="335" alt="image" src="https://github.com/user-attachments/assets/7e7cb02c-8b3b-4937-93d2-c851a0c6d806">

6. Keluar
<img width="188" alt="image" src="https://github.com/user-attachments/assets/ecae9b20-63c6-439c-9be0-6ca7f9ce47bd">


### FLowChart

![image](https://github.com/user-attachments/assets/ed4cb032-8daa-4e86-9c4a-1cc9e7dd5022)







