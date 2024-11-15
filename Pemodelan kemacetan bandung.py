import random
import matplotlib.pyplot as plt

# Parameter simulasi
jam = 12  # Durasi simulasi dalam jam
kapasitas_jalan = 100  # Kapasitas jalan (jumlah kendaraan yang dapat lewat per jam)
rata_rata_veh_permenit = 20  # Rata-rata kendaraan yang lewat per menit
lampu_hijau = 30  # Waktu lampu hijau dalam detik
lampu_merah = 60  # Waktu lampu merah dalam detik
total_kendaraan_masuk = 0  # Total kendaraan yang datang
total_kendaraan_lolos = 0  # Total kendaraan yang berhasil lolos
total_kendaraan_tertahan = 0  # Total kendaraan yang tertahan

# Simulasi
kendaraan_per_jam = []  # Daftar kendaraan yang lolos per jam
kendaraan_terlambat_per_jam = []  # Daftar kendaraan terlambat per jam

for i in range(jam):
    # Kendaraan yang berada di simpang (random)
    kendaraan_di_simpang = random.randint(0, kapasitas_jalan)
    
    # Kendaraan yang datang setiap jam
    kendaraan_masuk = random.randint(10, rata_rata_veh_permenit * 60)
    
    total_kendaraan_masuk += kendaraan_masuk  # Update total kendaraan yang masuk
    
    # Kendaraan yang bisa lolos (maksimal kapasitas jalan)
    kendaraan_lolos = min(kendaraan_di_simpang + kendaraan_masuk, kapasitas_jalan)
    
    # Kendaraan yang tertahan (jika ada)
    kendaraan_terlambat = max(0, kendaraan_masuk + kendaraan_di_simpang - kapasitas_jalan)
    
    total_kendaraan_lolos += kendaraan_lolos  # Update total kendaraan yang lolos
    total_kendaraan_tertahan += kendaraan_terlambat  # Update total kendaraan yang tertahan
    
    # Simpan data per jam
    kendaraan_per_jam.append(kendaraan_lolos)
    kendaraan_terlambat_per_jam.append(kendaraan_terlambat)

# Grafik Hasil Simulasi
plt.figure(figsize=(10, 6))
plt.plot(range(jam), kendaraan_per_jam, marker='o', label="Kendaraan Lolos")
plt.title("Simulasi Kemacetan Kota Bandung")
plt.xlabel("Jam")
plt.ylabel("Kendaraan Lolos (per jam)")
plt.grid(True)
plt.legend()
plt.show()

# Tabel Hasil
print("Tabel Hasil Simulasi Kemacetan Kota Bandung")
print(f"{'Jam':<10}{'Kendaraan Masuk':<20}{'Kendaraan Lolos':<20}{'Kendaraan Tertahan':<20}")
for i in range(jam):
    kendaraan_masuk = random.randint(10, rata_rata_veh_permenit * 60)  # Random kendaraan masuk tiap jam
    print(f"{i+1:<10}{kendaraan_masuk:<20}{kendaraan_per_jam[i]:<20}{kendaraan_terlambat_per_jam[i]:<20}")

# Output Total
print("\nTotal Kendaraan yang Masuk:", total_kendaraan_masuk)
print("Total Kendaraan yang Lolos:", total_kendaraan_lolos)
print("Total Kendaraan yang Tertahan:", total_kendaraan_tertahan)
