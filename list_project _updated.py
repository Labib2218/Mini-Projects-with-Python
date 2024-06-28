# list print function
def fruits_list():
    print("Name of all Item in this list:")
    print("------------------------------")
    for serial, fruit_name in enumerate(mylist, start=1):
        print(f"{serial}.{fruit_name.capitalize()}")
    print()


# Intro section
print("The Program is starting now")
print("Please READ the instruction Carefully and INPUT correctly")
print("..........This is all about List...........")
mylist = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'pineapple', 'kiwi', 'mango', 'pear']
print(f"Total number of fruits: {len(mylist)}")

# Check Item using condition
print("____Check fruits is Available or not____"'\n')
f_name = input("Enter your desire fruits name: ").lower()
if f_name in mylist:
    print("Yeah..!found it")
else:
    print("This item is not available")
# check item in true or false
print(f"Is this item on the list: {f_name in mylist}"'\n')
# Index of Fruits
item_num = int(input("Enter the Serial Number of fruit[1 to 10]: "))
print("Name of the item:", mylist[item_num - 1].capitalize())
print("Last fruits in the list is:", mylist[-1], "\n")
# print fruits name
fruits_list()
# Add item Append methods
print(".........Add new fruit in the list.......")
new_fruit = input("Enter the fruit name: ").lower()
mylist.append(new_fruit)
run = False
while not run:
    another_fruit = input('Do you want to add another fruit? [yes/no]: ').lower()
    if another_fruit == 'yes':
        new_fruit = input("Enter the fruit name: ").lower()
        mylist.append(new_fruit)
        continue
    else:
        run = True
print(f"Now last item is: {mylist[-1].capitalize()}")
print("Total number of fruits:", len(mylist), "\n")
fruits_list()
# insert methods
print(".......Want to add a new fruit in specific serial number.....")
y = int(input("Then enter the serial number: "))
new_fruit_2 = input("Enter the fruit name: ").lower()
mylist.insert(y - 1, new_fruit_2)
print(f"Congratulation..!Now {new_fruit_2.capitalize()} is in the list", '\n')
ans = input("Want to see fruits list again?[yes/no]:").lower()
if ans == "yes":
    fruits_list()
else:
    print("Ok, thank you")
print()
# Remove Item
print(".......Item Remove section.......")
ans_2 = input("Input the delete methods by[name/serial]:").lower()
if ans_2 == "name":
    rem_fruit = input("Enter the name: ")
    if rem_fruit in mylist:
        mylist.remove(rem_fruit)
        run = True
        while run:
            rem_another = input('Want to remove another fruit?[yes/no]').lower()
            if rem_another == 'yes':
                rem_fruit = input("Enter the name: ")
                if rem_fruit in mylist:
                    mylist.remove(rem_fruit)
                else:
                    print("This fruit is not in the List.")
                    continue
            else:
                run = False
    else:
        print("This fruit is not in the List.")
elif ans_2 == "serial":
    print(f'Total number of fruits: {len(mylist)}')
    y2 = int(input("Enter the serial number: "))
    mylist.pop(y2 - 1)
    run = True
    while run:
        rem_another = input('Want to remove another fruit?[yes/no]').lower()
        if rem_another == 'yes':
            y2 = int(input("Enter the serial number: "))
            mylist.pop(y2 - 1)
            continue
        else:
            run = False
fruits_list()
# Sorting list item
print("________Sort the fruits________")
ans_3 = input("Want to sort?[yes/no]: ").lower()
if ans_3 == "yes":
    mylist.sort()
    fruits_list()
else:
    print("Ok, thank you")
print()
print("Thanks for your time.")
print("THE END")
