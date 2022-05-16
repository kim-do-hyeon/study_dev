# 단어 정렬
import sys
N = int(input())
list_ = []
for i in range(N) :
    temp = sys.stdin.readline().strip()
    list_.append(temp)

'''
먼저 set을 통해 같은 단어를 삭제한다.
sort 를 2회 해주는 이유는 조건의 경우
1. 길이가 짧은 것부터
2. 길이가 같으면 사전순으로

먼저 list_를 사전순으로 정렬한다.
이후 문자열의 길이 순으로 정렬한다면,
i, no, want, it, ia, abc 이 입력되었다면
먼저 abc, i, ia, it, no, want 으로 정렬이 된다.
그후 문자열의 길이순으로 정렬하면,
i, ia, it, no, abc, want 가 되기 떄문에, 조건에 맞게된다.

'''
list_ = list(set(list_)) 
list_.sort()
list_.sort(key = len)
for i in list_ :
    print(i)