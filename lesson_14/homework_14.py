class Student:

    def __init__(self, first_name:str, family_name:str, age: int, average_score:float=0):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        self.averafe_score = average_score
    
    def set_average_score(self, value:float):
        self.averafe_score = value


vasya = Student("Vasya", "Petrenko", 17)
petya = Student(first_name="Petya", family_name="Grib", age=18)
vasya.set_average_score(74.5)
petya.set_average_score(value=80.1)
print(f"Average score for {vasya.first_name} {vasya.family_name} is {vasya.averafe_score}")
print(f"Average score for {petya.first_name} {petya.family_name} is {petya.averafe_score}")