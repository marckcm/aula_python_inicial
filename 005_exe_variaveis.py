'''
Construindo um  - indice de massa corporal
usando o comando .format ou f''
'''


nome = "Marcelo"
idade = 42
altura = 1.83
e_maior = idade > 18
peso = 64
ano = 2022
nascimento = ano - idade
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
# modos de usar a formatação do texto
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')            # Colocando um f antes das aspas echaves indicando os nomes das variaveis

# Segundo modo
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))    # colocando chaves na fase e no final dando um .format para indicar as variaveis segue sequencia da chave

# Segundo modo com variaveis determidas
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))     # 0 correspode a 1ª variavel 1 a 2ª e 2 a 3ª

# Segundo modo com variaveis determidas com nomeclaturas:
print('{n} tem {i} anos de idade e seu imc é {m:.2f}'.format(n=nome, i=idade, m=imc))     # 0 correspode a 1ª variavel 1 a 2ª e 2 a 3ª

'''
Exercicio:
criar variavel para nome str , idade int,
altura (float) e peso (float) de uma pessoa
Criar variavel com o ano atual (int)
obeter o ano de nascimento da pessoa
Obeter o imc da pessoa com 2 casas decimais 
exibir o texto com todos os valores na tela usando F-string () com chaves
'''

print((40*'\U0000f125'), '\nExercicio:\n')

# Resposta:
print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é  {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

