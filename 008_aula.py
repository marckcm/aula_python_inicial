"""
operadores logicos:
and, or, not
in  e not in
"""

comp1 = 10
comp2 = 20
comp3 = 30
variavel1 = ""

# and da verdadeiro somente se duas comparações forem verdadeiras caso contrario volta falso

if comp1 == comp2 and comp2 == comp3:
    print('Verdadeiro')
else:
    print("Falso")

# or se algumas das duas comparações forem verdadeiras a expreção volta verdadeiro

if comp1 == comp2 or comp2 == comp3:
    print('Verdadeiro')
else:
    print("Falso")

# not inverte o valor comparativo muito usado para ver se a variavel tem algum valor ou esta vazia
if not comp1 > comp2 or not comp2 > comp3:
    print('Verdadeiro')
else:
    print("Falso")

if not variavel1:
    print("favor preencher os dados")

# in e not in e pra saber se em uma variavel tem alguma condição ex. uma letra esta presente ou um nome
nome = 'marcelo'

if 'a' in nome:
    print('existe a letra a em seu nome')
else:
    print('não existe')

if "não deu" not in nome:
    print('Não possui a expreção')
else:
    print('Possui')

print(40*'\U0000F300')

usuario = input('nome do usuario:')
senha = input('digite uma senha:')

# banco de dados:
bd_usuario = 'marcelo'
bd_senha = '123456'

if bd_usuario == usuario and bd_senha == senha:
    print('Você está logado')
else:
    print('Usuario ou senha Inválido')
