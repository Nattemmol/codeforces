def longest_regular_bracket_sequence():
    s = input()
    n = len(s)
    max_len = 0
    count = 0
    
    stack = [-1]
    
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                current_len = i - stack[-1]
                if current_len > max_len:
                    max_len = current_len
                    count = 1
                elif current_len == max_len and max_len > 0:
                    count += 1
                
    if max_len == 0:
        print(0, 1)
    else:
        print(max_len, count)

longest_regular_bracket_sequence()
