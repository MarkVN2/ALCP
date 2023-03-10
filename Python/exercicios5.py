#MARKOS VINÍCIUS NUNES DA SILVA 1º ADS
print('        ===EXERCICIO_1===\n')
x = 2
y = 5

if y > 8 :
    y = y * 2
else:
    x = x * 2

print(x + y)

print('        ===EXERCICIO-2===\n')
x = 0

for i in range(1,10):
    if i != 3 :
        for j in range(1,7):
            x = x + 1
print(x)  
print("        ===EXERCICIO_3===\n")
x = 0
i = 0
for i in range(1067,3628):
    if i % 7 == 0 and i % 2:
        x += 1
print(x)

print("        ===EXERCICIO_4===\n")
x = 0
i = 0
for i in range(18644,33088):
    if '2' in str(i) and '7' not in str(i): 
        x += 1 
print(x)
print("        ===EXERCICIO_5===\n")