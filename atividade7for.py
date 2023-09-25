#Fatorial de um número usando for

n  = int(input("Insira um número para o calculo do fatorial: "))

fatorial = 1
for i in range(1, n+1):
    if n == 0:
        fatorial = 1
    
    else:
        fatorial = i*fatorial

print(f'O fatorial de {n} é {fatorial}')


del(fatorial, n)