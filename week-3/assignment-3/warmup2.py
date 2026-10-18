user_age = int(input("How old are you?"))

if user_age < 0:
  print ("Please enter correct age")
elif user_age >=65:
  print ("You are a Senior.")
elif user_age >=18 and user_age < 65:
  print ("You are an Adult.")
elif user_age>=13 and user_age < 18:
  print ("You are a Teen.")
else:
  print ("You are a Child.")