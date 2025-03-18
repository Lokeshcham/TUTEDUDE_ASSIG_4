def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + "\n")
    print(f"Data successfully written to {filename}.")

def append_to_file(filename):
    user_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(user_input + "\n")
    print(f"Data successfully appended.")

def read_file(filename):
    print(f"\nFinal content of {filename}:")
    with open(filename, 'r') as file:
        print(file.read())

# Define the file name
filename = "output.txt"

# Perform write, append, and read operations
write_to_file(filename)
append_to_file(filename)
read_file(filename)
