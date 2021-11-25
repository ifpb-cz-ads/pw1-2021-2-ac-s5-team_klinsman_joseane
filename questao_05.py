num1 = float(input("Informe um número: "))
num2 = float(input("Agora informe outro número: "))

operacao = input("""Qual operação você deseja fazer? Digite: 
                 + 
                 -
                 *
                 / \n""")
if operacao == '+':
    total = num1 + num2
    print("A soma dos dois números informados é:", total)
elif operacao == '-':
    total = num1 - num2
    print(f"A subtração dos dois números informados é:{total:.2f}")
elif operacao == '*':
    total = num1 * num2
    print("A multiplicação dos dois números informados é: ", total)
elif operacao == '/':
    total = num1 / num2
    print("A divisão entre os dois números informados é:", total)
else:
    print("Operação inválida")