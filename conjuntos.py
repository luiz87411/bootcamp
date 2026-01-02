#criando sets e como funciona
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# Operações com conjuntos union, interseção e diferença
uniao = conjunto1 | conjunto2
intersecao = conjunto1 & conjunto2
diferenca = conjunto1 - conjunto2

print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)

#métodos  de sets
conjunto1.add(5)
print("Após adicionar 5 ao conjunto1:", conjunto1)
conjunto1.remove(2)
print("Após remover 2 do conjunto1:", conjunto1)
conjunto1.discard(10)  # Não gera erro se o elemento não existir
print("Após tentar descartar 10 do conjunto1:", conjunto1)
tamanho = len(conjunto1)
print("Tamanho do conjunto1:", tamanho)     
conjunto1.clear()
print("Após limpar o conjunto1:", conjunto1)    
