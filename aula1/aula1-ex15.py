# aula1 - ex 15 - Arnott Ramos Caiado
# calculo de salario

valor_hora = float(input("\n Quanto vc ganha por hora? "))
horas_trabalhadas = int(input("\n Quantas horas vc trabalhou no mes? "))

salario_bruto = valor_hora * horas_trabalhadas
inss = 0.08 * salario_bruto
ir = 0.11 * salario_bruto
sindicato = 0.05 * salario_bruto

print("\n +Salario Bruto: ", salario_bruto)
print("\n - IR (11%) : ", ir)
print("\n - INSS (8%) : ", inss)
print("\n - Sindicato (5%) : ", sindicato)
print("\n = Salario Liquido : ", salario_bruto - inss - ir - sindicato )
