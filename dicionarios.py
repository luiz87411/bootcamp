pessoas = {'nome': 'luiz', ' idade': 23} #dicionario em python é uma estrutura de dados que armazena pares de chave-valor.  

print(pessoas['nome'])# Imprime o valor associado à chave 'nome'    
print(pessoas[' idade'])# Imprime o valor associado à chave 'idade'
pessoas['sexo'] = 'M'# Adiciona uma nova chave 'sexo' com o valor 'M' ao dicionário
print(pessoas)# Imprime o dicionário atualizado
pessoas['nome'] = 'maria'# Altera o valor associado à chave 'nome'
print(pessoas)
 


dados = {
    'luiz' :{'gmail': 'luiz@gmail.com', 'idade': 23, 'cargo':'gerente'},
    'maria' :{'gmail': 'maria@gmail.com', 'idade': 25, 'cargo':'analista'},
}
print(dados['luiz'])# Acessa o dicionário associado à chave 'luiz'
print(dados['maria']['cargo'])# Acessa o valor associado à chave 'cargo' dentro do dicionário de 'maria'
print(dados['luiz']['cargo'])# Acessa o valor associado à chave 'cargo' dentro do dicionário de 'luiz'