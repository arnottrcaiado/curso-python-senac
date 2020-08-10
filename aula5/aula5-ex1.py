# aula5 - exercicios em aula - Arnott Ramos Caiado

def imprime ( numero ):
    i=1
    while i <= numero :
        for j in range(1,i+1) :
            print( j,end=" ")
        print( )
        i +=1


imprime(10)