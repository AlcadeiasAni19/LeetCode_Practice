import string
from functools import reduce
def isAnagram(s: str, t: str) -> bool:
    al = dict(zip(string.ascii_lowercase, range(1, 27)))
    al.update(al.fromkeys(al,0))
    for x in s:
        al[x] += 1
    for y in t:
        if al[y] > 0:
            al[y] -= 1
        else: return False
    res = reduce((lambda x, y: x + y), al.values())
    if (res == 0):
        return True
    else: return False

s = "aba"
t = "ab"
A = isAnagram(s,t)
print(A)