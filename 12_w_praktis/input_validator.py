def get_postive_number():
    try:
        number=float(input("Enter the number :"))
        if number < 0 :
            raise ValueError("number must be postive ! Negative values are not allowed.")
        print(f"Thank you! You entered a valid positive number: {number}")

    except ValueError as e:
        print (f"Error{e}")

get_postive_number()