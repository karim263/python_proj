import csv

class Employee:
    def __init__(self, name, emp_id, position, salary, email):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
        self.email = email
class EmployeeManger:
    def __init__(self,filename='employees.csv'):
      self.filename=filename
     
    def add_employee(self,employee):
        with open('employees.csv', mode="a", newline="") as csvfile:
            fieldnames = ['name', 'id', 'position', 'salary', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if the file is empty
            if csvfile.tell() == 0:  # Check if the file is empty
                writer.writeheader()

            writer.writerow({
                "name": employee.name,
                "id": employee.emp_id,
                "position": employee.position,
                "salary": employee.salary,
                "email": employee.email
            })
    def search_employee(self,emp_id):
       found = False  # Initialize the found variable

       with open('employees.csv', mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if the ID in the current row matches the search ID
                if row['id'] == emp_id:
                    print(f"Found: Name: {row['name']}, ID: {row['id']}, Position: {row['position']}, Salary: {row['salary']}, Email: {row['email']}")
                    found = True
                    break  # Stop the loop once the ID is found
       if not found:
            print(f"No employee found with ID {emp_id}.")

       # the ubdate function
    def update_employee(self, emp_id):
        found = False  # Initialize the found variable

        employees = []

        with open(self.filename, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == emp_id:
                    print("Employee found. Enter new details (leave empty to keep current value):")
                    row['name'] = input(f"New name ({row['name']}): ") or row['name']
                    row['position'] = input(f"New position ({row['position']}): ") or row['position']
                    row['salary'] = input(f"New salary ({row['salary']}): ") or row['salary']
                    row['email'] = input(f"New email ({row['email']}): ") or row['email']
                    found = True
                employees.append(row)
        if not found:
            print(f"No employee found with ID {emp_id}.")
            return

        with open(self.filename, mode="w", newline="") as csvfile:
            fieldnames = ['name', 'id', 'position', 'salary', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
        print("Employee updated successfully!")
    def delete_employee(self, emp_id):
        employees = []
        with open(self.filename, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] != emp_id:
                    employees.append(row)

        with open(self.filename, mode="w", newline="") as csvfile:
            fieldnames = ['name', 'id', 'position', 'salary', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
        print(f"Employee with ID {emp_id} deleted successfully!")

def show_menu():
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Search Employee by ID")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
     
     
Manager=EmployeeManger()
    
while True:
    show_menu()
    
    choice = input("Enter your choice: ")

    if choice == '1':
            name = input("Enter the first name: ")
            emp_id = input("Enter ID: ")
            position = input("Enter position: ")
            salary = input("Enter salary: ")
            email = input("Enter email: ")
            employee = Employee(name, emp_id, position, salary, email)
            Manager.add_employee(employee)

    elif choice == '2':
        emp_id = input("Enter ID: ")
        
        Manager.search_employee(emp_id)
    elif choice == '3':
        # Updating employee information
        emp_id = input("Enter the ID you want to update: ")
        Manager.update_employee(emp_id)
    
    
    elif choice == '4':
          emp_id = input("Enter ID: ")
          Manager.delete_employee(emp_id)

    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
