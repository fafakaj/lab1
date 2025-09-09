def simplesum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if type(nums[i]) == str or type(nums[j]) == str:
                continue
            elif nums[i] + nums[j] == target:
                return [i, j]
    return "NO"