import random

choosing_number = random.randint(1,100)

tries = 2
count = 0

while count <= tries:
    count += 1 
    amin_bener =int(input("Choose a random number between 1-100:\n "))
    if amin_bener == choosing_number:
        print(" you guessed correctly!!!")
        break
    elif choosing_number > amin_bener:
        print(" you guessed too small!!!")
    elif choosing_number < amin_bener:
        print("you guessed too high!!!")

if count >= tries:
    print("You failed the guessing, the number is ", choosing_number)

