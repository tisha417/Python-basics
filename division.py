a= float(input("type num1:"))
b= float(input("type num2:"))

try:
    result= a/b
except ZeroDivisionError:
     print("Error! \nCannot divide by zero") 
else:
     print(result)
