# aula3 - exercicio aula - Arnott Ramos Caiado
# ex 2 - pede usuario e senha, e continua se nome igual senha

for continua in range(100): # 100 tentativas
    nome = input("\n Entre com nome: ")
    senha = input("\n Entre com senha: ")
    nome = nome.lower()
    senha = senha.lower()
    if nome != senha :
        break
    else :
        print( "\n Nome não pode ser igual a senha!")

if continua < 100 :
    print( "\n Terminou ok")