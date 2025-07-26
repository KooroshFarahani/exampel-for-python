contact={
    "ali":"09121234567",
    "sara":"09351234567",
    "koorosh":"09901783176",
    "bahram":"09109137995"
}

while True:
    print("1. Add contact\n2. Find number\n3. Delete contact\n4. Show all\n5. Exit")
    operator=input("Enter choice:")
    if operator=="5":
        break
    elif operator=="1":
        name=input("Enter name:")
        phon_number=input("Number:")
        contact[name]=phon_number
        print(f"your contact name is {name} added")
    elif operator=="2":
        find_name=input("Enter your name to find :")
        print(f"your name is : {find_name} \n phon number is {contact[find_name]}")
    elif operator=="3":
        del_name=input("Enter the name want too delete :")
        del contact[del_name]
        print(f"deleted this contact {del_name}")
    elif operator=="4":
        print ("show contact \n")
        for key,value in contact.items():
            print (f"{key} : {value}")

        