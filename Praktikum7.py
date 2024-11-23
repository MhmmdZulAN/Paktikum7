mahasiswa = {}
pilihan = ""

def tambah_data():
    Nama = input('Masukan Nama: ')
    NIM = input('Masukan NIM: ')
    Nilai_Tugas = float(input('Masukan Nilai Tugas: '))
    Nilai_UTS = float(input('Masukan Nilai UTS: '))
    Nilai_UAS = float(input('Masukan Nilai UAS: '))
    Nilai_Akhir = (Nilai_Tugas * 0.3) + (Nilai_UTS * 0.35) + (Nilai_UAS * 0.35)
    mahasiswa[NIM] = {'Nama': Nama, 'Nilai Tugas': Nilai_Tugas, 'Nilai UTS': Nilai_UTS, 'Nilai UAS': Nilai_UAS, 'Nilai Akhir': Nilai_Akhir}
    print('Data Berhasil Ditambahkan.')

def ubah_data():
    NIM = input('Masukan NIM Mahasiswa yang ingin diubah: ')
    if NIM in mahasiswa:
        Nama = input('Masukan Nama baru: ')
        Nilai_Tugas = float(input('Masukan Nilai Tugas baru: '))
        Nilai_UTS = float(input('Masukan Nilai UTS baru: '))
        Nilai_UAS = float(input('Masukan Nilai UAS baru: '))
        Nilai_Akhir = Nilai_Tugas * 0.3 + Nilai_UTS * 0.35 + Nilai_UAS * 0.35
        mahasiswa[NIM] = {'Nama': Nama, 'Nilai Tugas': Nilai_Tugas, 'Nilai UTS': Nilai_UTS, 'Nilai UAS': Nilai_UAS, 'Nilai Akhir': Nilai_Akhir}
        print('Data Berhasil Diubah.')
    else:
        print('NIM tidak ditemukan!')

def hapus_data():
    NIM = input('Masukan NIM mahasiswa yang ingin dihapus: ')
    if NIM in mahasiswa:
        del mahasiswa[NIM]
        print('Data Berhasil dihapus!')
    else:
        print('NIM tidak ditemukan!')

def tampilkan_data():
    if not mahasiswa:
        print("Tidak Ada Data Mahasiswa")
    else:
        print("No\tNama\tNIM\tTugas\tUTS\tUAS\tAkhir")
        for i, (NIM, data) in enumerate(mahasiswa.items(),start=1):
            print(f"{i}\t{data['Nama']}\t{NIM}\t{data['Nilai Tugas']:.0f}\t{data['Nilai UTS']:.0f}\t{data['Nilai UAS']:.0f}\t{data['Nilai Akhir']:.0f}")


def cari_data():
    NIM = input('Masukan NIM Mahasiswa yang ingin dicari: ')
    if NIM in mahasiswa:
        data = mahasiswa[NIM]
        print(f"Nama: {data['Nama']}")
        print(f"Nilai Tugas: {data['Nilai Tugas']:.0f}")
        print(f"Nilai UTS: {data['Nilai UTS']:.0f}")
        print(f"Nilai UAS: {data['Nilai UAS']:.0f}")
        print(f"Nilai Akhir: {data['Nilai Akhir']:.0f}")
    else:
        print('NIM Tidak Ditemukan!')

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        break
    else:
        print('Pilihan Tidak Valid. Silahkan masukan kembali!')

