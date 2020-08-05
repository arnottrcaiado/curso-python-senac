# aula2 - ex6 - Arnott Ramos Caiado
# a partir de tres numeros entrados pelo teclado, informar qual o maior

print("\n Verificacaop do maior numero de tres")
numero1 = float(input("\n Informe o primeiro numero:"))
numero2 = float(input("\n Informe o segundo numero:"))
numero3 = float(input("\n Informe o terceiro numero:"))

if numero1 > numero2 :
    if numero1> numero3 :
        print("\n O maior é o primeiro:", numero1)
    elif numero1 == numero3 :
        print("\n Há dois maiores, o um e o tres:", numero1, " / ", numero3)
    else :
        print("\n O maior é o terceiro:", numero3)
elif numero2 > numero3 :
    print("\n O maior é o segundo:", numero2)
elif numero2 == numero3 :
    print("\n Há dois maiores, o dois e o tres:", numero2, " / ", numero3)
elif numero1 == numero2 :
    print("\n Há dois maiores, o um e o dois:", numero1, " / ", numero2)
elif numero3 > numero2 :
    print("\n O maior é o terceiro:", numero3)



