class Employee:
    bonus = 1.04

    def __init__(self, first, last, emp_no, age, pay):
        self.first = first
        self.last = last
        self.emp_no = emp_no
        self.age = age
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def yearly_bonus(self):
        self.pay = int(self.pay * self.bonus)


class Managers(Employee):
    bonus = 1.10

    def __init__(self, first, last, emp_no, age, pay, employees=None):
        super().__init__(first, last, emp_no, age, pay)
        if employees is None:
            self.employees = list()
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_emp(self):
        for emp in self.employees:
            print('THE EMPLOYEES ARE:\n %s \n' % emp.fullname())


emp = Employee('sam', 'ghadri', '007', 28, 50000)
emp_1 = Employee('harry', 'walker', '008', 23, 50000)
emp_2 = Employee('tony', 'ward', '009', 40, 50000)
mng = Managers('Tim', 'Jones', '100', 55, 80000, [emp])

mng.add_emp(emp_1)
mng.add_emp(emp_2)
print(mng.list_emp())
mng.remove_emp(emp_1)
print(mng.list_emp())
