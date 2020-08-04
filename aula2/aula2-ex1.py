# aula2 - ex1 - Arnott Ramos Caiado
# entrar com dois numeros e imprimir o maior

numero1 = float(input("\n Digite um numero:"))
numero2 = float(input("\n Digite outro numero:"))

if numero1 > numero2 :
    print("O primeiro eh o maior: ", numero1)
elif numero2 > numero1 :
    print("O segundo eh o maior: ", numero2)
else :
    print("Os dois são iguais:", numero1, " = ", numero2 )

