# aula4 - ex9 - Arnott Ramos Caiado
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


def reverso( numero ) :
    numero_str = str(numero)
    inverso=""
    for i in range(len(numero_str)-1,-1,-1) :
        inverso += numero_str[i]

    return( int(inverso))

numero = int ( input("Entre com um numero:"))
print( "Numero inicial ", numero, " - invertido", reverso(numero))