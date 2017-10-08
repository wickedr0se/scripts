#Mulai
print("Kalkulator")
print(" ")
#masukan operasi
operasi = input('''Masukkan operasi 
penjumlahan (+) 
pengurangan(-) 
perkalian(*) 
pembagian(/) 
perpangkatan(**) 
sisa bagi(%) 
pembagian bulat(//) = ''')
print(" ")
#Angka masuk
var1= int(input("Masukin angka pertama: "))
var2= int(input("Masukin angka kedua: "))
#variabel
if operasi == '+':
	print (var1 + var2)
elif operasi == '-':
	print (var1 - var2)
elif operasi == '*':
	print (var1 * var2)
elif operasi == '/':
	print (var1 / var2)
