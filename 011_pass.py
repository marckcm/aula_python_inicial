"""
pass usado para aguardar um codigo tambem pode ser usado os ...

"""
valor = True

if valor:
    pass            # Não vai dar erro e posteriormente o desenvolvedor pode completar a formula
else:
    print('tchau')

valor = True

if valor:
    ...             # Não vai dar erro e posteriormente o desenvolvedor pode completar a formula e o codigo continua
else:
    print('tchau')


print("ultima função")
