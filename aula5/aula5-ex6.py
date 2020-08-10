# aula5 - ex6 - Arnott Ramos Caiado
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
# o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
# a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def converte_24_12( hora ) : # recebe hora padrao 24
    if hora < 12 :
        return hora, 'AM'
    if hora > 12 :
        hora = hora - 12
        return hora, 'PM'


hora_24= int(input("Entre com a hora ( o-24 "))
minutos = int(input("Entre com os minutos ( 0-59 ) "))

hora_12, sigla = converte_24_12 ( hora_24 )

print( "hora 24:", hora_24,":", minutos, " - hora 12 = ", hora_12,":", minutos, sigla)