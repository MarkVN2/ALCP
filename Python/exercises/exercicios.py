#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS
import sys
sys.set_int_max_str_digits(302000)

print("        ===EXERCICIO_1===\n")
print(" Soma de dois números inteiros.\n")

x = int(input("Por favor me diga o primeiro número\n"))
y = int(input("Por favor me diga o segundo número\n"))
z = str(x + y)

print(f"\nA soma dos dois números é {z}\n")

input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO-2===\n")
print("Conversão de metros para milímetros\n")

m = float(input("Por favor me diga o valor em metros\n"))
mm = m * 1000

print (f"\nO valor convertido é de {mm:.0f}mm.\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_3===\n")
print("Conversão de dias,horas,minutos e segundos em um total de segundos.\n")

day = int(input("Número de dias para serem convertidos é?\n"))
hr = int(input("\nQuantas horas a serem convertidas\n"))
mn = int(input("\nNúmero de minutos para a conversão\n"))
sec = int(input("\nSegundos a serem adicionados para a conta final\n"))

t_sec = ((day*24)*3600) + (hr*3600) + (mn * 60) + sec

print (f"\nO total de segundos é de {t_sec}\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_4===\n")
print("Calculo para acrescimo percentual ao salario\n")

sal = float(input("Qual o seu salario atual?\n"))
per = float(input("\nAgora me diga qual foi o percentual acrescentado.\n"))
sal_a = sal * (per/100)
sal_n = sal + sal_a

print(f"\nO seu novo salario é de R${sal_n:.2f} tendo um acrescimo de R${sal_a:.2f} \n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_5===\n")
print("Calculo para preço reduzido de um produto em uma promoção\n")

prod = float(input("Qual o preço do produto?\n"))
p_des = float(input("\nQual é a porcentagem da promoção?\n"))
desc = prod * p_des/100
t_prod =  prod - desc

print(f"\nO preço a se pagar com o desconto é de R${t_prod:.2f} tendo uma redução no preço da mercadoria de R${desc:.2f}\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_6===\n")
print("Calculo de tempo necessario para percorrer uma distancia especifica.\n")

dist = float(input("A distancia a ser percorrida em quilometros é de?\n"))
mspeed = float(input("\nQual é a velocidade média do veiculo (km/h)?\n"))

t = dist/mspeed

print(f"\nO tempo necessario para se chegar ao destino é de {t:.1f} horas.\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_7===\n")
print("Conversor de Celsius para Fahrenheit.\n")
#Conversão de °C para °F é F = 9*C/5 + 32

c = float(input("Temperatura em Celsius\n"))
f = 9*c/5 + 32

print(f"\nA temperatura convertida é de {f:.1f}°F.\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_8===\n")
print("Conversor de Fahrenheit para Celsius.\n")

f = float(input("\nTemperatura em Fahrenheit\n"))
c = (f - 32) * 5/9

print(f"\nA temperatura convertida para Celsius é {c:.1f}°C\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_9===\n")
print(" Calculo do preço a se pagar ao alugar um carro em que o preço por dia é de R$60 e por quilometro R$0.15 \n")

d_alugado = float(input("Por quantos dias o carro foi alugado?\n"))
km_rodado = float(input("\nPor quantos quilometros o carro andou?\n"))
t_prod = d_alugado*60 + km_rodado*0.15

print (f"\nO total a ser pago é de R${t_prod:.2f}\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_10===\n")

print("Tempo de vida perdido por fumar cigarros.\n")

cig_dia = int(input("Quantos cigarros são fumados por dia?\n"))
cig_ano = int(input("Quantos anos fumando?\n"))
cig_vid = ((cig_dia*10)*(cig_ano*365))/1440

print (f"O número de dias perdidos por fumar é de {cig_vid:.2f}\n")
input("Aperte Enter para prosseguir...\n") #Aqui só para não fazer os resultados passarem muito rapido.

print("        ===EXERCICIO_11===\n")
print("Quantos digitos tem em dois elevado a um milhão?\n")

v = (2 ** (10**6))
d = len (str(v))
#Excendendo o limite, não achei solução sem que eu tivesse de aumentar o limite
#Aumentei o limite para 302000 de 4300 (Python 3.11.2)
print (f"Há {d} digitos em dois elevado a um milhão.")