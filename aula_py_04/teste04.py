# Conteúdo praticado durante a quarta aula de Python

# Conteúdo demonstrado pelo instrutor
# n1 = float(input('Digite o valor da primeira nota: '))
# n2 = float(input('Digite o valor da segunda nota: '))
# n3 = float(input('Digite o valor da terceira nota: '))
# frequencia = int(input('Digite a frequência do aluno(%): '))
# media = (n1 + n2 + n3) / 3

# if media >= 70 and frequencia >= 75:
#     print(f'Aprovado : {media} e {frequencia}')
# else:
#     print(f'Reprovado : {media} e {frequencia}')
# print("Marca : L'oreal") Não precisa escapar o apostrofo

# Prática 1
# nome_1 = str(input('Digite o primeiro nome: '))
# nome_2 = str(input('Digite o segundo nome: '))
# nome_3 = str(input('Digite o terceiro nome: '))

# print('Certo') if nome_1 < nome_2 < nome_3 else print('Errado')

# Prática 2
# Entrar com notas e frequencia e mostrar média e conceito
# n1 = float(input('Digite o valor da primeira nota: '))
# n2 = float(input('Digite o valor da segunda nota: '))
# n3 = float(input('Digite o valor da terceira nota: '))
# frequencia = int(input('Digite a frequência do aluno(%): '))
# media = (n1 + n2 + n3) / 3

# if frequencia < 75:
#   print("Aluno Reprovado por frequência.")
# elif media < 40:
#   print("Você foi reprovado com conceito E.")
# elif media < 70:
#   print("Você está no exame especial seu conceito é D")
# elif media < 80:
#   print("Você está aprovado com conceito C")
# elif media < 90:
#   print("Você está aprovado com conceito B")
# else:
#   print("Você é estrela conceito A!")


# # Atividade 01 - Enviada na Plataforma de Ensino
# jogador_1 = str(input('Jogador 1 - Joga? ')).strip()
# jogador_2 = str(input('Jogador 2 - Joga? ')).strip()

# if jogador_1 == jogador_2:
#     print('Empate')
# elif jogador_1.lower() == 'r' and jogador_2.lower() == 't':
#     print('Jogador 1 venceu!')
# elif jogador_2.lower() == 'r' and jogador_1.lower() == 't':
#     print('Jogador 2 venceu!')
# elif jogador_1.lower() == 't' and jogador_2.lower() == 'p':
#     print('Jogador 1 venceu!')
# elif jogador_2.lower() == 't' and jogador_1.lower() == 'p':
#     print('Jogador 2 venceu!')
# elif jogador_1.lower() == 'p' and jogador_2.lower() == 'r':
#     print('Jogador 1 venceu!')
# elif jogador_2.lower() == 'p' and jogador_1.lower() == 'r':
#     print('Jogador 2 venceu!')
# else:
#     print('Digite apenas r, t, p')


# Atividade 01
# import random

# arr = ['r', 'p', 't']
# dicValues = {
#     'r' : 'pedra',
#     'p' : 'papel',
#     't' : 'tesoura'
# }

# while True:
#     jogador_1 = str(input('Jogador 1 - Joga? ')).strip()
#     jogador_2 = random.choice(arr)

#     if jogador_1 == jogador_2:
#         print('Empate')
#     elif jogador_1.lower() == 'r' and jogador_2.lower() == 't':
#         print(f'Jogador 1 venceu! {dicValues[jogador_1]}')
#     elif jogador_2.lower() == 'r' and jogador_1.lower() == 't':
#         print(f'Jogador 2 venceu! {dicValues[jogador_2]}')
#     elif jogador_1.lower() == 't' and jogador_2.lower() == 'p':
#         print(f'Jogador 1 venceu! {dicValues[jogador_1]}')
#     elif jogador_2.lower() == 't' and jogador_1.lower() == 'p':
#         print(f'Jogador 2 venceu! {dicValues[jogador_2]}')
#     elif jogador_1.lower() == 'p' and jogador_2.lower() == 'r':
#         print(f'Jogador 1 venceu! {dicValues[jogador_1]}')
#     elif jogador_2.lower() == 'p' and jogador_1.lower() == 'r':
#         print(f'Jogador 2 venceu! {dicValues[jogador_2]}')
#     else:
#         print('Símbolos inválidos foram digitados')

#     print(('-' * 30) + '+')
#     continuar_jogo = str(input('Deseja continuar o jogo? s/n ')).strip()
#     print(('-' * 30) + '+')

#     if continuar_jogo == 'n':
#         exit()


# Atividade 02
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

print('+' + ('-' * 9) + ' Bar Tô na Facul ' + ('-' * 10) + '+')
print(('-' * 10) + ' Nosso Cardápio ' + ('-' * 12))
print('n° - | O que? ' + ('-' * 15) + ' | Preço-')
print('1 -- | Pinga ' + ('-' * 16) + ' | 1.20--')
print('2 -- | Pinga dedão ' + ('-' * 10) + ' | 3.00--')
print('7 -- | Torresmo ' + ('-' * 13) + ' | 1.50--')
print('9 -- | Dobradinha ' + ('-' * 11) + ' | 2.00--')
print('11 - | Mandi frita porc ' + ('-' * 5) + ' | 12.00-')
print('+' + ('-' * 36) + '+')

pedido = str(input('Digite seu pedido: '))
quantidade = int(input('Digite a quantidade: '))

dicCardapio = {
    '1' : 1.20,
    '2' : 3,
    '7' : 1.50,
    '9' : 2,
    '11' : 12
}

if pedido in dicCardapio:
    print(f'Sua conta ficou em {locale.currency(dicCardapio[pedido] * quantidade)}')
else:
    print('Digite apenas os números que estiverem no cardápio')