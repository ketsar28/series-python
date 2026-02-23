
#? === PYTHON DASAR: EPISODE 03 (VARIABEL) ===

# %% 0. KENAPA HARUS PAKAI VARIABEL?

# --- TANPA VARIABEL (Manual) ---
print("Halo Budi, selamat berpuasa!")
print("Halo Budi, apa kabar?")
print("Besok main yuk, Budi!")

# %% --- PAKAI VARIABEL (Efisien) ---
nama = "Andi" 
print("Halo", nama + ", selamat berpuasa!")
print("Halo", nama + ", apa kabar?")
print("Besok main yuk,", nama + "!")


# %% 1. APA ITU VARIABEL?
#? Variabel adalah sebuah nama yang mewakili sebuah nilai di memori.

nama_user = "Budi" #? Menyimpan teks (String)
umur = 20          #? Menyimpan angka (Integer)

print("Halo, nama saya", nama_user)
print("Umur saya sekarang", umur, "tahun")


# %% 2. ATURAN MAIN (Naming Convention)
#! [!] TIDAK BOLEH pakai spasi (Gunakan underscore _)
#! [!] TIDAK BOLEH diawali angka
#! [!] Bersifat Case Sensitive (Huruf besar/kecil berpengaruh)

nama_lengkap = "Budi Sudarsono" #? BENAR
# 1nama = "Error"               #! SALAH (Akan error)

x = 5
X = 10
print("x kecil:", x) #? Hasilnya 5, bukan 10


# %% 3. DYNAMIC TYPING
#? Di Python, tipe data variabel bisa berubah-ubah secara fleksibel.
data = 100
print("Data awal:", data)

data = "Selesai"
print("Data berubah:", data)


# %% 4. MULTIPLE ASSIGNMENT (Cara Isi Banyak Variabel)

#? --- Cara Standar (Non-Pythonic) ---
panjang_1 = 10
lebar_1 = 5
tinggi_1 = 2
print("P_1:", panjang_1, "L_1:", lebar_1, "T_1:", tinggi_1)

#? --- Cara Cepat (Pythonic) ---
panjang_2, lebar_2, tinggi_2 = 10, 5, 2

print("P_2:", panjang_2, "L_2:", lebar_2, "T_2:", tinggi_2)


# %% 5. SWAP (Tukar Nilai)

#? --- Cara Standar (Pake Variabel Bantuan) ---
a = "Botol"
b = "Meja"

temp = a
a = b
b = temp

print("A dengan temp jadi:", a)
print("B dengan temp jadi:", b)

print("="*30)

#? --- Cara Cepat (Pythonic Swap) ---
#? Di Python gak perlu variabel temp!
a, b = b, a 

print("A pythonic jadi:", a)
print("B pythonic jadi:", b)
# %%
