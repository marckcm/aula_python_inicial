'''
For Else em Puthon
'''


variavel = ['Cicatriz', 'Cobertor', 'helicoptero', 'aniversario']

for valor in variavel:
    if valor.startswith('c'):
        print('começa com c', valor)
    else:
        print('não começa com c', valor)


print('\U0001f501'*20 )

item_c = False
for valor in variavel:
    if valor.lower().startswith('c'):          # vai colocar todas as primeira letras em minusculo e ver se começa com c
        item_c = True

if item_c:
    print('Existe Palavras que começam com c.')
else:
    print('Não existe Palavras que começam com c')




