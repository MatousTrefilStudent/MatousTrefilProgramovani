import os
def ASCII_string(number):
    return f"{ascii(chr(number))[1:-1]:<6}{bin(number)[2:]:<9}{oct(number)[2:]:<5}{number:<5}{hex(number)[2:]:<5}"
def ASCII_table():
    print(f"{"ASCII":<6}{"Bin":<9}{"Oct":<5}{"Dec":<5}{"Hex":<5}")
    for i in range(128):
        print(ASCII_string(i))

def multi_column_ASCII_table(columns):
    for i in range(128//columns+1):
        for x in range(columns):
            print (ASCII_string(i*columns+x),"|    ",end="")
        print()

"""for i in range(128):
    print(f"{i:<4}{ascii(chr(i))}")"""

#ASCII_table()



if __name__=="__main__":
    os.system("cls")

    multi_column_ASCII_table(5)