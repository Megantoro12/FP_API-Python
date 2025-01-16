import requests
import json

API_BASE_URL = "http://127.0.0.1:8000"

def print_response(response): #Cetak data respons dalam format yang sesuai.
    if response.status_code in [200, 201]:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_int_input(prompt):#Meminta pengguna untuk memasukkan input bertipe bilangan bulat/integer.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Masukkan tidak sesuai, harap masukkan angka.")

def get_float_input(prompt): #Meminta pengguna untuk memasukkan input bertipe float.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan tidak sesuai, harap masukkan angka.")

def create_data_pasien(): #Kirim permintaan POST untuk membuat pasien baru.
    while True:
        print("Masukan Detail Pasien (atau ketik '0' untuk kembali ke menu utama):")
        nama_lengkap = input("Nama Lengkap: ")
        if nama_lengkap == "0":
            return  # Kembali ke menu utama

        umur = get_int_input("Umur: ")
        jenis_kelamin = input("Gender (L/P): ")
        alamat = input("Alamat: ")
        nomor_telepon = input("Nomor Telpon: ")
        riwayat_alergi = input("Riwayat Alergi: ")
        berat_badan = get_float_input("Berat Badan (kg): ")
        tinggi_badan = get_float_input("Tinggi Badan (cm): ")
        tekanan_darah = input("Golongan Darah: ")
        suhu_tubuh = get_float_input("Suhu Tubuh (\u00b0C): ")
        denyut_nadi = get_int_input("Denyut Nadi (bpm): ")
        diagnosa = input("Diagnosis: ")
        obat = input("Obat: ")
        tindakan = input("Tindakan: ")
        tanggal_kunjungan = input("Tanggal Kunjungan (YYYY-MM-DD HH:MM:SS): ")

        payload = {
            "nama_lengkap": nama_lengkap,
            "umur": umur,
            "jenis_kelamin": jenis_kelamin,
            "alamat": alamat,
            "nomor_telepon": nomor_telepon,
            "riwayat_alergi": riwayat_alergi,
            "berat_badan": berat_badan,
            "tinggi_badan": tinggi_badan,
            "tekanan_darah": tekanan_darah,
            "suhu_tubuh": suhu_tubuh,
            "denyut_nadi": denyut_nadi,
            "diagnosa": diagnosa,
            "obat": obat,
            "tindakan": tindakan,
            "tanggal_kunjungan": tanggal_kunjungan
        }
        response = requests.post(f"{API_BASE_URL}/data_pasien", json=payload)
        print_response(response)
        break

def read_data_pasien_by_id(): #"""Kirim permintaan GET untuk mengambil data pasien berdasarkan ID."""
    id_pasien = get_int_input("Masukan ID Pasien: ")
    response = requests.get(f"{API_BASE_URL}/data_pasien/{id_pasien}")
    print_response(response)

def update_data_pasien(): #"""Kirim permintaan PUT untuk memperbarui data pasien."""
    id_pasien = get_int_input("Masukan ID Pasien Yang Ingin Diperbarui: ")
    print("Masukan Detail Pasien:")
    nama_lengkap = input("Nama Lengkap: ")
    umur = get_int_input("Umur: ")
    jenis_kelamin = input("Gender (L/P): ")
    alamat = input("Alamat: ")
    nomor_telepon = input("Nomor Telepon: ")
    riwayat_alergi = input("Riwayat Alergi: ")
    berat_badan = get_float_input("Berat Badan (kg): ")
    tinggi_badan = get_float_input("Tinggi Badan (cm): ")
    tekanan_darah = input("Golongan Darah: ")
    suhu_tubuh = get_float_input("Suhu Tubuh (C): ")
    denyut_nadi = get_int_input("Denyut Nadi: ")
    diagnosa = input("Diagnosis: ")
    obat = input("Obat: ")
    tindakan = input("Tindakan: ")
    tanggal_kunjungan = input("Tanggal Kunjungan (YYYY-MM-DD HH:MM:SS): ")

    payload = {
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "alamat": alamat,
        "nomor_telepon": nomor_telepon,
        "riwayat_alergi": riwayat_alergi,
        "berat_badan": berat_badan,
        "tinggi_badan": tinggi_badan,
        "tekanan_darah": tekanan_darah,
        "suhu_tubuh": suhu_tubuh,
        "denyut_nadi": denyut_nadi,
        "diagnosa": diagnosa,
        "obat": obat,
        "tindakan": tindakan,
        "tanggal_kunjungan": tanggal_kunjungan
    }
    response = requests.put(f"{API_BASE_URL}/data_pasien/{id_pasien}", json=payload)
    print_response(response)

def delete_data_pasien(): #"""Kirim permintaan DELETE untuk menghapus data pasien berdasarkan ID."""
    id_pasien = get_int_input("Masukan ID pasien yang ingin dihapus: ")
    response = requests.delete(f"{API_BASE_URL}/data_pasien/{id_pasien}")
    print_response(response)

def main(): #"""Program Utam C-R-U-D."""
    while True:
        print("\nMenu:")
        print("1. Tambahkan Data Pasien")
        print("2. Tampilkan Semua Data Pasien")
        print("3. Tampilkan Data Pasien Berdasarkan ID")
        print("4. Perbarui Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")
        choice = input("Masukan Pilihan Anda: ")

        if choice == "1":
            create_data_pasien()
        elif choice == "2":
            response = requests.get(f"{API_BASE_URL}/data_pasien")
            print_response(response)
        elif choice == "3":
            read_data_pasien_by_id()
        elif choice == "4":
            update_data_pasien()
        elif choice == "5":
            delete_data_pasien()
        elif choice == "6":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak sesuai. Silakan coba lagi.")

if __name__ == "__main__":
    main()