'''
+, -, *, /, //, **, %, ()
'''
# Basicos:
# Lembrando que o python segue a ordem matemarica
print('adição:', 100+150)
print('subtrção:', 250-1500)
print('multiplicação:', 7*8*3)
print('divisão:', 400/10)

# O sinal de multiplição multiplica tambem as strings
print("\U0000F590"*10)

# o de adição concatena as strings
nome = 'Marcelo'
sobrenome = 'Castro'
print(nome+' '+sobrenome)

print("\U0000F590"*20)
# Divisão inteira arredonda a divisão enquanto a divisão normal volta em ponto flutuante (com todas as casas)
print('divisão Arredondada:', 10 // 3)
print(10 / 3)

print("\U0000F590"*20)
#exponenciação
print('Exponenciação:', 4 ** 2)

print("\U0000F590"*20)
# Retorna o Modulo o resto da Divisão vai ser 0 ou 1

print('Resto:', 40 % 3)
print('Resto:', 40 % 2)

print("\U0000F590"*20)
# Precedencia usa o parentese para calcular a primeira operação

print((5+2)*2)          # Soma o 5+2 primeiro depois multiplica por 2
print(5+2*2)            # Multiplica o 2 primeiro depois soma o 5
