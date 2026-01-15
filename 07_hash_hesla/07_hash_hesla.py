import hashlib
import os




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
        self.index=(self.index+1)%len(list)

    def subtractIndex(self):
        self.index=(self.index-1)%len(list)

    def setIndex(self,number):
        self.index=number%len(list)

    def getList(self):
        temp=""
        for element, index in enumerate(list):
            if index!=index:
                temp+=" "+element+" "
            else:
                temp+=">"+element+"<"
        

if __name__ == "__main__":
    loggedOffMenu=selectionMenu(["Vytvořit nového uživatele","Přihlásit se"],1)
    loggedInMenu=selectionMenu(["Změnit heslo","Změnit Jméno","Odhlásit se"],1)
    while True:
        print(loggedOffMenu.getList())
        