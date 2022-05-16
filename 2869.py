# 달팽이는 올라가고 싶다.
import math
a, b, c = map(int, input().split())
height = c - a
if height % (a - b) == 0 :
    day = int(height / (a - b))
else :
    day = int(height / (a - b) + 1)
print(day + 1)