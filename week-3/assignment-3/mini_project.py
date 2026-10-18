day = input("What day is it?").strip().lower()
time = input ("What time of day?").strip().lower()

if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
  print ("Sorry, I don't know this day. Please try again.")
elif time not in ("morning", "afternoon", "evening"):
  print("Please enter morning, afternoon, or evening.")
else:
  if day in ("monday", "wednesday", "friday") and time == "morning":
    print("Time to study Python!")
  elif day in ("tuesday", "thursday") and time == "morning":
    print ("Let's go to the gym!")
  elif day in ("monday", "tuesday", "thursday", "friday") and time == "afternoon":
    print ("Time to work!")
  elif day in ("monday", "thursday") and time == "evening":
    print ("Let's spend time with family!")
  elif day == "tuesday" and time == "evening":
    print ("Time for dance class!")
  elif day in ("wednesday", "saturday") and time == "evening":
    print ("Let's watch a movie!")
  elif day == "wednesday" and time == "afternoon":
    print ("Let's go grocery shopping!")
  elif day == "friday" and time == "evening":
    print ("Let's have dinner with friends!")
  elif day == "saturday" and time == "morning":
    print ("Let's have a family breakfast!")
  elif day == "saturday" and time == "afternoon":
    print ("Let's go to the park with the kids!")
  elif time == "morning":
    print ("Let's sleep a little longer!")
  elif time == "afternoon":
    print ("Let's go on a family trip!")
  else:
    print ("Let's get ready for next week!")