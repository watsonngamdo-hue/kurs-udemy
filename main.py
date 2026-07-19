
print("Hallo an alle")

print("a\nd")
print("\u2764")
# Bemerkung : lorsqu'on parle de casse en programmation ce sont les majuscules et les minuscules
var = "bonjour".upper()
print(var)

var = "BONJOUR".lower()
print(var)
var = "bonjour tout le monde".capitalize()
print(var)

var = "bonjour tout le monde".title()
print(var)

var = "bonjour bonjour".replace("jour","soir")
print(var)

var = "bonjour bonjour".replace(" ","")
print(var)

var = "bonjour bonjour".replace("jour","soir").replace(" ","")
print(var)

var = " bonjour ".strip()
print(var)

var = " bon jour ".strip()
print(var)

var = "1, 2, 3, 4, 5".split(", ")
print(var)
var =", ".join("1, 2, 3, 4, 5".split(", "))
print(var)
"""
while True:
    try:
        valeur = input("Entrez un nombre: ")
        if valeur.isdigit() :
           break

    except:
        print("Entrez un nombre correct") """



import  os

weg = r"C:\Users\HIGH-TECH CORP'S\PycharmProjects"
unterlagen = os.path.join(weg,"Unterlagen","test")
#if not os.path.exists(unterlagen) :
#os.makedirs(unterlagen,exist_ok= True)

if os.path.exists(unterlagen):
    os.removedirs(unterlagen)


