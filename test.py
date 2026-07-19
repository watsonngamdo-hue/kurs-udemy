


#for i in range (1,10):
    #print("utilisateur",i)
"""
nbre1 = input("Entrez un premier nombre :")
nbre2 = input("Entrez un deuxieme nombre :")

while not( nbre1.isdigit()  and  nbre2.isdigit()):
    print("Veuillez entrer deux nombres valides")
    nbre1 = input("Entrez un premier nombre :")
    nbre2 = input("Entrez un deuxieme nombre :")
print(f"Le résultat de l'addition de {nbre1} avec{nbre2} est égal à {int(nbre1) + int(nbre2)}" )



liste = []
while True :
    print("Choississez parmi les options suivantes : \n 1: Ajouter un element a la liste \n 2: Retirer un element de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
    wahl = input ("Votre choix :")
    print("-" * 50)
    if wahl == str(1) :
        element1 = input ("Entrez le nomd'un element a ajouter a la liste de course :")
        liste.append(element1)
        print(f"l'element {element1} a bien ete ajouter a la liste")

    elif wahl == str(2):
        element2 = input ("Entrez le nom d'un element a retirer de la liste de course :")
        if element2 in liste :
            liste.remove(element2)
            print(f"l'element {element2} a bien ete retirer a la liste")
        else :
            print(f"l'element {element2} n'est pas dans la liste")

    elif wahl == str(3):
        for i, element in enumerate(liste):
            print(f"{i}. {element}")

    elif wahl == str(4) :
        liste.clear()
        print(" La liste a ete videe de son contenu")
    elif wahl == str(5):
        print(" A bientot ")
        break
    else:
        print("Entrez un nombre entre 1 et 5")

nbre1 = input("Entrez un nombre :")
while not  nbre1.isdigit() :
    print(" erreur saisissez un nombre correct ")
    nbre1 = input("Entrez un nombre :")
if int(nbre1) % 2 == 0:
    print(" le nombre esy pair")
else :
    print(" le nombre est impair")

import random
r = random.randint(1,100)
nbre_de_tour = input(" Geben Sie die Anzahl der Versuche ein :")

while not nbre_de_tour.isdigit():
    print("Geben Sie ein richtige zahl")
    nbre_de_tour = input(" Geben Sie die Anzahl der Versuche ein :")

i = 1
while i <= int(nbre_de_tour):
    while True:
        try :
            spiler = int(input("Geben Sie ein zahl zwinschen 1 et 100 ein :"))
            break
        except:
            print("Geben Sie ein richtige zahl")


    if r == int(spiler):
        print("bingo, Sie haben gewonnen ")
        break
    else:
        print("Nein falsche Anworte , versuchen Sie noch einmal ")
        if r < int(spiler):
            print("Sie befinden sich uber")
            print(f"Es fehlen nur { int(nbre_de_tour) -i}")
            print("-" * 50)
        elif r > int(spiler):
            print("Sie befinden sich unten")
            print(f"Es fehlen nur {int(nbre_de_tour) - i}")
            print("-" * 50)
        i += 1
        if i <= int(nbre_de_tour):
            continue
        else:
            print("Sie haben das Spiel verloren")

import random

# jeux
i = 3
Lebenspunkt = 50
gegner_lebenspunkt = 50
print(" Los geht's :) :) :) ")
while Lebenspunkt > 0 and gegner_lebenspunkt > 0 :
    while True:
        try:
            spielerwahl = int(input("Mochtest du angreifen (1) oder einen Trank verwenden (2) ? :"))
            # if not (int(spielerwahl) == 1 or int(spielerwahl) == 2):
            if int((spielerwahl)) in [1, 2]:
                break
            else:
                print("Wahlen Sie zwinchen 1 oder 2 ein")
        except:
            print("Wahlen Sie zwinchen 1 oder 2 ein")

    if spielerwahl == 1 :
        Feindlicher_Angriff = random.randint(5, 15)
        Angriff_ausgefuhrt = random.randint(5, 10)
        Lebenspunkt = Lebenspunkt - Feindlicher_Angriff
        gegner_lebenspunkt = gegner_lebenspunkt - Angriff_ausgefuhrt
        print(f"Sie haben {Angriff_ausgefuhrt} Schadenspunkte verursacht \u2694\ufe0f ")
        print(f"Der Gegner hat dir {Feindlicher_Angriff} Punkte zugefugt \u2694\ufe0f")
        print(f"Dir felhen {Lebenspunkt} Punkte")
        print(f"Dem Gegner felhen {gegner_lebenspunkt} Punkte")
        print("-"*50)

    else :

        if i > 0 :
            trank = random.randint(15, 50)
            Feindlicher_Angriff = random.randint(5, 15)

            print(f"Sie bekommen {trank} Lebenspunkte ({i - 1} \u2764\ufe0f bleiben ubrig )")
            Lebenspunkt = Lebenspunkt + trank
            print(f"Der Gegner hat dir {Feindlicher_Angriff} punkte zugefugt \u2694\ufe0f")
            Lebenspunkt = Lebenspunkt - Feindlicher_Angriff
            print(f"Dir felhen {Lebenspunkt} Punkte ")
            print(f"Dem Gegner felhen {gegner_lebenspunkt} Punkte")
            i -=1
            print("-" * 50)
            if Lebenspunkt > 0 :
                Feindlicher_Angriff = random.randint(5, 15)
                print("Sie setzen eine Runde aus ...")
                print(f"Der Gegner hat dir {Feindlicher_Angriff} zugefugt \u2694\ufe0f")
                Lebenspunkt = Lebenspunkt - Feindlicher_Angriff
                print(f"Dir felhen {Lebenspunkt}")
                print(f"Dem Gegner felhen {gegner_lebenspunkt} Punkte")
                print("-" * 50)

            else:
                print("Sie haben verloren")
        else :
            print("Sie haben keine Lebenstranke mehr")
            print("-" * 50)
if Lebenspunkt > gegner_lebenspunkt :
    print(" Sie haben gewonne :) !!!")
else :
    print(" schade, Sie haben verloren :( ") """

