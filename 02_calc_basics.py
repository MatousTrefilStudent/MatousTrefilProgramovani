import os
import csv


os.system('cls')




while True:
    try:
        firstNumber= float(input("Prvni cislo:\t"))
        secondNumber= float(input("Druhe cislo:\t"))
        break
    except ValueError:
        print("Hodnota, kterou si vložil je neplatná.")

print(str(firstNumber)+"\t+\t"+str(secondNumber)+"\t=\t"+str(firstNumber+secondNumber))
print(str(firstNumber)+"\t-\t"+str(secondNumber)+"\t=\t"+str(firstNumber-secondNumber))
print(str(firstNumber)+"\t*\t"+str(secondNumber)+"\t=\t"+str(firstNumber*secondNumber))

if secondNumber==0:
    print("Dělení nulou, nelze provést operaci")
else:
    print(str(firstNumber)+"\t/\t"+str(secondNumber)+"\t=\t"+str(firstNumber/secondNumber))

inputWriteCSV=""

while inputWriteCSV != "ANO" and  inputWriteCSV != "ANO":

    inputWriteCSV = input("Chcete uložit výsledky do csv souboru? ANO/NE\t")

if inputWriteCSV == "ANO":
    with open('calc_basics_vysledky.csv', 'w', newline='') as file:
        writer=csv.writer(file)

        writer.writerow(["Operace","Produkt"])

        writer.writerow(["+",firstNumber+secondNumber])
        writer.writerow(["-",firstNumber-secondNumber])
        writer.writerow(["*",firstNumber*secondNumber])
        if secondNumber == 0:
            writer.writerow(["/","Dělení nulou, nelze provést operaci"])
        else:
            writer.writerow(["/",firstNumber/secondNumber])

