#Vendo a sintaxe dos laços de repetição

#while
x = 0
print("Entrou no while!")
while(x <= 10):
	print(x)
	x += 1
else:
	print("Saiu do while!")

#for
for caractere in "Rodrigo":
	print(caractere)

#range
print(list(range(0, 10, 2)))

#for e range
for i in range(10):
	print(i)

#break
for i in range(10):
	if(i == 5):
		print("entrou no if e fará um break")
		break
	print(i)

#continue
for i in range(10):
	if(i == 5):
		print("entrou no if e fará um continue")
		continue
	print(i)