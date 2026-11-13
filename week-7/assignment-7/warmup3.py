import os

print(os.getcwd())

expenses_path = os.path.join("..", "data", "expenses.csv")

if os.path.exists(expenses_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print(expenses_path)