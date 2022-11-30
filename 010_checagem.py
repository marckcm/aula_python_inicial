# isnumeric isdigit isdecimal
# checa se a variavel pode ser convertida em inteiros ou float

num1 = input('digite um numero:')
num2 = input('digite outro numero:')

#isnumeric vai retornar um valor boleano verdadeiro ou falso checa numeros positivos inteiros
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print('Não pude realizar a conta')

#pode se executar o try para tentar executar uma função e so se não conseguir o python da erro
try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
except:
    print('Não pude realizar a conta')