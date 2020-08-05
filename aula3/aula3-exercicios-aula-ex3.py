# aula3 - exercicio aula - Arnott Ramos Caiado
# ex 3 - pede nome, idade, salario, sexo, estado civil
continua = True

while continua :
    nome = input("\n Entre com nome (maior que 3 caracteres): ")
    nome = nome.upper()
    if len(nome) > 3  :
        continua = False
    else :
        print( "\n Nome de 0 a 3 caracteres")

continua = True
while continua :
    idade = int(input("\n Entre com idade (de 0 a 150): ")
    if idade >=0 and idade <=150 :
        continua = False
    else :
        print( "\n Idade de 0 a 150")

continua = True
while continua :
    salario = float(input("\n Entre salario (maior que 0): ")
    if salario > 0:
        continua = False
    else :
        print( "\n Salario deve ser maior que 0")

# entrar sexo
continua = True
while continua:
    sexo = (input("\n Sexo (m ou f): ")
    sexo = sexo.lower())
    if sexo == 'f' or sexo == 'm' :
        continua = False
    else:
        print("\n Sexo deve ser f ou m")

# entrar Estado Civil
continua = True
while continua:
    estado_civil = (input("\n Estado Civil (s , c, v, d ): ")
    estado_civil = estado_civil.lower())
    if estado_civil == 's' or estado_civil == 'c' or estado_civil=='v' or estado_civil='d' :
        continua = False
    else:
        print("\n Estado Civil deve ser (s,c,v,d)!")

