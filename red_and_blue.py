def red_and_blue():
    t = int(input())

    for _ in range(t):
        n = int(input())
        r = list(map(int, input().split()))

        m = int(input())
        b = list(map(int, input().split()))
        
        r_sum = 0
        r_max = 0
        for i in r:
            r_sum += i
            r_max = max(r_max, r_sum)

        b_sum = 0
        b_max = 0
        for i in b:
            b_sum += i
            
            b_max = max(b_max, b_sum)
        ans = r_max + b_max

        print(ans)   
    
red_and_blue()
