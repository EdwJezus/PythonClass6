paises = {'br':'Brasil', 'eua':'Estados Unidos', 'esp':'Espanha'}
print(paises)
print(type(paises))

###################
print('')

print(paises['br'])

###################
print('')

print(paises.get('br'))

###################
print('')

print('br' in paises)
print('ru' in paises)

###################
print('')

paises['ru'] = 'União Soviética'
print(paises)

###################
print('')

paises.update({'ru':'Rússia'})
print(paises)

###################
print('')

paises.pop('ru')
print(paises)

###################
print('')

carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

###################
print('')

cesta = []
product = ''

print('Catalogo: Coca-cola, Pepsi, Guaraná, Fanta.')
catalogo = {'coca-cola': 10, 'pepsi': 9, 'guaraná': 7, 'fanta': 8}

print('Digite "sair" para finalizar o carrinho.')
while product != 'sair':
  product = input('Qual o produto? ')
  if product != 'sair':
    cesta.append(product)
cesta
print(cesta)


###################
print('')


starwars = {'nome': 'Star Wars: Uma nova esperança', 'ano': 1977, 'diretor': 'George Lucas', 'ator': 'Mark Hamill'}

n1 = ''
while n1 != 'sair':
  n1 = input('Qual o nome do filme? ')
  if n1 == 'star wars':
    print(f'Você selecionou {starwars["nome"]}')
    n2 = ''
    while n2 != 'sair':
      n2 = input('Qual informação sobre o filme você deseja saber? ')
      if n2 == 'ano':
        print(starwars['ano'])
      elif n2 == 'diretor':
        print(starwars['diretor'])
      elif n2 == 'ator':
        print(starwars['ator'])
