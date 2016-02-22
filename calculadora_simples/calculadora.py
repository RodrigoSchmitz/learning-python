#calculadora simples com elif
#recebe dois valores e após o tipo da operação
#operações permitidas (+, -, *, /)

primeiro_numero = float(input("Digite o primero valor: "))
segundo_numero = float(input("Digete o segundo valor: "))
operacao = input("Informe a operacao desejada: ")

if(operacao == "+"):
	print(primeiro_numero + segundo_numero)
elif(operacao == "-"):
	print(primeiro_numero - segundo_numero)
elif(operacao == "*"):
	print(primeiro_numero * segundo_numero)
elif(operacao == "/"):
	print(primeiro_numero / segundo_numero)
else:
	print("Operação ilegal! por favor use (+ ou - ou * ou /)")