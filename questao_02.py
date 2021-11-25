numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe um número: "))
numero3 = int(input("Informe um número: "))

menor = numero1
maior = numero1

if(numero2 > maior):
    maior = numero2
if(numero3 > maior):
    maior = numero3

if(numero2 < menor):
    menor = numero2
if(numero2 < numero3):
    manor = numero3
    
print("O maior número informado foi: ", maior)
print("O menor número informado foi: ", menor)