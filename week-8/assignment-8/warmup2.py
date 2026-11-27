def get_number(number_name):
    while True:
        try:
            number = float(input(f"Enter the {number_name}: "))
        except ValueError:
            print("It's not a valid number. Try again.")
        else:
            return number


numerator = get_number("numerator")
denominator = get_number("denominator")

try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")
else:
    print(f"{numerator} ÷ {denominator} = {result:.2f}")
