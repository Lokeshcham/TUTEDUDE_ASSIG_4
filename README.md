# README

## Task 1: Read a File and Handle Errors
### Problem Statement
Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

### Code Explanation
1. **Opening the File:**
   - The program attempts to open `sample.txt` in **read mode**.
2. **Reading Line by Line:**
   - It iterates over the file and prints each line without extra newlines.
3. **Handling Errors:**
   - If the file does **not exist**, it catches a `FileNotFoundError` and prints an error message.
   - If any other error occurs, it catches the exception and displays a generic error message.

### Usage
1. Run the script.
2. If `sample.txt` exists, the contents will be displayed.
3. If the file does not exist, an error message will be shown.

### Example Output
**If the file exists:**
```
This is the first line.
This is the second line.
```
**If the file does not exist:**
```
Error: The file 'sample.txt' does not exist.
```

---

## Task 2: Write and Append Data to a File
### Problem Statement
Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

### Code Explanation
1. **Writing to the File (`w` mode):**
   - The program asks the user for input and writes it to `output.txt`.
   - If the file already exists, it overwrites the content.
2. **Appending to the File (`a` mode):**
   - The user is prompted for additional input.
   - The program appends the new data to `output.txt` without erasing existing content.
3. **Reading the File (`r` mode):**
   - After writing and appending, the program reads and prints the full content of the file.

### Usage
1. Run the script.
2. Enter the text to write to the file.
3. Enter additional text to append to the file.
4. The final content of the file will be displayed.

### Example Output
```
Enter text to write to the file: Hello, world!
Data written to output.txt successfully.

Enter additional text to append to the file: Python is awesome!
Data appended to output.txt successfully.

Final content of the file:
Hello, world!
Python is awesome!
```
