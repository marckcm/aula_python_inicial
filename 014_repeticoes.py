"""
While em Python
utilizado para realizar ações enquanto uma condição for verdadeira
Requisitos: entender condições de operadores
"""

while True:         # Loop Infinito
    nome = input('Qual seu nome?\n')
    print(f'Bem vindo ao sistema {nome}')
    break           # Para o laço

# A função abaixo vai se repetir add 1 ate chegar ao numero 5 pq a partir do 6 a condição sera falsa 6 < 5
x = 0
while x < 5:
    print(x)
    x = x + 1
print('Acabou')


# a função abaixo pula o numero 3

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue            # Vai para a proxima função vai pular x = x + 1
    print(x)
    x = x + 1
print('Acabou')

x = 0   # Coluna
while x < 5:
    y = 0   # Linha
    while y < 5:
        print(f'x vale {x} e y vale {y}')
        y += 1
    x += 1          # E o mesmo que x = x + 1
print('Acabou')


