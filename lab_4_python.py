class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = []
        for employee in self.employees:
            if employee.age == target_age:
                result.append(employee)
        return result

    def search_by_name(self, target_name):
        result = []
        for employee in self.employees:
            if employee.name.lower() == target_name.lower():
                result.append(employee)
        return result

    def search_by_salary(self, operator, target_salary):
        result = []
        for employee in self.employees:
            if operator == '>' and employee.salary > target_salary:
                result.append(employee)
            elif operator == '<' and employee.salary < target_salary:
                result.append(employee)
            elif operator == '>=' and employee.salary >= target_salary:
                result.append(employee)
            elif operator == '<=' and employee.salary <= target_salary:
                result.append(employee)
        return result

def main():
    employee_table = EmployeeTable()

    # Populate the employee table
    employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("Search Options:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            target_age = int(input("Enter the age to search for: "))
            result = employee_table.search_by_age(target_age)
        elif choice == '2':
            target_name = input("Enter the name to search for: ")
            result = employee_table.search_by_name(target_name)
        elif choice == '3':
            operator = input("Enter the operator (<, >, <=, >=): ")
            target_salary = int(input("Enter the salary to search for: "))
            result = employee_table.search_by_salary(operator, target_salary)
        else:
            print("Invalid choice. Please try again.")
            continue

        if not result:
            print("No matching records found.")
        else:
            print("Matching Records:")
            for employee in result:
                print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

        another_search = input("Do you want to perform another search? (yes/no): ")
        if another_search.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
