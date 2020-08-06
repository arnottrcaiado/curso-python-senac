# aula3 - ex7 - Arnott Ramos Caiado
# ler 5 numeros, calcular a soma e a media

soma =0
media = 0

for i in range(1,6) :
    numero=float(input("\n Entre com numero :"))
    soma += numero

media = soma / 5
print("\n A soma dos numeros= ", soma, ", e amédia= ", media)