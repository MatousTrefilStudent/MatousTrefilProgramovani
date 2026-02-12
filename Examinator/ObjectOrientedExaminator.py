import os
import random
from datetime import datetime

questions  = []

def loadQuestions(path):
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        for i in files:
            if os.path.isfile(os.path.join(path, i)) and os.path.join(path, i).endswith('.txt'):
                with open(os.path.join(path, i), 'r', encoding='utf-8') as f:
                    author = f.readline().split(":")[1][1::].replace("\n","")
                    """print(author)"""

                    file = f.readlines()

                    answers = []
                    
                    for x, line in enumerate(file):
                        if "Otázka: " in line and x > 1 and file[x-1]==file[x-2]=="\n" and file[x+1][1]==file[x+2][1]==file[x+3][1]==file[x+4][1]==";" and ((file[x + 5] == "\n") if x + 5 < len(file) else True):
                            """print(line[8::].replace("\n",""))"""
                            """print(file[x+1:x+5])"""
                            for answer in file[x+1:x+5]:
                                answers.append(answer.replace("\n",""))
                            """print(f"answers:{answers}\n")"""

                            questions.append(Question(author, i, line[8::].replace("\n",""),answers))
                            answers = []
    else:
        print("Neexistuje složka Testy_zdroj_otazek, program nemůže být spuštěn.")
        input()
        exit()

    if len(questions)<15:
        print("Nebyl vložen dostatek otázek, program nemůže být spuštěn.")
        input()
        exit()


class Question:
    def __init__(self, author, file, question, answers):
        self.author = author
        self.file = file
        self.question = question
        self.answers = answers
        pass

    def __str__(self):
        return f"Autor: {self.author} \nSoubor: {self.file}\n\nOtázka: {self.question} \n{self.answers[0]}\n{self.answers[1]}\n{self.answers[2]}\n{self.answers[3]}\n"
    
class SpecificQuestion(Question):
    def __init__(self, generalQuestion):
        super().__init__(generalQuestion.author, generalQuestion.file, generalQuestion.question, generalQuestion.answers)
        shuffle = random.sample(range(0, len(self.answers)), len(self.answers))
        self.correctAnswer=""
        self.letteredAnswers=[]
        for i in range(len(self.answers)):
            self.letteredAnswers.append(f"{chr(i+65)}) {self.answers[shuffle[i]][3::]}")

            if self.answers[shuffle[i]][0]=="1":
                self.correctAnswer =chr(i+65)

    def __str__(self):
        return f"Autor: {self.author} \nSoubor: {self.file}\n\nOtázka: {self.question} \n{self.letteredAnswers[0]}\n{self.letteredAnswers[1]}\n{self.letteredAnswers[2]}\n{self.letteredAnswers[3]}\n"
    

