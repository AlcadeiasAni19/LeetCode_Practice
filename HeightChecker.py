def heightChecker(heights: list[int]) -> int:
    counter = 0
    sorted_heights = heights.copy()
    sorted_heights.sort()
    for i in range(len(heights)):
        if sorted_heights[i] != heights[i]:
            counter += 1
        else: continue
    return counter

heights = [1,2,3,4,5]
A = heightChecker(heights)
print(A)
        