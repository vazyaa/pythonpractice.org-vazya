number = int(input("Please input a number: "))
if number % 4 == 0:
    print("The number can be fully devided by 4")
elif number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
num = int(input("Please input a number to be divided "))
divBy = int(input("Please input a number to be devided by "))

if num % divBy == 0:
    print(str(num) + " can be fully divided by " + str(divBy))
else:
    print(str(num) + " cannot be fully divided by " + str(divBy))