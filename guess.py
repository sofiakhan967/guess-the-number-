import random 

def guess(x):
    number= random.randint(1,x)
    user=0
    while user!=number:
        user= int(input(" GUESS THE NUMBER :"))
        if user > number :
            print(" woah !!. you guess higher number  "  )
        elif user < number :
            print("Dammit ..... lower number")

    print(" you have guess the correct number " )
    print('correct number is :' , number)
guess(100)        