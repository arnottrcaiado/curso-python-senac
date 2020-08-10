# aula4 - ex12 - Arnott Ramos Caiado
# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random

idades = []
alturas = []
NUM_ALUNOS = 30

for i in range( NUM_ALUNOS ):
    # gerar idades e alturas, usando random.randint
    idades.append( random.randint( 6, 19 ))
    alturas.append( random.randint( 100, 250 ) / 100.00 )

media_altura = 0
for i in range ( len(alturas )):
    media_altura += alturas[i]

media_altura /= len(alturas)

maiores_13 = 0
for i in range( len(alturas)) :
    if alturas[i] < media_altura and idades[i] > 13 :
        maiores_13 += 1
        print( "Mais que 13 anos e menor que media", alturas[i])

print( idades )
print( alturas )
print ("Tem mais de 13 anos e menores que media de altura:", maiores_13)