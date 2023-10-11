#Encontra as raízes da equação de 2º grau

print("ax²+bx+c=0")

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - (4*a*c)

if delta < 0: 
    print(f'A equação {a}x² + {b}x + {c} = 0 não possui raízes.')
    del(a, b, c, delta)

else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)

    if delta > 0:
        print(f'A equação {a}x² + {b}x + {c} = 0 possui 2 raízes: {x1} e {x2}')

    elif delta == 0:
        print(f'A equação {a}x² + {b}x + {c} = 0 possui apenas uma raíz: {x1}')

    del(a, b, c, delta, x1, x2)
