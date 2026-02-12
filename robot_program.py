import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pos = x
    first_hit = -1
    
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    ans = 1
    remaining = k - first_hit
    
   # pos = 0
    cycle_len = -1
    
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            cycle_len = i + 1
            break
    
    if cycle_len == -1:
        print(ans)
    else:
        ans += remaining // cycle_len
        print(ans)
