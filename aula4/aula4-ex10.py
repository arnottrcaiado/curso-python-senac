# aula4 - ex10 - Arnott Ramos Caiado
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.
import random

vet1 = []
vet2 = []
vet12 = []

for i in range(10) :
    vet1.append( random.randint(1,100))
    vet2.append( random.randint(1,100))

for i in range( len(vet1)) :
    vet12.append(vet1[i])
    vet12.append(vet2[i])

print( vet1 )
print( vet2 )
print( vet12 )
