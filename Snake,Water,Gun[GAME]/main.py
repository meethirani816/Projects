import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter (s,w,g) Your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Sanke", -1:"Water", 0:"Gun"}

you = youDict[youstr]

# BY now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]} | Compuer chose {reverseDict[computer]}")

if(you == computer):
    print("It's Draw")
else:
    if(you == -1 and computer == 1):
        print("You Lose")

    elif(you == -1 and computer == 0):
        print("You Win")

    elif(you == 1 and computer == 0):
        print("You Lose")

    elif(you == 1 and computer == -1):
        print("You Win")

    elif(you == 0 and computer == 1):
        print("You Win")
        
    elif(you == 0 and computer == -1):
        print("You Lose")

    else:
        print("Something went wrong!")

    '''
        # the below logic written on the basis of computer - you
    
        if((computer - you) == -1 or (computer - you) == 2):
            print("You Lose!")
        else:
            print("You Win!")
    '''