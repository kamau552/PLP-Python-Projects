#Week 1 introduction to python
#Instructions:
#Basic Calculator Program
#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
input_num =input("Enter a number:")
input_operator = input("Enter a mathematical operator:")
input_num2 = input("Enter a number:")

calculation = (input_num + input_operator + input_num2)
totalcalculation = eval(calculation)

print("totalcalculation:", totalcalculation)