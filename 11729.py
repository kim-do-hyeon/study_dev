def answer(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    answer(n-1, start, 6-start-end)
    print(start, end)
    answer(n-1, 6-start-end, end) 
    
n = int(input())
print(2**n-1)
answer(n, 1, 3)