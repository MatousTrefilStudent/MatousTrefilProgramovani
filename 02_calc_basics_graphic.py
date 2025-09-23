import tkinter as tk
import math

global system


root=tk.Tk()

root.title("Kalkulačka")

root.geometry("300x500")

class calculator:
    def __init__(self, system):
        
        self.system=system

        self.displayFrame=tk.Frame(root)
        self.displayFrame.pack(side="top", fill="x")

        self.operationsButtonFrame=tk.Frame(root)
        self.operationsButtonFrame.pack(side="top",fill="both")

        self.numberButtonFrame=tk.Frame(root)
        self.numberButtonFrame.pack(side="top",fill="both",expand=True)

        self.number=[]
        self.operations=[]

        self.createDisplay()
        self.createOperationsButtons()
        self.createNumberKeyboard()

    def createDisplay(self):
        self.operationsDisplayText=""
        self.operationsDisplayVar = tk.StringVar()
        self.operationsDisplay=tk.Label(
                        self.displayFrame,
                        textvariable=self.operationsDisplayVar,
                        text=self.operationsDisplayText,
                        font=("Arial", 10),
                        anchor="e",
                        bg="white")
        self.operationsDisplay.pack(fill="x")
        
        self.displayText=""
        self.displayVar = tk.StringVar()
        self.display=tk.Label(
                        self.displayFrame,
                        textvariable=self.displayVar,
                        text=self.displayText,
                        font=("Arial", 40),
                        anchor="e",
                        bg="white")
        self.display.pack(fill="x")

    def writeOnOperationsDisplay(self, text):
        self.operationsDisplayText=text
        self.operationsDisplayVar.set(text)

    def writeOnDisplay(self, text):
        self.displayText=text
        self.displayVar.set(text)

    def createOperationsButtons(self):
        self.newSystemButton=tk.Button(self.operationsButtonFrame, 
                                       text="/\\Nová číselná soustava/\\",
                                       font=("Segoe UI", 15),
                                       command=self.newSystemFromDisplay)
        self.newSystemButton.grid(sticky="nsew",columnspan=4,row=0,column=0)

        [ self.operationsButtonFrame.grid_columnconfigure(i, weight=1) for i in range(4) ]

        self.plus=operatorButton("+",self, 1,0)
        self.minus=operatorButton("-",self, 1,1)
        self.multiply=operatorButton("*",self, 1,2)
        self.divide=operatorButton("/",self, 1,3)

        self.newSystemButton=tk.Button(self.operationsButtonFrame, 
                                       text="=",
                                       font=("Segoe UI", 15),
                                       command=self.calculatePressed)
        self.newSystemButton.grid(sticky="nsew",columnspan=4,row=4,column=0)


    def newSystemFromDisplay(self):
        self.newSystem(int(self.displayText))

    def newSystem(self, system):
        maxRow = max(widget.grid_info()['row'] for widget in self.numberButtonFrame.winfo_children())
        maxCol = max(widget.grid_info()['column'] for widget in self.numberButtonFrame.winfo_children())

        for i in range(maxRow + 1):
            self.numberButtonFrame.grid_rowconfigure(i, weight=0)
        for i in range(maxCol + 1):
            self.numberButtonFrame.grid_columnconfigure(i, weight=0)

        for widget in self.numberButtonFrame.winfo_children():
            widget.destroy()

        self.system=system

        self.createNumberKeyboard()

    def createNumberKeyboard(self):
        self.buttons=[]
        for i in range(self.system):
            self.buttons.append(numberButton(i, self))

        for i in range(int(math.ceil(self.system ** 0.5))):
            if not (math.ceil(self.system ** 0.5)*(math.ceil(self.system ** 0.5)-1)>self.system and i == int(math.ceil(self.system ** 0.5))-1):
                self.numberButtonFrame.grid_rowconfigure(i, weight=1)
            self.numberButtonFrame.grid_columnconfigure(i, weight=1)

    def calculatePressed(self):
        self.operationPressed("=")

        print(self.calculateAddSubtract(self.operations))

    def calculateAddSubtract(self, operations):
        result=fromSystem(operations[0], self.system)
        i=1
        while i < len(operations)-1:
            operation=operations[i]
            number=fromSystem(operations[i+1], self.system)

            if operation=="+":
                result+=number
            elif operation=="-":
                result-=number

            i+=2

        return result

    def operationPressed(self, operation):
        self.operations.append(self.number)
        self.number=[]

        self.operations.append(operation)
        self.writeOnOperationsDisplay(self.operationsDisplayText+self.displayText+" "+operation+" ")

        self.writeOnDisplay("")

    def numberPressed(self, number):
        self.number.append(number)
        self.writeOnDisplay(self.displayText+str(number))


class operatorButton:
    def __init__(self,operation,calc,row,column):
        self.operation=operation
        self.calc=calc

        self.button = tk.Button(self.calc.operationsButtonFrame, text=self.operation, command=self.clicked, font=("Segoe UI", 15))
        self.button.grid(row=row,column=column, sticky="nsew")

    def clicked(self):
        self.calc.operationPressed(self.operation)


class numberButton:
    def __init__(self, number, calc):
        self.number = number
        self.system=calc.system
        self.calc=calc

 
        self.button = tk.Button(self.calc.numberButtonFrame, text=self.number, command=self.clicked).grid(row=int(number/int(math.ceil(self.system ** 0.5))),
                                                                                    column=int(number%int(math.ceil(self.system ** 0.5))),
                                                                                    sticky="nsew")
    def clicked(self):
        self.calc.numberPressed(self.number)

def fromSystem(number, system):
    result=0
    for i in range(len(number)):
        result+=number[len(number)-1-i]*(system**i)
    return result


calculator(10)


root.mainloop()


"""Notes for tomorrow:

Display the result
    in correct system
    clear operations and number lists
    allow further operations on result

Button for clearing everything
    clear operations and
    number lists
    clear displays

Keyboard input
    numbers
    operations
    enter for equals
    backspace for deleting last number/operation

Allow switching systems mid-calculation
    convert all numbers in operations list to new system

Parenteces
    correct order of operations
    nested parentheses

Multiply and divide
    correct order of operations
    divide by zero handling

Other operations
    power
    square root
    factorial
    logarithm
    trigonometric functions

EXTRA:
    History of calculations, option to save into csv
    constant buttons (pi, e, golden ratio, ...)

EXTRA EXTRA:
    complex numbers
"""