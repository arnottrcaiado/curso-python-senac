# aula3 - ex7 - Arnott Ramos Caiado
# ler 5 numeros e informar o maior

maior =0
posicao = 0
for i in range(1,6) :
    numero=float(input("\n Entre com numero :"))
    if numero > maior :
        maior = numero
        posicao = i

print("\n O maior numero lido foi o ", posicao, "o numero , = ", maior)