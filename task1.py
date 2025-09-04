# string values "saad"
# char 's'
# digits 1234

# task1 calculator (+, - , /, *, ^)
print("enter 2 numbers for multiplication, addition, division, power, and subtraction")
number = int(input("num1: ")) 
number2= int(input("num2: "))
# print('the multpilication is', number*number2)
# print("the addition is" , number+number2)
# print("the subtraction is" , number-number2)
# print("the division of the numbers is" , number/number2)
# print("the power of the numbers is" , number**number2)
print("What you want ")
what_i_want =int(input("1: Addition,  2: Subtraction,  3:Multiplication,  4:Division: "))
if (what_i_want == 1): print(number+number2)
if (what_i_want == 2): print(number-number2)
if (what_i_want == 3): print(number*number2)
if (what_i_want==4 and number2!=0): print(number/number2)
else: print("invalid number 2")