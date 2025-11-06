from random import randint, random

def random_walk(steps, space, output = False):
    position = space/2

    for i in range(steps):
        step = [-1,1][randint(0,1)]

        if 0<position+step<space:
            position+=step
        elif 0<position+step:
            return "A"
        else:
            return "B"
        if output:
            print("A", "-"*int(position - 1),"T","-"*int(space - position),"B")

def random_walk_analysis(space, steps, attempts):
    A= 0
    B= 0 
    No = 0
    for i in range(attempts):

        destination= random_walk(space,steps)
        if destination == None:
            No+=1
        elif destination == "A":
            A+=1
        elif destination == "B":
            B+=1
    return A, B, No

A,B,No = random_walk_analysis(100,10,100000)

print("A:\t",A,"\tB\t",B,"\tNe\t",No)


"""
for i in range(200):
 for i in range(1000):
    destination= random_walk(100,10)
    if destination == None:
        No+=1
    elif destination == "A":
        A+=1
    elif destination == "B":
        B+=1

 print("A:\t", A, "B:\t", B, "No:\t", No)
 A=0
 B=0
 No=0
"""



"""
def distance_random_walk(steps):
    position = 0
    for i in range(steps):
        position += [-1,1][randint(0,1)]
    return position

for i in range(100):
    distances = []
    for x in range(10000):
        distances.append(abs(distance_random_walk(i)))

    distance = sum(distances)/10000
    print("steps:\t",str(i),"\tdistance:\t",str(round(distance,3)),"\tsqrt:\t", str(i**0.5))
"""