"""
Manipulando strings

*String indices
*Fatiamento de Strings (inicio:fim:passo )
*Funções built-in, len, abs, type, print, etc...

Você pode conferir tudo em :
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
#positivos        [0123456789]
texto           = 'Python s23'
#negativos       -[987654321]

print(texto[4])         # Pega o caractere correspondente a string no caso o 4 vai pegar o 5º caractere pois o 0 conta

# Positivos
print('\U0001f320'*20)
url = 'www.google.com.br/'

print(url[4:10])    # Primenro numero de onde começa e o outro onde termina
print(url[:4])      # Vai da primeira letra até a 4 casa lembrando que 0 conta
print(url[10:])     # Vai pegar do caracter 10 ate o final da string

print('\U0001f320'*20)
# Negativos

print(url[:-1])     # Elimina o ultimo caracteres
print(url[-1])      # Pega o ultimo caracteres da string
print(url[-8:])     # Pega do .com para frente por ai vai

print('\U0001f320'*20)
# Pulando caracteres

print(len(url))
print(url[0::2])    # Pega a string e vai pulando de 2 em 2 caracteres







