import array

# Integers
# Example student grades
grades = [85, 90, 78, 92, 88]
total = sum(grades)
average = total / len(grades)
minimum = min(grades)
maximum = max(grades)

print("=== Integers ===")
print(f"Total: {total}, Average: {average}, Min: {minimum}, Max: {maximum}")
print()

# Strings
# Formatted string report
print("=== Strings ===")
report = f"Total Grades: {total}\nAverage Grade: {average:.2f}\nMaximum Grade: {maximum}\nMinimum Grade: {minimum}"
print(report)
print()
print(f"The total marks obtained by all students is {total}, and the average is {average:.2f}.")
print()

# Booleans
# Threshold condition
threshold = 85
print("=== Booleans ===")
if average > threshold and maximum > 90:
    print("Above Standard")
else:
    print("Below Standard")
print()

# Lists
# Maintaining a list of student names
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

print("=== Lists ===")
print("Original List:", students)

# Add a new student
students.append("Frank")
# Remove a student based on a condition (e.g., remove if name starts with 'C')
students = [student for student in students if not student.startswith("C")]
# Sort the list
students.sort()

print("Modified List:", students)
print()

# Arrays
# Using Python's array module
print("=== Arrays ===")
grades_array = array.array('i', grades[:3])  # Fixed-size subset of grades
grades_list_sum = sum(grades[:3])
grades_array_sum = sum(grades_array)

print(f"Array Sum: {grades_array_sum}, List Sum: {grades_list_sum}")
print()

# Dictionaries
# List of student dictionaries
students_data = [
    {"id": 1, "name": "Alice", "value": 85},
    {"id": 2, "name": "Bob", "value": 90},
    {"id": 3, "name": "Charlie", "value": 78},
    {"id": 4, "name": "David", "value": 92},
    {"id": 5, "name": "Eve", "value": 88},
]

print("=== Dictionaries ===")
print("Original Data:", students_data)

# Update one record (e.g., update Eve's grade)
for student in students_data:
    if student["name"] == "Eve":
        student["value"] = 95

# Delete a record (e.g., remove Charlie)
students_data = [student for student in students_data if student["name"] != "Charlie"]

# Compute the total value across all records
total_value = sum(student["value"] for student in students_data)

print("Updated Data:", students_data)
print(f"Total Value of Grades: {total_value}")