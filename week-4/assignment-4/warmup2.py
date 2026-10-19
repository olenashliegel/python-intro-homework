student = {
  "name" : "Olena",
  "grade" : "A",
  "subjects" : ["Math", "Art", "Biology"] 
}

for key, value in student.items():
  print (key, value)

student["graduated"] = False

print (student)