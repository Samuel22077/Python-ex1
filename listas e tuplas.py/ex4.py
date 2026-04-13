numero = []

for i in range(10):
    valor = float(input("Digite um numero: "))
    numero.append(valor)
    soma_pares = 0
    soma_indices_pares = 0

    for i in range(len(numero)):
        if numero [i] % 2 == 0:
            soma_pares += numero[i]

        if i % 2 == 0:
            soma_indices_pares += numero[i]

print("Soma dos valores pares:", soma_pares)
print("Soma dos índices pares:", soma_indices_pares)