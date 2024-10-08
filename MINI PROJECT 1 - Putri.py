# Data user
data = {
    "Putri": "015",
    "Putra": "016"
}

# Program sederhana login (Nama dan NIM)
def login():
    while True:
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        
        if nama in data and data[nama] == nim:
            print("Selamat datang. Silahkan lanjut mengisi tarif gaji.")
            break
        else:
            print("Nama atau NIM salah. Coba lagi.")

login()

# Perhitungan gaji dengan memasukkan tarif gaji beserta total jam kerja
while True:
    jam_kerja = float(input("Masukkan total jam kerja selama sebulan: "))
    tarif_kerja = float(input("Masukkan tarif kerja per jam: "))
    total_gaji = jam_kerja * tarif_kerja

    if jam_kerja > 160:
        bonus = 0.1 * total_gaji
        total_gaji += bonus
        print("Anda mendapatkan bonus 10% karena melebihi target.")
    else:
        print("Anda tidak mendapat bonus. Nominal gaji tetap.")

    print("Nominal gaji Anda:", total_gaji)

    # Membuat looping jika ingin menghitung gaji kembali
    ulang = input("Apakah Anda ingin menghitung gaji kembali? (y/n): ")

    if ulang == 'n':
        print("Terima kasih.")
        break
    else:
        print("Silahkan masukkan data kembali.")
        login()
