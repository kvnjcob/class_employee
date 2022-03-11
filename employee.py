class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name)
        print(self.last_name)


if __name__ == "__main__":
    employee_list = []

    for index in range(2):
        employee_first_name = input("Please Enter the first Name :")
        employee_last_name = input("Please enter the second name :")
        employee = Employee(employee_first_name, employee_last_name)

        print(employee)
        employee.print_name()
        employee_list.append(employee)

    print("The list of all employees")
    for employee_variable in employee_list:
        print(employee_variable)
        employee_variable.print_name()
        print("----------------------------------")

