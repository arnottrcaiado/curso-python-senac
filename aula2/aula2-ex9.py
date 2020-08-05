# aula2 - ex9 - Arnott Ramos Caiado
# a partir de tres numeros, mostrar em ordem decrescente

def ordena_decrescente( vetor ) :
    i,j = 0,0
    for i in range(0,len(vetor)-1,1) :
        for j in range(i+1, len(vetor),1) :
            if vetor[i] < vetor[j] :
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp
    return vetor

numeros=[]

continua = True
numero_itens = 0

while continua :
    print("\n Entrar com numero n.", numero_itens+1)
    item = input("\nEntrar um numero ( apenas ENTER para terminar ):")
    if len(item) > 0 :
        numeros.append( item )
        numero_itens +=1
    else :
        continua = False

numeros = ordena_decrescente( numeros )

print( "\n Numeros em ordem decrescente")
for i in range (len(numeros)) :
    print("\n Numero ( ",i," ) = ", numeros[i])
