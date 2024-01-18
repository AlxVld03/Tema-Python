class Employee:
    """Common base class for all employees"""
    empCount = 0

    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def _del_ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in _init_)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

## x = 4  VLAD
## y = 14 ALEXANDRU MIHAI

class Manager(Employee):

    mgr_count = 0

    def _init_(self, name, salary, departament):
        super()._init_(name, salary)
        self.departament = f"B02_{departament}"
        Manager.mgr_count += 1

    def display_employee(self):
        print("Salariu: ", self.salary)  

    def marire_salariu_minim(self):
        if self.salary < 3000:
            self.salary = 3000


y = 14

managers = []

Manager1 = Manager("Alex", 4456, "dep1")
managers.append(Manager1)
Manager2 = Manager("Mihai", 10010, "dep2")
managers.append(Manager2)
Manager3 = Manager("Geani", 7290, "dep3")
managers.append(Manager3)
Manager4 = Manager("David", 2560, "dep4")
managers.append(Manager4)

for i in managers:
    i.display_employee()

print(f"Nr. de angajati: {managers[1].empCount}")
print(f"Nr. de manageri: {managers[3].mgr_count}")

for i in managers:
    i.marire_salariu_minim()

for i in managers:
    i.display_employee()