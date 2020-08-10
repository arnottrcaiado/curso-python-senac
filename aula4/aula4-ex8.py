# aula4 - ex8 - Arnott Ramos Caiado
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade_vet = []
altura_vet = []

for i in range( 5 ) :
    idade =0
    while idade <= 0 or idade > 150 :
        print("Entre com a idade entre 1 e 150 :", i)
        idade = int(input("Idade:"))
    idade_vet.append(idade)

    altura = 0
    while altura <= 0 or altura > 150:
        print("Entre com a altura entre 1 e 2.50 :", i)
        altura = float(input("Altura:"))

    altura_vet.append( altura )

for i in range( 4,-1, -1 ) :
    print( "Idade ", idade_vet[i],)
    print( "Altura:", altura_vet[i])
