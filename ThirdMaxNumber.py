def thirdMax(nums: list[int]) -> int:
    N = dict()
    maximum = [-1]*3
    for x in nums:
        if N.get(x) == 0:
            N[x] = 1
        if x > maximum[2] and x < maximum[1]:
            maximum[2] = x
        elif x > maximum[1] and x < maximum[0]:
            maximum[2] = maximum[1]
            maximum[1] = x
        elif x > maximum[0]:
            maximum[2] = maximum[1]
            maximum[1] = maximum[0]
            maximum[0] = x
        else: continue
    if maximum[2] == -2147483649:
        return maximum[0]
    else: return maximum[2]

nums = [3,2,2,3,2,1]
A = thirdMax(nums)
print(A)

            
