# aula5 - ex1 - Arnott Ramos Caiado
def imprime ( numero ):
    i=1
    while i <= numero :
        for j in range(1,i+1) :
            print( i,end=" ")
        print( )
        i +=1

numero = int(input("entre com um numero inteiro:"))
imprime( numero )