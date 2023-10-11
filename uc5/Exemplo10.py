from random import randint

listaAleatoria = []
tamanhoDaLista = int(input("Insira o tamanho da lista aleatória: "))

for i in range(tamanhoDaLista):
    listaAleatoria.append(randint(20,100))

def soma(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma(lista[1:])
    
print(f'Os elementos da lista são {listaAleatoria}, a soma dos elementos da lista é {soma(listaAleatoria)}.')
