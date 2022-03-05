# 5. Crie um algoritmo para calcular um financiamento para um usuário.
# O usuário deve fornecer o valor total a ser financiado (em R$), a quantidade de prestações
# que deseja pagar e a taxa de juros ao mês vigente no momento (em %).
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

valor_inicial = float(input('Digite o valor total a financiar: \n'))
taxa_de_juros = float(input('Digite a taxa de juros (%ao mês): \n'))
qntd_parcelas = int(input('Digite a quantidade de parcelas: \n'))
coeficiente_financiamento = valor_inicial * ((taxa_de_juros / 100) / (1 - (1 + (taxa_de_juros / 100))** -qntd_parcelas))

print(f'O valor da parcela será de: {locale.currency(coeficiente_financiamento)} \nO valor total pago será de: {locale.currency(coeficiente_financiamento * qntd_parcelas)}')