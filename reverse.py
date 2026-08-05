def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Driver Code
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

print("Reversed array:", reverseArray(arr))