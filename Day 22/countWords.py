# Get user input
text = input("Enter a sentence: ")

# Write into file
with open("words.txt", "w") as file:
    file.write(text)

# Read the file
with open("words.txt", "r") as file:
    content = file.read()

# Count words
words = content.split()

print("Total Words:", len(words))