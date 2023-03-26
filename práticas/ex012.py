# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Insira o preço atual do produto ; '))

precoDesconto = preco - (preco*0.05)

print('O produto custará R${:.2f} com o desconto de 5%.'.format(precoDesconto))