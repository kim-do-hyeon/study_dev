# 15651 - N과 M (3) - 백트래킹

N, M = list(map(int, input().split()))

Array = []

def DFS() :
    if len(Array) == M :
        print(' '.join(map(str, Array)))
        return
    for i in range(1, N + 1) :
            Array.append(i)
            DFS()
            Array.pop()
DFS()