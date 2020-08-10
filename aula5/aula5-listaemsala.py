# aula5 - exercicios em aula - Arnott Ramos Caiado

def soma( *numeros ) : # *numeros é uma tupla, com qualquer quantidade de elementos
    resultado = 0
    for numero in numeros :
        resultado += numero
    return resultado

def nomes( *nome ):
    lista = list(nome)
    print(lista)

nomes("antonio","carlos","pedro",20)

def imprime ( numero ):
    i=1
    while i <= numero :
        for j in range(1,i+1) :
            print( j,end=" ")
        print( )
        i +=1


imprime(10)

soma_num = soma( 10,20,30,40)
print(soma_num)

# crie um algoritmo que informe se um numero eh primo ou nao
def eh_primo ( numero ):
    num1 = int( numero/2)
    while num1 > 1 :
        resto = numero % num1
        if resto == 0 :
            return False
        num1 -= 1
    return True


for i in range(1,100) :
    print(i, eh_primo(i))