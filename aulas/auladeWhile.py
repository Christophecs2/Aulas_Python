condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')