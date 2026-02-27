def most_socially_distance_subsequence():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        ans = []
        i = 0
        j = 0
        while j < len(p)-2:
            if (p[i] <= p[j+1] and p[j+1] <= p[j+2]) or (p[i] >= p[j+1] and p[j+1] >= p[j+2]):
                p[j+1] = 0
            else:
                i = j+1
            j+=1

        i = 0
        while i < len(p):
            if p[i] != 0:
                ans.append(p[i])
            i+= 1
        print(len(ans))
        print(*ans)
            
most_socially_distance_subsequence()
