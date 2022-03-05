# 9. Gerar números aleatórios é muito útil em programação por diversos motivos. A natureza
# tem comportamento aleatório e, portanto, a geração de números aleatórios é bastante usada
# em pesquisa científica, simuladores e jogos. Agora você usará o Python para criar um
# pequeno jogo de adivinhação com o usuário. Importe a biblioteca random do Python
# Depois use a função random.randint(a,b) para gerar um número aleatório entre ‘a’ e ‘b’. Onde
# ‘a’ e ‘b’ serão limites definidos pelo usuário. Depois peça a dois jogadores para tentarem
# acertar o número gerado. Em seguida o algoritmo deve mostrar qual dos jogadores chegou mais perto 
# de acertar o número e qual a margem de erro do mesmo. Dica: vamos simplificar as coisas por enquanto e,
# se der empatem, diga que o jogador 1 venceu.
import random

limite_inferior = int(input('Qual será o limite inferior do sorteio? '))
limite_superior = int(input('Qual será o limite superior do sorteio? '))
numero_aleatorio = random.randint(limite_inferior, limite_superior)

print('Foi sorteado um número... \nAgora vamos aos palpites...')
jogador_1 = int(input('Jogador 1, qual número eu sorteei? '))
jogador_2 = int(input('Jogador 2, qual número eu sorteei? '))


if (jogador_1 < limite_inferior or jogador_1 > limite_superior) or (jogador_2 < limite_inferior or jogador_2 > limite_superior):
    print(f'Apenas números entre {limite_inferior} e {limite_superior}')
elif jogador_1 == numero_aleatorio or jogador_2 == numero_aleatorio:
    print(f'Quem chutou {numero_aleatorio} acertou na mosca!')
elif (jogador_1 == numero_aleatorio) and (jogador_2 == jogador_1):
    print('Empate!')
elif ((numero_aleatorio - 3) <= jogador_1 <= (numero_aleatorio + 3)):
    print(f'O jogador 1 venceu! Foi sorteado o número {numero_aleatorio} e ele disse {jogador_1}, errou por {numero_aleatorio - jogador_1}.')
elif ((numero_aleatorio - 3) <= jogador_2 <= (numero_aleatorio + 3)):
    print(f'O jogador 2 venceu! Foi sorteado o número {numero_aleatorio} e ele disse {jogador_2}, errou por {numero_aleatorio - jogador_2}.')
else:
    print(f'Tentem novamente.')