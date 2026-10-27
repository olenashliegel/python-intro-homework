while True:
  positive_number = input ("Enter a positive integer:")
  if positive_number.isdigit() and int (positive_number) > 0:
      print (f"Got it: {positive_number}")
      break
  else:
        print ("That's not a positive integer. Try again.")
