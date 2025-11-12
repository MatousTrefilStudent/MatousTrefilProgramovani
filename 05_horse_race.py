import random
import os
import time

def horse_race(distance, horses):
    horse_positions =[]

    for i in range(horses):
        horse_positions.append(0)

    while True:
        for i in range(horses):
            horse_positions[i] += random.randint(0,1)
            if horse_positions[i]>= distance:
                print("Winner:\t",i)
                return i 
        printHorses(distance, horse_positions)

        
def printHorses(distance, horse_positions):
    os.system('cls')
    for i in horse_positions:
        print("_"*int(i),i,"_"*int(distance - i-1))
    print()



class horse:
    def __init__(self, name, stepsPossible):
        self.name = name
        self.stepsPossible = stepsPossible

    def generate_step(self):
        return self.stepsPossible[random.randint(0, len(self.stepsPossible)-1)]
    
    def get_name(self):
        return self.name
    
    def generate_horse():
        return horse([
        "Thunder", "Shadow", "Spirit", "Blaze", "Midnight", "Silver",
        "Golden", "Star", "Iron", "Lucky", "Wind", "Dusty"
    ][random.randint(0,10)], [random.randint(0,2) for i in range(4)])

    def generate_horses(numberOfHorses):
        horses=[]
        for i in range(numberOfHorses):
            horses.append([horse.generate_horse(),0])
        
        return horses

    def horse_race(distance, numberOfHorses):
        horses = horse.generate_horses(numberOfHorses)
        
        while True:
            time.sleep(0.1)
            os.system('cls')
            for i in range(len(horses)):
                horses[i][1]+=horses[1][0].generate_step()
                print("_"*int(horses[i][1]),horses[i][0].get_name(),"_"*int(distance - horses[i][1]-1-len(horses[i][0].get_name())))
                if horses[i][1]>distance:
                    print(horses[i][0].get_name()+" je vítěz.")
                    return horses
            print()
                

                

            






for i in (horse.horse_race(100,3)):
    print(i[0].get_name(),"\t",i[0].stepsPossible,"\t",i[1])


"""
test
for i in range(20):
    h = horse.generate_horse()

    print(h.get_name(), h.stepsPossible)

    for i in range(10):
        print(h.generate_step(),end="")
    print()

"""