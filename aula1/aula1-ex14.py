# aula1 - ex14 - Arnott Ramos Caiado
# calcular multa por excesso de pesca

limite_peso = 50
multa_kg = 4
multa_excesso = 0
peso_pescado = float( input("\n Peso da pesca ( em kg):"))

if peso_pescado > limite_peso :
    excesso_peso = peso_pescado - limite_peso
    multa_excesso = excesso_peso * multa_kg
    print("\n Peso pescado:", peso_pescado, "- Excesso de ", excesso_peso, " - multa de :", multa_excesso)
else :
    print("\n Não houve excesso. Peso:", peso_pescado)
