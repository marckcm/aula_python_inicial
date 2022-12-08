"""
Operador ternário em Python
"""

idade = input('Qual dua idade?\n')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)

log_user = False

if log_user:
    msg1 = 'Usuário logado'
else:
    msg1 = 'Usuário precisar logar.'

print(msg1)
