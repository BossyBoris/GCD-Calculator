## a crappy calculator
def Get_Value(order):    
    while True:
        try:
            num = int(input("Enter %s number: " % order))
            return num
        except ValueError:
            print("Please enter a valid number ... ", end="")    

x = Get_Value("first");
y = Get_Value("second");

while y != 0:
    a = x
    b = y
    x = b
    y = a % b

print (x)