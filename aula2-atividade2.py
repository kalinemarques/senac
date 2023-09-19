print("ax²+bx+c=0")

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - (4*a*c)


x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)

print(f'As raízes da equação {a}x² + {b}x + c = 0 são {x1} e {x2}')

