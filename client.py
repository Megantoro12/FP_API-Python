import requests
import json

API_BASE_URL = "http://127.0.0.1:8000"

def print_response(response):
    """Print response data in a formatted way."""
    if response.status_code in [200, 201]:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_data_pasien():
    """Send POST request to create a new pasien."""
    print("Masukan Detail Pasien:")
    nama_lengkap = input("Nama Lengkap: ")
    umur = int(input("Umur: "))
    jenis_kelamin = input("Gender (L/P): ")
    alamat = input("Alamat: ")
    nomor_telepon = input("Nomor Telpon: ")
    riwayat_alergi = input("Riwayat Alergi: ")
    berat_badan = float(input("Berat Badan (kg): "))
    tinggi_badan = float(input("Tinggi Badan (cm): "))
    tekanan_darah = input("Golongan Darah: ")
    suhu_tubuh = float(input("Suhu Tubuh (°C): "))
    denyut_nadi = int(input("Denyut Nadi (bpm): "))
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

def read_all_data_pasien():
    """Send GET request to fetch all pasien data."""
    response = requests.get(f"{API_BASE_URL}/data_pasien")
    print_response(response)

def read_data_pasien_by_id():
    """Send GET request to fetch pasien data by ID."""
    id_pasien = input("Masukan ID Pasien: ")
    response = requests.get(f"{API_BASE_URL}/data_pasien/{id_pasien}")
    print_response(response)

def update_data_pasien():
    """Send PUT request to update pasien data."""
    id_pasien = input("Masukan ID Pasien Yang Ingin Diperbarui: ")
    print("Masukan Detail Pasien:")
    nama_lengkap = input("Nama Lengkap: ")
    umur = int(input("Umur: "))
    jenis_kelamin = input("Gender (L/P): ")
    alamat = input("Alamat: ")
    nomor_telepon = input("Nomor Telepon: ")
    riwayat_alergi = input("Riwayat Alergi: ")
    berat_badan = float(input("Berat Badan (kg): "))
    tinggi_badan = float(input("Tinggi Badan (cm): "))
    tekanan_darah = input("Golongan Darah: ")
    suhu_tubuh = float(input("Suhu Tubuh (C): "))
    denyut_nadi = int(input("Denyut Nadi: "))
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

def delete_data_pasien():
    """Send DELETE request to delete pasien data."""
    id_pasien = input("Masukan ID pasien yang ingin dihapus: ")
    response = requests.delete(f"{API_BASE_URL}/data_pasien/{id_pasien}")
    print_response(response)

def main():
    """Main menu for CRUD operations."""
    while True:
        print("\nMenu:")
        print("1. Tambahkan Data Passien")
        print("2. Tampilkan Semua Data Pasien")
        print("3. Tampilkan Data Pasien Berdasarkan ID")
        print("4. Perbarui Data Pasien")
        print("5. Hapus Data Pasien") 
        print("6. Keluar")
        choice = input("Masukan Pilihan Anda: ")

        if choice == "1":
            create_data_pasien()
        elif choice == "2":
            read_all_data_pasien()
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
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
