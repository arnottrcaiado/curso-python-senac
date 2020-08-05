# aula3 - exercicio aula - Arnott Ramos Caiado
# ex 1 - pede nota e continua enquanto nota invalida - com for

for continua in range(100) :
    nota = int(input("\n Entre com nota de 0 a 10: "))
    if nota >=0 and nota <= 10 :
        break
    else :
        print( "\n Nota invalida !")

print("\n Processo terminado")