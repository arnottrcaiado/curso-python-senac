# aula4 - ex24 - Arnott Ramos Caiado
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

numeros = []
conta_dados = [0,0,0,0,0,0]


for i in range(100) :
    numero =  random.randint(1,6)
    print(i)
    print( numero )
    numeros.append( numero )

for i in range( len( numeros )) :
    if numeros[i] == 1 :
        conta_dados[0] += 1
    if numeros[i] == 2:
        conta_dados[1] += 1
    if numeros[i] == 3:
        conta_dados[2] += 1
    if numeros[i] == 4:
        conta_dados[3] += 1
    if numeros[i] == 5:
        conta_dados[4] += 1
    if numeros[i] == 6:
        conta_dados[5] += 1

for i in range ( 6 ) :
    print( "Quantidade de numeros {} = ",i+1,conta_dados[i])
