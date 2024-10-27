def sortedSquares(nums: list[int]) -> list[int]:
    Sq = [-1]*len(nums)
    for i in range(len(nums)):
        Sq[i] = nums[i]*nums[i]
    Sq.sort()
    return Sq

nums = [-4,-1,0,3,10]
A = sortedSquares(nums)
print(A)