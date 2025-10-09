# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: Matoš Trefil
DATUM: 2024-10-09
-----------------------------------------------------------------
"""

import os

os.system("cls")


##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)

# Načtení čísel
a=float(input("Zadej první číslo: "))
b=float(input("Zadej druhé číslo: "))

# a) Sčítání

print(a,"+",b,"=",str(a+b))

# b) Dělení a celočíselné dělení
print(a,"/",b,"=",str(a/b))
print(a,"//",b,"=",str(int(a/b)))


##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla

# Načtení čísla

a = float(input("Zadej číslo: "))

# a) Třetí odmocnina

print("Třetí odmocnina čísla",a,"je",a**(1/3))

# b) Druhá odmocnina

print("Druhá odmocnina čísla",a,"je",a**(1/2))

##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.

my_savings = float(input("Zadej částku, kterou máš našetřenou: "))
my_interest = .1

print("Po přidání 10% úroků budete mít:",my_savings*(1+my_interest))


##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek

# a) Načtení řetězců

a = input("Zadej první řetězec: ")
b = input("Zadej druhý řetězec: ")

# b) Zkontrolujte délku řetězců

if len(a) == len(b):
    print("Oba řetězce jsou stejné délky.")
else:
    print("Řetězce nejsou stejné délky.")

# c) Spojení řetězců

print("Spojené řetězce:", a + b)

##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"

# Načtení čísla

a = int(input("Zadej číslo: "))

# b) Výpis čísel

for i in range(1, a+1):
    print(i,end="")
    if i % 5 == 0:
        print("\tPátý krok!")
    else:
        print("")

##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu

# a) Vytvoření slovníku

person = {}

# b) Načtení údajů od uživatele

name = input("Zadej jméno: ")
age = float(input("Zadej věk: "))
city = input("Zadej město: ")

# Přidání údajů do slovníku

person["name"] = name
person["age"] = age
person["city"] = city

# c) Výpis slovníku

print(person)

##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa

# Načtení čísel

result =  float(input("Zadej výsledek: "))
score = float(input("Zadej skóre: "))

# a) Použití f-string

print(f"Výsledek je {result}\n Skóre je {score}")

# b) Použití f-string s přesností na 2 desetinná místa

print(f"Výsledek je {round(result,2)}\n Skóre je {round(score,2)}")

##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky seznamu

# a) Vytvoření seznamu

my_list = []
for i in range(5):
    my_list.append(input("Zadej prvek seznamu: "))

# b) Třetí prvek

print("3. Prvek:\t",my_list[2])

# c) Poslední dva prvky

print("Poslední dva prvky:\t",my_list[-2:])

##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí

# a) Vytvoření seznamu a přidání nového prvku

my_list = ["a", "z", "c"]
my_list.append("e")

print(my_list)

# b) Odstranění prvku na zvoleném indexu

my_list.pop(int(input("index prvku k odstranění:\t")))

# c) Seřazení seznamu

my_list.sort()
print(my_list)

##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple

# a) Vytvoření tuple

array = [input("Zadej prvek tuple: ") for i in range(3)]

my_tuple = (array[0], array[1], array[2])

# b) První prvek

print("1.:\t",my_tuple[0])

# c) Poslední prvek

print("-1:\t",my_tuple[-1])

##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()

# a) Vytvoření tuple a použití metody count()

my_tuple = (1, 2, 3, 2, 4, 2, 5)

element = int(input("Zadej prvek, jehož výskyty chceš spočítat:\t"))

count = my_tuple.count(element)
print("Počet výskytů:\t",count)

# b) Použití metody index()

print("Místo výskytu:\t"+str(my_tuple.index(element)))

##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě

# a) Vytvoření tuple

tuple = (1, 2, 3)

# b) Pokus o změnu prvku

while True:
    try:
        tuple[0] = 5
    except TypeError:
        print("Chyba: Tuple je neměnný, nelze měnit jeho prvky.")
        break
    else:
        break

##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##