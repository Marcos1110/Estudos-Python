# Crie um algoritmo que leia um número e nmostre o seu dobro, triplo e raiz quadrada

numero = float(input('Digite um número : '))

dobro = numero * 2
triplo = numero * 3
Rquadrada = numero ** (1 / 2)

print('O dobro de [{}] é [{}]'.format(numero, dobro))
print('O triplo de [{}] é [{}]'.format(numero, triplo))
print('A raiz quadrada de [{}] é [{:.2f}]'.format(numero, Rquadrada))