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

        self.createDisplay()
        self.createOperationsButtons()
        self.createNumberKeyboard()

    def createDisplay(self):
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

class operatorButton:
    def __init__(self,operation,calc,row,column):
        self.operation=operation
        self.calc=calc

        self.button = tk.Button(self.calc.operationsButtonFrame, text=self.operation, font=("Segoe UI", 15))
        self.button.grid(row=row,column=column, sticky="nsew")

    def clicked(self):
        pass


class numberButton:
    def __init__(self, number, calc):
        self.number = number
        self.system=calc.system
        self.calc=calc

 
        self.button = tk.Button(self.calc.numberButtonFrame, text=self.number, command=self.clicked).grid(row=int(number/int(math.ceil(self.system ** 0.5))),
                                                                                    column=int(number%int(math.ceil(self.system ** 0.5))),
                                                                                    sticky="nsew")
    def clicked(self):
        print(self.number)
        self.calc.writeOnDisplay(self.number)


calculator(70)


root.mainloop()