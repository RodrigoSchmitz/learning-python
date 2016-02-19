idade = int(input("Digite sua idade: "))

if(idade <= 0): 
	print("Sua idade não pode ser 0 ou menos que 0!")
elif(idade > 150):
	print("Sua idade não pode ser superior a 150!")
elif(idade >= 18):
	print("Você é maior de idade pode tirar a cnh")
else:
	print("Você é menor de idade vai ter que pegar carona com o pai")
