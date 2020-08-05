# aula2 - ex10 - Arnott Ramos Caiado
# pergunta o turno de estudo e mostra mensagem

turno = input("\n Informe seu turno de Estudos (M=Matutino, V=Vespertino, N=Noturno ) : ")
turno = turno.upper()

if turno == 'M' :
    print("\n Bom dia!")
elif turno == 'V' :
    print("\n Boa Tarde!")
elif turno == 'N' :
    print("\n Boa Noite!")
else :
    print("\n Valor Inválido ( M, V ou N )")

