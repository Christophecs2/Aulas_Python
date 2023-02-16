primeiro_num = int(input('Digite um numero para comparar>>  '))


segundo_num = int(input('Digite outro numero para comparar>>  '))

if primeiro_num > segundo_num:
    print(f'O primeiro numero é maior que o segundo!!\n {primeiro_num} é maior que {segundo_num}')
elif segundo_num > primeiro_num:
    print('O segundo numero é maior que o primeiro!!\n {} é maior que {} '.format(segundo_num,primeiro_num))
elif primeiro_num == segundo_num:
    print('Os numeros tem o mesmo valor!!!')
else:
    print('Valores invalidos, tente denovo!!')