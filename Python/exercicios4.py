#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS
import random
print('        ===EXERCICIO_1===\n')

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
print(lista)
print('O maior é ' + str(maioremenor(lista)[0]) + '\n' + 'O menor é ' + str(maioremenor(lista)[1]))

print('        ===EXERCICIO-2===\n')

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

print("        ===EXERCICIO_3===\n")

lista = random.sample(range(1,101),10)
lista2 = random.sample(range(1,101),10)
lista3 = []
def intercalar(lista,lista2):
    for k in range(0,10):
        lista3.append(lista[k])
        lista3.append(lista2[k])
    return lista3
print(intercalar(lista,lista2))


print("        ===EXERCICIO_4===\n")
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

print(pythonica(text))

print("        ===EXERCICIO_5===\n")

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
print(pythonicus(text))
