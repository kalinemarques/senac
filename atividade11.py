#verifica se é primo
def primo (n):
    cont = 0
    #n<=1 não é primo:
    if n<=1:
        return False
    else:
        for i in range(2,n+1):
            if n%i ==0:
                cont+= 1
        if cont == 1:
            return True
        elif cont != 1:
            return False

#calculo do mmc, inicialisando o divisor = 2 q é primo
def mmc_recursivo(a, b, divisor=2, multiplica=1):
    #se a e b são 1 mmc=1:
    if a == 1 and b == 1:
        return multiplica
    #Caso o divisor seja primo:
    if primo(divisor):
        #Enquanto um dos números seja divisível:
        while a % divisor == 0 or b % divisor == 0:
            multiplica *= divisor
            #alteração dos valores de a e b:
            if a % divisor == 0:
                a //= divisor
            if b % divisor == 0:
                b //= divisor
    return mmc_recursivo(a, b, divisor + 1, multiplica)
                
                
print("____MMC DE 2 NÚMEROS____ \n")
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

print(f"\nMMC({n1},{n2}) = {mmc_recursivo(n1,n2)}")

