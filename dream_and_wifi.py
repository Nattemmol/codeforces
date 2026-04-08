import math

def dream_and_wifi():
    
    s1 = input()
    s2 = input()

    count1_p = s1.count("+")
    count1_m = s1.count("-")
    count2_p = s2.count("+")
    count2_m = s2.count("-")
    
    count_q = s2.count("?")
    
    need_p = count1_p - count2_p
    need_q = count1_m - count2_m
    
    if need_p < 0 or need_q < 0:
        print(f"{0.0:.12f}")
        return

    if count_q == 0:
        if need_p == 0 and need_q == 0:
            print(f"{1.0:.12f}")
        else:
            print(f"{0.0:.12f}")
        return

    ways = math.comb(count_q, need_p)
    ans = ways / (2**count_q)
    print(f"{ans:.12f}")

dream_and_wifi()
