const API_URL = "http://127.0.0.1:8000/data_pasien";

async function fetchPasien() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        const identitasTable = document.querySelector("#identitas-table tbody");
        const penyakitTable = document.querySelector("#penyakit-table tbody");

        // Clear existing rows
        identitasTable.innerHTML = "";
        penyakitTable.innerHTML = "";

        data.forEach((pasien, index) => {
            // Tambahkan data ke tabel Identitas Pasien
            const identitasRow = `
                <tr>
                    <td>${index + 1}</td>
                    <td>${pasien.nama_lengkap}</td>
                    <td>${pasien.jenis_kelamin}</td>
                    <td>${pasien.alamat}</td>
                    <td>${pasien.nomor_telepon}</td>
                    <td>${pasien.umur}</td>
                </tr>
            `;
            identitasTable.insertAdjacentHTML("beforeend", identitasRow);

            // Tambahkan data ke tabel Informasi Penyakit dan Penanganan
            const penyakitRow = `
                <tr>
                    <td>${index + 1}</td>
                    <td>${pasien.riwayat_alergi}</td>
                    <td>${pasien.berat_badan}</td>
                    <td>${pasien.tinggi_badan}</td>
                    <td>${pasien.tekanan_darah}</td>
                    <td>${pasien.suhu_tubuh}</td>
                    <td>${pasien.denyut_nadi}</td>
                    <td>${pasien.diagnosa}</td>
                    <td>${pasien.obat}</td>
                    <td>${pasien.tindakan}</td>
                    <td>${pasien.tanggal_kunjungan}</td>
                </tr>
            `;
            penyakitTable.insertAdjacentHTML("beforeend", penyakitRow);
        });
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Panggil fetchPasien saat halaman dimuat
document.addEventListener("DOMContentLoaded", fetchPasien);
