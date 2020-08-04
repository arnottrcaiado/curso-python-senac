# aula2 - ex3 - Arnott Ramos Caiado
# verifica se letra é F ou M

letra = input("\n Digite F(para feminino) ou M(para masculino):")
letra = letra.upper()

if letra == 'F' :
    print("\n Feminino")
elif letra == 'M' :
    print("\n Masculino")
else :
    print("\n Letra Inválida")
    