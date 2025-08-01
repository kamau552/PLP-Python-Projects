#Week 1 introduction to python
input_num =input("Enter a number:")
input_operator = input("Enter a mathematical operator:")
input_num2 = input("Enter a number:")

calculation = (input_num + input_operator + input_num2)
totalcalculation = eval(calculation)

print("totalcalculation:", totalcalculation)