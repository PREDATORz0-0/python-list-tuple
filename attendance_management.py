
attendance= [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),

]
employees = [
    (101, "Echo", "HR"),
    (102, "Migule'o Hara", "IT"),
    (103, "Miles Morales", "Finance"),
]

def mark_attendance(employee_id, date, status):
    attendance.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")

def search_attendance(employee_id):
    print(f"\nSearching Attendance for Employee ID {employee_id}:")
    found = False
    for record in attendance:
        if record[0] == employee_id:
            print(f"Date: {record[1]}, Status: {record[2]}")
            found = True
    if not found:
        print("No attendance records found for this employee.")

def attendance_summary():
    print("\nAttendance Summary:")
    for employee in employees:
        emp_id, emp_name, _ = employee
        total_days = len([record for record in attendance if record[0] == emp_id])
        present_days = len([record for record in attendance if record[0] == emp_id and record[2] == "Present"])
        percentage = (present_days / total_days) * 100 if total_days > 0 else 0
        print(f"{emp_name}: {percentage:.2f}% Present")
mark_attendance(101, "2025-03-02", "Present")
mark_attendance(102, "2025-03-02", "Present")
mark_attendance(103, "2025-03-02", "Absent")
search_attendance(102)
attendance_summary()
