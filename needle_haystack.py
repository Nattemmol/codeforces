from collections import Counter

def solve():
    
    t = int(input())

    for _ in range(t):
        s = input().strip()
        t2 = input().strip()

        s_count = Counter(s)
        t_count = Counter(t2)

        if not (s_count <= t_count):
            print("Impossible")
            continue

        remaining = t_count - s_count
        
        extra_chars = sorted(remaining.elements())
        
        result = []
        extra_idx = 0
        n_extra = len(extra_chars)

        for char_s in s:
            while extra_idx < n_extra and extra_chars[extra_idx] < char_s:
                result.append(extra_chars[extra_idx])
                extra_idx += 1
            result.append(char_s)

        if extra_idx < n_extra:
            result.extend(extra_chars[extra_idx:])

        print("".join(result))


solve()
