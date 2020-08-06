# aula3 - ex9 - Arnott Ramos Caiado
# imprime apenas numeros impares entre 1 e 50

for numero in range(1,51) :
    resto = numero % 2
    if resto != 0 :
        print("\n Numero impar: ", numero)