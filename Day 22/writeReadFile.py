# Get user input
text = input("Enter text to save: ")

# Write into file
with open("sample.txt", "w") as file:
    file.write(text)

# Read the file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:", content)