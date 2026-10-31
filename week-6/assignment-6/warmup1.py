def greet (name, greeting="Hello"):
  print (f"{greeting}, {name.capitalize()}!")

if __name__ == "__main__":
  user_name="Olena"
  greet (user_name)
  greet (user_name, "Hi")
  greet (user_name, greeting="Good morning")