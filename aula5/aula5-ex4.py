# aula5 - ex4 - Arnott Ramos Caiado
# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def positivo_negativo ( numero ):
    if numero >0 :
        return ('P')
    else:
        return ('N')

numero = int(input("entre com um numero inteiro:"))
print(positivo_negativo( numero ))