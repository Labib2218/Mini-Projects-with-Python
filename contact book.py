contact = {
    'LABIB': '+8801793-892420',
    'IMRAN': '+8801408-526030',
    'LEON': '+8801581-897473'
}


def showcontact():
    print('Name \t Contact')
    print('---------------')
    for key in contact:
        print(f'{key} \t {contact.get(key)}')


while True:
    print("Manu Bar")
    print("--------")
    choice = int(input('1. Add contact in list\n'
                       '2. Find contact\n'
                       '3. Display all contact\n'
                       '4. Eidt contact\n'
                       '5. Delete contact\n'
                       '6. Exit\n'
                       'Enter a number between 1 to 6: '))
    if choice == 1:
        name = input("Enter the name: ").upper()
        phone = input('Enter the phone number: ')
        contact[name] = phone
        print("Your contact is added successfully.")

    elif choice == 2:
        con_name = input('Enter the Name: ').upper()
        if con_name in contact:
            print(con_name, "'s Contact number is: ", contact[con_name])
        else:
            print("Contact not Found")

    elif choice == 3:
        if not contact:
            print("Contact list is Empty")
        else:
            showcontact()

    elif choice == 4:
        edit_name = input('Enter the name that you want to edit: ').upper()
        if edit_name in contact:
            new_num = input('Enter the number: ').upper()
            contact[edit_name] = new_num
            print("Contact number is updated successfully.")
            showcontact()
        else:
            print("Contact Not in the list.")

    elif choice == 5:
        del_contact = input('Enter the name you want to delete: ').upper()
        if del_contact in contact:
            print(f'{del_contact} \t{contact.get(del_contact)} ')
            confirm = input('Are you sure?[yes/no] ').lower()
            if confirm == 'yes':
                contact.pop(del_contact)
                showcontact()
            else:
                pass
    else:
        break
    print()
