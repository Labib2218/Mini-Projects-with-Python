import time
# x = float(input("Enter time: "))
x = .001
# Code for printing A
for i in range(7):
    for j in range(5):
        if (((j==0 or j==4) and i!=0)) or ((i == 0 or i == 3) and (j>0 and j<4)):
            print('*', end=' ')
            time.sleep(x)
        else:
            print(' ',end=' ')
    print()
print()

#Code for printing B
for i in range(7):
    for j in range(5):
        if (((j == 0 or j == 4) and (i != 0 and i != 3 and i != 6)) or
            ((i == 0 or i == 3 or i == 6) and (j <4))):
            print('*', end=' ')
            time.sleep(x)
        else:
            print(' ',end=' ')
    print()
print()

#Code for printing C
for i in range(7):
    for j in range(5):
        if (((j==0) and (i !=0 and i!=1 and i!=5 and i!=6)) or
                ((i ==0 or i==6) and (j>0 and j<4)) or
                ((i==1 or i == 5) and (j!=1 and j!=2 and j!=3))):
            print('*', end=' ')
            time.sleep(x)
        else:
            print(' ', end=' ')
    print()
print()

#Code for printing D
for i in range(7):
    for j in range(5):
       if ((j == 0 or j == 4) and (i != 0 and i !=6)) or ((i == 0 or i == 6) and (j<4)):
           print('*',end=' ')
           time.sleep(x)
       else:
           print(' ',end=' ')
    print()
print()

loop = 0
for i in range(10):
    for j in range(13):
        loop+=1
        if ( j==0 or j==12)or ((j==1 or j==11)and (i!=2 and i!=3)) or ((j==2 or j==10) and (i!=2 and i!=3 and i!=4))\
                or ((j==3 or j==9)and( i!=2 and i!=3 and i!=4 and i!=5)) \
                or ((j==4 or j==8) and (i!=2 and i!=3 and i!=4 and i!=5 and i!=6))\
                or ((j==5 or j==7) and (i!=3 and i!=4 and i!=5 and i!=6 and i!=7))\
                or (j==6) and ((i!=4 and i!=5 and i!=6 and i!=7 and i!=8)):
            print('#', end=' ')
            time.sleep(x)
        else:
           print('.',end=' ')
    print()
print(loop)
