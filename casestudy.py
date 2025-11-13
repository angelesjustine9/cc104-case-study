import json
import os

DATA_FILE = "students_data.json"
students = []

def load_students():
    global students
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            students = json.load(f)
            print(f"Loaded {len(students)} student(s) from file.")

def save_students():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    sid = input("Enter student ID: ").strip()
    for s in students:
        if s["id"] == sid:
            print("ID already exists.")
            return
    name = input("Enter student name: ").strip()
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid grade.")
        return
    students.append({"id": sid, "name": name, "grade": grade})
    save_students()
    print("Student added.")

def edit_student():
    sid = input("Enter student ID to edit: ").strip()
    # Sort by id for binary search
    sorted_list = sorted(students, key=lambda x: x["id"])
    # Binary search
    left, right = 0, len(sorted_list) - 1
    found = None
    while left <= right:
        mid = (left + right)//2
        if sorted_list[mid]["id"] == sid:
            found = sorted_list[mid]
            break
        elif sorted_list[mid]["id"] < sid:
            left = mid + 1
        else:
            right = mid - 1
    if not found:
        print("Student not found.")
        return
    print(f"Editing student: {found}")
    new_name = input("New name (leave blank to keep): ").strip()
    new_grade_input = input("New grade (leave blank to keep): ").strip()
    if new_name:
        found["name"] = new_name
    if new_grade_input:
        try:
            found["grade"] = float(new_grade_input)
        except ValueError:
            print("Invalid grade input; skipping grade update.")
    save_students()
    print("Student updated.")

def delete_student():
    sid = input("Enter student ID to delete: ").strip()
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students()
            print("Student deleted.")
            return
    print("Student not found.")

def display_sorted():
    if not students:
        print("No students to display.")
        return
    print("Sort by: 1) Name  2) Grade")
    choice = input("Enter choice: ").strip()
    key = "name" if choice == "1" else "grade"
    # Simple sort (Python built-in)
    students.sort(key=lambda x: x[key])
    print("{:<10} {:<20} {:<10}".format("ID","Name","Grade"))
    print("-"*40)
    for s in students:
        print("{:<10} {:<20} {:<10}".format(s["id"], s["name"], s["grade"]))

def search_student():
    if not students:
        print("No students to search.")
        return
    sid = input("Enter student ID to search: ").strip()
    sorted_list = sorted(students, key=lambda x: x["id"])
    left, right = 0, len(sorted_list) - 1
    found = None
    while left <= right:
        mid = (left + right)//2
        if sorted_list[mid]["id"] == sid:
            found = sorted_list[mid]
            break
        elif sorted_list[mid]["id"] < sid:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        print("Student found:")
        print(found)
    else:
        print("Student not found.")

def main():
    load_students()
    while True:
        print("\n--- STUDENT RECORD SYSTEM ---")
        print("1) Add Student")
        print("2) Edit Student")
        print("3) Delete Student")
        print("4) Display Sorted List")
        print("5) Search Student by ID")
        print("0) Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_sorted()
        elif choice == "5":
            search_student()
        elif choice == "0":
            print("Saving and exiting...")
            save_students()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
