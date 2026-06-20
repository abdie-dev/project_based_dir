# Deskripsi
marker = "(...)"
placeholder = "Pada suatu hari, (...) berjalan-jalan ke (...). Di sana, (...) bertemu dengan (...) yang sedang (...). Kemudian, (...) pun pulang."
jumlah_placeholder: int = placeholder.count(marker)
print(jumlah_placeholder)

print("=== SELAMAT DATANG DI GAME CERITA INTERAKTIF ===")
print(
    f"Cerita memiliki {jumlah_placeholder}  bagian kosong yang ditandai dengan (...)",
)
print(placeholder)

daftar_kata: list = []
while True:
    input_user = input("masukan input anda: ")

    daftar_kata: list = input_user.split(",")
    # Menghapus space tidak perlu dalam daftar kata
    daftar_kata = [kata.strip() for kata in daftar_kata]

    # Error Handling:
    # apabila jumlah daftar kata melebihi atau kurang dari placeholder
    if len(daftar_kata) != jumlah_placeholder:
        print(
            f"Error: Jumlah tidak sesuai dengan slot placeholder, {jumlah_placeholder} kata yang harus di masukan"
        )
    elif len(daftar_kata) == jumlah_placeholder:
        print("Data sesuai tunggu proses selanjutnya...")
        break

bagian_cerita = placeholder.split(marker)
final_cerita = str = ""
print(bagian_cerita)
for i in range(0, jumlah_placeholder):
    final_cerita = final_cerita + bagian_cerita[i] + daftar_kata[i]
akhir_cerita = final_cerita + bagian_cerita[jumlah_placeholder]

print("\n=== CERITA ANDA ===")
print(akhir_cerita)

# function HITUNG JUMLAH PLACEHOLDER
