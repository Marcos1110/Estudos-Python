# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan

angulo = float(input('Insira o valor de um ângulo qualquer : '))

print('Seno : {:.3f} | Cosseno : {:.3f} | Tangente : {:.3f}'.format(sin(angulo),
                                                                    cos(angulo),
                                                                    tan(angulo)))
