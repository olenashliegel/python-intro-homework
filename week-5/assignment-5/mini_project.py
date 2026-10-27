numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
  print (f""" === Number Cruncher ===
  {numbers}
  1. Find minimum
  2. Find maximum
  3. Search for a number
  4. Sort the list
  5. Quit""")
  choice = input ("Choose an option (1-5):")

  if choice == "5":
    print ("Bye-bye")
    break

  elif choice == "1":
    min_number=numbers[0]
    for i in range (1, len(numbers)):
      if numbers [i]<=min_number:
        min_number=numbers[i]
    print (f"Minimum number is {min_number}")

  elif choice == "2":
    max_number=numbers[0]
    for i in range (1, len(numbers)):
      if numbers [i]>=max_number:
        max_number=numbers[i]
    print (f"Maximum number is {max_number}")

  elif choice == "3":
    while True:
      try:
        input_number= int (input("Please enter number to search:"))
      except ValueError:
        print("Please enter a valid number.")
      else:
        is_found=False
        for index, number in enumerate(numbers):
          if number == input_number:
            print (f"The index of {input_number} is {index}")
            is_found=True
            break
        if not is_found:
          print (f"The number {input_number} is not found")
        break

  elif choice == "4":
    shallow_numbers= numbers.copy()
    is_swapped = True
    while is_swapped == True:
      is_swapped = False
      for i in range (len(shallow_numbers)-1):
        if shallow_numbers[i] > shallow_numbers [i + 1]:
          shallow_numbers [i], shallow_numbers [i + 1] = shallow_numbers [i + 1], shallow_numbers [i]
          is_swapped = True
    print (f"sorted list {shallow_numbers}")
     