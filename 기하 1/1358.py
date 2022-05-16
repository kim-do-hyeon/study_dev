# 1358 - 하키
import math

W, H, X, Y, P = map(int, input().split())


def square(x, y) :
    if(x >= X and x <= X + W and y >= Y and y <= Y + H) :
        return True
    else :
        return False

def distance(a1, b1, a2, b2) :
    return math.sqrt((a1 - a2) * (a1 - a2) + (b1 - b2) * (b1 - b2))

def circle(x, y) :
    if(distance(X, Y + H / 2, x, y) <= H / 2) :
        return True
    if(distance(X + W, Y + H / 2, x, y) <= H / 2) :
        return True


result = 0
for i in range(P) :
    x, y = map(int, input().split())
    if(square(x, y)) == True :
        result += 1
    elif(circle(x, y) == True) :
        result += 1
print(result)