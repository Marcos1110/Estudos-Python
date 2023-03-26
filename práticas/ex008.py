# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

vlMetro = float(input('Insira o valor em metros que será convertido : '))

vlCentimetro = vlMetro * 100
vlMilimetro  = vlMetro * 1000

print('[{}] metros é igual a [{}] centímetros e [{}] milímetros'.format(vlMetro, vlCentimetro, vlMilimetro))
