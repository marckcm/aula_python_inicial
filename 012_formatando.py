"""
Formatando valores com modificadores

:s - texto (string)
:d - inteiro (int)
:f - numero de ponto flutuante (float)
:.(numero) f - quantidade de casas decimais (float)
:(caractere)(< (esquerda) ou >(direita) ou ^(centro))(quantidade) (tipo - s, d ou f)
"""

num_1 = 5
num_2 = 20
div = num_1/num_2
print('{:.2f}'.format(div))         # vai formatar o número com duas casas decimais
                                    # pode ser usado o f no inicio igualmente

print(f'{num_1:0>30}')              # minha variável acrescenta 30 zeros a esquerda e o numero a direita
print(f'{num_1:0<30}')              # minha variável acrescenta 30 zeros a direita e o numero a esquerda
print(f'{num_1:0^30}')              # minha variável acrescenta 30 zeros e o numero centralizado

print(f'{num_2:0>8.2f}')            # minha variável acrescenta 30 zeros a esquerda
                                    # e o numero a direita com ponto flutuante
nome = 'mArcElo de caStro'
nome_formatado = '{:\U0001F4B0^50}'.format(nome)        # "\U0000f001" - "\U0001f539" unicode-codepoint
                                                        # classificação de simbolos - https://codepoints.net
print(nome_formatado)

print(nome.lower())     # tudo minusculo
print(nome.upper())     # tudo maiusculo
print(nome.title())     # Primeiras letras maiuscula
