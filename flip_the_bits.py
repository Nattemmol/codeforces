def flip_the_bits():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a = input()
        b = input()
        a += '0'
        b += '0'
        zero_count = 0
        one_count = 0
        possible = True
        for i in range(n):
            if a[i] == "0":
                zero_count += 1
            if a[i] == "1":
                one_count += 1
            curr_match = (a[i] == b[i])
            next_match = (a[i+1] == b[i+1])

            if curr_match != next_match:

                if zero_count != one_count:
                    possible = False
                    break
            
        print("YES" if possible else "NO")
    
flip_the_bits()