class Test:
    def __init__(self, numberOfQuestions, name):
        self.questions=[]
        shuffle = random.sample(range(0, len(questions)), numberOfQuestions)
        for i in shuffle:
            self.questions.append(SpecificQuestion(questions[i]))
        self.name=name
        self.wrongAnswers=[]
        self.scale="<100-90>,(90-75>,(75-60>,(60-45>,(45-0>"
        
    
    def __str__(self):
        temp=""
        for i in self.questions:
            temp += str(i)
        return temp
    
    def administerTest(self):
        for question in self.questions:
            os.system("cls")
            print(f"Student: {self.name}")
            print(f"Otázka: {self.questions.index(question)+1}/{len(self.questions)}")
            print(question)
            answer = input("Správná odpověď:\t").replace(")","")
            if answer == question.correctAnswer:
                print("Správně")
            else:
                print("Špatně")
                self.wrongAnswers.append(question)
            input()
        self.giveGrade()
        os.system("cls")
        print(f"""
Vypracoval/a:               {self.name}
Otázek v testu:             {len(self.questions)}
Výsledná známka:            {self.grade}
Procentní úspěšnost:        {(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100}%
Stupnice:                   {self.scale}
Datum a čas vyhodnocení:    {datetime.now().strftime("%d.%m.%Y, %H:%M:%S")}

----------------------
Chybně zodpovězeno:

{"\n".join(str(i) for i in self.wrongAnswers)}----------------------
""")
        self.saveResults("Examinator/Vysledky_testu/")


    def giveGrade(self):
        self.grade=0
        for grade, i in enumerate(self.scale.split(",")):
            if ((i[0] == "<" and int(i[i.index("<")+1:i.index("-")])>=(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100) or 
                (i[0] == "(" and int(i[i.index("(")+1:i.index("-")])>(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100)) and (
                (i[-1] == ">" and int(i[i.index("-")+1:i.index(">")])<=(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100) or 
                (i[-1] == ")" and int(i[i.index("-")+1:i.index(")")])<(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100)):
                self.grade =grade+1


    def saveResults(self, path):
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.makedirs(path, exist_ok=True)
        with open(f"{path}{self.name.replace(" ","_")}_{datetime.now().strftime("%d%m%Y_%H%M%S")}_{len(self.questions)}_{self.grade}.txt","w",encoding="utf-8") as f:
                f.write(f"""
Vypracoval/a:               {self.name}
Otázek v testu:             {len(self.questions)}
Výsledná známka:            {self.grade}
Procentní úspěšnost:        {(len(self.questions)-len(self.wrongAnswers))/len(self.questions)*100}%
Stupnice:                   {self.scale}
Datum a čas vyhodnocení:    {datetime.now().strftime("%d.%m.%Y, %H:%M:%S")}

----------------------
Chybně zodpovězeno:

{"\n".join(str(i) for i in self.wrongAnswers)}----------------------
""")
                f.close()


if __name__ == "__main__":
    loadQuestions("Examinator/Testy_zdroj_otazek")
    name = input("Jménu:\t\t")
    while len(name)<4:
        name = input("Vlož skutečné jméno:\t")

    surName = input("Příjmení:\t")
    while len(name)<4:
        surName = input("Vlož skutečné Příjmení:\t")
    
    numberOfQuestions = 0
    while True:
        numberOfQuestions = input("Počet otázek:\t")
        try:
            numberOfQuestions = int(numberOfQuestions)
            if numberOfQuestions>=len(questions):
                print(f"Nevložili jste validní počet otázek, je jich méně než celkový počet({len(questions)})")
            else:
                break
        except ValueError:
            print("Nevložili jste validní počet otázek")

    while True:
        
        Test(numberOfQuestions, f"{name} {surName}").administerTest()

        option = input("Nový test (1)\nNový test s jiným studentem (2)\nUkončit aplikaci(3)\n\nCo chcete udělat dál(napište čislo v závorkách)?:")

        if "1" in option:
            pass
        elif "2" in option:
            name = input("Jménu:\t\t")
            while len(name)<4:
                name = input("Vlož skutečné jméno:\t")

            surName = input("Příjmení:\t")
            while len(name)<4:
                surName = input("Vlož skutečné Příjmení:\t")

            numberOfQuestions = 0
            while True:
                numberOfQuestions = input("Počet otázek:\t")
                try:
                    numberOfQuestions = int(numberOfQuestions)
                    if numberOfQuestions>=len(questions):
                        print(f"Nevložili jste validní počet otázek, je jich méně než celkový počet({len(questions)})")
                    else:
                        break
                except ValueError:
                    print("Nevložili jste validní počet otázek")

        elif "3" in option:
            break


"""
def giveAGrade(number):
    for grade, i in enumerate("<100-90>,(90-75>,(75-60>,(60-45>,(45-0>".split(",")):
            print(i)
            print(i[0] == "<" and int(i[i.index("<")+1:i.index("-")])>=number)
            print(i[0] == "(" and int(i[i.index("(")+1:i.index("-")])>number)
            print(i[-1] == ">" and int(i[i.index("-"):i.index(">")])<=number)
            print(i[-1] == ")" and int(i[i.index("-"):i.index(")")])<number)
            if ((i[0] == "<" and int(i[i.index("<")+1:i.index("-")])>=number) or 
                (i[0] == "(" and int(i[i.index("(")+1:i.index("-")])>number)) and (
                (i[-1] == ">" and int(i[i.index("-")+1:i.index(">")])<=number) or 
                (i[-1] == ")" and int(i[i.index("-")+1:i.index(")")])<number)):
                print(number, str(grade+1))

for i in range(101):
    giveAGrade(i)
"""