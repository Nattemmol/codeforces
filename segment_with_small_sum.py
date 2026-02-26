def segment_with_small_sum():
    n,s = map(int, input().split())
    a = list(map(int, input().split()))
    
    l = 0
    r = 0
    sums = 0
    longest = 0

    for r in range(len(a)):
        sums += a[r]
        while sums > s:
            sums -= a[l]
            l += 1
        longest = max(longest, r-l+1)
    print(longest)

    return
segment_with_small_sum()
