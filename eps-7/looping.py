#? =======================================================
#? EPISODE 7: LOOPING (PERULANGAN)
#? =======================================================

#%%
print("=" * 50)
print("LEVEL 1: FOR LOOP - DASAR PERULANGAN")
print("=" * 50)

#? Kasus A: For Loop dengan Range Angka
print("\n>>> For Loop dengan Range:")
for i in range(1, 6):  # 1 sampai 5 (stop tidak termasuk)
    print(f"Perulangan ke-{i}")

#? Kasus B: For Loop dengan List
print("\n>>> For Loop dengan List:")
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

for item in buah:
    print(f"Saya suka makan: {item}")

#? Kasus C: For Loop dengan String
print("\n>>> For Loop dengan String:")
nama = "PYTHON"

for huruf in nama:
    print(f"Huruf: {huruf}")


#%%
print("\n" + "=" * 50)
print("LEVEL 2: WHILE LOOP - LOOP BERDASARKAN KONDISI")
print("=" * 50)

#? Kasus A: While Loop Sederhana (Counter)
print("\n>>> While Loop Counter:")
count = 1

while count <= 5:
    print(f"Hitungan: {count}")
    count += 1  # Jangan lupa increment, kalau tidak infinite loop!

#? Kasus B: While Loop dengan Input (Tebak Angka)
print("\n>>> Game Tebak Angka Sederhana:")
import random

angka_rahasia = random.randint(1, 10)
tebakan = 0
kesempatan = 3

print("Saya thinking of a number between 1 and 10.")
print(f"Kamu punya {kesempatan} kesempatan!\n")

while tebakan < kesempatan:
    guess = int(input("Masukkan tebakanmu: "))
    
    if guess == angka_rahasia:
        print(f"Benar! Angkanya adalah {angka_rahasia}! 🎉")
        break
    elif guess < angka_rahasia:
        print("Tebakanmu terlalu KECIL! Coba lagi.")
    else:
        print("Tebakanmu terlalu BESAR! Coba lagi.")
    
    tebakan += 1
    
    if tebakan < kesempatan:
        print(f"Sisa kesempatan: {kesempatan - tebakan}\n")

if tebakan == kesempatan and guess != angka_rahasia:
    print(f"\nSayang sekali! Angka yang benar adalah {angka_rahasia}.")


#%%
print("\n" + "=" * 50)
print("LEVEL 3: LOOP CONTROL - BREAK, CONTINUE, PASS")
print("=" * 50)

#? BREAK - Keluar dari loop secara paksa
print("\n>>> BREAK - Keluar paksa dari loop:")
daftar_harga = [5000, 12000, 8000, 25000, 15000]

for harga in daftar_harga:
    if harga > 20000:
        print(f"Produk dengan harga {harga} - MEWAH, skip!")
    break  # Stop loop saat ketemu harga > 20000
    print(f"Produk dengan harga {harga} - masih dalam budget")

#? CONTINUE - Skip iterasi tertentu
print("\n>>> CONTINUE - Skip iterasi tertentu:")
angka_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Hanya menampilkan angka GENAP:")
for num in angka_list:
    if num % 2 != 0:  # Jika ganjil
        continue  # Skip ke iterasi berikutnya
    print(num, end=" ")
print()

#? PASS - Placeholder (do nothing)
print("\n>>> PASS - Placeholder:")
for i in range(5):
    if i == 2:
        pass  # TODO: Akan dibuat fitur khusus nanti
    else:
        print(f"Proses item ke-{i}")


#%%
print("\n" + "=" * 50)
print("LEVEL 4: NESTED LOOP - LOOP DALAM LOOP")
print("=" * 50)

#? Kasus A: Segitiga Bintang
print("\n>>> Segitiga Bintang:")
baris = 5

for i in range(1, baris + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Pindah baris

#? Kasus B: Tabel Perkalian
print("\n>>> Tabel Perkalian 1-3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)

#? Kasus C: Matrix 2D
print("\n>>> Akses Matrix 2D:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for baris in matrix:
    for elemen in baris:
        print(elemen, end="\t")
    print()


#%%
print("\n" + "=" * 50)
print("LEVEL 5: ENUMERATE & ELSE CLAUSE")
print("=" * 50)

#? ENUMERATE - Dapet Index dan Value Sekaligus
print("\n>>> ENUMERATE - Index dan Value:")
makanan = ["Nasi Goreng", "Mie Ayam", "Sate Ayam", "Bakso"]

for index, item in enumerate(makanan, start=1):  # start=1 biar index mulai dari 1
    print(f"{index}. {item}")

#? ELSE di Loop - Jalan jika loop selesai normal (tidak di-break)
print("\n>>> ELSE di Loop:")
cari = "Jeruk"
daftar_buah = ["Apel", "Mangga", "Pisang", "Anggur"]

for buah in daftar_buah:
    if buah == cari:
        print(f"Ketemu! {cari} ada di dalam daftar!")
        break
else:
    # Ini akan jalan JIKA loop selesai tanpa break
    print(f"Tidak ketemu {cari} dalam daftar.")


#%%
print("\n" + "=" * 50)
print("BONUS: LIST COMPREHENSION (Gaya Pro)")
print("=" * 50)

#? List Comprehension - Cara singkat membuat list dengan loop
print("\n>>> List Comprehension:")

# Cara biasa
kuadrat_biasa = []
for i in range(1, 6):
    kuadrat_biasa.append(i ** 2)
print(f"Cara biasa: {kuadrat_biasa}")

# List Comprehension
kuadrat_pro = [i ** 2 for i in range(1, 6)]
print(f"List Comprehension: {kuadrat_pro}")

# List Comprehension dengan Filter
genap_kuadrat = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Genap kuadrat: {genap_kuadrat}")


#%%
#? ==========================================
#? CHALLENGE 
#? ==========================================
"""
? BUAT GAME TEBak ANGKA DENGAN BATAS PERCOBAAN
?
? Kriteria:
? 1. Komputer membuat angka random 1-50
? 2. User punya maksimal 5 kesempatan menebak
? 3. Setiap tebakan, kasih hint:
?    - "Tinggi sekali!" jika tebakan > angka_rahasia
?    - "Rendah sekali!" jika tebakan < angka_rahasia
? 4. Jika berhasil dalam <= 5x, tampilkan:
?    - "Hebat! Kamu nebak dalam X kesempatan!"
? 5. Jika gagal setelah 5x, tampilkan:
?    - "Game Over! Angka yang benar adalah X"
?
? EKSTRA CHALLENGE:
? - Simpan semua tebakan user dalam list
? - Tampilkan riwayat tebakan di akhir game
?
"""
