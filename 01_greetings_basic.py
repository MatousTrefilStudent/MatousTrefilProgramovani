# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

import os

# Vymazání obrazovky terminálu (Windows)
os.system("cls")

##############################################################
### Základní verze - vždy stejná odpověď

name=""
surname=""
# Získání jména a příjmení od uživatele
while not (type(name)==type("abc") and len(name)>2):
    name = input("Jméno:\t\t")
while not (type(surname)==type("abc") and len(surname)>2):
    surname = input("Příjmení:\t")




# Generování pozdravu bez náhodného prvku a zobrazení v terminálu
print("Ahoj "+name+" "+surname+", přeji hezký den!")

##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání
# vytvořit greetings jako list pozdravů

import random

pozdravy = ["Dobrý den "+name+", neznáme se? Můj strejda máb taky příjmení "+surname, "Nazdar "+ name + " " + surname+"."]

print(pozdravy[random.randint(0,len(pozdravy)-1)])

##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

random.seed()



##############################################################
### *verze - pozdrav podle denní doby

from datetime import datetime

hour = datetime.now().hour

if (hour<6):
    print("Ahoj "+name+" "+surname+", vypadá to že ses probudil brzy, je" + str(hour) +" hodin.")
elif (hour<12):
    print("Dobré ráno "+name+" "+surname+", rád vás vidím je "+str(hour)+" hodin. Rád tě vidím, máš toho ještě dneska spoustu před sebou!")
elif (hour<20):
    print("Dobré odpoledne "+name+" "+surname+"je "+str(hour)+" hodin, a zbývá ti jich "+str(20-hour)+" do 8 hodin")
else:
    print("Je "+str(hour)+" hodin, jdi spát "+ name+" "+surname)
