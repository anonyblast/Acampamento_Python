# Atividade 01
ethanol_value = float(input('Digite o preço do Etanol: '))
gas_value = float(input('Digite o preço da Gasolina: '))
new_value_percent = 100 * ethanol_value / gas_value

print(f'O preço do etanol está {new_value_percent:.2f}% do preço da gasolina.')

if new_value_percent >= 70:
    print('ABASTEÇA COM GASOLINA!!!')
else:
    print('ABASTEÇA COM ETANOL!!!')


# Atividade 02
grade_01 = float(input('Digite a nota da primeira prova: '))
grade_02 = float(input('Digite a nota da segunda prova: '))
grade_03 = float(input('Digite a nota da terceira prova: '))
student_avarage = (grade_01 + grade_02 + grade_03) / 3

print(f'Sua média foi de: {student_avarage:.2f}')

if student_avarage >= 70:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')


# Desafio Extra
purchase_value = float(input('Digite o valor da compra: '))
installments = int(input('Digite a quantidade de parcelas: '))

if installments < 4:
    print(f'Você pagará {installments} de R${purchase_value / installments:.2f}.')
elif (installments >= 4 and installments <=6):
    print(f'Você pagará {installments} de R${(purchase_value + (purchase_value * 0.025)) / installments:.2f}, foi aplicada uma taxa de 2,5% no valor.')
else:
    print('Você só pode pagar em até 6 vezes')