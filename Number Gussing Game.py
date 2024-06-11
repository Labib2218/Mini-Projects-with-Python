import random
print("...........Welcome to our Number Guessing Game..........")


user_input = input("Enter a number as the maximum range of guessing: ")
if user_input.isdigit():
    user_input =int(user_input)
else:
    print("Your number is invalid.")
    quit()


random_number = random.randint(1,user_input)
print('\n')

attemp = 0
guess = 0
while guess != random_number:
    attemp += 1
    guess = input("Guess a Number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("You should enter a real number.\n")
    if guess > random_number:
        print("Your number is higher than value.\n")
    elif guess < random_number:
        print("Your number is lower than value.\n")
        continue
    elif guess == random_number:
        print("Yeah..! you match the number.\n")
        break


print(f'Your total try is: {attemp}')