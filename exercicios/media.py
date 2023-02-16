n1 = float(input('Digite a nota do primeiro bimestre:'))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))

media = (n1 + n2 + n3 + n4) / 4

print('A media do aluno seria: ', media)

if media < 7:
    print('Aluno esta de recuperação')
else:
    print('aluno aprovado')