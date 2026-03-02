def black_and_white_stripe():
    t = int(input())

    for _ in range(t):
        n,k = map(int, input().split())
        stripe = input()
        left = 0
        right = k
        b_count = stripe[left:right].count("B")

        recolor = k - b_count
        mini = recolor

        while right < len(stripe):
            if stripe[left] == "W":
                recolor -= 1
            if stripe[right] == "W":
                recolor += 1
            mini = min(mini, recolor)
            
            right += 1
            left += 1
        print(mini)

black_and_white_stripe()
            

