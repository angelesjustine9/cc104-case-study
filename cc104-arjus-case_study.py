import json
import os

DATA_FILE = "payroll_data.json"


def load_employees():
    """Load employee data from a file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_employees(employees):
    """Save employee data to a file."""
    with open(DATA_FILE, "w") as f:
        json.dump(employees, f, indent=4)


def add_employee(employees):
    """Add a new employee to the payroll."""
    emp_id = input("Enter employee ID: ").strip()
    if any(emp["id"] == emp_id for emp in employees):
        print("ID already exists.")
        return employees

    name = input("Enter employee name: ").strip()
    position = input("Enter employee position: ").strip()
    try:
        salary = float(input("Enter employee salary: "))
    except ValueError:
        print("Invalid salary. Please enter a valid number.")
        return employees

    employees.append({"id": emp_id, "name": name, "position": position, "salary": salary})
    save_employees(employees)
    print("Employee added.")
    return employees


def edit_employee(employees):
    """Edit an existing employee's details."""
    emp_id = input("Enter employee ID to edit: ").strip()
    # Sort list before searching
    sorted_employees = sorted(employees, key=lambda x: x["id"])
    left, right = 0, len(sorted_employees) - 1
    found = None
    while left <= right:
        mid = (left + right) // 2
        if sorted_employees[mid]["id"] == emp_id:
            found = sorted_employees[mid]
            break
        elif sorted_employees[mid]["id"] < emp_id:
            left = mid + 1
        else:
            right = mid - 1

    if not found:
        print("Employee not found.")
        return employees

    print(f"Editing employee: {found}")
    new_name = input("New name (leave blank to keep): ").strip()
    new_position = input("New position (leave blank to keep): ").strip()
    new_salary_input = input("New salary (leave blank to keep): ").strip()

    if new_name:
        found["name"] = new_name
    if new_position:
        found["position"] = new_position
    if new_salary_input:
        try:
            found["salary"] = float(new_salary_input)
        except ValueError:
            print("Invalid salary input; skipping salary update.")

    save_employees(employees)
    print("Employee updated.")
    return employees


def delete_employee(employees):
    """Delete an employee from the payroll."""
    emp_id = input("Enter employee ID to delete: ").strip()
    employee_to_remove = next((emp for emp in employees if emp["id"] == emp_id), None)

    if employee_to_remove:
        employees.remove(employee_to_remove)
        save_employees(employees)
        print("Employee deleted.")
    else:
        print("Employee not found.")
    return employees


def display_sorted(employees):
    """Display employees sorted by name or salary."""
    if not employees:
        print("No employees to display.")
        return

    print("Sort by: 1) Name  2) Salary")
    choice = input("Enter choice: ").strip()
    key = "name" if choice == "1" else "salary"

    employees.sort(key=lambda x: x[key])
    print("{:<10} {:<20} {:<20} {:<10}".format("ID", "Name", "Position", "Salary"))
    print("-" * 60)
    for emp in employees:
        print("{:<10} {:<20} {:<20} {:<10}".format(emp["id"], emp["name"], emp["position"], emp["salary"]))


def search_employee(employees):
    """Search for an employee by ID."""
    if not employees:
        print("No employees to search.")
        return

    emp_id = input("Enter employee ID to search: ").strip()
    sorted_employees = sorted(employees, key=lambda x: x["id"])
    left, right = 0, len(sorted_employees) - 1
    found = None
    while left <= right:
        mid = (left + right) // 2
        if sorted_employees[mid]["id"] == emp_id:
            found = sorted_employees[mid]
            break
        elif sorted_employees[mid]["id"] < emp_id:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print("Employee found:")
        print(f"ID: {found['id']}, Name: {found['name']}, Position: {found['position']}, Salary: {found['salary']}")
    else:
        print("Employee not found.")


def main():
    """Main driver function for payroll system."""
    employees = load_employees()

    while True:
        print("\n--- PAYROLL SYSTEM ---")
        print("1) Add Employee")
        print("2) Edit Employee")
        print("3) Delete Employee")
        print("4) Display Sorted List")
        print("5) Search Employee by ID")
        print("0) Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            employees = add_employee(employees)
        elif choice == "2":
            employees = edit_employee(employees)
        elif choice == "3":
            employees = delete_employee(employees)
        elif choice == "4":
            display_sorted(employees)
        elif choice == "5":
            search_employee(employees)
        elif choice == "0":
            print("Saving and exiting...")
            save_employees(employees)
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
