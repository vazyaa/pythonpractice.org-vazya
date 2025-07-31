list = [1, 2 ,3 , 4, 5, 6, 7, 8, 9, 10]
lesser_number = []
num = int(input("Please input the number you would like to compare "))
for i in list:
    if i <= num:
        lesser_number.append(i)
print("The numbers wich are less or equal than " + str(num) + " are: " + str(lesser_number))
        
