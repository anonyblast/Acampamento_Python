# 2. Um vendedor recebe por mês um salário fixo de R$1.480,00 mais uma comissão de 4,5% sobre
# as vendas realizadas. Faça um algoritmo que solicite o valor total das vendas e calcule o salário
# do funcionário naquele mês.

total_vendas = float(input('Digite o valor total das vendas R$: \n'))

print(f'O salário do funcionário no mês será de R${1480 + (total_vendas * 0.045):.2f}')