# Atividade 01
# import random

# print('Foi sorteado um número entre 1 e 20 \nTente advinhar!')

# random_number = random.randint(1, 20)
# chances = []

# while len(chances) < 5:
#     luck = int(input('Escolha um número: '))
#     chances.append(luck)
#     if luck == random_number:
#         print('Acertou na mosca!')
#         break
#     elif luck > random_number:
#         print('Errou pra mais. Tente novamente!')
#     else:
#         print('Errou pra menos. Tente novamente!')
        
# print(f'Foram 5 tentativas, você jogou esses números {chances} e o número correto é {random_number}')


# Atividade 02
# select_number = int(input('Para qual número você deseja a tabuada? '))

# for i in range(1, 10):
#     print(f'{i} X {select_number} = {i * select_number}')

# select_number, x = int(input('Para qual número você deseja a tabuada? ')), 1

# while x < 10:
#     print(f'{x} X {select_number} = {x * select_number}') 
#     x += 1


# Desafio 01
candidate_1, candidate_2, candidate_3 = 1, 2, 3

ballot_box = []
default_value = 0
total_votes = 0

while True:
    voting_paper = int(input('Digite o número do candidato 1, 2 ou 3: '))
    ballot_box.append(voting_paper)
    if voting_paper == -1:
        break
    if voting_paper > 3:
        default_value += 1 
    total_votes += 1

candidate_1 = ballot_box.count(candidate_1)
candidate_2 = ballot_box.count(candidate_2)
candidate_3 = ballot_box.count(candidate_3)


print('Eleição finalizada, o resultado é: ')
print(f'Candidato 1: {candidate_1}')
print(f'Candidato 2: {candidate_2}')
print(f'Candidato 3: {candidate_3}')
print(f'Votos nulos: {default_value}')

def votes_percent(x, y):
    return int((x * (y / 100)) * 100)

if candidate_1 > candidate_2 and candidate_1 > candidate_3:
    print(f'Candidato 1 venceu com {votes_percent(total_votes, candidate_1)}% dos votos!')
elif candidate_2 > candidate_1 and candidate_2 > candidate_3:
    print(f'Candidato 2 venceu com {votes_percent(total_votes, candidate_2)}% dos votos!')
else:
    print(f'Candidato 3 venceu com {votes_percent(total_votes, candidate_3)}% dos votos!')