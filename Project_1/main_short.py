import random
'''
1 for snake 
2 for water
3 for gun
'''
computer = random.choice([1,2,3])
you_str = input("Enter your choice: ")
youDict = {"s": 1, "w":2, "g": 3}
reverseDict = {1:"Snake",2:"Water" ,3:"Gun" }

you = youDict[you_str]

# by now we have 2 number(variable), you and computer

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

'''
else:
    if (computer == 2 and you == 1): (computer - you) = 1   (2 - 1 = 1)
        print("You win!")

    elif(computer == 2 and you == 3): (computer - you) = -1   (2 - 3 = -1) 
        print("You lose!")

    elif (computer == 1 and you == 2): (computer - you) = -1   (1 - 2 = -1)
        print("You lose!")

    elif(computer == 1 and you == 3): (computer - you) = -2    (1 - 3 = -2)
        print("You win!")

    elif (computer == 3 and you == 2): (computer - you) = 1    (3 - 2 = 1)
        print("You win!")

    elif(computer == 3 and you == 1): (computer - you) = 2    (3 - 1 = 2)
        print("You lose!")

    else:
        print("something went wrong")
    
    this below logic is written on the basic of the value computer - you
'''
if computer == you:
    print("It's a tie!")

else:
    if ((computer - you) == 1 or (computer - you) == -2):
        print("You win!")
    else:
        print("You lose!")