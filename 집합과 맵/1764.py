# 듣보잡
import sys
N, M = map(int, input().split())
USER = []
NO_USER = []
for i in range(N) :
    USER.append(sys.stdin.readline().strip())
for i in range(M) :
    NO_USER.append(sys.stdin.readline().strip())

result = list(set(USER) & set(NO_USER))
result.sort()
print(len(result))
for i in result :
    print(i)