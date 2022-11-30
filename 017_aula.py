"""
For in em Python
iterando strings com for
Função  range(start=0, stop, step=1 )
"""
texto = 'Python'
nova_string = ''

for n, letra in enumerate(texto):
    print(n, letra)

for letra_2 in texto:
    if letra_2 == 't':
        nova_string = nova_string + letra_2.upper()     # Vai verificar se tem a letra t percorrendo cada letra do texto
    elif letra_2 == 'h':                                # se tiver vai coloca-la em maiúsculo.
        nova_string += letra_2.upper()
    else:
        nova_string += letra_2
print(nova_string)

# Positivo
for numero in range(5, 10, 2):          # primeiro argumento do range (conta ate o número indicado) 5 inicia no nº 5
    print(numero)                       # 10 vai contar ate o número 10 e o 2 que vai pular de dois em dois números.

# Negativo
for n in range(20, 10, -1):             # primeiro argumento do range (conta ate o número indicado) 20 inicia o nº 20
    print(n)                            # 10 vai contar ate o número 11 e o -1 que vai decrescer o número.

# Achar numero divisíveis:
for n1 in range(0, 100, 8):
    print(n1)

for n2 in range(100):                # às duas funções dão o mesmo resultado.
    if n2 % 8 == 0:
        print(n2)
