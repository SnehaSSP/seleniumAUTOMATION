class Employee:
    emp_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.emp_count = Employee.emp_count + 1
        print(Employee.emp_count)


e1 = Employee("sneha", 35)
e1 = Employee("Rajnish", 38)
e1 = Employee("Bubu", 35)
e1 = Employee("Dudu", 38)
e1 = Employee("Dudu", 100)
e1 = Employee("Dudu", 1000)






