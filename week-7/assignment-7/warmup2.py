import csv

with open('../data/students.csv', 'r', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(f"{row['name']}: {row['score']}")