## Author: Boris Chan
## Date: 04/12/2016
## Purpose: Using Eculid algorithm to find GCD

def get_value(order):    
    while True:
        try:
            num = int(input("Enter %s number: " % order))
            return num
        except ValueError:
            print("Please enter a valid number ... ", end="")    

x = get_value("first")
y = get_value("second")

while y != 0:
    a = x
    b = y
    x = b
    y = a % b

print (x)
