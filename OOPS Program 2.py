class Person():
    def __init__(self,name,age,salary):
        self.name =name
        self.age=age
        self.salary=salary

person1=Person("Parinitha", 26, 1000000000)
print("Person 1 Name:{}".format(person1.name))
print("Person 1 details ({0},{1},{2}):".format( person1.name, person1.age, person1.salary ))

