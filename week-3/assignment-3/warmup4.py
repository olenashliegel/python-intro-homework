number = int(input("Please enter the number:"))

if number > 0:
  print(f"{number} is positive")
elif number == 0:
  print(f"{number} is zero")
else:
  print(f"{number} is negative")

if number % 2 == 0:
  print(f"{number} is even")
else: 
  print(f"{number} is odd")  
