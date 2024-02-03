soma = 0
cont = 0
while True:
    n = int(input('Digite um número: [999 para PARAR]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos valores dos {cont} é de {soma}.')
