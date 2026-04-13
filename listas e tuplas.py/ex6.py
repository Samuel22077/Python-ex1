temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = temperaturas[0]
maior = temperaturas[0]
soma = 0

for temp in temperaturas:
    if temp < menor:
        menor = temp
    
    if temp > maior:
        maior = temp
    
    soma += temp

media = soma / len(temperaturas)

print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Média das temperaturas:", media)