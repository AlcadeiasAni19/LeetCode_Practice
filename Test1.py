def A(x:list[int]):
    for i,a in enumerate(x):
        x[i] = a * 2 + B(a)    #[5,8,11]
    return x

def B(x:int):
    return x + 2
    
heights = [1,2,3]
p = A(heights)
print(p)