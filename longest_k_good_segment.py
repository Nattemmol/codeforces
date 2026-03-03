from collections import defaultdict


def longest_k_good_segment():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    l = 0
    r = 0
    unique_char = 0
    longest = 0
    left = 0
    right = 0
    if len(a) == k:
        print(1,k)
        return
    count = defaultdict(int)
    for r in range(len(a)):
        if count[a[r]] == 0:
            unique_char += 1
        count[a[r]] += 1
        while unique_char > k:
            count[a[l]] -= 1
            if count[a[l]] == 0:
                unique_char -= 1
            l += 1
        dis = r - l +1
        if dis > longest:
            longest = dis
            left = l + 1
            right = r + 1
    print(left, right)
    
longest_k_good_segment()
             
