import math
import random
import tkinter as tk

def Monte_Carlo_PI(attempts):
    insideCircle = 0
    for i in range(attempts):
        if math.sqrt(random.random()**2+random.random()**2)<1:
            insideCircle+=1

    return insideCircle*4/attempts

def Monte_Carlo_PI_displayed(attempts):
    root=tk.Tk()
    root.title()
    root.geometry("550x550")

    c=tk.Canvas(root,width=550,height=550)

    c.create_oval(25, 25, 525, 525, width = 3)

    c.pack()

    inside_circle=0
    for i in range(attempts):
        x=random.random()
        y=random.random()
        if math.sqrt(x**2+y**2)<1:
            inside_circle+=1

        real_x=(250*x*([-1,1][random.randint(0,1)])+250+25)
        real_y=(250*y*([-1,1][random.randint(0,1)])+250+25)

        c.create_oval(real_x-1,real_y-1,real_x+1,real_y+1)

    c.mainloop()

print(Monte_Carlo_PI(1000))

Monte_Carlo_PI_displayed(123)

