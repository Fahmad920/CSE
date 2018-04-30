class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, education, salary):
        super(Employee, self).__init__(name, education)
        self.salary = salary

    def earn(self):
        print("%s got their pay check" % self.education)


class Programmer(Employee):
    def __init__(self, name, education, salary):
        super(Programmer, self).__init__(name, education, salary)

    def create(self):
        print("%s created some code with a computer" % self.name)


programmer1 = Programmer('Sophia', 'Stanford University', 'Sophia earns $1,000')
programmer1.create()