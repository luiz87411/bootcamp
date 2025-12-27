curso = (' carro').strip()  # Remove espaços em branco no início e no fim
print(curso.center(10, '-'))  # Centraliza a string com '-' preenchendo os lados os numeros que dizem o tamanho total da string
print('*'.join(curso))  # Junta cada caractere da string com '*'
print(curso.upper())  # Converte todos os caracteres para maiúsculo
print(curso.lower())  # Converte todos os caracteres para minúsculo
print(curso.split())  # Divide a string em uma lista de palavras
print(curso.replace('carro', 'moto'))  # Substitui 'carro' por 'moto'
print('curso' in curso)  # Verifica se 'curso' está na string
print(curso.find('rro'))  # Retorna o índice da primeira ocorrência de 'rro' 
print(curso.lstrip())  # Remove espaços em branco no início da string
print(curso.rstrip())  # Remove espaços em branco no fim da string