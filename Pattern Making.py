import time
# t = float(input("Enter a time(second): "))
t=0.001
#Down and Up arrow with python
for i in range(5):
    for j in range(i+1):
        print(f'{'*':3}', end='')
        time.sleep(t)
    for k in range(i,5):
        print(f'{' ':3}', end='')
    for k in range(i,4):
        print(f'{' ':3}', end='')
    for j in range(i+1):
        print(f'{'*':3}', end='')
        time.sleep(t)
    print()


for tr in range(6):
    for blb in range(tr):
        print(' ', end = '  ')
    for ftr in range(tr,6):
        print('*',end ='  ')
        time.sleep(t)
    for ftl in range(tr,5):
        print('*', end ='  ')
        time.sleep(t)
    print()

for da in range(6):
    for trb in range(da,5):
        print(' ',end='  ')
    for brf in range(da +1):
        print('*',end= '  ')
        time.sleep(t)
    for lbf in range(da):
        print('*', end='  ')
        time.sleep(t)
    print()

for da in range(5):
    for tlf in range(da,5):
        print('*', end='  ')
        time.sleep(t)
    for brb in range(da):
        print(' ', end='  ')
    for blb in range(da+1):
        print(' ', end='  ')
    for trf in range(da,5):
        print('*', end='  ')
        time.sleep(t)
    print()
print()
#squre pattern
for i in range(6):
    for j in range(6):
        print(f'{'*':3}', end='')
        if j == 5:
            print()

#half square left bottom
for i in range(6):
    for j in range(i):
        print(f'{'*':3}', end='')
    print()

#half square top left
for i in range(6):
    for j in range(6-i):
        print(f'{'*':3}', end='')
    print()

day = ['Su','Mo','Tu','We','Th','Fr','Sa']
for days in day:
    print(f'{days:8}', end='')
print()


    for i in range(1, 31):
        print(f"{i:2}", end=' ')
        if i % 7 == 0:
            print()
    print()