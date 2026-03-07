#? =======================================================
#? EPISODE 5: USER INPUT, CASTING (TIPE DATA), & F-STRING
#? =======================================================

#%%
print("--- 🏪 Kasir Warung Kopi Interaktif ---")

#? 1. INPUT STRING (Teks)
#? Input akan selalu mengubah ketikan menjadi String (Teks).
nama_kasir = input("Siapa nama kasir hari ini? ")
pelanggan = input("Siapa nama pelanggan? ")

print("\nCek Hasil Input & Tipe Data:")
print(f"Kasir yang diinput : '{nama_kasir}' (Tipe data: {type(nama_kasir)})")
print(f"Pelanggan diinput  : '{pelanggan}' (Tipe data: {type(pelanggan)})")


#%%
#? 2. INPUT INTEGER (Angka Bulat)
#? input() akan MENGANGGAPNYA SEBAGAI TEKS
qty_kopi = input(f"\nBerapa gelas kopi pesanan {pelanggan}? ")

print("\nCek Hasil Input SEBELUM diubah (Casting):")
print(f"Nilai: '{qty_kopi}' (Tipe data: {type(qty_kopi)}) -> Masih berupa Teks/String")

#? Karena masih teks, kita harus ubah ke angka matematis dengan int()
qty_kopi = int(qty_kopi)  

print("\nCek Hasil Input SESUDAH diubah dengan int():")
print(f"Nilai: {qty_kopi} (Tipe data: {type(qty_kopi)}) -> Sekarang Angka Bulat/Integer")


#! ==========
#! ⚠️ ERROR
#! ==========
#%%
#! KASUS 1: Lupa diubah (Casting) ke angka
qty = input("\nBeli berapa gelas? ")  # Misalnya user ngetik: 5
hasil_tanpa_casting = qty * 2
hasil_casting = int(qty) * 2
print(f"Hasil tanpa casting: {hasil_tanpa_casting}")    # Hasilnya bukan 10, tapi "55"
print(f"Hasil dengan casting: {hasil_casting}")

#%%
#! KASUS 2: ValueError karena salah ketik
umur = input("\nBerapa umur kamu? ")  # Misalnya: "dua puluh"
umur = int(umur)                      # Akan menghasilkan ERROR merah (ValueError)


#%% 
#? 3. INPUT FLOAT (Angka Desimal / Pecahan)
#? cocok untuk berat, jarak, atau suhu.
jarak_antar = input("\nBerapa km jarak rumah pelanggan? (Boleh pakai koma, misal: 2.5): ")

print("\nCek Hasil Input SEBELUM diubah (Casting):")
print(f"Nilai: '{jarak_antar}' (Tipe data: {type(jarak_antar)}) -> Masih berupa Teks/String")

jarak_antar = float(jarak_antar)  # Ubah "2.5" jadi angka desimal 2.5

print("\nCek Hasil Input SESUDAH diubah dengan float():")
print(f"Nilai: {jarak_antar} (Tipe data: {type(jarak_antar)}) -> Sekarang Angka Desimal/Float")


#%%
#? ==========================================
#? 4. MATH OPERATIONS & F-STRING DALAM AKSI!
#? ==========================================
# Variabel bantuan
harga_kopi = 15000
ongkir_per_km = 2000
potongan_diskon = 5000

print("\n=== 🧾 STRUK PEMBELIAN ===")
print("Kasir yang melayani   :", nama_kasir)
print(f"Kasir yang melayani   : {nama_kasir}")
print(f"Nama Pelanggan        : {pelanggan}")

#? A. Perkalian Angka Bulat (*)
total_harga_kopi = qty_kopi * harga_kopi
print(f"Total harga Kopi      : Rp {total_harga_kopi:,} ({qty_kopi} x Rp {harga_kopi:,})")

#? B. Perkalian Angka Float (*)
total_ongkir = jarak_antar * ongkir_per_km
print(f"Total Ongkir ({jarak_antar}km)  : Rp {total_ongkir:,.0f}") # .0f menghilangkan koma di belakang

#? C. Penjumlahan (+)
sub_total = total_harga_kopi + total_ongkir
print(f"Sub-Total             : Rp {sub_total:,}")

#? D. Pengurangan (-)
total_bayar = sub_total - potongan_diskon
print(f"Diskon Promo          : -Rp {potongan_diskon:,}")
print(f"TOTAL BAYAR           : Rp {total_bayar:,}")


#%%
#? ==========================================
#? 5. BERMAIN MATEMATIKA LANGSUNG DI F-STRING
#? ==========================================
print("\n--- 👫 Split Bill (Ganti-gantian Bayar) ---")
jumlah_orang = input("Mau dibayar patungan sama berapa orang? ")
jumlah_orang = int(jumlah_orang) # Pastikan diubah ke angka!

#? E. Pembagian (/) langsung di dalam f-string!
print(f"Okelah, karena ada {jumlah_orang} orang...")
print(f"Masing-masing harus bayar patungan: Rp {total_bayar / jumlah_orang:,.2f}")
