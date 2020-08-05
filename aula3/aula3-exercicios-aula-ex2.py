# aula3 - exercicio aula - Arnott Ramos Caiado
# ex 2 - pede usuario e senha, e continua se nome igual senha

continua = True

while continua :
    nome = input("\n Entre com nome: ")
    senha = input("\n Entre com senha: ")
    nome = nome.lower()
    senha = senha.lower()
    if nome != senha :
        continua = False
    else :
        print( "\n Nome não pode ser igual a senha!")
