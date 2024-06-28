n1 = 0
n2 = 1
position = int(input("Enter the position of number: "))
for i in range(position):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

