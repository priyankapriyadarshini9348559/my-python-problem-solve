students=[]
attendance=[]

names=input("Enter student's name:").split(",")
students.append(names)
present=0
for name in names:
    status=input(f"{name.strip()}(P/A):").upper()
    attendance.append(status)
    if status=="P":
        present+=1
        
print(students)
total=len(names)
percentage=(present/total) *100
print("\n present:",present)
print("Absent:",total-present)
print("Attendance %",round(percentage,2))
