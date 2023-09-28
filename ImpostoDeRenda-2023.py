hora = int(input('Digite o valor da sua hora de trabalho: '))

salario = hora * 8 * 5 * 4
salario_bruto = salario

if salario <= 2112:
    print('Você está insento do Imposto de Renda!')
    aux = 0

elif salario > 2113 and salario <= 2826:
    salario = salario - salario * 0.08
    aux = 8
else:
    salario = salario - salario * 0.15
    aux = 15

salario = salario - salario * 0.09
#INSS

print('=-=' * 15)
print('IMPOSTO DO TRABALHADOR')
print('-' * 15)
print('Valor do salário bruto: R${:.2f}'.format(salario_bruto))
print('-' * 15)
print('IMPOSTOS:')
print('Desconto do Imposto de Renda:',aux, '%')
print('Desconto do ICSM: 9%')
print('-' * 15)
print('Valor do salário líquido: R${:.2f}'.format(salario))
print('=-=' * 15)

