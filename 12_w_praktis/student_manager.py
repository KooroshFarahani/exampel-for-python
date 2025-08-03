import csv


name = input ("what is name :")
age= int(input("what is the age :"))
grade=input("what is the grade :")
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    writer.writerow([name, age, grade])