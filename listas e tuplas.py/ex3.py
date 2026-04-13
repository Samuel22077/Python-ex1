numero = []

for i in range(10):
    valor = float(input("Digite um numero: "))
    numero.append(valor)
    maior = numero[0]
    indice_maior = 0

    for i in range(len(numero)):
        if numero[i] > maior:
            maior = numero[i]
            indice_maior = i

print(f"Maior valor:" , maior)
print(f"Indice do maior valor:", indice_maior)


