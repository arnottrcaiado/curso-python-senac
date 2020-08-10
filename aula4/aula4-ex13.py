# aula4 - ex13 - Arnott Ramos Caiado
# Faça um programa que receba a temperatura média de cada mês do ano e a
# rmazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
# mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random

meses = ["1-Janeiro","2-Fevereiro","3-Março","4-Abril","5-Maio","6-Junho","7-Julho","8-Agosto","9-Setembro","10-Outubro","11-Novembro","12-Dezembro"]

temperatura = []

for i in range(12):
    temperatura.append( random.randint( -50,+50 ) )

media = 0
for i in range( len(temperatura )) :
    media += temperatura[i]

media /= len(temperatura)

for i in range(len(temperatura))