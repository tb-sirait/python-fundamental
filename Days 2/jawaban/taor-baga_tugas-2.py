# "Hari ke-2: Fundamental Phyton"

print("DAY 2 - LVL 1")
nama = "Taor Baga"
jurusan = "Ilmu Komputer"
angkatan = 20
umur = 21
asal_daerah = "Jakarta"
money_amount = 99999999999999999999999
isMahasiswa = True
isAlien = False
print(nama, jurusan, angkatan, umur, asal_daerah, money_amount, isMahasiswa, isAlien)
print("")

print("DAY 2 - LVL 2")
# 1
print("Tipe data Nama: ",type(nama))
print("Tipe data Jurusan: ",type(jurusan))
print("Tipe data Angkatan: ",type(angkatan))
print("Tipe data Umur: ",type(umur))
print("Tipe data Asal Daerah: ",type(asal_daerah))
print("Tipe data Money Amount: ",type(money_amount))
print("Tipe data isMahasiswa: ",type(isMahasiswa))
print("Tipe data isAlien: ",type(isAlien))
print("")

# 2
print("Jumlah karakter Nama: ",len(nama))
print("")

# 3
num_one = 5
num_two = 4
tot = num_two + num_one
diff = num_one - num_two
mlt = num_one * num_two
remainder = num_two % num_one
exp = num_one**num_two
fld = num_one//num_two

print("1. Penjumlahan num one dan num two: ", tot)
print("2. Pengurangan num two dan num one: ", diff)
print("3. Perkalian num two dan num one: ", mlt)
print("4. Pembagian num one dan num two: ", diff)
print("5. modulus num one dan num two: ", remainder)
print("6. eksponensial num one dan num two: ", exp)
print("7. floor division num one dan num two: ", fld)
print("")

# 4
name = input("Siapa nama mu: ")
age = input("Berapa umur anda: ")
asal = input("Darimana asalmu: ")
print("")
print("Nama mu ", name, " dengan umur ", age, " berasal dari daerah ", asal)
print("")

# 5
rad = int(input("Masukkan nilai jari-jari: "))
phi = 3.14
area_of_circle = 0.5 * phi * rad * rad
circum_of_circle = 2 * phi * rad
print("Lingkaran dengan jari-jari: ", rad)
print("Menghasilkan nilai luas sebesar: ", area_of_circle)
print("Dan, menghasilkan nilai keliling sebesar: ", circum_of_circle)
print("")

#6
help('random thing')