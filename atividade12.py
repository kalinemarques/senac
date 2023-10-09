class Creeper:
    def __init__(self, nome, ataque, velocidade, raioPerseguicao, raioExplosao, dano, aparicao):
        self.nome = nome
        self.ataque = ataque
        self.velocidade = velocidade
        self.raioPerseguicao = raioPerseguicao
        self.raioExplosao = raioExplosao
        self.dano = dano
        self.aparicao = aparicao
    def toString(self):
        return f"Nome: {self.nome}\nAtaque: {self.ataque}\nVelocidade: {self.velocidade}\nRaio de perseguição: {self.raioPerseguicao}\nRaio de Explosão: {self.raioExplosao}\nDano: {self.dano}%\nAparição: {self.aparicao}"

creeper = Creeper('Creeper', 'Explosão', 2, 20, 5, 0.2, 'Qualquer momento')
print(creeper.toString())
print('--------------------------------------------------')

class Esqueleto:
    def __init__(self, nome, velocidade, ataque, raioPerseguicao, dano, aparicao):
        self.nome = nome
        self.ataque = ataque
        self.velocidade = velocidade
        self.raioPerseguicao = raioPerseguicao
        self.dano = dano
        self.aparicao = aparicao
    def toString(self):
        return f"Nome: {self.nome}\nAtaque: {self.ataque}\nVelocidade: {self.velocidade}\nRaio de perseguição: {self.raioPerseguicao}\nDano: {self.dano}%\nAparição: {self.aparicao}"


esqueleto = Esqueleto('Esqueleto', 'Flechas', 5, 12, 0.05, 'Noite')

print(esqueleto.toString())

'''
#Ambos os personagens possuem:
#  um nome,
#  um ataque,
#  uma velocidade,
#  um raio de perseguição,
#  um raio de ataque,
#  um dano associado ao ataque e
#  um horário de aparição.

class Personagem:
    def __init__(self, nome, ataque, velocidade, raioPerseguicao, raioAtaque, dano, aparicao):
        self.nome = nome
        self.ataque = ataque
        self.velocidade = velocidade
        self.raioPerseguicao = raioPerseguicao
        self.raioAtaque= raioAtaque
        self.dano = dano
        self.aparicao = aparicao

    def toString(self):
        return f"Nome: {self.nome}\nAtaque: {self.ataque}\nVelocidade: {self.velocidade}\nRaio de perseguição: {self.raioPerseguicao}\nRaio de Ataque: {self.raioAtaque}\nDano: {self.dano}%\nAparição: {self.aparicao}"

creeper = Personagem('Creeper', 'Explosão', 2, 20, 5, 0.2, 'Qualquer momento')
esqueleto = Personagem('Esqueleto', 'Flexas' , 5, 12, 12, 0.05, 'Noite')

print('--------------------------------------------------')
print(creeper.toString())
print('--------------------------------------------------')
print(esqueleto.toString())

'''