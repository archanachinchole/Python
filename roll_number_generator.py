def roll_number_generator():
    current_roll_number = 1
    while current_roll_number <= 20:
        yield current_roll_number
        current_roll_number += 1

roll_gen = roll_number_generator()

student_info = {}

def add_student():
    name = input("Enter student's name: ")
    mobile_number = input("Enter student's mobile number: ")
    marks = input("Enter student's marks: ")

    # Validate input data
    if not name:
        print("Name cannot be empty.")
        return
    if not mobile_number.isdigit() or len(mobile_number) != 10:
        print("Invalid mobile number. Please enter a 10-digit number.")
        return
    try:
        marks = float(marks)
    except ValueError:
        print("Invalid marks. Please enter a numeric value.")
        return

    roll_number = next(roll_gen)
    student_info[roll_number] = {'name': name, 'mobile_number': mobile_number, 'marks': marks}
    print("Student added successfully!")

# Add some students for testing
for _ in range(5):
    add_student()

print("Student Information:")
print(student_info)
