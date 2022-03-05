# 10. Uma loja de materiais de construção vende produtos à vista e a prazo.
# Se o cliente paga à vista, ou em até 3 parcelas, a loja aplica o preço normal do produto.
# Porém, se o cliente desejar dividir em 4, 5 ou 6 vezes a loja aplica uma taxa de 2,5% sobre o valor
# total da compra. Crie um algoritmo que solicite ao usuário digitar o valor total da compra e depois 
# a quantidade de parcelas. Se o cliente digitar um número maior que 6 o algoritmo deve terminar dizendo que a
# quantidade de parcelas é inválida.  Se o usuário digitar um número entre 1 e 6 o algoritmo deve mostrar
# o valor das parcelas dizendo se foi ou não aplicada a taxa.
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

valor_das_compras = float(input('Digite o valor da compra: '))
parcelas = int(input('Digite a quantidade de parcelas: '))

if parcelas < 4:
    print(f'Você pagará {parcelas} de {locale.currency(valor_das_compras / parcelas)}.')
elif (parcelas >= 4 and parcelas <=6):
    print(f'Você pagará {parcelas} de {locale.currency((valor_das_compras + (valor_das_compras * 0.025)) / parcelas)}, foi aplicada uma taxa de 2,5% no valor.')
else:
    print('Você só pode pagar em até 6 vezes')