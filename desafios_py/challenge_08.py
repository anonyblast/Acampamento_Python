# 8. Em um determinado país muito distante evita-se ao máximo construir telhados com inclinação
# (α)inferior a 22°. Crie um algoritmo que receba o valor da altura vertical de um telhado (b) e seu
# comprimento (c) mostre a inclinação e diga se a inclinação está adequada. Se não estiver, indique
# em quantos centímetros a altura vertical (b) precisa ser aumentada para atingir a inclinação
# adequada.
# Dica: use a biblioteca math para calcular funções trigonométricas. Lembre-se que todas as funções
# trigonométricas PRECISAM receber ângulos em radianos. Da mesma forma as funções trigonométricas 
# inversas fornecerão ângulos em radianos. Use a função math.degrees() para convertê-los em graus.
import math

comprimento_telhado = float(input('Digite o comprimento do telhado (c): '))
altura_telhado = float(input('Digite a altura do telhado (b): '))
inclinacao = math.degrees((altura_telhado / comprimento_telhado))

if inclinacao > 22:
    print(f'A inclinação do telhado é de: {inclinacao:.2f}°. A inclinação está adequada.')
else:
    print(f'Esta inclinação está inadequada, acrescente {(22 - inclinacao):.2f} na altura.')