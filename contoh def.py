#def sapa(nama):
#    print(f"halo, {nama}")

#sapa("dimas") # "Budi" adalah argumen

## Parameter posisi
#def perkenalan(nama, hobi):
#    print(f"Nama saya {nama}, hobi saya {hobi}.")

#perkenalan("Budi", "Bermain")  # Ani masuk ke 'nama', membaca masuk ke 'hobi'

## Parameter dengan nilai bawaan
#def hitung_pajak(harga, pajak=0.1):
#    return harga * pajak

#print(hitung_pajak(100000))        # Memakai nilai default pajak (0.1)
#print(hitung_pajak(100000, 0.25))  # Nilai default diganti 0.15

## Parameter kata kunci
#def info_motor(merk, warna):
#    print(f"Motor {merk} berwarna {warna}")

#info_motor(warna="Merah", merk="Honda")  # Urutan dibalik tetap benar

#def luas_persegi(sisi):
#    luas = sisi * sisi
#    return luas

## pemanggilan fungsi
#print ("Luas persegi: %d" % luas_persegi(6))

## rumus: sisi x sisi x sisi
#def volume_persegi(sisi):
#    volume = luas_persegi(sisi) * sisi
#    return volume

#print ("Volume persegi: %d" % volume_persegi(9))

## membuat variabel global
nama = "Dimas"
kelas = "A"

def identitas():
    # ini variabel lokal
    nama = "Dimsam"
    kelas = "a"
    # mengakses variabel lokal
    print("Nama: %s" % nama)
    print("Kelas: %s" % kelas)


## mengakses variabel global
print("Nama: %s" % nama)
print("Kelas: %s" % kelas)

## memanggil fungsi identitas()
identitas()