# Kurs uber Dateien
import random

"""
weg = 

with open(weg,"r") as f:
    inhalte = f.read().splitlines()
    print(inhalte)

with open(weg,"w") as p :
    p.write("Servus")

with open(weg, "a") as v :
    v.write("Valdes") 


import json
#weg = r"C:\sers\HIGH-TECH CORP'S\est 2.json"
with open(weg, "w") as f:
    json.dump(list(range(10)),f, indent=2)

with open(weg, "r") as f:
    #json.dump(list(range(10)),f, indent=2)
    liste = json.load(f)
    print(type(liste)) 

# bearbeitung eines json dateien

import json

#weg = r"C:\sers\HIGH-TECH CORP'S\est 2.json"

with open(weg , "r") as f:
    datein = json.load(f)

datein.append(4)

with open(weg , "w") as f:
    json.dump(datein,f, indent=4) 

# Einkaufslistenubung mit Sparen
import json
import os

CUR_DIR = os.path.dirname(__file__)
weg = os.path.join(CUR_DIR, "liste.json")
#weg = r"C:\sers\HIGH-TECH CORP'S\PycharmProjects\demy_python_Ausbildung"
if os.path.exists(weg):
    with open(weg, "r") as f:
        liste = json.load(f)
else:
    liste = []

# script
while True :
    print("Choississez parmi les options suivantes : \n 1: Ajouter un element a la liste \n 2: Retirer un element de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
    wahl = input ("Votre choix :")
    print("-" * 50)
    if wahl == str(1) :
        element1 = input ("Entrez le nom d'un element a ajouter a la liste de course :")
        liste.append(element1)
        print(f"l'element {element1} a bien ete ajouter a la liste")

    elif wahl == str(2):
        element2 = input ("Entrez le nom d'un element a retirer de la liste de course :")
        if element2 in liste :
            liste.remove(element2)
            print(f"l'element {element2} a bien ete retirer a la liste")
        else :
            print(f"l'element {element2} n'est pas dans la liste")

    elif wahl == str(3):
        for i, element in enumerate(liste):
            print(f"{i}. {element}")

    elif wahl == str(4) :
        liste.clear()
        print(" La liste a ete videe de son contenu")
    elif wahl == str(5):
        with open(weg, "w") as f:
            json.dump(liste, f, indent=4)
        print(" A bientot ")
        break
    else:
        print("Entrez un nombre entre 1 et 5") 

# Die Nutzung von Path

from pathlib import Path

print(Path.home())
print(Path.cwd())
p = Path.cwd()
print(p.parent)

weg =  Path.home()
weg1 = weg / "super"/"main.py"
weg2 = weg.joinpath("super","main.py")
print(weg1)
print(weg2)
print(weg1.suffix) # entweder weg1 = (weg / "super"/"main.py").suffix oder weg2 = weg.joinpath("super","main.py").suffix

m = Path(r"C:\sers\HIGH-TECH CORP'S\PycharmProjects\index.html.txt")
print(m.name)
print(m.parent) # man kann auch m.parent.parent machen 
print(m.stem)
print(m.suffix)
print(m.suffixes)
print(m.parts)
print(m.exists())
print(m.is_dir())
print(m.is_file()) 

# 2
from pathlib import Path
p = Path.home()

p = p /"Dossiertest"
print(p)

p.mkdir(exist_ok= True) # wenn die Datei bereits exietiert, wird kein Fehlermeldung zuruckgegeben und die Datein wird nicht loschen
p = p/"1"/"2"/"3"
#p.mkdir(parents=True)
p.mkdir(exist_ok= True)
p= p/"readme.txt"
p.touch() # um ein Datein zu erstellen
#p.mkdir(exist_ok= True)
p.unlink() # um ein Datei zu loschen
p = p.parent
#p.rmdir() # man kann nur rmdir verwenden, wenn die Unterlagen leer ist, nur !!!! B.z : ich kann nicht die Unterlagen 1 loschen, weil sie die Unterlagen 2 und 3 enthalt.

import shutil

shutil.rmtree(p) 

from pathlib import Path

p = Path.home()/"Pathlib"

p.mkdir(exist_ok= True)
p = p/"read.txt"
p.touch()

p.write_text("Bonjour")

print(p.read_text()) 

# Anderer Teil
from pathlib import Path

#Path.home().iterdir()
#for f in Path.home().iterdir():
#    print(f.name)
#for f in Path.home().iterdir():
    #if f.is_dir(): # dir = Unterlagen , file = Datein / is_file()
        #print(f.name)
#[print(f.name) for f in Path.home().iterdir() if f.is_dir()]

p = Path.home().glob("*.m") # glob suche dans le dossier et rglob suche soger les sous dossiers

for f in p :
    print(f.name) 

# Anderer Teil
from pathlib import Path

p = Path.home()/ "image.png"

p =p.parent/(p.stem +"_lowers"+p.suffix) # Das Ziel war, diesen Weg zu erstellen

print(p) 

# Anderer Teil : Ubung

from pathlib import Path

dirs = {".png":"Images",
        ".jpeg":"Images",
        ".jpg":"Images",
        ".gif":"Images",
        ".mp4":"Videos",
        ".mov":"Videos",
        ".zip":"Archives",
        ".pdf":"Documents",
        ".txt":"Documents",
        ".json":"Documents",
        ".mp3":"Musiques",
        ".mav":"Musiques"}

tri_dir = Path.home()/"Tri"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files :
    output_dir = tri_dir/ dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok =True)
    f.rename(output_dir/f.name) 
# Die Trennung von Datein per Grosse
from pathlib import Path

tri_dir = Path.home()/"Tri"/"Documents"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files :
    output_dir = Path.home()/"Tri"/"Documents"/"tri"
    output_dir.mkdir(exist_ok=True)
    if f.stat().st_size < 100000 :
        f.rename(output_dir / f.name) 

from pathlib import Path

tri_dir = Path.home()/"Tri"/"Documents"
files = [f for f in tri_dir.iterdir() if f.is_file()]
files_sorted = sorted(files,key=lambda f: f.stat().st_size)
output_dir = Path.home()/"Tri"/"Documents"/"Ordre"
output_dir.mkdir(exist_ok=True)

for f in files_sorted:
    #output_dir = Path.home()/"Tri"/"Documents"/"Ordre"
    #output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name) 

films = {
    "Le Seigneur des Anneaux": 12,
    "Harry Potter": 9,
    "Blade Runner": 7.5
}
print(films.get("prenom","Dieser Wert exitiert nicht"))
films["Blade Runner"]= 9
films["age"]=10
print(films)
del films["age"]
print(films)
print(films.keys())
print(films.values())
# Kurs
 for cle in dictionnaire :
    print(cle)
    print(dictionnaire[cle]) 
    
Oder
for cle,valeur in dictionnaire.items():
    print(cle, valeur )


employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

del employes["id03"]
employes["id02"]["age"]=26
age_paul = employes["id01"]["age"]
print(employes) 

# Projekt 1 
from pathlib import Path

Datein ={
    ".mp3" : "Musique",
    ".wav":"Musique",
    ".flac" :"Musique",
    ".avi"  : "Videos",
    ".mp4" :"Videos",
    ".gif":"Videos",
    ".bmp" : "Images",
    ".jpg": "Images",
    ".png": "Images"
}

weg = Path.home()/"Documents1"
liste =[ files for files in weg.iterdir() if files.is_file()]

for files in liste :
    weg1 = weg/Datein.get(files.suffix,"Divers")
    weg1.mkdir(exist_ok=True)
    files.rename(weg1/files.name) 
    
# projekt 2
from pathlib import Path

weg = Path.home()/"Documents1"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for film,title in d.items():
    weg = weg/film
    weg.mkdir(exist_ok=True)
    for v in title :
        weg = weg/v
        weg.mkdir()
        weg = weg.parent
    weg = Path.home()/"Documents1"

# Andere Methode 

for film in d :
    weg = weg/film
    weg.mkdir(exist_ok= True)
    
    for dir in d[film]:
        weg = weg/dir
        weg.mkdir()
        weg = weg.parent
    weg = Path.home()/"Documents1" 

# Projekt 3

from pathlib import Path

weg = Path.home()/"Documents1"/"Name.txt"

with open(weg, "r") as f:
    lines = f.read().splitlines()
prenoms = []
for line in lines:
    prenoms.extend(line.split())

ende_Name = [prenom.strip(",. ") for prenom in prenoms]

weg = Path.home()/"Documents1"/"Name_bearbeiten"

with open(weg, "w") as f:
    f.write("\ n".join(sorted(ende_Name))) 

# Anderer Teil
a= 5
b= 3
try:
    Ergebnis = a/ b
except ZeroDivisionError:
    print("Abteilung durch Null ist unmogilch")
except TypeError:
    print("Variable b ist kein guter Typ")
except NameError as f:
    print("Fehler:", f)
else :   #Wird nur ausgefurht, wenn Try bereits ausgefuhrt wurde
    print(Ergebnis)
finally: #wird immer ausgefurht
    print("Fin du bloc.") 

# Aufgabe
from pathlib import Path
weg = input("Entrez le chemin du fichier : ")

try:
    with open(weg, "r") as f:
      inhalte = f.read()
      print(inhalte)
except UnicodeDecodeError:
    print("Impossible d'ouvrir ce fichier")
except FileNotFoundError:
    print(" le fichier est introuvable.") """

# Funktion
# Annotation
# def add (a:int = 2.4 , b:int = 4  ) -> int :
#     return a+b

# add(3.1 , 2.3)
# def add() -> list[int]:
#     return [1, 2, 3]


#import mein_module

# import package

# package.users.get_users()

# Les Docstrings
# def fonction_example(nom, age) :
#     """
#     Beschreibung meines funktion
#     Args:
#         nom (str) :  der Benutzername
#         age (int) : Alter des Nuzter
#
#     Returns:
#         list : Liste der Zahlen
#     """
#     return [1, 2, 3]

# Das Logging
"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log", # normalement je dois donner le nom d'un chemin de fichier dans lequel je voudrais ecrire mes log
                    filemode="a",
                    format= '%(asctime)s - %(levelname)s - %(message)s') # man kann - durch irgendetwas ersetzen ( wie :)

logging.debug(" die Funktion wurde gut ausgefuhrt")
logging.info(" Allgemeine Infortionsmitteilung")
logging.warning("Achtung")
logging.error(" ein Fehler ist angekommen")
logging.critical(" Kritischer Fehler")

"""



print("Valdes Dieu t'aime ")

























