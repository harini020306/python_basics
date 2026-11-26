# Convert all words into uppercase

words = input("Enter words separated by spaces: ").split()

uppercase = [word.upper() for word in words]

print("Uppercase words:", uppercase)