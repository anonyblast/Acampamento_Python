# 6. Você vai a um clube que dá desconto de 10% no consumo dos clientes vip. Crie um algoritmo
# que identifique se o cliente é vip pela resposta sim ou não e depois solicite o valor do consumo.
# A seguir mostre o valor a ser pago dependendo do tipo de cliente
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

tipo_cliente = str(input('O cliente é vip (sim/não)? '))
valor_consumo = float(input('Digite o valor do consumo: '))

if tipo_cliente.upper() == 'SIM':
    print(f'O valor a pagar será de {locale.currency(valor_consumo - (valor_consumo * 0.1))}')
elif tipo_cliente.upper() != 'SIM' and tipo_cliente.upper() != 'NÃO':
    print('Por favor, digite apenas as palavras sim ou não')
else:
    print(f'O valor a pagar será de {locale.currency(valor_consumo)}.')