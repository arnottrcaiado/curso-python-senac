# aula2 - ex8 - Arnott Ramos Caiado
# a partir de tres produtos e seus precos, identifcar e mostrar o de menor preco

def ordena_prod_preco( prod, preco ) :
    i,j = 0,0
    for i in range(0,len(prod)-1,1) :
        for j in range(i+1, len(prod),1) :
            print(i, j)

            if preco[i] > preco[j] :
                temp = preco[i]
                preco[i] = preco[j]
                preco[j] = temp
                temp = prod[i]
                prod[i] = prod[j]
                prod[j] = temp
    return prod, preco

prod=[]
preco=[]
numero_produtos=0

continua = True

while continua :
    print("\n Entrar com produto n.", numero_produtos+1)
    produto = input("\nEntrar com o nome de um produto ( apenas ENTER para terminar ):")
    if len(produto) > 0 :
        prod.append( produto)
        preco.append( input("\nEntrar o preco do produto:"))
        numero_produtos +=1
    else :
        continua = False

prod, preco = ordena_prod_preco( prod, preco)

print ("\n O produto mais barato é ", prod[0], " com preço:", preco[0])
