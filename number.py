import random

print('Select number between 1 to 100 & let computer guess the correct one .....')
secret_num=int(input(" Enter any number between 1 to 100 : "))
print("----------------------")
guess=random.randint(1 ,100)
times=1

if secret_num > 100:
    print("select between 1 to 100 ")
    secret_num=int(input(" Enter any number between 1 to 100 : "))

while(times!=6):

    if guess > secret_num:
        print(" Computer guessed higher number : " , guess)
        guess=random.randint(1 ,100)
    
    else:
        print("Computer guessed lower number :" , guess)
        guess=random.randint(1 ,100)

    if guess == secret_num :
        print(" correct guess it tooks computer,",(times),"times to guess answer" , guess)
        break
    times+=1

if  guess!= secret_num:
    print("You are such a dumb ....can't guess correct number , Correct answer is :", secret_num)











