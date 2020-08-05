# aula3 - exe4 - Arnott Ramos Caiado
# encontrar ponto de equilibrio em anos de duas populacoes

pais_a = 80000.0
pais_b = 200000.0

taxa_a = 0.03
taxa_b = 0.015
ano = 0

while pais_a < pais_b :
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    ano += 1

print("\n Tempo em anos: ", ano)
print("\n Pais a:",  int(pais_a))
print("\n Pais b:" , int(pais_b))