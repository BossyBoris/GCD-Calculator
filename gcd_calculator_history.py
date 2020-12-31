## Author: Boris Chan
## Date: 06/12/2016
## Purpose: Storing previous history with read and write txt

import os

def clear():
    if os.name in ('nt','dos'):
        os.system("cls")
    elif os.name in ('linux','osx','posix'):
        os.system("clear")
    else:
        print("\n") * 120

## Cacalculate the GCD of a number and add to history array
def gcd_calculation():
    while True:
        def get_value(order):    
            while True:
                try:
                    num = int(input("Enter %s number: " % order))
                    return num
                except ValueError:
                    print("Please enter a valid number ... ", end="")    

        x = get_value("first")
        y = get_value("second")
        num1 = x
        num2 = y

        while y != 0:
            a = x
            b = y
            x = b
            y = a % b
        print (x)

        history.append("  GCD of %s and %s is %s" % (str(num1), str(num2), x))

        if input("Do you want to cacalculate again (Y/N): ").lower() != "y":
            break

## Main
file_name = "history.txt"
menu_text = """Menu: 
  1. Recent History
  2. Clear History
  3. GCD Calculation 
  4. Exit"""

try:
    with open(file_name,'r') as file:
        history = [i for i in file]
except:
    history = []

print("Welcome to GCD Calculator")
while True:
    clear()
    print(menu_text)
    select = input("You select: ")
    if select == "1":        
        print("\nRecent History:")
        if len(history) == 0:
            print("no history")
        else:
            for i in reversed(history):
                print(i)
        input("press any key to continue...")
    elif select == "2":
        history = []
    elif select == "3":
        gcd_calculation()
    elif select == "4":
        ## save the history to history.txt
        with open(file_name, 'w') as file:
            for i in history:
                file.write(i)
        ## exit program
        exit()
