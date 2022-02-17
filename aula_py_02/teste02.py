# Conteúdo praticado durante a segunda aula de Python
# import math
# import locale


# Conteúdo demonstrado pelo instrutor
# Objetivo : Criar um algoritmo que calcule a velocidade de um corpo com base no deslocamento e o tempo

# deslocamento = float(input('Digite o deslocamento do corpo (m) :'))
# tempo = float(input('Digite o tempo(s) :'))

# print(f'A velocidade é : {(deslocamento / tempo):.2f} m/s')

# print(math.cos(math.radians(60)))
# print(f'O fatorial de 12 é : {math.factorial(12)}')


# Atividade 01
# dias = int(input('Insira a quantidade de dias :'))
dias = 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f'O ano tem {dias} dias, {horas} horas, {minutos} minutos e {segundos:.2f} segundos')


# Atividade 02
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print(f'O IMC é: {(peso/(altura**2)):.2f}')


# Atividade 03
valor_total = float(input("Insira aqui o valor da compra: "))

total_notas_50 = int(input('Insira a quantidade de notas de R$50: '))
total_notas_20 = int(input('Insira a quantidade de notas de R$20: '))
total_notas_10 = int(input('Insira a quantidade de notas de R$10: '))
total_notas_5 = int(input('Insira a quantidade de notas de R$5: '))

valor_soma_notas = (50 * total_notas_50) + (20 * total_notas_20) + (10 * total_notas_10) + (5 * total_notas_5)

print(f'Prezado Cliente, o valor da sua compra ficou em R${valor_total}, você me entregou R${valor_soma_notas} e o seu troco é de R$ {valor_soma_notas - valor_total}')