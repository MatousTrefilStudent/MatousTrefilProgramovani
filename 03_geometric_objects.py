import math
import keyboard
import time
import os

consoleMenu="abcdefg"

def consoleSelection(list: list[str]) -> str:
    """Display a console menu navigable with keyboard arrows.

    Allows user to navigate through a list of options using arrow keys
    and select an option with Enter.

    Args:
        list (list[str]): List of menu items to display.

    Returns:
        str: The selected item from the list.
    """
    index=0

    def keyboardPressed(event):
        nonlocal index
        if event.name == "up":
            index = (index - 1) % len(list)
        elif event.name == "down":
            index = (index + 1) % len(list)
        elif event.name == "enter":
            input()
            keyboard.unhook(hook)
        
        os.system("cls" if os.name == "nt" else "clear")
        print("Použij šipku nahoru/dolů pro výběr a Enter pro vybrání:")
        for i, item in enumerate(list):
            if index==i:
                print(f"> {item} <")
            else:
                print(f"  {item}")
        

    keyboardPressed(keyboard.KeyboardEvent("down", 28, "down"))
    hook=keyboard.on_press(keyboardPressed)
    while hook in keyboard._hooks:
        time.sleep(0.1)
    else:
        return list[index]

class Shape:
    """Represents a regular polygon shape.

    Supports computation of circumference and area for polygons
    defined by sides and internal angles.

    Attributes:
        name (str): Name of the shape (e.g., 'trojúhelník').
        sides (list[float]): List of side lengths.
        angles (list[float]): List of internal angles in degrees.
    """

    def __init__(self, name: str) -> None:
        """Initialize the shape with default sides and angles.

        Args:
            name (str): The name of the polygon (triangle, quadrilateral, etc.).
        """
        self.name = name
        self.sides = []
        self.angles = []
        if name == "trojúhelník":
            self.sides = [1 for i in range(3)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        elif name == "čtyřúhelník":
            self.sides = [1 for i in range(4)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        elif name == "pětiúhelník":
            self.sides = [1 for i in range(5)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        elif name == "šestiúhelník":
            self.sides = [1 for i in range(6)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        elif name == "sedmiúhelník":
            self.sides = [1 for i in range(7)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        elif name == "osmiúhelník":
            self.sides = [1 for i in range(8)]
            self.angles = [180 - 360/(len(self.sides)) for i in range(len(self.sides))]
        print(self.sides)
        print(self.angles)

    def circumference(self) -> float:
        """Calculate the circumference (perimeter) of the polygon.

        Returns:
            float: The sum of all sides (total perimeter).
        """
        circumference = 0
        for i in self.sides:
            circumference += i
        return circumference

    def area(self) -> float:
        """Compute the total area of the polygon.

        Returns:
            float: The area of the polygon rounded to three decimals.
        """
        return round(self.calculateArea(self.sides.copy(), self.angles.copy()),3)

    def calculateArea(self, sides: list[float], angles: list[float]) -> float:
        """Recursively compute polygon area using triangle decomposition.

        The algorithm calculates the area of one triangle and recursively
        subtracts triangles until the whole polygon area is obtained.

        Args:
            sides (list[float]): List of polygon side lengths.
            angles (list[float]): List of polygon internal angles in degrees.

        Returns:
            float: The computed polygon area.
        """
        area =  math.sin(math.radians(angles[0])) * sides[0] * sides[1] / 2
        newSide = math.sqrt(sides[0]**2 + sides[1]**2 - 2 * sides[0] * sides[1] * math.cos(math.radians(angles[0])))
        sides.pop(0)
        sides[0] = newSide
        firstNewAngle = angles[0] - math.degrees(math.asin(sides[1] * math.sin(math.radians(angles[0])) / newSide))
        lastNewAngle = angles[-1] - (180 - math.degrees(math.asin(sides[1] * math.sin(math.radians(angles[0])) / newSide)) - angles[0])
        angles.pop(0)
        angles[0] = firstNewAngle
        angles[-1] = lastNewAngle

        if len(sides)+1== 3:
            return area
        else:
            a= self.calculateArea(sides, angles)
            return area + a

    def newInput(self, sides: list[float], angles: list[float]) -> None:
        """Set custom values for sides and angles.

        Args:
            sides (list[float]): New list of side lengths.
            angles (list[float]): New list of internal angles.
        """
        self.sides = sides
        self.angles = angles

    def sameSidesInput(self, side: float) -> None:
        """Set all sides to the same length.

        Args:
            side (float): Length to assign to all sides.
        """
        self.sides = [side for i in self.sides]

def drawPolygon(sides: list[float], angles: list[float]) -> None:
    """Draw a polygon using matplotlib.

    The function plots a polygon defined by given side lengths and angles.

    Args:
        sides (list[float]): List of side lengths.
        angles (list[float]): List of internal angles in degrees.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    points = [[0,0]]
    currentAngle = 0

    for i, side in enumerate((sides)):
        currentAngle += angles[i-1]
        newX = points[-1][0] + side * math.cos(math.radians(currentAngle))
        newY = points[-1][1] + side * math.sin(math.radians(currentAngle))
        points.append([newX, newY])
    
    points.append(points[0])
    points = np.array(points)

    plt.figure()
    plt.plot(points[:,0], points[:,1], marker='o')
    plt.title('Polygon')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

shape = consoleSelection(["trojúhelník", "čtyřúhelník", "pětiúhelník", "šestiúhelník", "sedmiúhelník", "osmiúhelník"])
print(shape)
firstShape = Shape(shape)

actions = ["Změnit všechny strany na jednu hodnotu", "Změnit hodnotu pro libovolné strany a úhly", "Vypočítat obvod", "Vypočítat obsah", "Vykresli v MathPlotLib","Konec"]

while True:
    print("Co chcete udělat?")

    action = consoleSelection(actions)
    if action == actions[0]:
        while True:
            try:
                length = float(input("Zadejte hodnotu stran: "))
                if length > 0:
                    break
                else:
                    print("Hodnota strany musí být kladné číslo.")
            except ValueError:
                print("Hodnota musí být číslo.")
        firstShape.sameSidesInput(length)

    elif action == actions[1]:
        sides = firstShape.sides.copy()
        angles = firstShape.angles.copy()
        while True:
            menu =[]
            for i, side in enumerate(sides):
                menu.append(str(str(i)+". strana\t=\t"+ str(side)))
            for i, angle in enumerate(angles):
                menu.append(str(str(i)+". úhel\t=\t"+ str(angle)))
            menu.append("Zkontroloval jsem, že jsou strany a úhly v pořádku a chci je zadat.(původně to tenhle program měl dělat sám, ale to je na mě moc složité)")
            change = consoleSelection(menu)
            os.system("cls" if os.name == "nt" else "clear")
            
            if change == menu[-1]:
                firstShape.newInput(sides, angles)
                break

            for i in menu:
                if change == i:
                    print(i,"<-this will be replaced by new value")
                else:
                    print(i)
            while True:
                try:
                    newValue = float(input("Zadejte novou hodnotu pro " + change.split("\t")[0] + ": "))
                    if newValue > 0:
                        break
                    else:
                        print("Hodnota musí být kladné číslo.")
                except ValueError:
                    print("Hodnota musí být číslo.")

            if int(menu.index(change)) < len(sides):
                sides[menu.index(change)] = newValue
            else:
                angles[menu.index(change)-len(sides)] = newValue

    elif action == actions[2]:
        print("Obvod je: "+str(firstShape.circumference()))
    elif action == actions[3]:
        print("Obsah je: "+str(firstShape.area()))
    elif action == actions[4]:
        drawPolygon(firstShape.sides, firstShape.angles)
    input("\nEnter pro další akci...")
