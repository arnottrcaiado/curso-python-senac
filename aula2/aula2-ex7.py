# aula2 - ex7 - Arnott Ramos Caiado
# a partir de tres numeros entrados pelo teclado, informar qual o maior

print("\n Verificacaop do menor numero de tres")
numero1 = float(input("\n Informe o primeiro numero:"))
numero2 = float(input("\n Informe o segundo numero:"))
numero3 = float(input("\n Informe o terceiro numero:"))

if numero1 < numero2 :
    if numero1 < numero3:
        print("\n O menor é o primeiro:", numero1)
if numero2 < numero1 :
    if numero2 < numero3 :
        print("\n O menor é o segundo:", numero2)
if numero3 < numero1 :
    if numero3 < numero2 :
        print("\n O maior é o terceiro", numero3)
if numero1 == numero2 == numero3 :
    print( "\n Os tres numeros sao iguais")




