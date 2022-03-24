# Atividade 01
# s0 = float(input('Digite a posição inicial : '))
# v = float(input('Digite a velocidade (m/s) : '))

# print('Tabela posição X tempo para este móvel')
# print('Tempo (s) --- Posição (m)')
# for t in range(1, 26):
#     print(f'{t:<9.2f} --- {s0 + v * t:>11.2f}') # Reservar espaço para alinhamento, argumento :9.2f

# Atividade 02
from random import randint

print('Gerador de jogos da Mega-Sena')

dozens = int(input('Digite a quantidade de dezenas que deseja apostar (6 - 15) : '))
game_sheet = []

if dozens < 6 or dozens > 15:
    print('Jogue novamente, somente números entre 6 e 15')
    exit()
else: 
    for i in range(dozens):
        aleatory_dozen = randint(1, 60)
        if aleatory_dozen not in game_sheet:
            game_sheet.append(aleatory_dozen)
        
game_sheet.sort()
print(" - ".join(str(e) for e in game_sheet))