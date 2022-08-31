class Employee:
    count = 0;

    def __init__(self, name, salary):
        Employee.count +=1;
        print("Call constructor = ", Employee.count)
        self.name = name;
        self.salary = salary;

    def __del__(self):
        Employee.count -=1;
        print("Call destrucor = ", Employee.count)

    def set_name(self):
        print("enter name:")
        self.name = str(input())

    def set_salary(self):
        print("enter salary:")
        self.salary = int(input())


    def get_name(self):
        return self.name;

    def get_salary(self):
        return self.salary;



    def show(self):
        print("Name - ", self.name, "\nSalary - ", self.salary)