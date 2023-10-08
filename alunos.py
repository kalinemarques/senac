"""
Atividade: Sistema de Gerenciamento de Alunos
Objetivo: Criar um sistema gerenciamento de alunos
Requisitos: 
1.	Criar coleção alunos para armazenar informações sobre os alunos. 
Cada chave deve ser o nome do aluno o valor associado deve ser uma lista que contenha as seguintes informações: nota1, nota2, nota3 e frequência (um valor entre 0 e 100).
2.	Crie uma função chamada calcular_media que recebe as notas de um aluno como argumento e retorna a média das notas.
3.	Crie uma função chamada verificar_aprovacao que recebe a média como argumento e retorna "Aprovado" se a média for maior ou igual a 60, caso contrário, retorne "Reprovado".
4.	Crie uma estrutura que permita adicionar alunos até que o usuário escolha parar.
5.	Percorra a coleção alunos e, para cada aluno, chame as funções calcular_media e verificar_aprovacao para determinar se o aluno está aprovado ou reprovado, exibindo o resultado na tela.

Requisito extra (valendo 1 ponto no nosso jogo):
1.	Associe o aluno a outra lista, chamada frequencia, e faça ela ser levada em consideração nos requisitos 2 e 3.
2.	Faça a impressão dessa lista frequencia no requisito 5.
"""

#função para o cálculo da média:
def calcular_media (nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    return round(media,2)

#função para verificar se aprovado ou reprovado:
def verifica_aprovacao (media, frequencia):
    if media >= 60 and frequencia >=75:
        return "APROVADO(A)"
    else:
        return "REPROVADO(A)"

#função que cadastra os alunos:
def cadastra_aluno ():
    nome = input('Insira o nome do(a) aluno(a): ')

    #lista para armazenar as notas, a média e a frequência
    dados = []

    print('Insira as notas (0-100):')
    for i in range(3):
        nota = float(input(f'{i+1}ª nota: '))
        while nota <0 or nota >100 :
            nota = float(input('NOTA INVÁLIDA! Insira uma nota entre 0 e 100: '))
        dados.append(nota)

    frequencia = int(input('Insira a frequência (0-100): '))
    dados.append(frequencia)

    while frequencia <0 or frequencia >100:
            frequencia = float(input('FREQUÊNCIA INVÁLIDA! Insira uma frequência entre 0 e 100: '))
    
    media = calcular_media(dados[0], dados[1], dados[2])
    dados.append(media)

    status = verifica_aprovacao(media, dados[3])
    dados.append(status)

    #adiciona o aluno ao dicionário
    alunos [nome] = dados

    print(f'\n{nome} cadastrado(a) com sucesso!')
    print(f'A média de {nome} é {media} e sua situação é {status}!')
    print('_______________________________________________')


#função para exibir as listas
def exibe_dados(indice):
    alunosOrdemAlfabetica = sorted(alunos.keys())
    for nome in alunosOrdemAlfabetica:
        dados = alunos[nome]
        print(f'{nome}: {dados[indice]}')
    print('_______________________________________________')

#inicialização da coleção alunos
alunos = {}

#inicializa o while na opção de cadastro
parada = 1

while True:    
    #opção de cadastro
    if parada == 1:
        cadastra_aluno()

    #opção de médias
    elif parada == 2:
        print('    Relação Alunos/Média')
        #a média está na posição 4 na lista de dados
        exibe_dados(4)

    #opção de situação
    elif parada == 3:
        print('    Relação Aluno/Situação')
        #a situação está na posição 5 na lista de dados
        exibe_dados(5)

    #sair do laço
    elif parada == 4:
        print('Você saiu!')
        break

    #menu de opções
    parada = int(input('\n[1] Cadastrar novo aluno\n[2] Ver médias\n[3] Ver status\n[4] Sair\n'))

    #Verifica se opção digitada é válida
    while parada != 1 and parada !=2 and parada !=3 and parada != 4:
            parada = int(input('Opção inválida. Tente novamente: ')) 
            print()
