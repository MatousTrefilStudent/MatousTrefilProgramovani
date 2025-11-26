import math
import random
import tkinter as tk
import time

def Monte_Carlo_PI(attempts):
    insideCircle = 0
    for i in range(attempts):
        if math.sqrt(random.random()**2+random.random()**2)<1:
            insideCircle+=1

    return insideCircle*4/attempts

def Monte_Carlo_PI_displayed(attempts):
    root=tk.Tk()
    root.title()
    root.geometry("550x700")

    c=tk.Canvas(root,width=550,height=550)

    c.create_oval(25, 25, 525, 525, width = 3)

    Attempts_Label = tk.Label(root)

    Attempts_Label.place(x=250,y=550)

    PI_Label = tk.Label(root)

    PI_Label.place(x=250,y=600)

    PI_Label.anchor("center")

    c.pack()

    inside_circle=0
    for i in range(attempts):
        x=random.random()
        y=random.random()
        color="red"
        if math.sqrt(x**2+y**2)<1:
            inside_circle+=1
            color="green"

        real_x=(250*x*([-1,1][random.randint(0,1)])+250+25)
        real_y=(250*y*([-1,1][random.randint(0,1)])+250+25)

        c.create_oval(real_x-3,real_y-3,real_x+3,real_y+3, width=2, outline=color)

        Attempts_Label.config(text="Attempts:" + str(i+1))
        Attempts_Label.pack()


        PI_Label.config(text="Current PI:" + f"{round(inside_circle*4/(i+1),5):.4f}")
        PI_Label.pack()

        c.update_idletasks()

        time.sleep(10/attempts)

        c.pack()

        

    c.mainloop()

print(Monte_Carlo_PI(1000))

Monte_Carlo_PI_displayed(1000)

