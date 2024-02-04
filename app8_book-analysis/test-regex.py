import re
from pprint import pprint

with open("miracle_in_the_andes.txt") as file:
    book = file.read()

#print(book)

# It's a string
print(f"Type: {type(book)}")


#####################################################
# HOW MANY CHAPTERS ARE THERE IN THE BOOK ?
#####################################################

## With string methods:
print(f"Chapthers with string methods: {book.count('Chapter')}")

## With regex:
# el signo + significa que debe haber 1 o mas números
# el signo * significa que debe haber 0 o mas numeros
pattern = re.compile("Chapter [0-9]+")
chapters = re.findall(pattern, book)
print(f"Chapthers with string methods: {len(chapters)} ")
print(chapters)
print()



#####################################################
# Which are the sentences where "love" vas used?
#####################################################
print("\nWhich are the sentences where 'love' vas used?")
pattern = re.compile("[a-zA-Z ,]* love [a-zA-Z ,]*")
love = re.findall(pattern, book)
#pprint(love) # uso pprint() para que se vea mejor
print(f"Size love: {len(love)}")

# Otra forma de hacerlo:
print("\nOther way: Which are the sentences where 'love' vas used?")
# el signo ^ es negacion
pattern = re.compile("[^.]* love [^.]*")
love = re.findall(pattern, book)
#pprint(love) # uso pprint() para que se vea mejor
print(f"Size love: {len(love)}")

# NO estamos capturando todos los casos
# ya que por ejemplo puede aparecer "love,"

# el siguiente patron lo que hace es decir que no queremos
# que haya letras minusculas ni mayusculas antes ni despues de
# la palabra "love". De esta forma puede haber signos de puntuacion
pattern = re.compile("[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*")
love = re.findall(pattern, book)
#pprint(love) # uso pprint() para que se vea mejor
print(f"\nThe correct size of love: {len(love)}")
print()
print()

# el anterior patron empieza cada oracion con un espacio
# esto se debe a que luego de un punto siempre hay un espacio
# para solucionar esto, podemos usar el siguiente patron
# que dice que haya solamente 1 letra mayuscula al principio
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*")
love = re.findall(pattern, book)
#print(love) # uso pprint() para que se vea mejor
print(f"\nThe ultimate size of love: {len(love)}")
print()
print()



#####################################################
# What are the most used words?
#####################################################
pattern = re.compile("[A-Za-z]+")
# transformo el book a minusculas para que poder comparar palabras
findings = re.findall(pattern, book.lower())
#print(findings)
print(f"Size findings: {len(findings)}")

d = {}
for word in findings:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
#print(d)

d_list = [(value, key) for key, value in d.items()]
d_list.sort(reverse=True)
print(d_list[:10])