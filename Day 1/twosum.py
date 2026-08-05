def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return []

# Input from user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target: "))

result = twoSum(nums, target)

if result:
    print("Indices:", result)
else:
    print("No two numbers add up to the target.")