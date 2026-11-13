import os
import csv
from datetime import datetime


def read_data_from_csv(path):
    expenses = []
    with open(path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expenses.append(row)
    return expenses


def convert_amount_to_float(expenses):
    for row in expenses:
        row["amount"] = float(row["amount"])


def filter_list_by_category(expenses, category):
    expenses_by_category = []
    for row in expenses:
        if row["category"].lower() == category.lower():
            expenses_by_category.append(row)
    return expenses_by_category


def calculate_total_amount(filtered_list_by_category):
    total_amount = 0
    for row in filtered_list_by_category:
        total_amount += row["amount"]
    return total_amount


def write_result_to_file(filtered_list_by_category, amount, category):
    file_name = category + "_report.txt"
    now = datetime.now()
    first_line = f"{category.capitalize()} Expense Report — generated {now.strftime('%B %d, %Y')}"
    with open(file_name, "w", encoding="utf-8") as report_file:
        report_file.write(first_line)
        for expense in filtered_list_by_category:
            report_file.write(f"\n{expense['date']}: ${expense['amount']:.2f}")
        report_file.write(f"\nTotal: ${amount:.2f}\n")


def create_set_of_categories(expenses):
    categories_set = set()
    for expense in expenses:
        categories_set.add(expense["category"].lower())
    return categories_set


def display_all_categories(set_of_categories):
    categories_list = sorted(set_of_categories)
    categories_string = ""
    for category in categories_list:
        categories_string = categories_string + f"{category.capitalize()} "
    return categories_string


def main(expenses):
    set_of_categories = create_set_of_categories(expenses)
    while True:
        print("Please select a category from the list below:")
        print(display_all_categories(set_of_categories))
        category = (
            input("Enter the category you want to generate a report for:")
            .lower()
            .strip()
        )
        if category not in set_of_categories:
            print(
                "This category was not found in the expense records. Please try again."
            )
        else:
            break
    convert_amount_to_float(expenses)
    category_expenses = filter_list_by_category(expenses, category)
    total_amount = calculate_total_amount(category_expenses)
    write_result_to_file(category_expenses, total_amount, category)


if __name__ == "__main__":
    expenses_path = os.path.join("..", "data", "expenses.csv")
    if not os.path.exists(expenses_path):
        print("expenses.csv doesn't exist. Please make sure that file exist")
    else:
        expenses = read_data_from_csv(expenses_path)
        main(expenses)
