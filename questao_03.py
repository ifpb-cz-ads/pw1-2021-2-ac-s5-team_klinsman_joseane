salario = float(input("Informe o valor do seu salário: "))
if salario <= 1250 : 
    reajuste = salario + (salario * 15 / 100)
    print(f"Com o aumento de 15% o valor do seu salário é R${reajuste:.2f}")
else:
    reajuste = salario + (salario * 10 / 100)
    print(f"Com o aumento de 10% o valor do seu salário é R${reajuste:.2f}")