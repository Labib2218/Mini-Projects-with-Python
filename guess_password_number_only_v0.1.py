import random

print('-------We can Guess Your Password--------')
print('------------------------------------------')
print('WARNING: Please try less than 5 number of password otherwise it take a long time')
p_length = input("Enter Your Password: ")
p_range = len(p_length) * '9'
pass_list = [i for i in range(0, int(p_range))]
print(f"Length of List: {len(pass_list)}")

guess = ''
counter = 0
while guess != p_length:
    guess = random.choice(pass_list)
    guess = str(guess)
    counter += 1
    print(counter, ':', guess)
    if guess == p_length:
        print('Found it!')
    else:
        guess = int(guess)
        pass_list.pop(pass_list.index(guess))
        continue

print(f'Total Number of try: {counter:}')
print('Your Password is:', guess)
