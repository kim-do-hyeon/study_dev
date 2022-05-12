# ACM 호텔
'''
    H => 호텔의 층수
    W => 각 층의 방수
    N => 몇번째 손님

    만약 H가 6이며, N이 4이라면
    count => 손님이 묵을 층수
    count = N % H 이므로, 4층이다.
    그후 호수의 계산은 N // H + 1 이므로, 1 이다.
    즉, 401호에 묵는다는 것이다.
    하지만, N이 H의 배수인 경우, 잘못된 값을 출력하기에,
    N이 H의 배수일때, 즉 N에 H를 나눈 나머지가 0이라면
    예시 ) H = 6, N = 6
    층수의 경우 => 호텔의 전체 높이가 되며,
    호수의 경우 => N 을 H로 나눴을떄의 몫이므로, 1이다. 즉 601호에 투숙하게 되는것이다.
'''

T = int(input())
for i in range(T) :
    H, W, N = map(int, input().split())
    num = N // H + 1
    count = N % H
    if count == 0 :
        num = N // H
        count = H
    print(count * 100 + num)