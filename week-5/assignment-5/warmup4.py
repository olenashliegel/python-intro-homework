start_loop=1
end_loop=30 

for i in range (start_loop, end_loop+1):
  if i % 3 == 0 and i % 5 == 0:
    print ("FizzBuzz")
  elif i % 3 == 0:
    print ("Fizz")
  elif i % 5 == 0:
    print ("Buzz")
  else:
    print (i)