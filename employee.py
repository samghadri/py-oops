class Employee:

    bonus = 1.04

    def __init__(self, first, last, emp_no, age, pay):
        self.first = first
        self.last = last
        self.emp_no = emp_no
        self.age = age
        self.email = self.first + '.' + self.last +'@company.com'
        self.pay = pay



    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def yearly_bonus(self):
        self.pay = int(self.pay * self.bonus)


class Managers(Employee):

    bonus = 1.10

    def __init__(self, first, last, emp_no, age, pay, department):
        super().__init__(first, last, emp_no, age, pay)
        self.department = department




emp = Employee('sam','ghadri', '007', 28, 50000)
mng = Managers('Tim','Jones', '100', 55, 80000, 'Back-End Developer')

print(mng.department)

