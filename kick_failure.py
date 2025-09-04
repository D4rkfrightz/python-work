array = [
    {"name": "saad", "percentage": 51},
    {"name": "ahmed", "percentage": 40},
    {"name": "taha", "percentage": 10},
    {"name": "muaz", "percentage": 60},
    {"name": "Aimen", "percentage": 5}
]
result = []
def keep_passed_only():
    for students in array:
        if students["percentage"] >= 50 :
            result.append(students)
            print("the student percentage who passed"  , students["percentage"] , "and name" , students["name"])        

keep_passed_only()