class CAR:
    def __init__(self,brand,color,year):
        self.brand=brand
        self.color=color
        self.year=year
    def info(self):
        print(f"car barnd : {self.brand} \n color car : {self.color} \n make at {self.year} ")
    def start(self):
        print(f"car{self.brand} is started !!")


car_name = input("pleas enter the brand of car :")
car_year = int(input("pleas enter the year of make this car :"))
car_color = input("pleas enter the color of the car :")

car1=CAR(car_name,car_color,car_year)

car1.info()
car1.start()