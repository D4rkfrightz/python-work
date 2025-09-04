array = [
    {
        "name": "saad",
        "percentage": 51
    },
    {
        "name": "ahmed",
        "percentage": 40
    },
    {
        "name":"taha",
        "percentage":83
    },
    {
        "name": "muaz",
        "percentage" : 90
    },
    {   "name" : "Ali",
        "percentage" : 68
    }
]

for i in array :
    if i["percentage"] < 50 :
        print("your percentage is too low, you have failed with grade F, and percentage" , i["percentage"])
    elif i["percentage"] >= 50 and i["percentage"] < 60 :
        print("You have passed with grade D, your percentage was" , i["percentage"])
    elif i["percentage"] >= 60 and i["percentage"] < 70 :
        print("you have passed with grade C, your percentage was" , i["percentage"]) 
    elif i["percentage"] >= 70 and i["percentage"] < 80 :
        print("you have passed with grade B, your percentage was" , i["percentage"])
    elif i["percentage"] >= 80 and i["percentage"] < 90 :
        print("you have passed with grade A, your percentage was" , i["percentage"])
    elif i["percentage"] >= 90 and i["percentage"] < 99 :
        print("Congratulations, you have passed with A+ grade, your percentage was" , i["percentage"])
    else :
        print("Error, invalid data")

       
       
       
       
       
       
       # print (("the student name "),i["name"] ,i["percentage"] , ("student has passed"))
    #else :
       # print(("the student name "),i["name"] ,i["percentage"] ,"student has failed")
        # grading system