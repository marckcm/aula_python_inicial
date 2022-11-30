usuario = input('digite seu usuario:')
qtd_caracteres = len(usuario)

# Esse comando tambem conta os espassos, e essa função não funciona com inteiros e boleanos apenas com strings
print(f'{usuario},possui um total de {qtd_caracteres} letras e a função len e do tipo, {type(qtd_caracteres)}')


if qtd_caracteres <= 8:
    print("você precisa digitar no minimo 8 caracteres")
else:
    print('vc foi cadastrado no sistema')