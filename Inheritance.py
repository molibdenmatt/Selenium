class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce_yourself(self):
        return "My name is " + self.name + " " + self.surname

class Student(Person):

    def __init__(self, name, surname, index_number):
        Person.__init__(self, name, surname)
        self.index_number = index_number

    def give_index_number(self):
        return self.index_number

    def introduce_yourself(self):  # Overrides the parent Class method
        return "My number is " + str(self.index_number) + "  and  my name is " + self.name

first_student = Student("Michael", "Catty", 65664)
print(first_student.introduce_yourself())
print(first_student.give_index_number())

first_person = Person("Peter", "Pan")
print(first_person.introduce_yourself())
