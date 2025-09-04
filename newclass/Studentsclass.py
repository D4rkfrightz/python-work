class Student:
    def __init__(self, name , roll_number , marks_obtain , total_marks ):
        self.name = name
        self.roll = roll_number
        self.marks_obtain = marks_obtain
        self.total_marks = total_marks
        self.percentage = 0

    def print_values(self):
        print(self.name, self.roll, self.marks_obtain, self.total_marks)

    def percentage_calculate(self):
        self.percentage = (self.marks_obtain/self.total_marks)*100
        print("percentage you got is :", self.percentage ,"%")
    
    def grades_calculate(self):
        if self.percentage < 50 :
           print("your percentage is too low, you have failed with grade F, and percentage" , self.percentage)
        elif self.percentage >= 50 and self.percentage < 60 :
           print("You have passed with grade D, your percentage was" , self.percentage) 
        elif self.percentage >= 60 and self.percentage < 70 :
           print("you have passed with grade C, your percentage was" , self.percentage)     
        elif self.percentage >= 70 and self.percentage < 80 :
           print("you have passed with grade B, your percentage was" , self.percentage)
        elif self.percentage >= 80 and self.percentage < 90 :
           print("you have passed with grade A, your percentage was" , self.percentage) 
        elif self.percentage >= 90 and self.percentage < 99 :
           print("Congratulations, you have passed with A+ grade, your percentage was" , self.percentage)

