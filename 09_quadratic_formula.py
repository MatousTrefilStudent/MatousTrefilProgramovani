import prg_library
import random

def get_coefficients():
    print(f"a ")
    a=prg_library.get_float_input()
    while a==None or a ==0:
        print("a nesmí být 0")
        a= prg_library.get_float_input()
    
    print(f"b ")
    b=prg_library.get_float_input()

    print(f"c ")
    c=prg_library.get_float_input()

    return a,b,c

def get_Discriminant(a,b,c):
    return b**2-4*a*c

def solve_quadratic(a,b,c):
    D= get_Discriminant(a,b,c)
    if D<0:
        return 0, []
    elif D==0:
        return 1, [-b/(2*a)]
    elif D>0:
        return 2, [(-b - D**0.5)/(2*a),(-b + D**0.5)/(2*a)]
    
def solve_quadratic_inequality(coefficients, sign):
    a,b,c=coefficients
    number_of_roots, roots = solve_quadratic(a,b,c)
    if number_of_roots == 0:
        return None
    if number_of_roots == 1:
        if "=" in sign:
            return f"{roots}"
        else:
            return None
    elif number_of_roots == 2:
        result = ""
        if a*(min (roots)-1)**2 +  b*(min (roots)-1) + c>0:
            if ">" in sign:
                result += f"(-Oo, {min (roots)}"
                if "=" in sign:
                    result +=">"
                else:
                    result +=")"
        else: 
            if "<" in sign:
                result += f"(-Oo, {min (roots)}"
                if "=" in sign:
                    result +=">"
                else:
                    result +=")"

        vertex = (roots[0]+roots[1])/2
        if a*(vertex)**2 +  b*(vertex) + c>0:
            if ">" in sign:
                result += " u "
                if "=" in sign:
                    result += f"<{min (roots)},{max (roots)}>"
                else:
                    result += f"({min (roots)},{max (roots)})"
        else: 
            if "<" in sign:
                result += " u "
                if "=" in sign:
                    result += f"<{min (roots)},{max (roots)}>"
                else:
                    result += f"({min (roots)},{max (roots)})"

        if a*(max (roots)+1)**2 +  b*(max (roots)+1) + c>0:
            if ">" in sign:
                
                if "=" in sign:
                    result +="<"
                else:
                    result +="("
                result += f"{max (roots)},+Oo)"
        else: 
            if "<" in sign:
                
                if "=" in sign:
                    result +="<"
                else:
                    result +="("
                result += f"{max (roots)},+Oo)"
    return result


    
def factor_quadratic(a,b,c):
    number_of_roots, roots = solve_quadratic(a,b,c)

    if number_of_roots==0:
        return f"rovnice nelze faktorizovat"
    else:
        return f"{a}(x - {roots[0]})(x - {roots[-1]})"
    
def easy_equation_generator():
    x1=0.1
    x2=0.2
    while int(x1)!= x1 or int(x2)!=x2:
        a,b,c = random.randint(1,100)*[1,-1][random.randint(0,1)], random.randint(0,100), random.randint(0,100)
        result = solve_quadratic(a,b,c)
        if result[0]!=0:
            x1=result[1][0]
            x2=result[1][-1]

    return(a,b,c)

