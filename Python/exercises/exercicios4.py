#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS
import random
print('        ===EXERCICIO_1===\n')
print('Sorteio de 10 números inteiros dentre 1 a 100 e descobrir o maior e o menor dentre eles\n')
lista = random.sample(range(1,101),10)
maior = 0
menor = 0
def maioremenor(v):
    maior = v[0]
    menor = v[0]
    for n in v :
        if n > maior :
            maior = n
        elif n < menor:
            menor = n
    v.sort()
    return maior , menor
print(f'A lista criada : {lista}')
print('Nela o maior é ' + str(maioremenor(lista)[0]) + ' e o menor é ' + str(maioremenor(lista)[1]) + '\n')
input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO-2===\n')
print('Sorteio de 20 números inteiros entre 1 e 100 armazenando os números impares e pares em uma lista extra, após tudo demonstrar todos os resultados em 3 listas.\n')

lista = random.sample(range(1,101),20)
par = []
impar = []
for p in lista:
    if p%2 == 0 :
       par.append(p)
    else:
       impar.append(p)

print(f'''Números originais: {lista}
Impares : {impar}
Pares :{par}\n''')
input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_3===\n')
print('Criar dois vetores de 10 elementos aleatorios entre 1 e 100 e desses vetores criar uma terceirade 20 elementos com valores intercalados dos vetores.\n')

lista = random.sample(range(1,101),10)
lista2 = random.sample(range(1,101),10)
lista3 = []
def intercalar(lista,lista2):
    for k in range(0,10):
        lista3.append(lista[k])
        lista3.append(lista2[k])
    return lista3

print(f'A lista 1 : {lista}')
print(f'A lista 2 : {lista2}')
print(f'A lista com intercalação é : {intercalar(lista,lista2)}\n')
input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_4===\n')
print('Apartir do texto dado criar uma lista de palavras que começam ou terminam com umas das letras em "python" e imprimir a lista resultante.\n')
lista.clear()
text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'
text = text.replace(',','').replace('.','').replace(':','').lower().split()

def pythonica(text):
    for p in text :
        l = p[0]
        if l in 'python':
            lista.append(p)
        l = p[-1]
        if l in 'python':
            lista.append(p)
    return lista

print(f'Há {len(pythonica(text))} palavras que possuem uma das letras de "python".\n')
input('\nAperte Enter para prosseguir...\n')

print('        ===EXERCICIO_5===\n')
print('Usando o mesmo texto do exercicio 4 utilize-se da função split() e  calcule quantas palavras com mais de 4 letras possuem alguma letra das letras de "python".\n')
text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'
text = text.replace(',','').replace('.','').replace(':','').lower().split()
lista = []

def pythonicus(text):
    for p in text :
        if 4 < len(p):
            for l in p :
                if  l in 'python':
                    lista.append(p)
                    break
    return lista
print(f'Há {len(pythonicus(text))} palavras com mais de 4 letras que possuem uma das letras de "python".\n')
