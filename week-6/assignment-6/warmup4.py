def is_valid_score(score):
  if score >= 0 and score <=100:
    return True
  else:
    return False

def user_input():
  while True:
    try:
      user_score = int(input ("Please enter number between 0 and 100 (inclusive):"))
    except ValueError:
      print("Please enter a valid number.")
    else:
      return user_score

def display_result (score):
  if is_valid_score(score):
    print ("Valid score.")
  else:
    print ("Invalid score — must be between 0 and 100.")

if __name__ == "__main__":
  user_score =  user_input()
  display_result (user_score)