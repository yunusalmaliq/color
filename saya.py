def luas_lingkaran(r):
	luas = phi*(2**r)
	return luas 
	
	
def keliling_lingkaran (r):
	keliling =2*phi*r
	return keliling 
	
	
def option():
		print("pilih salah satu dari tiga fungsionalitas berikut:")
		print("1. mencari luas lingkaran")
		print("2. mencari keliling lingkaran")
		print("3. keluar dari program")
		pilihan=int(input("masukan pilihan anda:"))
		return pilihan
		
phi = 3.14	
pilihan =True
while (pilihan <3):
	pilihan =option()
	if (pilihan ==1):
		r=int(input("Masukan jari-jari:"))
		l=luas_lingkaran (r)
		print("luas_lingkaran:%.2f"%(l))
	elif(pilihan==2):
		r=int(input("Masukan jari-jari:"))
		k=keliling_lingkaran(r)
		print("keliling_lingkaran:%.2f"%(k))
	
	
	