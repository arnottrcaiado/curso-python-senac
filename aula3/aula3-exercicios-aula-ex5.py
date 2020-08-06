# aula3 - exe5 - Arnott Ramos Caiado
# encontrar ponto de equilibrio em anos de duas populacoes
# com entrada de dados

continua = True
while continua :

    pais_a =0
    while pais_a <=0 :
        pais_a=int(input("\n Entre com população pais A ( maior que zero ):"))
        if pais_a >0 :
            break
        print("\n Valor invalido!")

    pais_b = 0
    while pais_b <=0 or pais_b < pais_a :
        pais_b=int(input("\n Entre com população pais B ( maior que pais A ):"))
        if pais_b > pais_a :
            break
        print("\n Valor invalido!")

    taxa_a = 0
    while taxa_a <=0 or taxa_a > 1 :
        taxa_a = float(input("\n Taxa de crescimento pais A ( entre 0 e 1) :"))
        if taxa_a >0 and taxa_a < 1 :
            break
        print("\n Valor invalido!")

    taxa_b = 0
    while taxa_b <= 0 or taxa_b > 1:
        taxa_b = float(input("\n Taxa de crescimento pais B ( entre 0 e 1) :"))
        if taxa_b > 0 and taxa_b < 1:
            break
        print("\n Valor invalido!")

    ano = 0

    while pais_a < pais_b :
        pais_a += pais_a * taxa_a
        pais_b += pais_b * taxa_b
        ano += 1

    print("\n Tempo em anos: ", ano)
    print("\n Pais a:",  int(pais_a))
    print("\n Pais b:" , int(pais_b))