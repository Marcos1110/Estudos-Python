# Escreva um programa  que pergunta a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado . Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0.15 por Km rodado

qtDiasAlugado = int(input('Quantos dias o carro ficou alugado    : '))
qtKmRodados = float(input('Quantos quilômetros foram percorridos : '))

precoAlugel = (qtDiasAlugado*60) + (qtKmRodados*0.15)

print('O preço do aluguel será R${:.2f}'.format(precoAlugel))

