from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import mysql.connector

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "puskesmas_db"
}

# Initialize FastAPI app
app = FastAPI()

# Pydantic models
class DataPasien(BaseModel):
    id_pasien: int = None  # A.I primary key
    nama_lengkap: str
    umur: int
    jenis_kelamin: str
    alamat: str
    nomor_telepon: str
    riwayat_alergi: str
    berat_badan: float
    tinggi_badan: float
    tekanan_darah: str
    suhu_tubuh: float
    denyut_nadi: int
    diagnosa: str
    obat: str
    tindakan: str
    tanggal_kunjungan: datetime

class DataPasienCreate(BaseModel):
    nama_lengkap: str
    umur: int
    jenis_kelamin: str
    alamat: str
    nomor_telepon: str
    riwayat_alergi: str
    berat_badan: float
    tinggi_badan: float
    tekanan_darah: str
    suhu_tubuh: float
    denyut_nadi: int
    diagnosa: str
    obat: str
    tindakan: str
    tanggal_kunjungan: datetime

# Database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Mount static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# API untuk mengambil data pasien
@app.get("/api/data_pasien")
def get_data_pasien():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM data_pasien")
    results = cursor.fetchall()
    connection.close()
    return results

# Endpoint utama untuk memuat index.html
@app.get("/", response_class=HTMLResponse)
def serve_index():
    return FileResponse("frontend/index.html")

# ========== Routes =============== #
# ======== MEMBUAT DATA PASIEN BARU ============= #
@app.post("/data_pasien", response_model=DataPasien)
def create_data_pasien(pasien: DataPasienCreate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
    INSERT INTO data_pasien (
        nama_lengkap, umur, jenis_kelamin, alamat, nomor_telepon, 
        riwayat_alergi, berat_badan, tinggi_badan, tekanan_darah, suhu_tubuh, 
        denyut_nadi, diagnosa, obat, tindakan, tanggal_kunjungan
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        pasien.nama_lengkap, pasien.umur, pasien.jenis_kelamin, pasien.alamat, pasien.nomor_telepon,
        pasien.riwayat_alergi, pasien.berat_badan, pasien.tinggi_badan, pasien.tekanan_darah, pasien.suhu_tubuh,
        pasien.denyut_nadi, pasien.diagnosa, pasien.obat, pasien.tindakan, pasien.tanggal_kunjungan
    ))
    connection.commit()
    pasien_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {**pasien.dict(), "id_pasien": pasien_id}

# ======== MENAMPILKAN DATA PASIEN secara KESELURUHAN ============= #
@app.get("/data_pasien", response_model=List[DataPasien])
def read_all_data_pasien():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM data_pasien"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# ======== MENAMPILKAN DATA PASIEN by ID ============= #
@app.get("/data_pasien/{id_pasien}", response_model=DataPasien)
def read_data_pasien_by_id(id_pasien: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM data_pasien WHERE id_pasien = %s"
    cursor.execute(query, (id_pasien,))
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    if not data:
        raise HTTPException(status_code=404, detail="Data pasien tidak ditemukan")
    return data

# ======== MEMPERBARUI DATA PASIEN by ID ============= #
@app.put("/data_pasien/{id_pasien}", response_model=DataPasien) 
def update_data_pasien(id_pasien: int, pasien: DataPasienCreate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
    UPDATE data_pasien SET
        nama_lengkap = %s, umur = %s, jenis_kelamin = %s, alamat = %s, nomor_telepon = %s,
        riwayat_alergi = %s, berat_badan = %s, tinggi_badan = %s, tekanan_darah = %s, suhu_tubuh = %s,
        denyut_nadi = %s, diagnosa = %s, obat = %s, tindakan = %s, tanggal_kunjungan = %s
    WHERE id_pasien = %s
    """
    cursor.execute(query, (
        pasien.nama_lengkap, pasien.umur, pasien.jenis_kelamin, pasien.alamat, pasien.nomor_telepon,
        pasien.riwayat_alergi, pasien.berat_badan, pasien.tinggi_badan, pasien.tekanan_darah, pasien.suhu_tubuh,
        pasien.denyut_nadi, pasien.diagnosa, pasien.obat, pasien.tindakan, pasien.tanggal_kunjungan, id_pasien
    ))
    connection.commit()
    cursor.close()
    connection.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Data pasien tidak ditemukan")
    return {**pasien.dict(), "id_pasien": id_pasien}

# ============== MENGHAPUS DATA PASIEN by ID ========================= #
@app.delete("/data_pasien/{id_pasien}")
def delete_data_pasien(id_pasien: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "DELETE FROM data_pasien WHERE id_pasien = %s"
    cursor.execute(query, (id_pasien,))
    affected_rows = cursor.rowcount  # Ambil jumlah baris yang terpengaruh
    connection.commit()
    cursor.close()
    connection.close()
    
    if affected_rows == 0:  # Jika tidak ada baris yang dihapus
        raise HTTPException(status_code=404, detail="Data pasien tidak ditemukan")
    
    return {"message": "Data pasien berhasil dihapus"}

if __name__ == "__main__":  # Start background task for writing data
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)