## Author: Boris Chan
## Date: 06/12/2016
## Purpose: Storing previous history with read and write txt

## Generate history from data.txt
readMe = open('data.txt','r')
history = [i for i in readMe]

## Shift the old history by index one
## Add new calculation to index 0
def history_additem(item):    
    for i in range(8,-1,-1):
        history [i+1] = history[i]
    history[0] = item

## Cacalculate the GCD of a number and add to history array
def GCD_Calculation():
    continued = True
    while continued:
        def Get_Value(order):    
            while True:
                try:
                    num = int(input("Enter %s number: " % order))
                    return num
                except ValueError:
                    print("Please enter a valid number ... ", end="")    

        x = Get_Value("first");
        y = Get_Value("second");
        num1 = x
        num2 = y

        while y != 0:
            a = x
            b = y
            x = b
            y = a % b
        print (x)

        history_additem("  GCD of %s and %s is %s \n" % (str(num1), str(num2), x))

        if input("Do you want to cacalculate again (Y/N): ").lower() != "y":
            continued = False

## Main
print("Welcome to GCD Calculator")
while True:
    print("""
Menu: 
  1. Recent History
  2. Clear History
  3. GCD Calculation 
  4. Exit""")
    select = input()
    if select == "1":        
        print("\nRecent History:")
        for i in history:
            if i != "  no history\n":
                print(i, end="")
        print()
    elif select == "2":
        history = ["  no history\n"]*9 + [" no history"]
    elif select == "3":
        GCD_Calculation()
    elif select == "4":
        ## save the history to data.txt
        saveFile = open('data.txt', 'w')
        for i in history:
            saveFile.write(i)
        saveFile.close()
        ## exit program
        exit()
    else:
        print("Please enter a valid choice: ")





