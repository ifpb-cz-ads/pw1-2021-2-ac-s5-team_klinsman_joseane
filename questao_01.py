velocidade = float(input("Informe a velocidade do seu carro: "))
if velocidade > 80 :
    multa = (velocidade - 80) * 5
    print(f"O valor da sua multa é R${multa:.2f}")
else :
    print("Você não possui multa!")