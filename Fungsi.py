import time

hasil = 0

def instruksi():
    print("Selamat datang di kalkulator")
    time.sleep(1)
    print("Masukkan 2 angka dan pilih jenis operasi")
    time.sleep(1)

def tambah(angka_1, angka_2):
    global hasil
    hasil = angka_1 + angka_2

def kurang(angka_1, angka_2):
    global hasil
    hasil = angka_1 - angka_2

def kali(angka_1, angka_2):
    global hasil
    hasil = angka_1 * angka_2

def bagi(angka_1, angka_2):
    global hasil
    hasil = angka_1 / angka_2

instruksi()

angka_1 = int(input("masukkan angka pertama : "))
angka_2 = int(input("masukkan angka kedua : "))

operasi = int(input("Jenis operasi : \n1 = + \n2 = - \n3 = * \n4 = / \n"))

if operasi == 1:
    tambah(angka_1, angka_2)
elif operasi == 2:
    kurang(angka_2, angka_2)
elif operasi == 3:
    kali(angka_1, angka_2)
elif operasi == 4:
    if not (angka_2 == 0):
        bagi(angka_1, angka_2)
    else:
        print("jika suatu angka dibagi 0, maka hasilnya 0")
        time.sleep(1)
else:
    print("angka operasi salah!")
    time.sleep(1)

print(f"hasil : {hasil}")