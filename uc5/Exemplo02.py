#calcula o 0 de uma função afim

print("ax+b=0")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))

x = -b/a

print(f'O zero da função {a}x + {b} = 0 é {x}.')

del(a, b, x)
