pessoa = {
    'nome': 'Vitor',
    'idade': 18,
    'email': 'vitorgabrielcont77@gmail.com'
}

print('Chaves em pessoas:')

for chaves in pessoa:
    print(chaves)

print('-' * 20)

print('valor em pessoas:')

for valor in pessoa.values():
    print(valor)

print('-' * 20)

print('itens em pessoas:')

for chave, valor in pessoa.items():
    print(f'Chave: {chave} | valor: {valor}')
