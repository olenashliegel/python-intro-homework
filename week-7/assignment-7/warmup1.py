with open ('../data/notes.txt', 'r') as file:
  line_number = 0
  for line in file:
    line_number +=1
    print(f"Line {line_number}: {line.strip()}")

