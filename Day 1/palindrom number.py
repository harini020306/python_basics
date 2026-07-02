def isPalindrome(x):
    original = x
    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    return original == reverse


# Driver Code
num = int(input("Enter a number: "))

if isPalindrome(num):
    print("Palindrome")
else:
    print("Not a palindrome")