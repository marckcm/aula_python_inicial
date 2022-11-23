'''
condições IF, ELIF, ELSE
operadores relacionais: == > >= < <= !=
'''

n1 = 10
n2 = 20.5

print(n1 == n2)           # igualdade ==
print(n1 > n2)            # maior
print(n1 >= n2)           # maior ou igual
print(n1 < n2)            # menor
print(n1 <= n2)           # menor ou igual
print(n1 != n2)           # diferente

if n1 == n2:
    print('Verdadeiro')
elif n1 > n2:
    print("primeiro numero é maio que o segunto")
else:
    print('segundo numero é maior que o primeiro')

nome = input('Qual seu nome?\n')
idade = input('qual sua idade?\n')
idade = int(idade)
#limite para pegar emprestimo
menor_idade = 20
maior_idade = 60


if idade >= menor_idade and idade <= maior_idade:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} Emprestimo Negado')
