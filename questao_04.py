distancia = float(input("informe a distancia em km: "))

passagem = 0
if(distancia <= 200):
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
    
print("Valor da passagem: R$", passagem)