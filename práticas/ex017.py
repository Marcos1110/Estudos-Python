# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catOp  = float(input('Insira o Cateto Oposto    : '))
catAdj = float(input('Insira o Cateto Adjacente : '))

print('A hipotenusa é {}'.format(hypot(catOp, catAdj)))

