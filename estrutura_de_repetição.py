# a estrutura de repetição em Python é usada para executar um bloco de código várias vezes, baseado em uma condição ou em um intervalo. Existem três principais tipos de estruturas de repetição: for, while e list comprehension.

# Exemplo de uso do for
texto = input("Digite um texto: ")
vogais =' AEIOU'
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
#o range é uma função que gera uma sequência de números, que pode ser usada para controlar o número de iterações em um loop for.
for numero in range(1, 11):
    print(numero, end=" ") # o end serve para evitar a quebra de linha após cada impressão. e me devolve um do lado do outro em vez de um em baixo do outro.


# while fuciona como uma condicional que se repete enquanto a condição for verdadeira.
