percentage = int(input("Enter the marks of dua :"))
Name = "dua"
if percentage < 50 :
        print("your percentage is too low, you", Name, "have failed with grade F, and percentage" , percentage)
elif percentage >= 50 and percentage < 60 :
        print("You", Name , "have barely passed with grade D, your percentage was" , percentage) 
elif percentage >= 60 and percentage < 70 :
        print("you", Name , "have passed with grade C, your percentage was" , percentage)     
elif percentage >= 70 and percentage < 80 :
        print("you" , Name , "have passed with grade B, your percentage was" , percentage)
elif percentage >= 80 and percentage < 90 :
        print("you", Name , "have passed with grade A, your percentage was" , percentage) 
elif percentage >= 90 and percentage < 99 :
        print("Congratulations, you" , Name , "have passed with A+ grade, your percentage was" , percentage)
else :
        print("Error, invalid data")