# 1. Crie um algoritmo que calcule a área de um trapézio (𝐴 = (𝐵+𝑏).ℎ / 2 ). 
# Use uma calculadora para verificar se seu algoritmo está correto.

base_maior = float(input('Digite a base maior do trapézio: '))
base_menor = float(input('Digite a base menor do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

print(f'A área do trapézio é: {((base_maior + base_menor) * altura) / 2:.3f}.')