import random
import os

os.system("cls")

def generate_example():
    example=[]

    example.append(random.randint(0,100))

    example.append(["+","-","*","/"][random.randint(0,3)])

    example.append(random.randint(0,100))

    return example, calculate(example)

def generate_example_by_difficulty(difficulty):
    example=[]

    for i in range(random.randint(2,difficulty*2)):
        example.append(random.randint(1,10**difficulty))

        if difficulty<4:
            example.append(["+","-"][random.randint(0,1)])
        elif difficulty<6:
            example.append(["+","+","-","-","*","/"][random.randint(0,5)]) 
        elif difficulty<8:
            example.append(["+","-","*","/"][random.randint(0,3)])
        elif difficulty<10:
            example.append(["+","-","*","*","/","/"][random.randint(0,5)])
        elif difficulty == 10:
            example.append(["+","-","*","*","/","/","**"][random.randint(0,5)])
    
    example.pop(-1)

    return example, calculate(example)



def calculate(example):
    array=example.copy()

    indexes = [i for i, x in enumerate(array) if x == "*"or x== "/"]

    subtractor = 0

    for i in indexes:
        if array[i-subtractor]=="*":
            array[i-1-subtractor]= array[i-1-subtractor]*array[i+1-subtractor]
        elif array[i-subtractor]=="/":
            array[i-1-subtractor]= array[i-1-subtractor]/array[i+1-subtractor]
        array.pop(i+1-subtractor)
        array.pop(i-subtractor)
        
        subtractor+=2


    while len(array)>1:
        if array[1]=="+":
            array[0]=array[0]+array[2]
        elif array[1]=="-":
            array[0]=array[0]-array[2]
        array.pop(2)
        array.pop(1)
        

    return array[0]

if __name__ == "__main__":
    difficulty = 1
    while True:
        number=generate_example_by_difficulty(difficulty)

        for i in number[0]:
            print(str(i)+"\t",end="")

        print("=\t",end="")

        while True:
            result = input("")
            try:
                result = float(result)
                break
            except ValueError:
                print(f"'{result}' není číslo, zkus to znova")
        
        if round(result,3) == round(number[1],3):
            difficulty+=1
            print("správně, obtížnost je zvýšena na: "+str(difficulty))
        else:
            if difficulty>1:
                difficulty-=1
            print("špatně, obtížnost je snížena na: "+str(difficulty))

    

        


        