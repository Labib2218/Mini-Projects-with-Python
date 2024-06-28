import random

print('-------We can Guess Your Password--------')
print('------------------------------------------')
print('WARNING: Please try less than 5 number of password otherwise it take a long time')
p_length = input("Enter Your Password: ")
p_range = len(p_length) * '9'
pass_list = (i for i in range(0, int(p_range)))
counter = 0
for pas in pass_list:
    counter += 1
    pas = str(pas)
    if pas == p_length:
        print('Found it!')
        print('Your Password is:', pas)
        break
    else:
        # print(pas)
        continue

print('\nThank You')

