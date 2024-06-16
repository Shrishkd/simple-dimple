"""SIMPLE CALCULATOR USING PYTHON"""
num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
oppr=input("Enter Airthmatic Operation: ") # ONLY +, - , *, /
if oppr=="+": # USE (+) FOR ADDITION
    print (f" Sum of {num1} and {num2} is: ", num1+num2)
elif oppr=="-": #USE (-) FOR SUBTRACTION
    print (f" Diffrence of {num1} and {num2} is: ",num1-num2)
elif oppr=="*":  #USE (*) FOR MULTIPLICATION
    print(f" Product of {num1} and {num2} is: ",num1*num2)
elif oppr=="/":  #USE (/) FOR DIVIDE
    print(f" Quotient of {num1} and {num2} is: ",num1/num2)
elif oppr=="**": #USE (**) FOR POWERING
    print(f" {num2} to the power {num1} is: ",num1**num2)
else:
    print("ERROR 404: INVALID OPERATION, PLEASE USE (+) FOR ADDTION , (-) FOR SUBTRACTION, (*) FOR MULTIPLICATION, (/) FOR DIVIDE AND (**) FOR POWERING  ")
