import csv
import json
import os
# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
OOP_Books_Library_empty.py

# Lekce: Základy tříd v Pythonu – Knihovna

V této lekci se naučíme pracovat s třídami v Pythonu na jednoduchém příkladu správy knih v knihovně. Cílem je pochopit:
- Jak definovat třídu a její atributy
- Jak používat metody třídy
- Jak pracovat s objekty (instancemi třídy)
- Jak používat dunder metody (`__str__` pro textovou reprezentaci)
- Jak ukládat a načítat objekty v seznamu

## Zadání úkolu
Vytvoříme systém pro správu knih v knihovně, který umožní:
1. **Vytvořit třídu `Book`**, která bude obsahovat:
   - `title` (název knihy)
   - `author` (autor knihy)
   - `year` (rok vydání)
   - `available` (dostupnost knihy, výchozí hodnota `True`)
   - Metodu `borrow()`, která označí knihu jako vypůjčenou (`available = False`).
   - Metodu `return_book()`, která označí knihu jako dostupnou (`available = True`).
   - Dunder metodu `__str__`, která vypíše informace o knize v přehledném formátu.

2. **Vytvořit seznam knih** (knihovna) a přidat do něj několik knih.
3. **Implementovat jednoduchý terminálový výpis**, který umožní zobrazit seznam knih a jejich dostupnost.

## Očekávaný výstup v terminálu
    Seznam knih v knihovně:
    1984 - George Orwell (1949) | Stav: Dostupná
    To Kill a Mockingbird - Harper Lee (1960) | Stav: Dostupná   
    Mistr a Markétka - Michail Bulgakov (1967) | Stav: Dostupná  
    Malý princ - Antoine de Saint-Exupéry (1943) | Stav: Dostupná

    --- Test vypůjčení a vrácení knih ---

    Kniha '1984' byla úspěšně vypůjčena.
    Kniha '1984' je již vypůjčená.
    Kniha '1984' byla úspěšně vrácena.
    Kniha '1984' již byla dostupná.

    Aktualizovaný seznam knih v knihovně:
    1984 - George Orwell (1949) | Stav: Dostupná
    To Kill a Mockingbird - Harper Lee (1960) | Stav: Dostupná   
    Mistr a Markétka - Michail Bulgakov (1967) | Stav: Dostupná  
    Malý princ - Antoine de Saint-Exupéry (1943) | Stav: Dostupná
"""

class Book:
    """Třída reprezentující knihu v knihovně.
    Args:
        title (str): Název knihy
        author (str): Autor knihy
        year (int): Rok vydání knihy
    Attributes:
        available (bool): Označuje, zda je kniha dostupná k vypůjčení
    Methods:
        borrow(): Označí knihu jako vypůjčenou
        return_book(): Vrátí knihu zpět jako dostupnou
    """

    def __init__(self, title: str, author: str, year: int, available=True):
        self.title=title
        self.author=author
        self.year=year
        self.available=available
        
    def borrow(self):
        if not self.available:
            print("Kniha ",self.title," není dostupná, nelze jí vypůjčit.")
        else:
            print("Kniha ",self.title," byla úspěšně vypůjčena.")
            self.available=False

    def return_book(self):
        if self.available:
            print("Kniha ",self.title," už byla vrácena.")
        else:
            print("Kniha ",self.title," byla úspěšně vrácena.")
            self.available=True

    def __str__(self):
        return f"{self.title} | {self.year} | {self.author} | Stav: {"Dostupná"*self.available}{"Nedostupná"*(not self.available)}"

    @staticmethod
    def is_valid_year(year):
        try:
            int(year)
            return True
        except (ValueError, TypeError):
            return False

    @classmethod
    def load_from_CSV(cls, data):
        return cls (data["title"],
         data["author"],
         int(data["year"]))
    
    @classmethod
    def from_string(cls, string):
        return cls (string.split(";")[0],string.split(";")[1],string.split(";")[2])
    
    def to_json(self):
        return {"title" : self.title,
                "author": self.author,
                "year"  : self.year,
                "available": self.available}
"""---

## Část 2 – Dědičnost: podtřídy `Ebook` a `AudioBook`

Vytvoř dvě podtřídy dědící z `Book`:
- `Ebook` – přidá atribut `file_format` (např. `"PDF"`, `"EPUB"`, `"MOBI"`).
- `AudioBook` – přidá atribut `duration` (délka audioknihy v minutách).
- Obě třídy přepíší metodu `__str__()`, aby zobrazovaly i nové atributy.

---"""
class Ebook(Book):
    def __init__(self, title, author, year, fileFormat, available = True):
        super().__init__(title, author, year, available)
        self.fileFormat=fileFormat

    def __str__(self):
        return f"{super().__str__()} | Formát souboru: {self.fileFormat}"
    
    def to_json(self):
        return {"title" : self.title,
                "author": self.author,
                "year"  : self.year,
                "file format": self.fileFormat,
                "available": self.available}
    
class AudioBook(Ebook):
    def __init__(self, title, author, year, fileFormat, duration, available = True):
        super().__init__(title, author, year, fileFormat, available)
        self.duration=duration

    def __str__(self):
        return f"{super().__str__()} | Délka trvání: {self.duration}"
    
    def to_json(self):
        return {"title" : self.title,
                "author": self.author,
                "year"  : self.year,
                "file format": self.fileFormat,
                "duration":self.duration,
                "available": self.available}
    
"""---

## Část 3 – Kompozice: třída `Library`

