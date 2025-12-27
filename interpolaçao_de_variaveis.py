nome = 'Henrique'
idade = 28
profissao = 'programador'
linguagem = 'Python'

# Usando f-strings (Python 3.6+)
print(f'Meu nome é {nome}, tenho {idade} anos, sou {profissao} e gosto de programar em {linguagem}.')

# old style de formatação com o operador %
print(' Olá me chamo %s. tenho %d anos, sou %s e gosto de programar em %s.' % (nome, idade, profissao, linguagem))

# Usando o método format()
print('Meu nome é {}, tenho {} anos, sou {} e gosto de programar em {}.'.format(nome, idade, profissao, linguagem))
PI = 3.14159
print('valor de pi:{}')