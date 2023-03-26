# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la , sabendo que cada litro de tinta pinta uma área de 2m^2

altura = float(input('Insira a altura da parede (em metros)  : '))
largura = float(input('Insira a largura da parede (em metros) : '))

areaParede = largura * altura
qtTinta = areaParede / 2

print('A parede tem uma área de [{}] m2.'.format(areaParede))
print('Serão necessários [{}] litros de tinta para pintá-la'.format(qtTinta))
