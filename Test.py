def A(x:list[int]):
    for i,a in enumerate(x):
        x[i] = a * 2 + B(a)
    return x

def B(x:int):
    return C(x+2)

def C(x:int):
    return x*x
    
heights = [1, 2, 3]
P = A(heights)
print(P)