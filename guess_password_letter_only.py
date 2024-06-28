import random
import string

print('-------We can Guess Your Password--------')
print('------------------------------------------')
print('WARNNING: Please try less than 5 numbor of passwprd otherwise it take a long time')
p_lenth = input("Enter Your Password: ")

resource = list(string.ascii_letters)
guess = ''
counter = 0
while guess != p_lenth:
    guess = ''
    for x in range(len(p_lenth)):
        guess_letter = resource[random.randint(0, 51)]
        guess = str(guess_letter) + str(guess)
        counter += 1
    print(counter, ':', guess)
print(f'Total Number of try: {counter:}')
print('Your Password is:', guess)
