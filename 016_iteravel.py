"""
Inteirando strings Utilizando o lasso While

atalho 'crtl + /' vira comentário a area selecionada

"""

frase = """
Ministro entendeu que PL agiu de forma irresponsável ao questionar
urnas e aplicou multa para todos os partidos da coligação.
PP e Republicanos informaram que discordam totalmente do
questionamento feito pelo PL.
"""

tamanho_do_texto = len(frase)
print(f'{tamanho_do_texto} Palavras')
contador = 0
nova_string = ''

perg_user = input('Qual letra vc quer em maiuscula: ')

while contador < tamanho_do_texto:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == perg_user:
        nova_string += perg_user.upper()
    else:
        nova_string += letra
    contador += 1


print(nova_string)
