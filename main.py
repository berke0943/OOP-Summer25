class Student:
    def __init__(self, first_name, last_name, index_number, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number
        self.nationality = nationality

    def __str__(self):
        return f"Student(name: {self.first_name}, Last name: {self.last_name}, index_number: {self.index_number}, nationality: {self.nationality})"

s1 = Student("Berke", "Haliloglu", 35274, "Turkish")
s2 = Student("Serra", "Ozbek", 35248, "Turkish")
s3 = Student("Sirri", "Cataloglu", 34854, "Turkish")

print(s1)
print(s2)
print(s3)
