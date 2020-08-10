# aula5 - ex3 - Arnott Ramos Caiado
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somanum( numeros ):
    soma =0
    for i in range(len(numeros)) :
        soma += numeros[i]
    return (soma)

# programa principal
num = []
qnum =0
while ( qnum < 3 ) :
    numero = int(input("Entre com numero inteiro :"))
    if numero != 0 :
        num.append( numero )
    else :
        print("numero invalido")
    qnum +=1

print( somanum( num ))
