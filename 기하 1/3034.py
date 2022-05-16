# 3034 - 앵그리 창영
import math
N, W, H = map(int, input().split())
S = int(math.sqrt(abs(W * W + H * H)))
for i in range(N) :
    temp = int(input())
    if S >= temp :
        print("DA")
    else :
        print("NE")
