def findAverage(arr):
    total = 0

    for num in arr:
        total += num

    average = total / len(arr)
    return average


arr = list(map(int, input("Enter array elements: ").split()))

print("Average of the array =", findAverage(arr))