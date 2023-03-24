#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS

print('        ===EXERCICIO_1===')
print('VERIFICAR SE UM TRIANGULO EXISTE E QUAL TIPO ELE É\n')

a = float(input('Me diga o primeiro número: '))
b = float(input('Me diga o segundo número: '))
c = float(input('Me diga o terceiro número: '))

if a < b + c and b < a + c and c < b + a :
    exist = True
    if exist == True and a == b == c :
        print('O triangulo existe e é quadrilatero')
    elif exist == True and a != b == c or b != a == c  or c != a == b :
        print('O triangulo existe e é isosceles')
    else :
        print('O triangulo existe e é escaleno')
else :
    print('O triangulo não existe')

input('\nAperte Enter para prosseguir...\n') #Aqui só para não fazer os resultados passarem muito rapido.

print('        ===EXERCICIO-2===')
print('DETERMINAR SE UM ANO É BISSEXTO\n')

yr = int(input('Ano a se determinar: '))

if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0 :
    print('O ano é bissexto.\n')
else :
    print('O ano não é bissexto.\n')
    
input('Aperte Enter para prosseguir...\n') 

print('        ===EXERCICIO_3===')
print('CALCULO PARA MULTA POR EXCEDER O LIMITE DE PESO PARA PEIXES\n')

p_p = float(input('Peso dos peixes : '))

if p_p > 50 :
    excess = p_p - 50
    fine = excess * 4
    
    print(f'Excesso no peso de peixes: {excess}kg')
    print(f'Valor da Multa: R${fine:.2f}')
else :
    excess = 0
    fine = 0
    print(f'Excesso no peso de peixes: {excess}kg')
    print(f'Valor da Multa: R${fine:.2f}')

input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_4===')
print('PROGRAMA PARA DESCOBRIR O MAIOR DENTRE OS NÚMEROS DADOS\n')

a = float(input('Me diga o primeiro número: '))
b = float(input('Me diga o segundo número: '))
c = float(input('Me diga o terceiro número: '))

if a > b and c :
    print(f'{a} é o maior')
elif b > c and a :
    print(f'{b} é o maior')
else :
    print(f'{c} é o maior')

input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_5===')
print('DESCOBRIR QUAL NÚMERO É O MAIOR E QUAL É O MENOR ENTRE 3 NÚMEROS\n')

a = float(input('Me diga o primeiro número: '))
b = float(input('Me diga o segundo número: '))
c = float(input('Me diga o terceiro número: \n'))

if a== b == c:
    print('Todos os números são iguais\n')
else:
    if a >= b and a >= c:
        print(f'{a} é o maior número.\n')
    elif b >= a and b >= c:
        print(f'{b} é o maior número.\n')
    elif c >= a and c >= a:
        print(f'{c} é o maior número.\n')
    if a <= b and a <= c:
        print(f'{a} é o menor número.\n')
    elif b <= a and b <= c:
        print(f'{b} é o menor número.\n')
    elif c <= a and c <= a:
        print(f'{c} é o menor número.\n')

input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_6===')
print('CALCULO DE SALARIO BRUTO,LIQUIDO E DESCONTO DO INSS E SINDICATO\n')

ghr = float(input('Qual é o pagamento por uma hora de trabalho? '))
whr = float(input('Quantas horas são trabalhadas por mês? '))

salary = ghr * whr

syn = salary * 5/100
ir = salary * 11/100
inss = salary * 8/100
liquid = salary - (inss + ir + syn)

print(f'\nSeu salário bruto é de R${salary:.2f} e seu liquido é R${liquid:.2f}')
print(f'Se foi pago R${inss:.2f} ao INSS.')
print(f'Se foi pago R${syn:.2f} ao sindicato.\n')

input('Aperte Enter para prosseguir...\n')

print('        ===EXERCICIO_7===\n')
print('CALCULO DE QUANTAS LATAS E O CUSTO QUE SERÃO NECESSARIOS PARA PINTAR UMA REGIÃO')

mpaint = float(input('Quantos M² serão pintados? '))

cans_l = round(mpaint/3)
cans = round(cans_l/18)
price = round(cans)*80 

print(f'Serão necessarias {cans} latas de tinta.')
print(f'Totalizando um preço de R${price:.2f}.')