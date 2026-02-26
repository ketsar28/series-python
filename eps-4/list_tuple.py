
#? === PYTHON DASAR: EPISODE 04 (LIST & TUPLE) ===

# %% 1. LIST: SI KANTONG AJAIB (Mutable)
#? List adalah koleksi data yang urutannya terjaga dan isinya BISA DIUBAH-UBAH.

daftar_belanja = ["Beras", "Telur", "Minyak"]
print("Daftar Belanja Awal:", daftar_belanja)

# %%
# --- Menambah Data (Append) ---
daftar_belanja.append("Sirup Marjan")
print("Setelah Tambah Sirup:", daftar_belanja)

# %%
# --- Mengakses Data (Indexing) ---
print("Barang pertama:", daftar_belanja[0]) 

# %%
# --- Mengubah Data ---
daftar_belanja[1] = "Telur Bebek" #? Ganti Telur Ayam jadi Telur Bebek
print("Daftar Belanja Update:", daftar_belanja)

# %%
# --- Menghapus Data ---
daftar_belanja.remove("Beras")
print("Setelah Beras Dihapus:", daftar_belanja)


# %% 2. TUPLE: SI KAKU YANG KONSISTEN (Immutable)
#? Tuple mirip List, tapi isinya GAK BISA DIUBAH setelah dibuat.

hari_kerja = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")
# hari_kerja.append("Sabtu") #! INI AKAN ERROR (AttributeError)
# hari_kerja[0] = "Minggu"    #! INI JUGA AKAN ERROR (TypeError)

print("Hari Kerja:", hari_kerja)
print("Jumlah hari kerja:", len(hari_kerja))


# %% 3. SLICING: CARA POTONG KANTONG
#? Mengambil sebagian data dari dalam list/tuple.

angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %%
#? Ambil dari index 1 sampai SEBELUM index 4
print("Ambil index 1-3:", angka[1:4]) 

# %%
#? Ambil 3 data pertama
print("3 Data Pertama:", angka[:3])

# %%
#? Ambil data dari index 5 sampai akhir
print("Index 5 ke atas:", angka[5:])


# %% 4. BUILT-IN FUNCTIONS (Power-ups)

skor = [80, 95, 70, 100, 85]

print("Skor Tertinggi:", max(skor))
print("Skor Terendah:", min(skor))
print("Banyaknya Data:", len(skor))
print("Urutkan Skor:", sorted(skor)) #? Dari kecil ke besar

# %%
