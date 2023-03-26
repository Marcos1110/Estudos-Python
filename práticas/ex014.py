# Escreva um programa que converta uma temperatura digitada em °C para °F

grauCelsius = float(input('Digite a temperatura em graus celsius (°C) : '))

grauFahrenheit = grauCelsius * (9/5) + 32

print('{}°C equivalem a {:.1f}°F.'.format(grauCelsius, grauFahrenheit))
