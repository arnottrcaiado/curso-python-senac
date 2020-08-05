
interador = 0

while interador <= 150 :
    tem_resto = interador %5 != 0
    if not tem_resto :
        print( interador )
    interador +=1

tabuada = input("\n Informe um numero para tabuada:")
tabuada = int(tabuada)

interador = 1
while interador <= 10 :
    soma = interador + tabuada
    subtracao = tabuada - interador
    multiplicacao = tabuada * interador

    print("Soma :",tabuada," + ",interador," = ", soma)
    print("Subtracao :",tabuada," - ",interador," = ", subtracao)
    print("Multiplicacao :",tabuada," x ",interador," = ", multiplicacao)

    interador += 1


