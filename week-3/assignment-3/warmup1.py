score = 59
if score < 0 or score >100: 
  print ("Please enter correct score")
elif score < 60:
  print (f"Score: {score} \nGrade: F")
elif score < 70:
  print (f"Score: {score} \nGrade: D")
elif score < 80:
  print (f"Score: {score} \nGrade: C")
elif score < 90:
  print (f"Score: {score} \nGrade: B")
else:
  print (f"Score: {score} \nGrade: A")