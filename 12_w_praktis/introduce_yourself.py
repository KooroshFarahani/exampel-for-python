name = input("name:")
age = int(input("age:"))
city=input("city:")
job=input("job:")
student = True
if job != "Student":
    student=False

text = f"hi {name} , your age is {age} years old \n and you are born in {city} \n your job is {job} \n is you are studen? {student}"
print (text)
