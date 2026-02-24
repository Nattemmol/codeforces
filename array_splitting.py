def array_splitting():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 1:
        print(a[-1] - a[0])
        return

    diffs = []
    for i in range(n - 1):
        diffs.append(a[i+1] - a[i])
    
    diffs.sort(reverse=True)
    
    
    res = a[n-1] - a[0]
    for i in range(k - 1):
        res -= diffs[i]
    
    print(res)
array_splitting()
