# aula3 - ex6 - Arnott Ramos Caiado
# laco para imprimir numeros de 1 a 20 de duas formas

print("Numeros de 1 a 20 - um embaixo do outro\n")
for i in range(1,21,1) :
    print("\n",i)

print("Numeros de 1 a 20 - um ao lado do outro\n")
while i > 0 :
    print(" ",21-i)
    i -=1
