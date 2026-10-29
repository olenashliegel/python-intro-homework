def find_min(numbers):
  """Return the smallest number in the list."""
  min_number = numbers[0]
  for i in range (1, len(numbers)):
    if numbers [i] < min_number:
      min_number = numbers[i]
  return min_number

def find_max(numbers):
  """Return the largest number in the list."""
  max_number = numbers[0]
  for i in range(1, len(numbers)):
    if numbers [i] > max_number:
      max_number = numbers[i]
  return max_number

def bubble_sort(numbers):
  """Return a new sorted list without changing the original."""
  shallow_numbers = numbers.copy()
  is_swapped = True
  while is_swapped == True:
    is_swapped = False
    for i in range(len(shallow_numbers) - 1):
      if shallow_numbers[i] > shallow_numbers[i + 1]:
        shallow_numbers[i], shallow_numbers[i + 1] = shallow_numbers[i + 1], shallow_numbers[i]
        is_swapped = True
  return shallow_numbers

def show_menu():
  """Display the main menu and return the user's choice."""
  print (f""" === Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit""")
  choice = input ("Choose an option (1-5):")
  return choice

def search(numbers, target):
  """Return the index of the target number, or -1 if not found."""
  for index, number in enumerate(numbers):
    if number == target:
      return index
  return -1

def find_number_menu ():
  """Ask the user for a number until valid input is entered."""
  while True:
    try:
      input_number= int (input("Please enter number to search:"))
    except ValueError:
      print("Please enter a valid number.")
    else:
      return input_number

def main(numbers):
  """Run the main menu and handle the user's choices."""
  while True:
    choice = show_menu()

    if choice == "5":
      print ("Bye-bye")
      break
 
    elif choice == "1":
      print (f"Minimum number is {find_min (numbers)}")

    elif choice == "2":
      print (f"Maximum number is {find_max (numbers)}")

    elif choice == "3":
      user_input_number = find_number_menu ()
      index = search(numbers, user_input_number)
      if index == -1:
        print (f"The number {user_input_number} is not found")
      else:
        print (f"The index of {user_input_number} is {index}")
   
    elif choice == "4":
      print (f"sorted list {bubble_sort(numbers)}")

if __name__ == "__main__":
  numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
  main(numbers)