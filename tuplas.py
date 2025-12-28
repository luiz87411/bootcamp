# tuplas sao estrururas de dados muitos parecidas com listas  aprincipal diferenca e que tuplas sao imutaveis
# ou seja, uma vez criada uma tupla, nao e possivel modificar seus elementos (adicionar, remover ou alterar valores)
# tuplas sao definidas usando parenteses () em vez de colchetes [] 
# exemplo de criacao de uma tupla
minha_tupla = (1, 2, 3, 'quatro', 'cinco')
print(minha_tupla)
# acesso aos elementos de uma tupla
print(minha_tupla[0])  # acessa o primeiro elemento
print(minha_tupla[3])  # acessa o quarto elemento   
# tuplas suportam fatiamento (slicing) assim como listas
print(minha_tupla[1:4])  # acessa do segundo ao quarto elemento
# tuplas podem conter elementos de tipos diferentes
outra_tupla = (10, 'texto', 3.14, True)
print(outra_tupla)
# tuplas podem ser aninhadas
tupla_aninhada = (1, 2, (3, 4), (5, 6))
print(tupla_aninhada)
# descompactacao de tuplas
a, b, c, d, e = minha_tupla
print(a, b, c, d, e)
# tuplas sao uteis quando voce quer garantir que os dados nao serao modificados
# elas tambem podem ser usadas como chaves em dicionarios devido a sua imut
# capacidade
# exemplo de uso de tupla como chave em um dicionario
dicionario = {(1, 2): 'valor1', (3, 4): 'valor2'}   
print(dicionario[(1, 2)])  # acessa o valor associado a chave (1, 2)