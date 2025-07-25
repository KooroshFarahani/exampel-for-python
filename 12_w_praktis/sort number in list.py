numbers=[]
sum_number= 0 
for num in range(0,5):
    number=int(input(f"Enter number {num}:"))
    numbers.append(number)
    sum_number+=number
sort_numbers=numbers.sort()
print(f"Sorted list:{numbers}")
print(f"Average: {sum_number/5}")
