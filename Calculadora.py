


num1 = int(input ("Digite um número inteiro:"))
num2 = int(input ("Digite um numero inteiro:"))
operacao = int(input("Digite a operação desejada:  soma digite 1 "))

if operacao == 1 :
    resultado = num1 + num2

elif operacao == 2 :
    resultado = num1 - num2

elif operacao == 3 :
    resultado = num1 / num2

elif operacao == 4 :
    resultado = num1 * num2
else:
    print("Digite uma categoria válida")

print (resultado)