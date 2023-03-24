#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS
print("        ===EXERCICIO_1===\n")
print("Verificar se um número está entre 0 e 10.\n")
nota = int(input("Me diga uma nota de 0 a 10:\n"))

while nota > 10 or nota <0 :
   nota = int(input("Por favor me diga uma nota de 0 a 10\n"))

print("Obrigado pela avaliação.")

input('\nAperte Enter para prosseguir...\n')

print("        ===EXERCICIO-2===\n")
print("Cadastro de Nome e Senha e verifica se são iguais.\n")

name = input("Nome do cadastro:\n")
password = input("Senha do cadastro:\n")

while name == password :
    print("ERRO--NOME e SENHA iguais.\n")
    print("Por favor reescreva as informações\n")
    name = input("Nome do cadastro: ")
    password = input("Senha do cadastro: ")

print("Cadastro foi um SUCESSO!")

input('\nAperte Enter para prosseguir...\n')

print("        ===EXERCICIO_3===\n")
print("Calculo de Crescimento de População A e B até A ultrapassar ou igualar B.\n")

hab_a = 80000
hab_b = 200000

count = 0

while hab_a < hab_b :
    hab_a *= 1.03
    hab_b *= 1.015
    count += 1 

print(f'Habitantes A: {hab_a:.2f}\nHabitantes B: {hab_b:.2f}\nAnos passados: {count}')

input('\nAperte Enter para prosseguir...\n')

print("        ===EXERCICIO_4===\n")
print("descobre o número de fibonacci de um certo número inteiro.\n")

n = int(input("Me diga um número para a sequencia de fibonacci: "))
a = 0
b = 1
c = 1
count = 0

while count != n:
    c = a + b
    a = b
    b = c
    count += 1
    print(f"{a,b}\n")
print(f"O número {n} na sequencia de fibonacci acaba em {b}")

input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_5===')
print("Calculo de MDC usando o algoritmo de Euclides\n")

a = int(input("Me diga o primeiro número: "))
b = int(input("Me diga o segundo número: "))
e = 1
d = 1
c = 1

while  (e != 0 or d !=0 or c != 0) and a !=0 and b != 0 :
    c = a % b 
    print(a,b,c,d,e)
    if c == 0:
        print(f"O MDC entre os números é {b}")
        break
    d = b % c
    print(a,b,c,d,e)
    if d == 0:
       print(f"O MDC entre os números é {c}")
       break
    e = c % d
    print(a,b,c,d,e)
    if e == 0 :
        print(f"O MDC entre os números é {d}")
        break
    
if a == 0:
        print(f"O MDC entre os números é {b}")

if b == 0:
        print(f"O MDC entre os números é {a}")
