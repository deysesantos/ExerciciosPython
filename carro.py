#Escreva um programa que pergunte a velocidade do carro de um
##usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
#80 km/h.




velocidade = int (input("Digite a sua velocidade:"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print ("Voce foi multado e sua multa é do valor de %d" %( multa))