import csv

path = "../data/messy_data.csv"


def read_data_from_csv(path):
    file_data = []
    try:
        with open(path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                file_data.append(row)
    except FileNotFoundError:
        print(f"{path} is not found. Please make sure that file exists")
        return None
    return file_data


def clean_data(file_data):
    error_list = []
    clean_data_list = []
    for index, row in enumerate(file_data, start=1):
        if None in row.keys():
            error_list.append(f"Row {index}: extra column detected — skipped")
            continue
        try:
            row["amount"] = float(row["amount"])
        except ValueError:
            error_list.append(
                f"Row {index}: ValueError — could not convert '{row['amount']}' to float"
            )
        except TypeError as e:
            error_list.append(f"Row {index}: TypeError — {e}")
        except KeyError as e:
            error_list.append(f"Row {index}: KeyError — {e}")
        else:
            clean_data_list.append(row)
    return clean_data_list, error_list


def print_result(clean_data_list, error_list):
    clean_rows_count = len(clean_data_list)
    error_rows_count = len(error_list)
    print(f"""=== CSV Report ===
Rows attempted: {(clean_rows_count + error_rows_count):>3}
Rows parsed:    {clean_rows_count:>3}
Rows skipped:   {error_rows_count:>3}
          """)
    print("Skipped rows:")
    for row in error_list:
        print(f"  {row}")
    print("")
    print("Clean data:")
    for row in clean_data_list:
        print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")


if __name__ == "__main__":
    file_data = read_data_from_csv(path)
    if file_data is not None:
        clean_data_list, error_list = clean_data(file_data)
        print_result(clean_data_list, error_list)
