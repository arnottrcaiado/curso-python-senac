# aula4 - ex8 - Arnott Ramos Caiado
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def qt_digito( numero ) :
    numero_str = str(numero)
    return( len(numero_str))

numero = int ( input("Entre com um numero:"))
print( "Quantidade de digitos do numero ", numero, " - digitos:", qt_digito(numero))