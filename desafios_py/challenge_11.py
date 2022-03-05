# 11. Uma aplicação interessante de programação é a de caixas eletrônicos que precisam fornecer
# valores inteiros de notas em função do valor de saque que o cliente deseja.
# Por exemplo: se você quiser sacar R$190,00 o caixa poderia fornecer uma nota de R$100, uma
# de R$50,00 e duas de R20,00. Considere que um caixa eletrônico trabalha com notas de R$100,00, R$50,00, 
# R$20,00 e R$10,00. Crie um algoritmo que receba o valor do saque desejado pelo cliente e retorne
# quantas notas precisarão ser fornecidas de cada valor. 
# Atenção você deve avisar o cliente se o valor digitado não puder ser fornecido pelo caixa.

print('Seja bem-vindo cliente, hoje temos notas de R$100, 50, 20 e 10 em nosso caixa.')

while True:
    valor_desejado = int(input('Qual valor você deseja sacar? '))

    notas_100 = int(valor_desejado // 100)
    valor_desejado -= notas_100 * 100

    notas_50 = int(valor_desejado // 50)
    valor_desejado -= notas_50 * 50

    notas_20 = int(valor_desejado // 20)
    valor_desejado -= notas_20 * 20

    notas_10 = int(valor_desejado // 10)
    valor_desejado -= notas_10 * 10

    if valor_desejado != 0:
        print('O valor solicitado não pode ser fornecido.')
    else:
        print(f'Você receberá {notas_100} notas de 100, {notas_50} notas de 50, {notas_20} notas de 20 e {notas_10} notas de 10')
    exit()