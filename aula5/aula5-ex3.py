# aula5 - ex3 - Arnott Ramos Caiado
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somanum( numeros ):
    soma =0
    for i in range(len(numeros)) :
        soma += numeros[i]
    return (soma)

num = []

while ( True ) :
    numero = int(input("Entre com numero inteiro (0 para terminar):"))
    if numero != 0 :
        num.append( numero )
    else :
        break;

print( somanum( num ))
