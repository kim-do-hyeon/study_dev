# 1193 - 분수찾기
# 2022-01-15 AM 3:38

n = int(input())
line = 1

while n > line :
    n -= line
    line += 1

if line % 2 == 0 :
    a = n
    b = line - n + 1

else :
    a = line - n + 1
    b = n

print(a, '/', b, sep = '')