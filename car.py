class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand                
        self.__engine_type = engine_type  

    def show_engine_type(self):           
        print(f"The engine type is: {self.__engine_type}")

    def __start_the_engine(self):         
        print("Engine is started")

    def start_the_car(self):              
        self.__start_the_engine()

my_car = Car("Toyota", "V6")
print(my_car.brand)

my_car.show_engine_type()  
my_car.start_the_car()