'''frutas = ["maçã", "banana", "laranja"]
print(frutas)
print(frutas[0])  # Acessa o primeiro elemento
print(frutas[-1]) # Acessa o último elemento

letras = list("Python") # Converte uma string em uma lista de caracteres
print(letras)# Imprime a lista de letras
numeros = list(range(10))# Cria uma lista de números de 0 a 9
print(numeros)
  #lista aninhadas como funcionam sao  basicamente listas dentro de listas
matriz = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
print(matriz[-1][-1]) # Acessa o último elemento da última lista
print(matriz[0][1])  # Acessa o segundo elemento da primeira lista
print(matriz[1])     # Acessa a segunda lista completa


# fatiamento de listas
lista = list('python')
print(lista)
lista[2:] # Acessa do índice 2 até o final
lista[:2] # Acessa do início até o índice 2 (não inclusivo)
lista[1:3] # Acessa do índice 1 até o índice 3 (não inclusivo)
lista[:]  # Acessa toda a lista
lista[0:3:2] # Acessa do índice 0 ao 3, pulando de 2 em 2
lista[::] # Acessa toda a lista, pulando de 1 em 1
lista[::-1] # Acessa a lista de trás para frente
'''

# listas usando o for 
carros = ["Ford", "Volvo", "BMW"]

for carro in carros:
    print(carro)

#FUNÇAO NUMERATE COMO FUCION ? A FUNÇAO ENUMERATE RETORNA UM OBJETO ENUMERATE QUE CONTÉM PARES DE ÍNDICE E VALOR DA LISTA FORNECIDA. ISSO PERMITE ITERAR SOBRE A LISTA E TER ACESSO TANTO AO ÍNDICE QUANTO AO VALOR DOS ELEMENTOS.
for indice, carro in enumerate(carros):
    print(indice, carro)

# METODOS DE LISTAS
lista=[]
lista.append("maçã") # Adiciona um elemento ao final da lista
lista.append("banana")
lista.append(['carro']) # Adiciona uma lista dentro da lista
print(lista)

# e tem o clear que limpa a lista
lista.clear()
print(lista) # ele vai retornar uma lista vazia []

# tem o metodo copy que cria uma copia da lista
frutas = ["maçã", "banana", "laranja"] # aonde podemos usar o metodoc copy quando queremos criar uma copia de uma lista sem alterar a original
copia_frutas = frutas.copy()
print(copia_frutas)


# tem o metodo count que conta quantas vezes um elemento aparece na lista
numeros = [1, 2, 2, 3, 4, 2]
contagem = numeros.count(2)
print(contagem) # ele vai retornar 3 porque o numero 2 aparece 3 vezes

# tem o metodo extend que adiciona os elementos de uma lista a outra lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1) # ele vai retornar [1, 2, 3, 4, 5, 6] 

# tem o metodo index que retorna o índice do primeiro elemento encontrado na lista
frutas = ["maçã", "banana", "laranja"]
indice_banana = frutas.index("banana")
print(indice_banana) # ele vai retornar 1 porque o índice da banana é 1

# tem o metodo pop que remove e retorna o elemento no índice especificado
numeros = [1, 2, 3, 4, 5]
ultimo_numero = numeros.pop() # se n passar o indice ele remove o ultimo elemento
print(ultimo_numero) # ele vai retornar 5
print(numeros) # ele vai retornar [1, 2, 3, 4]  

# tem o metodo remove que remove a primeira ocorrência do valor especificado
frutas = ["maçã", "banana", "laranja", "banana"]
frutas.remove("banana")
print(frutas) # ele vai retornar ['maçã', 'laranja', 'banana']

# tem o metodo reverse que inverte a ordem dos elementos na lista
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros) # ele vai retornar [5, 4, 3, 2, 1]

# tem o metodo sort que ordena os elementos da lista
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros) # ele vai retornar [1, 2, 5, 5, 6, 9]

# tem o metodo sorted que retorna uma nova lista ordenada sem modificar a original
numeros = [5, 2, 9, 1, 5, 6]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados) # ele vai retornar [1, 2, 5, 5, 6, 9]
print(numeros) # ele vai retornar [5, 2, 9, 1, 5, 6] 