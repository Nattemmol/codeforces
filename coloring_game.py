def coloring_game():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = 0

        for i in range(n-1,1,-1):
            l = 0
            for r in range(i-1, 0,-1):
                while l < r and a[l] + a[r] + a[i] <= max(2*a[i], a[-1]):
                    l += 1
                # print(l, r, i)
                ans += max(0, r-l)
        print(ans)

coloring_game()
