def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return []

nums = [1, 9, 8, 10]
target = 9

result = twoSum(nums, target)
print("Indices:", result)