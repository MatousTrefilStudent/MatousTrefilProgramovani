import hashlib
import os
import time
import keyboard



def newUser(name, password):
    if isNameTaken(name):
        print("Name is taken")
    else:
        with open("07_hash_hesla/users.txt", "a", encoding="utf-8") as f:
            f.write(f"{name};{hashPassword(name,password)}\n")

def isNameTaken(name):
    with open("07_hash_hesla/users.txt", "r", encoding="utf-8") as f:
        for i in f.readlines(-1):
            if name == i.split(";")[0]:
                return True
    return False

def hashPassword(name,password):
    return hashlib.sha256((name+password).encode()).hexdigest()

def login(name, password):
    with open("07_hash_hesla/users.txt", "r", encoding="utf-8") as f:
        for i in f.readlines(-1):
            if name == i.split(";")[0]:
                if hashPassword(name,password) == i.split(";")[1].strip():
                    print("logged in")
                    return True
                else:
                    print("wrong password")
                    return False
    print("name doesn´t exits")

class selectionMenu:
    def __init__(self, list, bgnIndex):
        self.index=bgnIndex

        self.list=list
    
    def getIndex(self):
        return self.index
    
    def getChoice(self):
        return self.list[self.index]
    
    def addIndex(self):
        self.index=(self.index+1)%len(self.list)

    def subtractIndex(self):
        self.index=(self.index-1)%len(self.list)

    def setIndex(self,number):
        self.index=number%len(self.list)

    def getList(self):
        temp=""
        for index, element in enumerate(self.list):
            if index!=self.index:
                temp += f" {element} \n"
            else:
                temp += f">{element}<\n"

        return temp
    
"""https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer"""
"""def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def tabPressed(menu):
    os.system("cls")
    print(loggedInName)
    menu.addIndex()
    print(menu.getList())

def enterPressed(menu):
    os.system("cls")
    input = menu.getChoice()
    if input == "Vytvořit nového uživatele":
        createNewUser()
    elif input == "Přihlásit se":
        loginUI()
    flush_input()
    
def createNewUser():
    print("Vytvořit nového uživatele")
    flush_input()
    name = input("Jméno:\t")
    while isNameTaken(name):
        name = input("Už takové jméno existuje, zvolte jiné:")
    password = input("Password:\t")
    newUser(name, password)
    tabPressed(loggedOffMenu)
    time.sleep(1)

def loginUI():
    print("Přihlásit se")
    name = input("Jméno:\t")
    password = input("Heslo:\t")
    if login(name,password) == True:
        loggedInName=name
        keyboard.on_press_key("tab", lambda e: tabPressed(loggedInMenu))
        keyboard.on_press_key("enter", lambda e: enterPressed(loggedInMenu))

if __name__ == "__main__":
    loggedOffMenu=selectionMenu(["Vytvořit nového uživatele","Přihlásit se"],1)
    loggedInMenu=selectionMenu(["Změnit heslo","Změnit Jméno","Odhlásit se"],1)

    keyboard.on_press_key("tab", lambda e: tabPressed(loggedOffMenu))
    keyboard.on_press_key("enter", lambda e: enterPressed(loggedOffMenu))
    loggedInName=""
    tabPressed(loggedOffMenu)
    
    while True:
        pass"""