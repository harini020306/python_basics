def findMedian(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2

    return median


# Driver Code
arr = list(map(int, input("Enter array elements: ").split()))

print("Median =", findMedian(arr))