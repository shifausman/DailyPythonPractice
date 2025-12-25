import math

x = int(input("Enter the first number: "))
op = (input("Enter the operation (+,-,*,/,%): "))
y = int(input("Enter the second number: "))

if(op == "+"):
  result = x+y
  print(f"{x} {op} {y} = {result}")
elif(op == "-"):
  result = x-y
  print(f"{x} {op} {y} = {result}")
elif(op == "*"):
  result = x*y
  print(f"{x} {op} {y} = {result}")
elif(op == "/"):
  if(y==0):
    print("can't divide by zero")
  else:
    result = x/y
    print(f"{x} {op} {y} = {result}")
elif(op == "%"):
  result = x%y
  print(f"{x} {op} {y} = {result}")
else:
  print("invalid operation")

