# Get user input
text = input("Enter text to append: ")

# Append text into file
with open("notes.txt", "a") as file:
    file.write(text + "\n")

# Read updated file
with open("notes.txt", "r") as file:
    content = file.read()

print("Updated File Content:")
print(content)