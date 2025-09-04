students = [
    {"name": "saad", "percentage": 51},
    {"name": "ahmed", "percentage": 40},
    {"name": "taha", "percentage": 10},
    {"name": "muaz", "percentage": 60},
    {"name": "Aimen", "percentage": 0}
]

result = []

def keep_passed_only():
    for student in students:
        if student["percentage"] >= 50:
            result.append(student)
    
    print("Students who passed:", result)

keep_passed_only()
