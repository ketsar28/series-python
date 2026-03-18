#? =======================================================
#? EPISODE 6: CONDITIONAL LOGIC
#? =======================================================

#%%
print("--- 1. BASIC IF-ELSE ---")
#? Kasus A: Cek Bilangan Positif atau Negatif
angka_input = int(input("Masukkan sebuah angka: "))

if angka_input >= 0:
    print(f"{angka_input} adalah bilangan POSITIF.")
else:
    print(f"{angka_input} adalah bilangan NEGATIF.")

#%%
#? Kasus B: Cek Password Sederhana
password_rahasia = "python123"
input_user = input("\nMasukkan password akses: ")

if input_user == password_rahasia:
    print("Akses Diterima! ✅")
else:
    print("Akses Ditolak! Password salah. ❌")


#%%
print("\n--- 2. LOGIKA ELIF ---")
#? Kasus: Penentuan Kategori Usia
usia = int(input("Masukkan usia anda: "))

if usia >= 60:
    status = "Lansia"
elif usia >= 18:
    status = "Dewasa"
elif usia >= 13:
    status = "Remaja"
elif usia >= 5:
    status = "Anak-anak"
else:
    status = "Balita/Bayi"

print(f"Kategori usia anda adalah: {status}")


#%%
print("\n--- 3. NESTED IF (LOGIKA BERTINGKAT) ---")
# Kasus: Nonton Film di Bioskop (Cek Tiket & Usia)
punya_tiket = input("Apakah sudah beli tiket? (y/n): ").lower()

if punya_tiket == 'y':
    usia_penonton = int(input("Masukkan usia kamu: "))
    if usia_penonton >= 17:
        print("Selamat menonton! Nikmati filmnya. 🎬")
    else:
        print("Wah, maaf ya... film ini khusus untuk 17 tahun ke atas. 🚫")
else:
    print("Silakan beli tiket dulu di loket depan ya!")


#%%
print("\n--- 4. LOGICAL OPERATORS (AND, OR, NOT) ---")
# Kasus: Syarat Beasiswa (IPK > 3.5 DAN Penghasilan Ortu < 5jt)
ipk = float(input("Masukkan IPK anda: "))
gaji_ortu = int(input("Penghasilan orang tua (Rp): "))
punya_prestasi = input("Ada prestasi nasional? (y/n): ").lower() == 'y'

# Logika AND & OR
if (ipk > 3.5 and gaji_ortu < 5000000) or punya_prestasi:
    print("Selamat! Anda LAYAK mendapatkan beasiswa. ✅")
else:
    print("Mohon maaf, anda belum memenuhi kriteria beasiswa. ❌")

# Logika NOT (Membalik keadaan)
sedang_libur = False
if not sedang_libur:
    print("Ayo belajar lagi, hari ini bukan hari libur!")


#%%
print("\n--- 5. TERNARY OPERATOR (SHORT-HAND IF) ---")
# Kasus: Cek Angka Ganjil/Genap dalam satu baris
angka = int(input("Masukkan angka: "))

# Cara Professional (Ternary):
hasil = "Genap" if angka % 2 == 0 else "Ganjil"
print(f"Angka {angka} adalah bilangan {hasil}")


#%%
print("\n--- 6. Keyword IN ---")
# Kasus: Cek Akses Fitur Beta Developer
email_user = input("Masukkan email kamu: ")
whitelist = [
    "ketsar@devspace.id", 
    "budi.dev@gmail.com", 
    "rahmat@devspace.id",
    "admin@koding.com"
]

if email_user in whitelist:
    print(f"Email '{email_user}' terdaftar\nAkses Fitur Beta DIIZINKAN. 🔓")
else:
    print(f"Email '{email_user}' tidak terdaftar\nAkses DITOLAK. 🔒")


#%%
print("\n--- 7. Implicit Boolean ---")
# Di Python, nilai kosong (empty) dianggap False
username = input("Daftar Username: ")

if username: # Jika string TIDAK KOSONG
    print(f"Username '{username}' berhasil didaftarkan!")
else:        # Jika user cuma pencet enter (string kosong)
    print("Error: Username tidak boleh kosong!")


#%%
print("\n--- 8. MATCH-CASE ---")
# Mirip 'switch' di bahasa lain, lebih rapi untuk banyak pilihan
print("Pilih Menu Kopi:")
print("1. Arabika\n2. Robusta\n3. Luwak")
pilihan = input("Masukkan nama kopi: ").capitalize()

match pilihan:
    case "Arabika":
        print("Harga Arabika: Rp 25,000. Rasanya agak asam segar.")
    case "Robusta":
        print("Harga Robusta: Rp 20,000. Rasanya pahit mantap.")
    case "Luwak":
        print("Harga Luwak: Rp 50,000. Kopi premium kualitas tinggi.")
    case _:
        print("Menu tidak tersedia. Silakan pilih 1-3.")


#%%
#? ==========================================
#? CHALLENGE 
#? ==========================================
"""
? Buatlah Sistem 'Penerimaan Karyawan Otomatis'
? Kriteria:
? 1. Umur 20 - 30 tahun.
? 2. Pendidikan minimal 'S1' atau memiliki pengalaman kerja > 2 tahun.
? 3. Tidak pernah terlibat kasus hukum (input 'y/n').

"""
