#Este é o jogo do pato, baseado no jogo do ganso e neste video. https://twitter.com/ivanreis1910/status/1091825650510516229
#foi um dos meus primeiros desafios de programação e demorou até algum tempo a entender como programar isto.
#A utilidade é a diversão, no entanto, isto fica velho muito rapidamente pois o desafio no jogo real é responder rápidamente
#aqui o tempo que se leva a escrever corta um pouco o desafio e também a certo ponto é só escrever o que a pessoa acima disse.

import random

players = input('Jogador0> Quantas pessoas vão jogar? ')
players = int(players)

if players < 2:
    print('Jogador0> Bruh')
    exit()
else:
    print('Jogador0> Awesome! Eu começo :D')

stspeaker = 0
turn = 0
round = 0
mensagem = 'Jogador' + str(turn) + '>'

respostas_possiveis_1 = ("O quê?", "O quê", "O que", "o que", "O que?","o que?", "o quê?", "o quê")
respostas_possiveis_3 = ("que pato?", "que Pato?", "Que Pato?", "que pato", "que Pato", "Que Pato", "Que pato?", "Que pato")
respostas_possiveis_4 = ("ah o pato", "Ah o Pato", "Ah o pato", "ah o Pato")
respostas_possiveis_0 = ("aqui vai o pato", "Aqui vai o Pato", "Aqui vai o pato", "aqui vai o Pato")
respostas_possiveis_2 = ("o pato", "O pato", "O Pato", "o Pato")
respostas_erradas_0 = ("Do you even Pato?", "Sabes sequer as regras?",
"Primeira vez, huh?", "What is WRONG with you!?")

def resp_errado():
    n_random = random.randint(0, 3)
    print(respostas_erradas_0[n_random])

while stspeaker != (players - 1):
    if turn != 1 and round == 0:
        mensagem = 'Jogador' + str(turn) + '>'
        print(mensagem, 'Aqui vai o pato')
        turn = turn + 1
        round = round + 1
    elif turn != 1 and round == 1:
        while turn != 1:
            mensagem = 'Jogador' + str(turn) + '>'
            print(mensagem, 'O quê?')
            turn = turn - 1
    elif turn != 1 and round == 2:
        if turn == 0:
            mensagem = 'Jogador' + str(turn) + '>'
            print(mensagem, 'O Pato')
            turn = turn + 1
        elif turn > 1:
            while turn != stspeaker + 1 :
                mensagem = 'Jogador' + str(turn) + '>'
                print(mensagem, 'O Pato')
                turn = turn + 1
            round = round + 1
    elif turn != 1 and round == 3:
        while turn != 1:
            mensagem = 'Jogador' + str(turn) + '>'
            print(mensagem, 'Que Pato?')
            turn = turn - 1
    elif turn != 1 and round == 4:
        if turn == 0:
            mensagem = 'Jogador' + str(turn) + '>'
            print(mensagem, 'O Pato')
            turn = turn + 1
        elif turn > 1:
            while turn != stspeaker + 1 :
                mensagem = 'Jogador' + str(turn) + '>'
                print(mensagem, 'O Pato')
                turn = turn + 1
            round = round + 1
    elif turn != 1 and round == 5:
        mensagem = 'Jogador' + str(turn) + '>'
        print(mensagem, 'Ah o Pato')
        stspeaker = stspeaker + 1
        turn = stspeaker
        round = 0
    elif turn == 1 and round == 0:
        mensagem = 'Jogador' + str(turn) + '>'
        resp0 = input(mensagem)
        if resp0 in respostas_possiveis_0:
            turn = turn + 1
            round = round + 1
        else:
            resp_errado()
            exit()
    elif turn == 1 and round == 1:
        mensagem = 'Jogador' + str(turn) + '>'
        resp1 = input(mensagem)
        if resp1 in respostas_possiveis_1:
            turn = turn - 1
            round = round + 1
        else:
            resp_errado()
            exit()
    elif turn == 1 and round == 2:
        if turn == stspeaker + 1:
            round = round + 1
        else:
            mensagem = 'Jogador' + str(turn) + '>'
            resp2 = input(mensagem)
            if resp2 in respostas_possiveis_2:
                turn = turn + 1
            else:
                resp_errado()
                exit()
    elif turn == 1 and round == 3:
        mensagem = 'Jogador' + str(turn) + '>'
        resp3 = input(mensagem)
        if resp3 in respostas_possiveis_3:
            turn = turn - 1
            round = round + 1
        else:
            resp_errado()
            exit()
    elif turn == 1 and round == 4:
        if turn == stspeaker + 1:
            round = round + 1
        else:
            mensagem = 'Jogador' + str(turn) + '>'
            resp4 = input(mensagem)
            if resp4 in respostas_possiveis_2:
                turn = turn + 1
            else:
                resp_errado()
                exit()
    elif turn == 1 and round == 5:
        mensagem = 'Jogador' + str(turn) + '>'
        resp5 = input(mensagem)
        if resp5 in respostas_possiveis_4:
            stspeaker = stspeaker + 1
            turn = stspeaker
            round = 0
        else:
            resp_errado()
            exit()
print('HELL YEAH')
