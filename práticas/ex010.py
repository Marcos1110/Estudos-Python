# Crie um programa que leia quanto dinheiro uma pessoa tem em sua carteira e mostre quantos Dólares ela pode comprar
# Cotação do Dólar (26 de março de 2023) : US$1.00 = R$5.25

montante = float(input('Digite o valor na sua carteira : '))

conversao = montante / 5.25

print('Você pode comprar US${:.2f}'.format(conversao))