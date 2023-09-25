#Soma de todos os números de 1 até n usando while

n = int(input("Insira um número: "))

soma = 0

print(f'\nA soma de todos os pares entre 1 e {n} é ', end="")

while n>=0:
    if n%2==0:
        soma += n
    n -= 1

print(f'{soma}')

del(n, soma)