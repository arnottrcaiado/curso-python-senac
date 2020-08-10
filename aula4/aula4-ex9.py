# aula4 - ex9 - Arnott Ramos Caiado
# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

A = []

for i in range(10) :
    print("Entre com um numero inteiro - ", i+1)
    numero = int(input(" "))
    A.append( numero )

soma = 0

for i in range(len(A)) :
    soma += A[i] ** 2

print("A soma dos quadrados dos elemento do vetor = ", soma)