from datetime import datetime

def write_log(action):
    with open("program.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")

def add_student(name, roll):
    with open("student.txt", "a") as f:
        f.write(f"{roll},{name}\n")
    print("✅ Student added successfully")
    write_log(f"Added student: roll={roll}, name={name}")

def view_student():
    valid_students = []
    with open("student.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:   # skip empty lines
                continue
            if "," not in line:   # skip invalid lines
                continue
            parts = line.split(",", 1)  # split only once
            if len(parts) == 2:
                roll, name = parts
                valid_students.append(f"{roll},{name}\n")
                print(f"Roll: {roll}, Name: {name}")

    # ✅ rewrite the file with only valid entries
    with open("student.txt", "w") as f:
        f.writelines(valid_students)

    write_log("Viewed all students (and cleaned invalid lines)")


def search_student(roll):
    with open("student.txt", "r") as f:
        for line in f:
            r, name = line.strip().split(",")
            if r == str(roll):
                print(f"🔎 Found: Roll={r}, Name={name}")
                write_log(f"Searched student: found roll={roll}")
                return
    print("❌ Student not found")
    write_log(f"Searched student: Roll={roll} not found")

def delete_student(roll):
    students = []
    with open("student.txt", "r") as f:   # ✅ consistent filename
        students = f.readlines()

    with open("student.txt", "w") as f:   # overwrite after filtering
        for line in students:
            r, name = line.strip().split(",")
            if r != str(roll):
                f.write(line)

    print("🗑️ Student deleted (if existed)")
    write_log(f"Deleted student: Roll={roll}")

# ---------------- Menu ----------------
while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        add_student(name, roll)
    elif choice == "2":
        view_student()
    elif choice == "3":
        roll = input("Enter roll to search: ")
        search_student(roll)
    elif choice == "4":
        roll = input("Enter roll to delete: ")
        delete_student(roll)
    elif choice == "5":
        write_log("Program exited")
        break
    else:
        print("❌ Invalid choice")
