# 7. Em muitos países é usual escrever o nome das pessoas colocando o último sobrenome primeiro.
# Crie um algoritmo que receba o nome da pessoa em três parte. Primeiro nome, sobrenomes do
# meio e último sobrenome. A seguir pergunte ao usuário se deseja escrever o nome na ordem
# normal ou invertida. Depois apresente o nome na ordem desejada. Outra coisa. Se optar pela forma 
# invertida o último sobrenome deve ser convertido para maiúsculas.

primeiro_nome = str(input('Digite o primeiro nome: '))
nomes_do_meio = str(input('Digite os nomes do meio: '))
ultimo_nome = str(input('Digite o último sobrenome: '))
escolha_ordem = int(input('Digite 1 para ordem normal ou 2 para ordem invertida: '))


if escolha_ordem == 1:
    print(f'O nome completo é {primeiro_nome} {nomes_do_meio} {ultimo_nome}.')
elif escolha_ordem == 2:
    print(f'O nome completo é {ultimo_nome.upper()}, {primeiro_nome} {nomes_do_meio}.')
else:
    print('Escolha somente as opções 1 ou 2')