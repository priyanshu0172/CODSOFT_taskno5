contact = {}

def view_contact():
    print("Name\t\tcontact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. View Contact List \n 4. Update Contact \n 5. Delete Contact \n 6. Exit \n Enter your choice"))
    if choice == 1:
        name = input("enter the contact name")
        phone = input("enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name,"'s contac number is",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            view_contact()
    elif choice == 4:
        update_contact = input(" Enter the contact to be update")
        if update_contact in contact:
            phone = input("enter a mobile number")
            contact[update_contact]=phone
            print("contact updated")
            view_contact()
        else:
            print("Name is not found in this contact book")
    elif choice == 5:
        delete_contact = input("Enter the contact to be deleted")
        if delete_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='yes' or confirm == 'y':
                contact.pop(delete_contact)
            view_contact()
        else:
            print("Name is not found in contact book")
    else:
        break