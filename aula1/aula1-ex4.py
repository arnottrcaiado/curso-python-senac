# aula 1 - exe 4 - Arnott Ramos Caiado
# obter 4 notas e calcular a media
from typing import List

nota1 = float(input("\n Nota1:"))
nota2 = float(input("\n Nota2:"))
nota3 = float(input("\n Nota3:"))
nota4 = float(input("\n Nota4:"))

media = (nota1 + nota2 + nota3 + nota4)/4
print ( "\n Media:", media)

# outra opção

nota = []
soma=0
for i in range(0,4) :
    print("\nNota : ",i+1)
    nota.append(float(input()))
    soma = soma+ nota[i]

media = soma / 4
print( "\n Media=", media)
