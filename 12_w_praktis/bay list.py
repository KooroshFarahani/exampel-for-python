list_by=[]
while True:

    print("1. Add item \n 2. Remove item \n 3. Show list \n 4. Quit")
    operator=input("Enter choice:")
    if operator == "4":
        break
    elif operator == "1":
        item=input("Enter item:")
        list_by.append(item)
        print(f"{item} is add")
    elif operator == "2":
        item=input("Enter item:")
        list_by.remove(item)
        print(f"{item} is delete")
    elif operator == "3":
        print(list_by)
    
    
