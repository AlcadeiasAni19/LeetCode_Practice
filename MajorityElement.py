from statistics import mode
def majorityElement(nums: list[int]) -> int:
    return mode(nums)

nums = [2,2,1,1,1,2,2]
A = majorityElement(nums)
print(A)