# aula1 - ex12 - Arnott Ramos Caiado
# calculo do peso ideal

altura = float(input("\n Entrar com altura de uma pessoa, em metros: "))
sexo = input("\n Informe o sexo da pessoa ( F/M ):")

sexo = sexo.upper()
if sexo == 'M' :
    peso_ideal = (72.7 * altura )-58
elif sexo == 'F' :
    peso_ideal == ( 62.1*altura)-44.7

print("\n Peso ideal:", peso_ideal )