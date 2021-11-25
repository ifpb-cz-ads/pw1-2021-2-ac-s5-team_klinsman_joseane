salario = float(input("Informe seu salário: "))
casa = float(input("Informe o valor da casa: "))
parcelas = int(input("Informe em quantas o número de parcelas: "))

porcetagemSalario = (salario * 30)/100
valorParcela = casa/parcelas
if(valorParcela > porcetagemSalario):
    print("Emprestimo recusado :(")
else:
    print(f'Emprestimo aprovado! :) você pagará R${casa:.2f} em {parcelas} vezes de {valorParcela:.2f}')