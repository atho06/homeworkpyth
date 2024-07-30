class Person:
    def __init__(self, name, age)->None:
        self.name=name
        self.age=int(age)
    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, empid, salary)->None:
        super().__init__(name, age)
        self.empid=empid
        self.salary=float(salary)
    def display(self):
        print(self.name, self.age, self.empid, self.salary)
    def increment_salary(self, amount):
        self.salary+=amount
        print("salary after incrementing:", self.salary)

if __name__=='__main__':
    p1=Person("P1", 20)
    p2=Employee("P2", 35, 'id345', 10000)
    p1.display()
    p2.display()
    p2.increment_salary(10000)
    p2.display()
