import sys
from collections import Counter

def phoenix_and_socks():
    t = int(input())
    
    for _ in range(t):
        n,l_count, r_count = map(int,input().split())

        colors = list(map(int, input().split()))

        
        L = Counter(colors[:l_count])
        R = Counter(colors[l_count:])

        for c in L:
            if c in R:
                mn = min(L[c], R[c])
                L[c] -= mn
                R[c] -= mn
                l_count -= mn
                r_count -= mn
        
        if l_count > r_count:
            L, R = R, L
            l_count, r_count = r_count, l_count
            
        
        diff = (r_count - l_count) // 2
        cost = diff
        
        rem_pairs = 0
        for c in R:
            rem_pairs += R[c] // 2
          
        can_fix_by_flipping = min(diff, rem_pairs)
        
        print(cost + (l_count + (diff - can_fix_by_flipping)))


phoenix_and_socks()
