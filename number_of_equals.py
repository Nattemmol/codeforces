from collections import Counter


def num_equals():
    fir, sec = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    i = 0
    j = 0
    count_a = Counter(a)
    count_b = Counter(b)
    
    for k, v in count_a.items():
        if count_a[k] > 0 and count_b[k]> 0:
            count += count_a[k] * count_b[k]
    print(count)
    return

num_equals()
