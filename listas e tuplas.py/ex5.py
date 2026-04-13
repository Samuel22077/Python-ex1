n = int(input("Digite a qtde de numeros: "))
numeros = []

for i in range(n):
    valor = int(input("Digite um numero: "))
    numeros.append(valor)

    for i in range(len(numeros) -1, -1, -1):
        print(numeros[i])