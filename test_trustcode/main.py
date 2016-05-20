import csv
from operator import itemgetter
#Fiquei com uma duvida na hora de listar os municipios do estado pois a busca pode voltar mais que um estado então listaria todos os municipios do estado ou o usuario escolheria um estado. implementei como se o usuario escolhesse um estado depois da busca

#busa otimizada decidi importar o arquivo csv e ordenar por nome do estado quando o arquivo fosse executado assim so faria a ordenacao uma vez nao consumindo muito desempenho e podendo utilizar uma busca binaria que e muito mais performada do que uma busca linear
listaMunicipios = csv.reader(open('Municipio.csv'), delimiter = ',')
listaMunicipios = sorted(listaMunicipios, key=itemgetter(1))

def buscaMunicipiosOtimizada(municipio):
	inicio, fim, tentativa = 0, len(listaMunicipios), 1
	while tentativa:
		meio = (inicio + fim) // 2
		print(inicio)
		print(meio)
		print(fim)
		if(municipio == listaMunicipios[meio][1]):
			tentativa = 0
			return listaMunicipios[meio]
		else:
			if(len(municipio) < len(listaMunicipios[meio][1])):
				menor = municipio
			else:
				menor = listaMunicipios[meio][1]
			for i in range(len(menor)):
				if(municipio[i] != listaMunicipios[meio][1][i]):
					if(municipio[i] < listaMunicipios[meio][1][i]):
						fim = meio
						break
					else:
						inicio = meio
						break
		
#metodos da entidade estado
def listarEstados():
	lista = []
	arq = csv.reader(open('Estados.csv'), delimiter = ',')
	for [id,estado,uf,regiao] in arq:
		lista.append([id,estado,uf,regiao])
	return lista

def municipiorEstadoPeloNome(nomeEstado):
	lista = []
	arq = csv.reader(open('Estados.csv'), delimiter = ',')
	for [id,estado,uf,regiao] in arq:
		if(nomeEstado.upper() == estado[0:len(nomeEstado)].upper()):
			lista.append([id,estado,uf,regiao])
	return lista

def buscarEstadoPeloUf(municipio):
	arq = csv.reader(open('Estados.csv'), delimiter = ',')
	for [id,estado,uf,regiao] in arq:
		if(municipio[2].upper() == uf.upper()):
			return [id,estado,uf,regiao]

#metodos da entidade municipios
def listarMunicipios():
	lista = []
	arq = csv.reader(open('Municipio.csv'), delimiter = ',')
	for [id,municipio,uf] in arq:
		lista.append([id,municipio,uf])
	return lista
		


def listarMunicipiosPeloEstado(estado):
	lista = []
	arq = csv.reader(open('Municipio.csv'), delimiter = ',')
	for [id,municipio,uf] in arq:
		if(estado[2].upper() == uf.upper()):
			lista.append([id,municipio,uf])
	return lista

def buscarMunicipiosPeloNome(nomeMunicipio):
	lista = []
	arq = csv.reader(open('Municipio.csv'), delimiter = ',')
	for [id,municipio,uf] in arq:
		if(nomeMunicipio.upper() == municipio[0:len(nomeMunicipio)].upper()):
			estado = buscarEstadoPeloUf([id,municipio,uf])
			lista.append([id,municipio,estado[1]])
	return lista

#main do programa
#variavel para identificar 'sessao do programa'
programa = True

#enquanto o programa estiver 'aberto' nao fechar terminal
while(programa):

	print("Digite 1 para listar estados \nDigite 2 para listar municipios \nDigite 3 para pesquisar estado pelo nome \nDigite 4 para pesquisar municipio pelo nome \nDigite 5 para fazer uma busca otimizada \nDigite 6 para sair")

	opcao = input("Escolha uma opcao: ")

	if(opcao.isdigit()):
		opcao = int(opcao)

		#selecionando opcao de acordo com o digitado no terminal
		if(opcao == 1):
			lista = listarEstados()

			for [id,estado,uf,regiao] in lista:
				print(str(estado) + " | " + str(uf) + " | " + str(regiao))

			print("\n")

		elif(opcao == 2):
			lista = listarMunicipios()

			for [id,municipio,uf] in lista:
				print(str(municipio) + " | " + str(uf))

			print("\n")

		elif(opcao == 3):
			nomeEstado = input("Digite o nome do estado: ")

			if(len(nomeEstado) >= 3):
				estado = buscarEstadoPeloNome(nomeEstado)

				if(len(estado) != 0):	
					if(len(estado) > 1):
						print("Foram encontrados mais de um estado com termo da busca por favor escolha o estado desejado")

						i = 0
						for [id,nomeEstado,uf,regiao] in estado:
							print(str(i) + " | " + str(nomeEstado) + " | " + str(regiao))
							i = i + 1
						invalido = True
						while invalido:
							item = input("Escolha o estado usando o numero que aparece na primeira coluna: ")
							if(item.isdigit()):
								item = int(item)
								if(item < len(estado)):
									estado = estado[item]
									invalido = False
								else:
									print("ecolha uma opcao valida")
							else:
								print("ecolha uma opcao valida")

					else:
						estado = estado[0]
						print(str(estado[1]) + " | " + str(estado[3]))

					print("Voce deseja listar os municipios desse estado?")
					listar = input("Digite 's' para sim e 'n' para nao: ")

					if(listar == "s"):
						municipios = listarMunicipiosPeloEstado(estado)

						for [id,municipio,uf] in municipios:
							print(str(municipio) + " | " + str(uf))

				else:
					print("Nao foi encontrado estado com o termo da busca")
			else:
				print("Voce deve informar pelo menos 3 caracteres")
			print("\n")

		elif(opcao == 4):
			nomeMunicipio = input("Digite o nome do municipio: ")

			if(len(nomeMunicipio) >= 3):
				municipios = buscarMunicipiosPeloNome(nomeMunicipio)

				if(len(municipios) != 0):
					for [id,municipio,estado] in municipios:
						print(str(municipio) + " | " + str(estado))

				else:
					print("Nao foi encontrado municipios com o termo da busca\n")
			else:
				print("Voce deve informar pelo menos 3 caracteres")
				print("\n")

		elif(opcao == 5):
			nomeMunicipio = input("Digite o nome do municipio: ")

			if(len(nomeMunicipio) >= 3):
				municipios = buscarMunicipiosPeloNome(nomeMunicipio)

				if(len(municipios) != 0):
					for [id,municipio,estado] in municipios:
						print(str(municipio) + " | " + str(estado))

				else:
					print("Nao foi encontrado municipios com o termo da busca\n")
			else:
				print("Voce deve informar pelo menos 3 caracteres")
				print("\n")


		elif(opcao == 6):
			#desligando programa ele saira do while portando fechara a execucao no terminal
			programa = False
			
		else:
			print("ecolha uma opcao valida")
	else:
		print("ecolha uma opcao valida")