def arrayPairSum(nums: list[int]) -> int:
    MaxSum = 0
    sorted_nums = nums.copy()
    sorted_nums.sort()
    for i in range(int(len(nums)/2)):
        MaxSum += sorted_nums[2*i]
    return MaxSum

nums = [1,4,3,2]
A = arrayPairSum(nums)
print(A)