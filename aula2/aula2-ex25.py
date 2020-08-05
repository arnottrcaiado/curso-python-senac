# aula2 - ex25 - Arnott Ramos Caiado
# faz perguntas e identifica se uma pessoa eh suspeita de um crime

classificacao=0

pergunta = ["Telefonou para a Vitima?",
            "Esteve no Local do Crime?",
            "Mora perto da Vítima?",
            "Devia para a Vítima?",
            "Já trabalhou para a Vítima?"]

for i in range ( len(pergunta) ) :
    print("\n Pergunta :", i+1, " - ")
    resposta = input( pergunta[i] )
    resposta = resposta.upper()
    if resposta == 'S' :
        classificacao +=1

if classificacao < 2 : # inocente
    print("\n Inocente")
if classificacao == 2 : # suspeita
    print( "\n Suspeito")
if classificacao >= 3 and classificacao <=4 : # cumplice
    print( "\n Cumplice")
if classificacao == 5 : # assassino
    print( "\n Assassino")


