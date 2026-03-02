from collections import defaultdict


def segment_with_small_set():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    l = 0
    r = 0
    maxi = 0
    
    l = 0
    unique_count = 0
    freq = defaultdict(int)
    total = 0

    for r in range(len(a)):
        if freq[a[r]] == 0:
            unique_count += 1
        freq[a[r]] += 1

        while unique_count > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                unique_count -= 1
            l += 1
        total += r-l+1
        
    
    print(total)
segment_with_small_set()
