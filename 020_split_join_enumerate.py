"""
Split, Join, Enumerate em Python

Split = Dividir uma string # str
join = Junta uma lista # str
enumerate = enumera elementos da lista # apenas numeros inteiros
"""

string = "O Brasil e o País do futebol, o Brasil é Penta."
lista = string.split(' ')
lista_2 = string.split(',')         # O demarcador das strings fica sendo a virgula

print(lista)
print(lista_2)
palavra = ''
contagem = 0

for item in lista:
    print(f'a palavra "{item}" apareceu {lista.count(item)}x na frase')
    qtd_vezes = lista.count(item)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = item
print(f'\n\nA palavra que apareceu mais vezes foi a {palavra} ({contagem}x)\n')


for valor in lista_2:
    print(valor.strip().capitalize())       # strip tira os espaços inicio e fim da palavra
                                            # capitalize coloca a primeira letra em maiusculo

# Usando o join para juntar os elementos da lista
string_2 = '#'.join(lista)
print(string_2)
string_2 = ' '.join(lista)
print(string_2)


# enumerate:
print('\U0001f502'*40)
str1 = 'O Brasil e penta'
l1 = str1.split(' ')

for indice, valor in enumerate(l1):
    print(indice, valor, l1[indice])




