'''
Listas em python
fatiamento
append, insert, pop, clear, extend, min, max
'''

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista[0:3])           # Mostra os 3 primeiros itens da lista
print(lista[2:])            # Mostra a partir do terceiro item da lista.
print(lista[-1])            # Mostra o último item da lista.
print(lista[::2])           # Vai pulando um item da lista.
print(lista[::-1])          # Vai inverter a lista

print('\U0001f610'*40)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)             # l3 = l1 + l2 igual essa formula mais não cria a lista l3 apenas estende a l1 com os n da l2
print(l1)
l2.append(7)                 # Adiciona o numero 7 na lista 2
print(l2)
l2.insert(0, 'maca')        # Insere maca no primeiro indice
print(l2)
l2.pop(0)                   # deleta o índice selecionado se não informar o índice ele exclui o ultimo.
print(l2)
del(l2[1:3])                # Deletar determinados trechos
print(l2)

print('\U0001f610'*40)

l3 = list(range(1, 11))         # Cria uma lista com as numerações de 1 a 10 sem ter que escrever cada numero
print(l3)

l4 = ["string", True, 10, -10.5]

for item in l4:
    print(f'O tipo de elemento é {type(item)} e seu valor é {item}')

