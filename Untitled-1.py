#altura=float (input("Digite sua altura: "))
#Peso_Ideal= (72.7* altura) -58
#print("Seu peso Ideal é: %.2f" %Peso_Ideal)

#KMS=float (input("Digite a quantidade de quilometros: "))
#Dias=float(input("Digite a quantidade de dias: "))
#Total= (KMS*0.15)+(Dias*60)
#print("Total a pagar: %.2f" %Total)

#Dias=float(input("Digite a quantidade de dias: "))
#Horas=float(input("Digite a quantidade de horas: "))
#Minutos=float(input("Digite a quantidade de minutos: "))
#Segundos=float(input("Digite a quantidade de segundos: "))
#Tempo_total= (Dias*86400)+(Horas*3600)+(Minutos*60)+Segundos
#print("Tempo total foi de: %.2f" %Tempo_total)

Hora_Trabalhada=float(input("Digite o valor da hora de trabalho: "))
Horas_do_mes=float(input("Digite o numero de horas trabalhadas no mês: "))
salario_bruto = (Hora_Trabalhada*Horas_do_mes)
ir= salario_bruto * 0.11
inss= salario_bruto *0.08
sindicato= salario_bruto *0.05
print("IR (11%) R$:",ir)
print("INSS (8%) R$:",inss)
print("SINDICATO (5%) R$:",sindicato)
salario_liquido= salario_bruto - ir,inss,sindicato
print("Salário Liquido, R$:",salario_liquido)

