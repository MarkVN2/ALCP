
import random


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