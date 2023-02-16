"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if idade and nome:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espços!')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    print(f'E sua idade é: {idade}')

else:
    print('Voce precisa digitar algumas informações para continuar.')