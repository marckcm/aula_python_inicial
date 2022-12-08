"""
Condicionais usando o or
"""


nome = input('Qual o seu nome?')
print(nome or None or False or 0 or 'Você não digitou nada')

print('\U0001f310'*40)

a = 0               # false
b = None            # false
c = {}              # false
d = False           # false
e = 'marcelo'       # verdadeiro

variavel = a or b or c or d or e

# Vai passando as condicionais ate achar a condicional verdadeira e mantela
print(variavel)
