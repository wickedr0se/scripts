cont = "ya"
while cont == "ya":
	print(" ")
	o = input('''penjumlahan (+) 
pengurangan(-) 
perkalian(*) 
pembagian(/) 
perpangkatan(**) 
sisa bagi(%) 
pembagian bulat(//) = ''')
	print (" ")
	v1= int(input("Angka pertama: "))
	v2= int(input("Angka kedua: "))
	print(" ")
	if o == '+':
		print ("%d + %d = " % (v1,v2) , v1 + v2 )
	elif o == '-':
		print ("%d - %d = " % (v1,v2) , v1 - v2)
	elif o == '*':
		print ("%d * %d = " % (v1,v2) , v1 * v2)
	elif o == '/':
		print ("%d / %d = " % (v1,v2) , v1 / v2)
	elif o == '**':
		print ("%d ** %d = " % (v1,v2) , v1 ** v2)
	elif o == '%':
		print ("%d % %d = " % (v1,v2) , v1 % v2)
	elif o == '//':
		print ("%d // %d = " % (v1,v2) , v1 // v2)
	else:
		print("MATH ERROR")
	cont = input("Lagi ? (ya) ")
	cont = cont.lower()

print ("Bye")
