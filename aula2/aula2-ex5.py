# aula2 - ex5 - Arnott Ramos Caiado
# entra com duas notas, calcula media e mostra status do aluno

nota1 = float(input("\n Entrar primeira nota:"))
nota2 = float(input("\n Entrar segunda nota:"))

media = (nota1 + nota2) / 2

if media == 10 :
    print("\n Aprovado Com Distinção. Media=", media)
elif media >= 7 :
    print("\n Aprovado. Media=", media)
elif media < 7 :
    print("\n Reprovado. Media=", media)
