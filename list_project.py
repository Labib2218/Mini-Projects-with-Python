#lists
print("The Program is starting now")
print("Please READ the instraction Carefully and INPUT correctly")
print("..........This is all about List...........")
mylist=['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'pineapple', 'kiwi', 'mango', 'pear']
length_list=len(mylist)
print("Total number of fruits:",length_list,"\n")

#Check Item using condition
print("____Check fruits is Availabe or not____")
f_name= input("Enter your desire fruits name:")
l_case =f_name.lower()
if l_case in mylist:
    print("Yeah..!found it")
else:
    print("This item is not availabe")

#check item in true or false
check_item= l_case in mylist
print("Is this item on the list:",check_item,"\n")

#Index of Fruits
item_num = int(input("Enter the Serial Number of fruit[1 to 10]:"))
index_item= mylist[item_num-1]
print("Name of the item:",index_item)
print("Last fruits in the list is:", mylist[-1],"\n")

#print fruits name using for loop
print("Name of all Item in this list:")
print("______________________________")
for i,fruit in enumerate(mylist,start=1):
    print(f"{i}.{fruit}")
print("\n")

#add item Append methods
print(".........Want to Add new fruit in the list.......")
new_fruit=input("Enter your fruit name:")
x = new_fruit.lower()
mylist.append(x)

#Index of Fruits
print(f"Now last item is:",mylist[-1])
length_list=len(mylist)
print("Total number of fruits:",length_list,"\n")

#New name list
print("Name of all Item in this list:")
print("______________________________")
for i,fruit in enumerate(mylist,start=1):
    print(f"{i}.{fruit}")
print("\n")

#insert methods
print(".......Want to add new fruit in specific serial number.....")
y= int(input("Then enter the serial number:"))
y1 = y-1
new_fruit_2 =input("Enter your fruit name:")
x1 = new_fruit_2.lower()
mylist.insert(y1,x1)
print(f"Congratulation..!Now {x1} is in the list")
print("\n")
ans = input("Want to see fruits list again?[yes/no]:")
if ans == "yes" or ans == "Yes":
    print("Name of all Item in this list:")
    print("______________________________")
    for i,fruit in enumerate(mylist,start=1):
        print(f"{i}.{fruit}")
    print("\n")
elif ans == "no" or ans == "No":
    print("Ok, thank you")
print("\n")

#Remove Item
print(".......Item Remove section.......")
ans_2 = input("Input the delete methods by[name/serial]:")
if ans_2 == "name" or ans_2 == "Name":
    new_fruit_3 = input("Enter the name:")
    x_2 = new_fruit_3.lower()
    mylist.remove(x_2)
    print("Name of all Item in this list:")
    print("______________________________")
    for i, fruit in enumerate(mylist, start=1):
        print(f"{i}.{fruit}")
    print("\n")
elif ans_2 == "Serial" or ans_2 == "serial":
    y2 = int(input("Enter the serial number:"))
    y2_2=y2-1
    mylist.pop(y2_2)
    print("Name of all Item in this list:")
    print("______________________________")
    for i, fruit in enumerate(mylist, start=1):
        print(f"{i}.{fruit}")
    print("\n")

#Sorting list item
print("________want to sort the fruits________")
ans_3 = input("Want to see fruits list again?[yes/no]:")
if ans_3 == "yes" or ans_3 == "Yes":
    mylist.sort()
    print("Name of all Item in this list:")
    print("______________________________")
    for i,fruit in enumerate(mylist,start=1):
        print(f"{i}.{fruit}")
    print("\n")
elif ans_3 == "no" or ans_3 == "No":
    print("Ok, thank you")
print("\n")

print("Thanks for your time.")
print("THE END")