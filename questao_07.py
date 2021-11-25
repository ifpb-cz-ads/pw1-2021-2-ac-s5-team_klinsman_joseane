consumo = float(input("Informe a quantidade em kWh consumida: "))
instalacao = input("""Qual o tipo de instalação?
                   R para residências
                   I para indústrias 
                   C para comércios\n""")

if instalacao == "R" or instalacao == "r":
    if consumo <= 500:
        valor = consumo * 0.40
        print("Valor total a pagar: R$", valor)
    elif consumo > 500: 
        valor = consumo * 0.65
        print("Valor total a pagar: R$", valor)
        
elif instalacao == "C" or instalacao == "c":
    if consumo <= 1000:
        valor = consumo * 0.55
        print("Valor total a pagar: R$", valor)
    elif consumo > 1000: 
        valor = consumo * 0.60
        print("Valor total a pagar: R$", valor)
        
elif instalacao == "I" or instalacao == "i":
    if consumo <= 5000:
        valor = consumo * 0.55
        print("Valor total a pagar: R$", valor)
    elif consumo > 5000: 
        valor = consumo * 0.60
        print("Valor total a pagar: R$", valor)

else:
    print("Tipo de instalação inválida!")
    