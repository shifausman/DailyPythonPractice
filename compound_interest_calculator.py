principle = 0
rate = 0
time = 0

while principle <=0:
  principle = float(input("Enter the principle amount: "))
  if(principle<=0):
    print("you cant enter principle amount less than or equal to zero")

while rate <=0:
  rate = float(input("Enter the rate of interest: "))
  if(rate<=0):
    print("you cant enter rate of interest less than or equal to zero")

while time <=0:
  time = float(input("Enter the no. of years: "))
  if(time<=0):
    print("you cant enter no. of years less than or equal to zero")

result = principle * (pow((1+ rate/100),time))
print(f"annual amount for ${principle} for {time} years under compound interest at a rate of {rate} is {result:.2f}")
