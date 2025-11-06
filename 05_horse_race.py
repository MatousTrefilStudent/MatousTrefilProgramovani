import random
import os
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





horse_race(100,2)

"""
test
for i in range(20):
    h = horse.generate_horse()

    print(h.get_name(), h.stepsPossible)

    for i in range(10):
        print(h.generate_step(),end="")
    print()

"""