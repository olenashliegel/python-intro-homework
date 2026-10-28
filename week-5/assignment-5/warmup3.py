names = ["Olena", "Anna", "Rob", "Sergei", "Ivan", "Maria"]
input_name = input ("Enter a name to search for:")
is_found=False

for index, name in enumerate(names):
  if name.lower() == input_name.lower():
    print (f"{input_name} was found at index {index}")
    is_found=True
    break

if not is_found:
  print (f"{input_name} was not found in the list")