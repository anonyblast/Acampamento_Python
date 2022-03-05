# 3. Um algoritmo fundamental no Twitter é utilizado para identificar menções a empresas,
# pessoas e assuntos em geral. Crie um algoritmo que receba como entrada um texto e solicite 
# ao usuário digitar a palavra que deve ser procurada e contada no texto.
# Dica: leia a documentação de strings do Python em https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods
# ou qualquer outro artigo sobre Strings em Python, ou pesquise direto no Google e verá que isso é
# bem mais fácil do que parece.

texto = str(input('Digite o texto:\n'))
termo = str(input('Qual palavra deseja buscar no texto?\n'))

print(f'{termo} foi mencionada {texto.count(termo)} vezes no texto!')