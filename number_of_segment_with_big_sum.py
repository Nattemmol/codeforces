def number_of_segment_with_big_sum():
    n,s = map(int, input().split())
    a = list(map(int, input().split()))  

    left = 0
    window_sum = 0
    count = 0
    for right in range(n):
        window_sum += a[right]
        while window_sum >= s:
            count += (n - right)
            window_sum -= a[left]
            left += 1
            
    print(count)

    return
number_of_segment_with_big_sum()


