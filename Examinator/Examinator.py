import os
import random
from datetime import datetime

questions = []

def loadQuestions(path):
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        for i in files:
            if os.path.isfile(os.path.join(path, i)) and os.path.join(path, i).endswith('.txt'):
                questions.append([i])
                with open(os.path.join(path, i), 'r', encoding='utf-8') as f:
                    questions[-1].append(f.read())
    else:
        print("složka s otázkami nebyla nalezena")
        input()
        exit()
    poolOfQuestions =[]
    for i in questions:
        for question in i[-1].split("\n\n")[1::]:
            poolOfQuestions.append([i[-1].split("\n\n")[0].replace("\n",""),i[0],question.replace("\n\n","")])
    if len(poolOfQuestions) <15:
        print("Test nejde spustit, protože je málo otátek")
        input()
        exit()
    
def createTest(numberOfQuestions):
    poolOfQuestions =[]
    for i in questions:
        for question in i[-1].split("\n\n")[1::]:
            poolOfQuestions.append([i[-1].split("\n\n")[0].replace("\n",""),i[0],question.replace("\n\n","")])
    
    print(range(1, len(poolOfQuestions)))
    print(numberOfQuestions)
    questionIndexes = random.sample(range(0, len(poolOfQuestions)), numberOfQuestions)

    test = []
    for i in range(numberOfQuestions):
        test.append(poolOfQuestions[questionIndexes[i]])

    return test

def printQuestion(name, surName, numberOfQuestion, numberOfAllQuestions, author, file, question):
    print("Student:",name,surName)
    print("Otázka\t",numberOfQuestion," / ", numberOfAllQuestions)
    print("Autor:\t",author[author.index(":")+2::])
    print("Soubor:\t",file)

    print()

    correctAnswer = ""
    answers = []
    for i in (question.split("\n")):
        if ";" in i:
            answers.append(i[3::])
            if i[0] == "1":
                correctAnswer=i[3::]
        else:
            print(i)

    letteredAnswers = []
    shuffle = random.sample(range(0, len(answers)), len(answers))
    for i in range(len(answers)):
        print(chr(i+65),") ",answers[shuffle[i]])

        if correctAnswer == answers[shuffle[i]]:
            correctAnswer =[chr(i+65),answers[shuffle[i]]]
    
    return correctAnswer


def newTest():
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
            break
        except ValueError:
            print("Nevložili jste validní počet otázek")
    test = (createTest(numberOfQuestions))


    wrongAnswers= []
    for i in enumerate(test):
        os.system("cls")
        correctAnswer = (printQuestion(name, surName, i[0]+1, numberOfQuestions, i[1][0], i[1][1], i[1][2]))

        answer = input("\nLetter of the correct answer:\t ")

        print()
        if answer == correctAnswer[0]:
            print("Správná odpověď")
        else:
            wrongAnswers.append(i[1]), answer
            print("Špatná odpověď")

        input()

    result = []

    scale = "<100-90>,(90-75>,(75-60>,(60-45>,(45-0>"

    result.append(str("Vypracoval/a:\t\t"+name+" "+surName))

    result.append(str("Otátek v testu:\t\t"+str(numberOfQuestions)))

    grade=0
    for i in enumerate(scale.split(",")):
        if int(i[1][1:i[1].index("-")])>=(((numberOfQuestions-len(wrongAnswers))/numberOfQuestions)*100)>=int(i[1][i[1].index("-")+1:-1]):
            grade=i[0]+1
            result.append(str("Výsledná známka:\t"+str(i[0]+1)))


    result.append(str("Procentní úspěšnost:\t"+str(str(((numberOfQuestions-len(wrongAnswers))/numberOfQuestions)*100)+"%")))

    result.append(str("Stupnice:\t\t"+str(scale)))

    result.append(str("Datum a čas vyhodnocení:"+str(datetime.now().strftime("%d.%m.%Y, %H:%M:%S"))))

    result.append("")
    result.append("----------------------")
    result.append("Chybně zodpovězeno:")
    result.append("")
    result.append("")

    for i in wrongAnswers:
        for x in i:
            for y in x.split("\n"):
                result.append(y)
        result.append("")

    result.append("----------------------")

    for i in result:
        print(i)

    f = open("Examinator/Vysledky_testu/"+str(name+"_"+surName+"_"+str(datetime.now().strftime("%d.%m.%Y_%H:%M:%S")).replace(":","").replace(".","")+str(len(questions)))+str(grade)+".txt", "w")

    "valek_vladislav_20241006_132845_10_2.txt"

"""print(questions)"""
"""for i in questions:
    for x in i:
        print(x)"""

if __name__ == "__main__":
    loadQuestions("Examinator/Testy_zdroj_otazek")


    newTest()
