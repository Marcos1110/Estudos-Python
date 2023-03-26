# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Insira o salário do funcionário : '))

salAumento = salario + (salario * 0.15)

print('O funcionário recebrá R${:.2f} após o aumento de 15%.'.format(salAumento))