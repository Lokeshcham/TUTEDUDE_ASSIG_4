def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the sample file name
read_file("sample.txt")
