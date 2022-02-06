#Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.


salario = float(input("Qual o seu salário ?:"))

base = salario
salario_novo = 0
if base>= 1.250:
    salario_novo = salario + (salario * 0.10)
if base < 1.250:
    salario_novo = salario + (salario * 0.15)

print("O seu salario agora é de : %5.2f" %salario_novo)