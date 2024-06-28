import random
import string

print('-------We can Guess Your Password--------')
print('------------------------------------------')
print('WARNING: Please try less than 5 number of password otherwise it take a long time')
p_length = input("Enter Your Password: ")

resource = list(string.digits)
guess = ''
counter = 0
while guess != p_length:
    guess = ''
    for x in range(len(p_length)):
        guess_letter = resource[random.randint(0, 9)]
        guess = str(guess_letter) + str(guess)
        counter += 1
    print(counter, ':', guess)
print(f'Total Number of try: {counter:}')
print('Your Password is:', guess)
