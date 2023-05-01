def find_duplicate(nums):
    nums.sort()
    for index, n in enumerate(nums[1::]):
        if n == nums[index] and n > 0:
            return n
    return False
