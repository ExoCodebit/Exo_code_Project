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

if computer == you:
    print("It's a tie!")

else:
    if (computer == 2 and you == 1): 
        print("You win!")

    elif(computer == 2 and you == 3):
        print("You lose!")

    elif (computer == 1 and you == 2):
        print("You lose!")

    elif(computer == 1 and you == 3): 
        print("You win!")

    elif (computer == 3 and you == 2): 
        print("You win!")

    elif(computer == 3 and you == 1):
        print("You lose!")

    else:
        print("something went wrong")
