'''
Tipos de dados

str = string = textos
int = inteiros = numeros inteiros
float = ponto flutuante = numeros com casas decimais
bool = boleanos = (True) verdadeiros ou (False) falsos
'''

nome = 'Marcelo'
numero = 123456
pt_flutuante = 0.16
boleano = False


#comando type muito util para informar o tipo de infarmação esta em uma variavel
print(type(nome))
print(type(numero))
print(type(pt_flutuante))
print(type(boleano))

# Com o comando int converto uma string(testo) para int(inteiro) numero inteiro
#lembrando que tudo que esta em aspas é uma strin numero inteiro não tem aspas nem flutuante

print('10', type('10'), type(int('10')))

# Com o comanto float transformo minha string em ponto flutuante
print('10', type('10'), type(float('10')))