Místo prostého seznamu vytvoř třídu `Library`, která bude obsahovat seznam knih.
Přidej metody:
- `add_book(book)` – přidá knihu do knihovny.
- `remove_book(title)` – odstraní knihu podle názvu.
- `list_books()` – vypíše všechny knihy v knihovně.

---"""

class Library():
    def __init__(self, name):
        self.name=name
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)

    def add_book_from_json(self,json):
        if "duration" in json:
            self.books.append(AudioBook(json["title"],json["author"],json["year"],json["file format"],json["duration"],available=json["available"]))
        elif "file format" in json:
            self.books.append(Ebook(json["title"],json["author"],json["year"],json["file format"],available=json["available"]))
        else:
            self.books.append(Book(json["title"],json["author"],json["year"],available=json["available"]))

    def remove_book(self, bookTitle):
        for i in self.books:
            if i.title==bookTitle:
                self.books.pop(self.books.index(i))

    def list_books(self):
        for i in self.books:
            print(i) 
    """---

    ## Část 4 – Ukládání a načítání dat (JSON)

    Rozšiř třídu `Library` o metody:
    - `save_to_file(filename)` – uloží seznam knih do JSON souboru.
    - `load_from_file(filename)` – načte seznam knih z JSON souboru.

    ---"""
    def save_to_file(self, filename):
        json_books=[i.to_json() for i in self.books]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(json_books, f,ensure_ascii=False, indent=2)
        f.close()

    def load_from_file(self, filename):
        
        with open(filename, "r", encoding="utf-8") as f:
            json_books = json.load(f)
        self.books=[]
        for i in json_books:
            self.add_book_from_json(i)

if __name__ == "__main__":
    

    """with open("knihy.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print(reader)
        for row in reader:
            test_book=Book.load_from_CSV(row)  
            print(test_book)

    # Seznam knih v knihovně
    library = [
        Book("1984", "George Orwell", 1949),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("Mistr a Markétka", "Michail Bulgakov", 1967),
        Book("Malý princ", "Antoine de Saint-Exupéry", 1943)
    ]

    # Výpis knih v knihovně
    print("\nSeznam knih v knihovně:")
    for i in library: print(i)

    # Simulace vypůjčení a vrácení knihy
    print("\n--- Test vypůjčení a vrácení knih ---\n")
    library[0].borrow()
    library[0].borrow()  # Pokus o vypůjčení již vypůjčené knihy
    library[0].return_book()
    library[0].return_book()  # Pokus o vrácení již dostupné knihy
    library[3].borrow() 

    # Znovu vypíšeme knihovnu po změnách
    print("\nAktualizovaný seznam knih v knihovně:")
    for i in library: print(i)"""


    """# =============================================================================
    # Testovací kód – spusť po doplnění implementace výše
    # =============================================================================

    # --- Část 1: Statické metody a metody třídy ---
    print("=== Test statických metod a metod třídy ===")
    print(f"Je rok 1984 validní? {Book.is_valid_year(1984)}")
    print(f"Je rok 1200 validní? {Book.is_valid_year(1200)}")
    tolkien = Book.from_string("Pán prstenů;J. R. R. Tolkien;1954")
    print(f"Kniha z řetězce: {tolkien}")

    # --- Část 2: Dědičnost ---
    print("\n=== Test dědičnosti ===")
    ebook = Ebook("Výzkum vesmíru", "Carl Sagan", 1980, "PDF")
    audiobook = AudioBook("Harry Potter a kámen mudrců", "J. K. Rowling",  1997, "mp3",498)
    print(ebook)
    print(audiobook)

    # --- Část 3: Třída Library ---
    print("\n=== Test třídy Library ===")
    library = Library("Městská knihovna")
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(ebook)
    library.add_book(audiobook)
    library.list_books()
    library.remove_book("1984")
    library.list_books()

    library.save_to_file("knihovnička")
    library.load_from_file("knihovnička")"""



    library = Library("Městská knihovna")

    if not os.path.isfile("knihovnička"):
        library.save_to_file("knihovnička")
    library.load_from_file("knihovnička")


    while True:
        print(
"""\n\n[1] Zobrazit knihy
[2] Přidat knihu
[3] Vypůjčit knihu
[4] Vrátit knihu
[5] Uložit a ukončit program""")
        entry = input("Číslo akce, kterou chcete provést:")
        if "1" in entry:
            library.list_books()

        elif "2" in entry:
            print("Informace o knížce, kterou chceš přidat:")
            title=input("Jméno knížky:")
            author=input("Autor knížky:")
            while True:
                try:
                    year = int(input("Rok vydání: "))
                    break
                except ValueError:
                    print("Musíš vložit číslo")
            file_format = input("Typ souboru(pokud není nechte prázdné):")
            duration = input("Doba trvání(pokud není nechte prázdné):")
            if duration.replace(" ","")=="" and file_format.replace(" ","")=="":
                library.add_book(Book(title,author,year))
            elif duration.replace(" ","")=="" and file_format.replace(" ","")!="":
                library.add_book(Ebook(title,author,year,file_format))
            elif duration.replace(" ","")!="" and file_format.replace(" ","")!="":
                library.add_book(AudioBook(title,author,year,file_format,duration))
            print("Kniha úspěšně přidána")
        
        elif "3" in entry:
            title = input("Jméno knížky, kterou si chceš pučit:")
            for i in library.books:
                if i.title==title:
                    i.borrow()
                    break
            
        elif "4" in entry:
            title = input("Jméno knížky, kterou chceš vrátit:")
            for i in library.books:
                if i.title==title:
                    i.return_book()
                    break
            
        elif "5" in entry:
            library.save_to_file("knihovnička")
            print("saved")
            break

        