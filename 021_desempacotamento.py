"""
Desempacotamento de lista
"""

lista = ['marcelo', 'curso', 'em', 'andamento', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1, n2, n3, *outra_lista = lista           # n1 = marcelo n2=curso o restante das variáveis ele coloca em *outra_lista
print(lista)
n1, n2, n3, *outra_lista, ultimo_n = lista      # Coloca o asterisco para juntar o intermediário da lista
print(ultimo_n)
*outra_lista, ultimo_n, n1, n2, n3 = lista
print(n1, n2, n3)
print(lista)
