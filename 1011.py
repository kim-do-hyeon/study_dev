# 1011 - Fly me to the Alpha Centauri
T = int(input())
for i in range(T) :
    x, y = map(int, input().split())
    dist = y - x
    cnt = 0
    move = 1
    result = 0
    while result < dist :
        cnt += 1
        result += move
        if cnt % 2 == 0 :
            move += 1
    print(cnt)