print("###################################################### ")
print(" ###                                                   ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########\n")

def kali(x) :
	hasil = 1
	for i in x :
		hasil *= i
	print("Hasil kali value list :",hasil)
	return hasil

list = [1, 2, 3, 4, 5]
print("List :",list)
kali(list)