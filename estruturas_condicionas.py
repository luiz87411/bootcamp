idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print(f" desculpe você não podera acessar pois {idade} nao e permitido, so com 18 anos ou acima .")


# if aninhados sao usados quando precisamos verificar multiplas condicoes dentro de uma condicao principal.

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450
if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso')
    elif saque <=(saldo + cheque_especial):
        print('saque realizado com uso do cheque especial')
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso')
    else:
        print('saldo insuficiente para saque em conta universitária')   

#if ternário

status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'O status do saque é: {status}')

# o if ternario permite escrever uma condicional em uma unica linha, tornando o código mais compacto e legível para condições simples.