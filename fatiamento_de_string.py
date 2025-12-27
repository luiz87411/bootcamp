nome = 'luiz henrique'
print(nome[0:3])  # 'lui' ele vai do indice 0 ate o 3, porem o 3 n entra
print(nome[4:13])  # 'henrique' ele vai do indice 4 ate o 13, porem o 13 n entra
print(nome[0:9:2])  # 'li enq' ele vai do indice 0 ate o 9, porem o 9 n entra, pulando de 2 em 2
print(nome[:9])  # 'luiz henr' ele vai do inicio ate o indice 9, porem o 9 n entra
print(nome[4:])  # 'henrique' ele vai do indice 4 ate o final
print(nome[::3])  # 'lhrq' ele vai do inicio ate o final, pulando de 3 em 3
print(nome[::-1])  # 'euqirneh ziul' ele vai do final ate o inicio, invertendo a string
print(nome[::-2])  # 'eqn iul' ele vai do final ate o inicio, pulando de 2 em 2, invertendo a string;;
print(nome[2::-1])  # 'izu' ele vai do indice 2 ate o inicio, invertendo a string
print(nome[7:2:-1])  # 'rne h' ele vai do indice 7 ate o indice 2, invertendo a string
print(nome[9:4:-1])  # 'euqnh' ele vai do indice 9 ate o indice 4, invertendo a string