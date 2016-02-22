#Estrutura de dados em python
lista = [1, 2, 3, 8, 15, 6, 4, 5]
print(lista[4])

lista = list("Rodrigo")
print(lista)

lista = list(("Rodrigo",))
print(lista)

#length
lista = [1, 2, 3, 8, 15, 6, 4, 5]
print(len(lista))

#ultimo elemento da lista
print(lista[-1])

#adicionar itens a listas
lista = [1,2,3]
lista += [4]
lista = [0] + lista

lista.append(5)
print(lista)

#deletar item na lista
del(lista[-1])
print(lista)