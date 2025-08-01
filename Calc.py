

#Basic calculator programme
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
Operation = input("Enter any of the operators (+, -, *, /) :")


#performing the programme based on the operation
if Operation == "+":
    result= num1 +  num2
    print(f"{num1} + {num2} = {result}")


elif Operation == "-" :
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")   


elif Operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

else :
    print("Invalid operation. Please use +, -, or *, ")