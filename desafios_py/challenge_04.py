# 4. Uma das dificuldades do algoritmo acima é que o tweet pode trazer “”JADE”, “Jade”, ou “jade”.
# Como utilizar o Python para contar as palavras independentemente de sua capitalização?
# Dica: continue lendo a documentação de métodos string e verá que está de graça.

texto = str(input('Digite o texto:\n').upper())
termo = str(input('Qual palavra deseja buscar no texto?\n').upper())

print(f'{termo} foi mencionada {texto.count(termo)} vezes no texto!')