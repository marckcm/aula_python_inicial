'''
comando input() guarda uma resposta dentro da variavel
'''


nome = input("Qual seu nome?\n")
idade = input('Qual sua idade?\n')
ano_nascimento = 2022 - int(idade)          #o comando input sempre volta uma string (texto) para converter em inteiro temos usar "int()'


print(f'o usuario digitou {nome} e o tipo da variavel é uma {type(nome)} e sua idade e de {idade} anos nasceu no ano de {ano_nascimento} ')

#calculadora basica:

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite o segundo numero:'))
print(n1 + n2)


