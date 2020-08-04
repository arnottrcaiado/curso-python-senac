# aula2 - ex4 - Arnott Ramos Caiado
# verificar se vogal ou consoante

vogal="aeiou"

letra = input("\n Digite uma letra e eu verifico se eh uma vogal :")
letra = letra.lower()

if vogal.find(letra) >= 0 :
    print("\n É uma vogal")
else :
    print("\n É uma consoante")
