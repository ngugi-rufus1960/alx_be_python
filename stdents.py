#Define a Student class with attributes like name and age. Include a method to display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")


# Example usage
student1 = Student("Alice", 20)
student1.display_info()
