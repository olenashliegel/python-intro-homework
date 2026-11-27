while True:
    number_string = input("Enter a number:")
    try:
        number = float(number_string)
    except ValueError:
        print(f"{number_string} is not a valid number. Try again.")
    else:
        print(f"You entered: {number:.2f}")
        break
