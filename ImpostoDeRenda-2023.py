hora = int(input('Digite o valor da sua hora de trabalho: '))

salario = hora * 8 * 5 * 4
salario_bruto = salario

if salario_bruto <= 1302:
    print('Você está isento do desconto do INSS!')
    aux = 0

if salario_bruto > 1302 and salario_bruto <= 2571:
    salario_bruto = salario - salario * 0.09
    aux = 9

if salario_bruto > 2572 and salario_bruto <= 3856:
    salario_bruto = salario - salario * 0.12
    aux = 12

elif salario_bruto > 3857 and salario_bruto >= 7507:
    salario_bruto = salario - salario * 0.14
    aux = 14

print('Desconto do INSS:' ,aux, '%')



if salario <= 2112:
    print('Você está insento do Imposto de Renda!')
    aux = 0

if salario > 2113 and salario <= 2826:
    salario = salario - salario * 0.08
    aux = 8
if salario > 2826 and salario <= 3751:
    salario = salario - salario * 0.15
    aux = 15
elif salario > 3751 and salario <= 4665:
    salario = salario - salario * 0.225
    aux = 22.5
elif salario > 4665:
    salario = salario - salario * 0.275
    aux = 27.5


print('=-=' * 15)
print('IMPOSTO DO TRABALHADOR')
print('=-=' * 15)
print('Valor do salário bruto: R${:.2f}'.format(salario_bruto))
print('=-=' * 15)
print('IMPOSTOS:')
print('Desconto do Imposto de Renda:' ,aux, '%')
print('=-=' * 15)
print('Valor do salário líquido: R${:.2f}'.format(salario))
print('=-=' * 15)

