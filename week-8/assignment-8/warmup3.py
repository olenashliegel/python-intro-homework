file_path = "../data/missing.txt"

try:
    with open(file_path, "r") as f:
        pass
except FileNotFoundError:
    print(
        f"Error: {file_path} was not found. Please check the file path and try again."
    )
